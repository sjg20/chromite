# Copyright 2014 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Module containing the various utilities to build Chrome with AFDO.

For a description of AFDO see gcc.gnu.org/wiki/AutoFDO.
"""

from __future__ import print_function

import datetime
import os
import re

from chromite.cbuildbot import failures_lib
from chromite.cbuildbot import constants
from chromite.lib import cros_build_lib
from chromite.lib import git
from chromite.lib import gs
from chromite.lib import osutils
from chromite.lib import timeout_util


# AFDO-specific constants.
# Chrome URL where AFDO data is stored.
AFDO_PROD_URL = 'gs://chromeos-prebuilt/afdo-job/canonicals/'
AFDO_TEST_URL = '%s/afdo-job/canonicals/' % constants.TRASH_BUCKET
AFDO_BASE_URL = AFDO_PROD_URL
AFDO_CHROOT_ROOT = os.path.join('%(build_root)s', constants.DEFAULT_CHROOT_DIR)
AFDO_LOCAL_DIR = os.path.join('%(root)s', 'tmp')
AFDO_BUILDROOT_LOCAL = AFDO_LOCAL_DIR % {'root': AFDO_CHROOT_ROOT}
CHROME_ARCH_VERSION = '%(package)s-%(arch)s-%(version)s'
CHROME_PERF_AFDO_FILE = '%s.perf.data' % CHROME_ARCH_VERSION
CHROME_PERF_AFDO_URL = '%s%s.bz2' % (AFDO_BASE_URL, CHROME_PERF_AFDO_FILE)
CHROME_AFDO_FILE = '%s.afdo' % CHROME_ARCH_VERSION
CHROME_AFDO_URL = '%s%s.bz2' % (AFDO_BASE_URL, CHROME_AFDO_FILE)
CHROME_ARCH_RELEASE = '%(package)s-%(arch)s-%(release)s'
LATEST_CHROME_AFDO_FILE = 'latest-%s.afdo' % CHROME_ARCH_RELEASE
LATEST_CHROME_AFDO_URL = AFDO_BASE_URL + LATEST_CHROME_AFDO_FILE
CHROME_DEBUG_BIN = os.path.join('%(root)s',
                                'build/%(board)s/usr/lib/debug',
                                'opt/google/chrome/chrome.debug')
CHROME_DEBUG_BIN_URL = '%s%s.debug.bz2' % (AFDO_BASE_URL, CHROME_ARCH_VERSION)

AFDO_GENERATE_GCOV_TOOL = '/usr/bin/create_gcov'

# regex to find AFDO file for specific architecture within the ebuild file.
CHROME_EBUILD_AFDO_EXP = r'^(?P<bef>AFDO_FILE\["%s"\]=")(?P<name>.*)(?P<aft>")'
# and corresponding replacement string.
CHROME_EBUILD_AFDO_REPL = r'\g<bef>%s\g<aft>'

# How old can the AFDO data be? (in days).
AFDO_ALLOWED_STALE = 7

# TODO(llozano): Currently using sandybridge boards. We should move to
# a more modern platform.
# Set of boards that can generate the AFDO profile (can generate 'perf'
# data with LBR events).
AFDO_DATA_GENERATORS = ('butterfly', 'lumpy', 'parrot', 'stumpy')

# For a given architecture, which architecture is used to generate
# the AFDO profile. Some architectures are not able to generate their
# own profile.
AFDO_ARCH_GENERATORS = {'amd64': 'amd64',
                        'arm': 'amd64',
                        'x86': 'amd64'}

AFDO_ALERT_RECIPIENTS = ['chromeos-toolchain@google.com']


class MissingAFDOData(failures_lib.StepFailure):
  """Exception thrown when necessary AFDO data is missing."""


class MissingAFDOMarkers(failures_lib.StepFailure):
  """Exception thrown when necessary ebuild markers for AFDO are missing."""


def CompressAFDOFile(to_compress, buildroot):
  """Compress file used by AFDO process.

  Args:
    to_compress: File to compress.
    buildroot: buildroot where to store the compressed data.

  Returns:
    Name of the compressed data file.
  """
  local_dir = AFDO_BUILDROOT_LOCAL % {'build_root': buildroot}
  dest = os.path.join(local_dir, os.path.basename(to_compress)) + '.bz2'
  cros_build_lib.CompressFile(to_compress, dest)
  return dest


def UncompressAFDOFile(to_decompress, buildroot):
  """Decompress file used by AFDO process.

  Args:
    to_decompress: File to decompress.
    buildroot: buildroot where to store the decompressed data.
  """
  local_dir = AFDO_BUILDROOT_LOCAL % {'build_root': buildroot}
  basename = os.path.basename(to_decompress)
  dest_basename = basename.rsplit('.', 1)[0]
  dest = os.path.join(local_dir, dest_basename)
  cros_build_lib.UncompressFile(to_decompress, dest)
  return dest


def GSUploadIfNotPresent(gs_context, src, dest):
  """Upload a file to GS only if the file does not exist.

  Will not generate an error if the file already exist in GS. It will
  only emit a warning.

  I could use GSContext.Copy(src,dest,version=0) here but it does not seem
  to work for large files. Using GSContext.Exists(dest) instead. See
  crbug.com/395858.

  Args:
    gs_context: GS context instance.
    src: File to copy.
    dest: Destination location.

  Returns:
    True if file was uploaded. False otherwise.
  """
  if gs_context.Exists(dest):
    cros_build_lib.Warning('File %s already in GS', dest)
    return False
  else:
    gs_context.Copy(src, dest, acl='public-read')
    return True


def CheckAFDOPerfData(arch, cpv, buildroot, gs_context):
  """Check whether AFDO perf data exists for the given architecture.

  Check if 'perf' data file for this architecture and release is available
  in GS. If so, copy it into a temp directory in the buildroot.

  Args:
    arch: architecture we're going to build Chrome for.
    cpv: The portage_util.CPV object for chromeos-chrome.
    buildroot: buildroot where AFDO data should be stored.
    gs_context: GS context to retrieve data.

  Returns:
    True if AFDO perf data is available. False otherwise.
  """
  # The file name of the perf data is based only in the chrome version.
  # The test case that produces it does not know anything about the
  # revision number.
  # TODO(llozano): perf data filename should include the revision number.
  version_number = cpv.version_no_rev.split('_')[0]
  chrome_spec = {'package': cpv.package,
                 'arch': arch,
                 'version': version_number}
  url = CHROME_PERF_AFDO_URL % chrome_spec
  if not gs_context.Exists(url):
    cros_build_lib.Info('Could not find AFDO perf data')
    return False
  dest_dir = AFDO_BUILDROOT_LOCAL % {'build_root': buildroot}
  dest_path = os.path.join(dest_dir, url.rsplit('/', 1)[1])
  gs_context.Copy(url, dest_path)

  UncompressAFDOFile(dest_path, buildroot)
  cros_build_lib.Info('Found and retrieved AFDO perf data')
  return True


def WaitForAFDOPerfData(cpv, arch, buildroot, gs_context,
                        timeout=constants.AFDO_GENERATE_TIMEOUT):
  """Wait for AFDO perf data to show up (with an appropriate timeout).

  Args:
    arch: architecture we're going to build Chrome for.
    cpv: CPV object for Chrome.
    buildroot: buildroot where AFDO data should be stored.
    gs_context: GS context to retrieve data.
    timeout: How long to wait total, in seconds.

  Returns:
    True if found the AFDO perf data before the timeout expired.
    False otherwise.
  """
  try:
    timeout_util.WaitForReturnTrue(
        CheckAFDOPerfData,
        func_args=(arch, cpv, buildroot, gs_context),
        timeout=timeout, period=constants.SLEEP_TIMEOUT)
  except timeout_util.TimeoutError:
    return False
  return True


def PatchChromeEbuildAFDOFile(ebuild_file, arch_profiles):
  """Patch the Chrome ebuild with the dictionary of {arch: afdo_file} pairs.

  Args:
    ebuild_file: path of the ebuild file within the chroot.
    arch_profiles: {arch: afdo_file} pairs to put into the ebuild.
  """
  original_ebuild = cros_build_lib.FromChrootPath(ebuild_file)
  modified_ebuild = '%s.new' % original_ebuild

  arch_patterns = {}
  arch_repls = {}
  arch_markers = {}
  for arch in arch_profiles.keys():
    arch_patterns[arch] = re.compile(CHROME_EBUILD_AFDO_EXP % arch)
    arch_repls[arch] = CHROME_EBUILD_AFDO_REPL % arch_profiles[arch]
    arch_markers[arch] = False

  with open(original_ebuild, 'r') as original:
    with open(modified_ebuild, 'w') as modified:
      for line in original:
        for arch in arch_profiles.keys():
          matched = arch_patterns[arch].match(line)
          if matched:
            arch_markers[arch] = True
            modified.write(arch_patterns[arch].sub(arch_repls[arch], line))
            break
        else: # line without markers, just copy it.
          modified.write(line)

  for arch, found in arch_markers.iteritems():
    if not found:
      raise MissingAFDOMarkers('Chrome ebuild file does not have appropriate '
                               'AFDO markers for arch %s' % arch)

  os.rename(modified_ebuild, original_ebuild)


def UpdateChromeEbuildAFDOFile(board, arch_profiles):
  """Update chrome ebuild with the dictionary of {arch: afdo_file} pairs.

  Modifies the Chrome ebuild to set the appropriate AFDO file for each
  given architecture. Regenerates the associated Manifest file and
  commits the new ebuild and Manifest.

  Args:
    board: board we are building Chrome for.
    arch_profiles: {arch: afdo_file} pairs to put into the ebuild.
  """
  # Find the Chrome ebuild file.
  equery_prog = 'equery'
  ebuild_prog = 'ebuild'
  if board:
    equery_prog += '-%s' % board
    ebuild_prog += '-%s' % board

  equery_cmd = [equery_prog, 'w', 'chromeos-chrome']
  ebuild_file = cros_build_lib.RunCommand(equery_cmd,
                                          enter_chroot=True,
                                          redirect_stdout=True).output.rstrip()

  # Patch the ebuild file with the names of the available afdo_files.
  PatchChromeEbuildAFDOFile(ebuild_file, arch_profiles)

  # Also patch the 9999 ebuild. This is necessary because the uprev
  # process starts from the 9999 ebuild file and then compares to the
  # current version to see if the uprev is really necessary. We dont
  # want the names of the available afdo_files to show as differences.
  # It also allows developers to do USE=afdo_use when using the 9999
  # ebuild.
  ebuild_9999 = os.path.join(os.path.dirname(ebuild_file),
                             'chromeos-chrome-9999.ebuild')
  PatchChromeEbuildAFDOFile(ebuild_9999, arch_profiles)

  # Regenerate the Manifest file.
  ebuild_gs_dir = None
  # If using the GS test location, pass this location to the
  # chrome ebuild.
  if AFDO_BASE_URL == AFDO_TEST_URL:
    ebuild_gs_dir = {'AFDO_GS_DIRECTORY': AFDO_TEST_URL}
  gen_manifest_cmd = [ebuild_prog,  ebuild_file, 'manifest', '--force']
  cros_build_lib.RunCommand(gen_manifest_cmd, enter_chroot=True,
                            extra_env=ebuild_gs_dir, print_cmd=True)

  ebuild_dir = cros_build_lib.FromChrootPath(os.path.dirname(ebuild_file))
  git.RunGit(ebuild_dir, ['add', 'Manifest'])

  # Check if anything changed compared to the previous version.
  mod_files = ['Manifest', os.path.basename(ebuild_file),
               os.path.basename(ebuild_9999)]
  modifications = git.RunGit(ebuild_dir,
                             ['status', '--porcelain', '--'] + mod_files,
                             capture_output=True, print_cmd=True).output
  if not modifications:
    cros_build_lib.Info('AFDO info for the Chrome ebuild did not change. '
                        'Nothing to commit')
    return

  # If there are changes to ebuild or Manifest, commit them.
  commit_msg = ('"Set {arch: afdo_file} pairs %s and updated Manifest"'
                % arch_profiles)
  git.RunGit(ebuild_dir,
             ['commit', '-m', commit_msg, '--'] + mod_files,
             print_cmd=True)


def VerifyLatestAFDOFile(afdo_release_spec, buildroot, gs_context):
  """Verify that the latest AFDO profile for a release is suitable.

  Find the latest AFDO profile file for a particular release and check
  that it is not too stale. The latest AFDO profile name for a release
  can be found in a file in GS under the name
  latest-chrome-<arch>-<release>.afdo.

  Args:
    afdo_release_spec: architecture and release to find the latest AFDO
        profile for.
    buildroot: buildroot where AFDO data should be stored.
    gs_context: GS context to retrieve data.

  Returns:
    The name of the AFDO profile file if a suitable one was found.
    None otherwise.
  """
  latest_afdo_url = LATEST_CHROME_AFDO_URL % afdo_release_spec

  # Check if latest-chrome-<arch>-<release>.afdo exists.
  try:
    latest_detail = gs_context.List(latest_afdo_url, details=True)
  except gs.GSNoSuchKey:
    cros_build_lib.Info('Could not find latest AFDO info file %s' %
                        latest_afdo_url)
    return None

  # Verify the AFDO profile file is not too stale.
  mod_date = latest_detail[0].creation_time
  curr_date = datetime.datetime.now()
  allowed_stale_days = datetime.timedelta(days=AFDO_ALLOWED_STALE)
  if (curr_date - mod_date) > allowed_stale_days:
    cros_build_lib.Info('Found latest AFDO info file %s but it is too old' %
                        latest_afdo_url)
    return None

  # Then get the name of the latest valid AFDO profile file.
  local_dir = AFDO_BUILDROOT_LOCAL % {'build_root': buildroot }
  latest_afdo_file = LATEST_CHROME_AFDO_FILE % afdo_release_spec
  latest_afdo_path = os.path.join(local_dir, latest_afdo_file)
  gs_context.Copy(latest_afdo_url, latest_afdo_path)

  return osutils.ReadFile(latest_afdo_path).strip()


def GetLatestAFDOFile(cpv, arch, buildroot, gs_context):
  """Try to find the latest suitable AFDO profile file.

  Try to find the latest AFDO profile generated for current release
  and architecture. If there is none, check the previous release (mostly
  in case we have just branched).

  Args:
    cpv: cpv object for Chrome.
    arch: architecture for which we are looking for AFDO profile.
    buildroot: buildroot where AFDO data should be stored.
    gs_context: GS context to retrieve data.

  Returns:
    Name of latest suitable AFDO profile file if one is found.
    None otherwise.
  """
  generator_arch = AFDO_ARCH_GENERATORS[arch]
  version_number = cpv.version
  current_release = version_number.split('.')[0]
  afdo_release_spec = {'package': cpv.package,
                       'arch': generator_arch,
                       'release': current_release}
  afdo_file = VerifyLatestAFDOFile(afdo_release_spec, buildroot, gs_context)
  if afdo_file:
    return afdo_file

  # Could not find suitable AFDO file for the current release.
  # Let's see if there is one from the previous release.
  previous_release = str(int(current_release) - 1)
  prev_release_spec = {'package': cpv.package,
                       'arch': generator_arch,
                       'release': previous_release}
  return VerifyLatestAFDOFile(prev_release_spec, buildroot, gs_context)


def GenerateAFDOData(cpv, arch, board, buildroot, gs_context):
  """Generate AFDO profile data from 'perf' data.

  Given the 'perf' profile, generate an AFDO profile using create_gcov.
  It also creates a latest-chrome-<arch>-<release>.afdo file pointing
  to the generated AFDO profile.
  Uploads the generated data to GS for retrieval by the chrome ebuild
  file when doing an 'afdo_use' build.
  It is possible the generated data has previously been uploaded to GS
  in which case this routine will not upload the data again. Uploading
  again may cause verication failures for the ebuild file referencing
  the previous contents of the data.

  Args:
    cpv: cpv object for Chrome.
    arch: architecture for which we are looking for AFDO profile.
    board: board we are building for.
    buildroot: buildroot where AFDO data should be stored.
    gs_context: GS context to retrieve/store data.

  Returns:
    Name of the AFDO profile file generated if successful.
  """
  CHROME_UNSTRIPPED_NAME = 'chrome.unstripped'

  version_number = cpv.version
  afdo_spec = {'package': cpv.package,
               'arch': arch,
               'version': version_number}
  chroot_root = AFDO_CHROOT_ROOT % {'build_root': buildroot }
  local_dir = AFDO_LOCAL_DIR % {'root': chroot_root }
  in_chroot_local_dir = AFDO_LOCAL_DIR % {'root': '' }

  # Upload compressed chrome debug binary to GS for triaging purposes.
  # TODO(llozano): This simplifies things in case of need of triaging
  # problems but is it really necessary?
  debug_bin = CHROME_DEBUG_BIN % {'root': chroot_root,
                                  'board': board }
  comp_debug_bin_path = CompressAFDOFile(debug_bin, buildroot)
  GSUploadIfNotPresent(gs_context, comp_debug_bin_path,
                       CHROME_DEBUG_BIN_URL % afdo_spec)

  # create_gcov demands the name of the profiled binary exactly matches
  # the name of the unstripped binary or it is named 'chrome.unstripped'.
  # So create a symbolic link with the appropriate name.
  local_debug_sym = os.path.join(local_dir, CHROME_UNSTRIPPED_NAME)
  in_chroot_debug_bin = CHROME_DEBUG_BIN % {'root': '', 'board': board }
  osutils.SafeUnlink(local_debug_sym)
  os.symlink(in_chroot_debug_bin, local_debug_sym)

  # Call create_gcov tool to generated AFDO profile from 'perf' profile
  # and upload it to GS. Need to call from within chroot since this tool
  # was built inside chroot.
  debug_sym = os.path.join(in_chroot_local_dir, CHROME_UNSTRIPPED_NAME)
  # The name of the 'perf' file is based only on the version of chrome. The
  # revision number is not included.
  afdo_spec_no_rev = {'package': cpv.package,
                      'arch': arch,
                      'version': cpv.version_no_rev.split('_')[0]}
  perf_afdo_file = CHROME_PERF_AFDO_FILE % afdo_spec_no_rev
  perf_afdo_path = os.path.join(in_chroot_local_dir, perf_afdo_file)
  afdo_file = CHROME_AFDO_FILE % afdo_spec
  afdo_path = os.path.join(in_chroot_local_dir, afdo_file)
  afdo_cmd = [AFDO_GENERATE_GCOV_TOOL,
              '--binary=%s' % debug_sym,
              '--profile=%s' % perf_afdo_path,
              '--gcov=%s' % afdo_path]
  cros_build_lib.RunCommand(afdo_cmd, enter_chroot=True, capture_output=True,
                            print_cmd=True)

  afdo_local_path = os.path.join(local_dir, afdo_file)
  comp_afdo_path = CompressAFDOFile(afdo_local_path, buildroot)
  uploaded_afdo_file = GSUploadIfNotPresent(gs_context, comp_afdo_path,
                                            CHROME_AFDO_URL % afdo_spec)

  if uploaded_afdo_file:
    # Create latest-chrome-<arch>-<release>.afdo pointing to the name
    # of the AFDO profile file and upload to GS.
    current_release = version_number.split('.')[0]
    afdo_release_spec = {'package': cpv.package,
                         'arch': arch,
                         'release': current_release}
    latest_afdo_file = LATEST_CHROME_AFDO_FILE % afdo_release_spec
    latest_afdo_path = os.path.join(local_dir, latest_afdo_file)
    osutils.WriteFile(latest_afdo_path, afdo_file)
    gs_context.Copy(latest_afdo_path,
                    LATEST_CHROME_AFDO_URL % afdo_release_spec,
                    acl='public-read')

  return afdo_file


def CanGenerateAFDOData(board):
  """Does this board has the capability of generating its own AFDO data?."""
  return board in AFDO_DATA_GENERATORS


def GenerateOrFindAFDOData(cpv, arch, board, buildroot):
  """Generate or find the appropriate AFDO profile for the given architecture.

  For the architectures that can generate a 'perf' tool profile, wait for
  it to be generated by the autotest AFDO_generate and generate an AFDO
  profile for it. In the generation of the 'perf' profile failed, use
  a previously generated AFDO profile that is not too stale.
  For the architectures that cannot generate a 'perf' tool profile, use
  the AFDO profile from another architecture (e.g.: ARM can use a profile
  from AMD64).
  Once we have an adequate AFDO profile, put this information in the
  chrome ebuild.

  Args:
    cpv: cpv object for Chrome.
    arch: architecture for which we are looking for AFDO profile.
    board: board we are building for.
    buildroot: buildroot where AFDO data should be stored.
  """
  gs_context = gs.GSContext()
  afdo_file = None
  if CanGenerateAFDOData(board):
    # Generation of AFDO could fail for different reasons. Try to be
    # resilient about this and in case of failure just find an
    # older AFDO profile.
    try:
      if WaitForAFDOPerfData(cpv, arch, buildroot, gs_context):
        afdo_file = GenerateAFDOData(cpv, arch, board, buildroot, gs_context)
        assert afdo_file
        cros_build_lib.Info('Generated %s AFDO profile %s',
                            arch, afdo_file)
    # Will let system-exiting exceptions through.
    except Exception:
      cros_build_lib.PrintBuildbotStepWarnings()
      cros_build_lib.Warning('AFDO profile generation failed with exception ',
                             exc_info=True)
  if not afdo_file:
    cros_build_lib.Info('Trying to find previous appropriate AFDO profile')
    afdo_file = GetLatestAFDOFile(cpv, arch, buildroot, gs_context)
    if afdo_file:
      cros_build_lib.Info('Found previous %s AFDO profile %s',
                          arch, afdo_file)
  if not afdo_file:
    raise MissingAFDOData('Could not generate or find appropriate AFDO profile')

  # We found an AFDO profile. Lets put the info in the chrome ebuild.
  UpdateChromeEbuildAFDOFile(board, {arch: afdo_file})
