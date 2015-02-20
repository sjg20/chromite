# Copyright (c) 2012 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Routines and classes for working with Portage overlays and ebuilds."""

from __future__ import print_function

import collections
import errno
import filecmp
import fileinput
import glob
import logging
import multiprocessing
import os
import re
import shutil
import sys

from chromite.cbuildbot import constants
from chromite.lib import cros_build_lib
from chromite.lib import gerrit
from chromite.lib import git
from chromite.lib import osutils


_PRIVATE_PREFIX = '%(buildroot)s/src/private-overlays'

# Define datastructures for holding PV and CPV objects.
_PV_FIELDS = ['pv', 'package', 'version', 'version_no_rev', 'rev']
PV = collections.namedtuple('PV', _PV_FIELDS)
CPV = collections.namedtuple('CPV', ['category'] + _PV_FIELDS)

# Package matching regexp, as dictated by package manager specification:
# http://www.gentoo.org/proj/en/qa/pms.xml
_pkg = r'(?P<package>' + r'[\w+][\w+-]*)'
_ver = (r'(?P<version>'
        r'(?P<version_no_rev>(\d+)((\.\d+)*)([a-z]?)'
        r'((_(pre|p|beta|alpha|rc)\d*)*))'
        r'(-(?P<rev>r(\d+)))?)')
_pvr_re = re.compile(r'^(?P<pv>%s-%s)$' % (_pkg, _ver), re.VERBOSE)

# This regex matches a category name.
_category_re = re.compile(r'^(?P<category>[\w\+\.][\w\+\.\-]*)$', re.VERBOSE)

# This regex matches blank lines, commented lines, and the EAPI line.
_blank_or_eapi_re = re.compile(r'^\s*(?:#|EAPI=|$)')

WORKON_EBUILD_VERSION = '9999'
WORKON_EBUILD_SUFFIX = '-%s.ebuild' % WORKON_EBUILD_VERSION


class MissingOverlayException(Exception):
  """This exception indicates that a needed overlay is missing."""


def _ListOverlays(board=None, buildroot=constants.SOURCE_ROOT):
  """Return the list of overlays to use for a given buildbot.

  Always returns all overlays in parent -> child order, and does not
  perform any filtering.

  Args:
    board: Board to look at.
    buildroot: Source root to find overlays.
  """
  # Load all the known overlays so we can extract the details below.
  paths = (
      'projects',
      'src/overlays',
      'src/private-overlays',
      'src/third_party',
  )
  overlays = {}
  for path in paths:
    path = os.path.join(buildroot, path, '*')
    for overlay in glob.glob(path):
      name = GetOverlayName(overlay)
      if name is None:
        continue

      # Sanity check the sets of repos.
      if name in overlays:
        raise RuntimeError('multiple repos with same name "%s": %s and %s' %
                           (name, overlays[name]['path'], overlay))

      try:
        masters = cros_build_lib.LoadKeyValueFile(
            '%s/metadata/layout.conf' % overlay)['masters'].split()
      except (KeyError, IOError):
        masters = []
      overlays[name] = {
          'masters': masters,
          'path': overlay,
      }

  # Easy enough -- dump them all.
  if board is None:
    return [x['path'] for x in overlays.values()]

  # Build up the list of repos we need.
  ret = []
  seen = set()
  def _AddRepo(repo, optional=False):
    """Recursively add |repo|'s masters from |overlays| to |ret|.

    Args:
      repo: The repo name to look up.
      optional: If |repo| does not exist, return False, else
        raise an MissingOverlayException.

    Returns:
      True if |repo| was found.
    """
    if repo not in overlays:
      if optional:
        return False
      else:
        raise MissingOverlayException('%s was not found' % repo)

    for master in overlays[repo]['masters'] + [repo]:
      if master not in seen:
        seen.add(master)
        _AddRepo(master)
        ret.append(overlays[master]['path'])
        if not master.endswith('-private'):
          _AddRepo('%s-private' % master, True)
    return True

  # Legacy: load the global configs.  In the future, this should be found
  # via the overlay's masters.
  _AddRepo('chromeos', optional=True)
  path = os.path.join(buildroot, 'src', 'private-overlays',
                      'chromeos-*-overlay')
  ret += glob.glob(path)
  _AddRepo('chromiumos')
  _AddRepo('portage-stable')

  # Locate the board repo by name.
  # Load the public & private versions if available.
  found_pub = _AddRepo(board, optional=True)
  found_priv = _AddRepo('%s-private' % board, optional=True)

  # If neither public nor private board was found, die.
  if not found_pub and not found_priv:
    raise MissingOverlayException('board overlay not found: %s' % board)

  return ret


def FindOverlays(overlay_type, board=None, buildroot=constants.SOURCE_ROOT):
  """Return the list of overlays to use for a given buildbot.

  The returned list of overlays will be in parent -> child order.

  Args:
    overlay_type: A string describing which overlays you want.
      'private': Just the private overlays.
      'public': Just the public overlays.
      'both': Both the public and private overlays.
    board: Board to look at.
    buildroot: Source root to find overlays.
  """
  overlays = _ListOverlays(board=board, buildroot=buildroot)
  private_prefix = _PRIVATE_PREFIX % dict(buildroot=buildroot)
  if overlay_type == constants.PRIVATE_OVERLAYS:
    return [x for x in overlays if x.startswith(private_prefix)]
  elif overlay_type == constants.PUBLIC_OVERLAYS:
    return [x for x in overlays if not x.startswith(private_prefix)]
  elif overlay_type == constants.BOTH_OVERLAYS:
    return overlays
  else:
    assert overlay_type is None
    return []


def FindOverlayFile(filename, overlay_type='both', board=None,
                    buildroot=constants.SOURCE_ROOT):
  """Attempt to find a file in the overlay directories.

  Searches through this board's overlays for the specified file. The
  overlays are searched in child -> parent order.

  Args:
    filename: Path to search for inside the overlay.
    overlay_type: A string describing which overlays you want.
      'private': Just the private overlays.
      'public': Just the public overlays.
      'both': Both the public and private overlays.
    board: Board to look at.
    buildroot: Source root to find overlays.

  Returns:
    Path to the first file found in the search. None if the file is not found.
  """
  for overlay in reversed(FindOverlays(overlay_type, board, buildroot)):
    if os.path.isfile(os.path.join(overlay, filename)):
      return os.path.join(overlay, filename)
  return None


def ReadOverlayFile(filename, overlay_type='both', board=None,
                    buildroot=constants.SOURCE_ROOT):
  """Attempt to open a file in the overlay directories.

  Searches through this board's overlays for the specified file. The
  overlays are searched in child -> parent order.

  Args:
    filename: Path to open inside the overlay.
    overlay_type: A string describing which overlays you want.
      'private': Just the private overlays.
      'public': Just the public overlays.
      'both': Both the public and private overlays.
    board: Board to look at.
    buildroot: Source root to find overlays.

  Returns:
    The contents of the file, or None if no files could be opened.
  """
  file_found = FindOverlayFile(filename, overlay_type, board, buildroot)
  if file_found is None:
    return None
  return osutils.ReadFile(file_found)


def FindPrimaryOverlay(overlay_type, board, buildroot=constants.SOURCE_ROOT):
  """Return the primary overlay to use for a given buildbot.

  An overlay is only considered a primary overlay if it has a make.conf and a
  toolchain.conf. If multiple primary overlays are found, the first primary
  overlay is returned.

  Args:
    overlay_type: A string describing which overlays you want.
      'private': Just the private overlays.
      'public': Just the public overlays.
      'both': Both the public and private overlays.
    board: Board to look at.
    buildroot: Path to root of build directory.

  Raises:
    MissingOverlayException: No primary overlay found.
  """
  for overlay in FindOverlays(overlay_type, board, buildroot):
    if (os.path.exists(os.path.join(overlay, 'make.conf')) and
        os.path.exists(os.path.join(overlay, 'toolchain.conf'))):
      return overlay
  raise MissingOverlayException('No primary overlay found for board=%r' % board)


def GetOverlayName(overlay):
  """Get the self-declared repo name for the |overlay| path."""
  try:
    return cros_build_lib.LoadKeyValueFile(
        '%s/metadata/layout.conf' % overlay)['repo-name']
  except (KeyError, IOError):
    # Not all layout.conf files have a repo-name, so don't make a fuss.
    try:
      with open(os.path.join(overlay, 'profiles', 'repo_name')) as f:
        return f.readline().rstrip()
    except IOError:
      # Not all overlays have a repo_name, so don't make a fuss.
      return None


class EBuildVersionFormatException(Exception):
  """Exception for bad ebuild version string format."""

  def __init__(self, filename):
    self.filename = filename
    message = ('Ebuild file name %s '
               'does not match expected format.' % filename)
    super(EBuildVersionFormatException, self).__init__(message)


class EbuildFormatIncorrectException(Exception):
  """Exception for bad ebuild format."""

  def __init__(self, filename, message):
    message = 'Ebuild %s has invalid format: %s ' % (filename, message)
    super(EbuildFormatIncorrectException, self).__init__(message)


class EBuild(object):
  """Wrapper class for information about an ebuild."""

  VERBOSE = False
  _PACKAGE_VERSION_PATTERN = re.compile(
      r'.*-(([0-9][0-9a-z_.]*)(-r[0-9]+)?)[.]ebuild')
  _WORKON_COMMIT_PATTERN = re.compile(r'^CROS_WORKON_COMMIT="(.*)"$')

  # A structure to hold computed values of CROS_WORKON_*.
  CrosWorkonVars = collections.namedtuple(
      'CrosWorkonVars', ('localname', 'project', 'subdir', 'always_live'))

  @classmethod
  def _Print(cls, message):
    """Verbose print function."""
    if cls.VERBOSE:
      cros_build_lib.Info(message)

  @classmethod
  def _RunCommand(cls, command, **kwargs):
    kwargs.setdefault('capture_output', True)
    return cros_build_lib.RunCommand(
        command, print_cmd=cls.VERBOSE, **kwargs).output

  @classmethod
  def _RunGit(cls, cwd, command, **kwargs):
    result = git.RunGit(cwd, command, print_cmd=cls.VERBOSE, **kwargs)
    return None if result is None else result.output

  def IsSticky(self):
    """Returns True if the ebuild is sticky."""
    return self.is_stable and self.current_revision == 0

  @classmethod
  def UpdateEBuild(cls, ebuild_path, variables, redirect_file=None,
                   make_stable=True):
    """Static function that updates WORKON information in the ebuild.

    This function takes an ebuild_path and updates WORKON information.

    Args:
      ebuild_path: The path of the ebuild.
      variables: Dictionary of variables to update in ebuild.
      redirect_file: Optionally redirect output of new ebuild somewhere else.
      make_stable: Actually make the ebuild stable.
    """
    written = False
    for line in fileinput.input(ebuild_path, inplace=1):
      # Has to be done here to get changes to sys.stdout from fileinput.input.
      if not redirect_file:
        redirect_file = sys.stdout

      # Always add variables at the top of the ebuild, before the first
      # nonblank line other than the EAPI line.
      if not written and not _blank_or_eapi_re.match(line):
        for key, value in sorted(variables.items()):
          assert key is not None and value is not None
          redirect_file.write('%s=%s\n' % (key, value))
        written = True

      # Mark KEYWORDS as stable by removing ~'s.
      if line.startswith('KEYWORDS=') and make_stable:
        line = line.replace('~', '')

      varname, eq, _ = line.partition('=')
      if not (eq == '=' and varname.strip() in variables):
        # Don't write out the old value of the variable.
        redirect_file.write(line)

    fileinput.close()

  @classmethod
  def MarkAsStable(cls, unstable_ebuild_path, new_stable_ebuild_path,
                   variables, redirect_file=None, make_stable=True):
    """Static function that creates a revved stable ebuild.

    This function assumes you have already figured out the name of the new
    stable ebuild path and then creates that file from the given unstable
    ebuild and marks it as stable.  If the commit_value is set, it also
    set the commit_keyword=commit_value pair in the ebuild.

    Args:
      unstable_ebuild_path: The path to the unstable ebuild.
      new_stable_ebuild_path: The path you want to use for the new stable
        ebuild.
      variables: Dictionary of variables to update in ebuild.
      redirect_file: Optionally redirect output of new ebuild somewhere else.
      make_stable: Actually make the ebuild stable.
    """
    shutil.copyfile(unstable_ebuild_path, new_stable_ebuild_path)
    EBuild.UpdateEBuild(new_stable_ebuild_path, variables, redirect_file,
                        make_stable)

  @classmethod
  def CommitChange(cls, message, overlay):
    """Commits current changes in git locally with given commit message.

    Args:
      message: the commit string to write when committing to git.
      overlay: directory in which to commit the changes.

    Raises:
      RunCommandError: Error occurred while committing.
    """
    logging.info('Committing changes with commit message: %s', message)
    git_commit_cmd = ['commit', '-a', '-m', message]
    cls._RunGit(overlay, git_commit_cmd)

  def __init__(self, path):
    """Sets up data about an ebuild from its path.

    Args:
      path: Path to the ebuild.
    """
    self.overlay, self.category, self.pkgname, filename = path.rsplit('/', 3)
    m = self._PACKAGE_VERSION_PATTERN.match(filename)
    if not m:
      raise EBuildVersionFormatException(filename)
    self.version, self.version_no_rev, revision = m.groups()
    if revision is not None:
      self.current_revision = int(revision.replace('-r', ''))
    else:
      self.current_revision = 0
    self.package = '%s/%s' % (self.category, self.pkgname)

    self._ebuild_path_no_version = os.path.join(
        os.path.dirname(path), self.pkgname)
    self.ebuild_path_no_revision = '%s-%s' % (
        self._ebuild_path_no_version, self.version_no_rev)
    self._unstable_ebuild_path = '%s%s' % (
        self._ebuild_path_no_version, WORKON_EBUILD_SUFFIX)
    self.ebuild_path = path

    self.is_workon = False
    self.is_stable = False
    self.is_blacklisted = False
    self._ReadEBuild(path)

  @staticmethod
  def Classify(ebuild_path):
    """Return whether this ebuild is workon, stable, and/or blacklisted

    workon is determined by whether the ebuild inherits from the
    'cros-workon' eclass. stable is determined by whether there's a '~'
    in the KEYWORDS setting in the ebuild. An ebuild is considered blacklisted
    if a line in it starts with 'CROS_WORKON_BLACKLIST='
    """
    is_workon = False
    is_stable = False
    is_blacklisted = False
    for line in fileinput.input(ebuild_path):
      if line.startswith('inherit ') and 'cros-workon' in line:
        is_workon = True
      elif line.startswith('KEYWORDS='):
        for keyword in line.split('=', 1)[1].strip("\"'").split():
          if not keyword.startswith('~') and keyword != '-*':
            is_stable = True
      elif line.startswith('CROS_WORKON_BLACKLIST='):
        is_blacklisted = True
    fileinput.close()
    return is_workon, is_stable, is_blacklisted

  def _ReadEBuild(self, path):
    """Determine the settings of `is_workon`, `is_stable` and is_blacklisted

    These are determined using the static Classify function.
    """
    self.is_workon, self.is_stable, self.is_blacklisted = EBuild.Classify(path)

  @staticmethod
  def GetCrosWorkonVars(ebuild_path, pkg_name):
    """Return computed (as sourced ebuild script) values of:

      * CROS_WORKON_LOCALNAME
      * CROS_WORKON_PROJECT
      * CROS_WORKON_SUBDIR
      * CROS_WORKON_ALWAYS_LIVE

    Args:
      ebuild_path: Path to the ebuild file (e.g: platform2-9999.ebuild).
      pkg_name: The package name (e.g.: platform2).

    Returns:
      A CrosWorkonVars tuple.
    """
    workon_vars = (
        'CROS_WORKON_LOCALNAME',
        'CROS_WORKON_PROJECT',
        'CROS_WORKON_SUBDIR',
        'CROS_WORKON_ALWAYS_LIVE',
    )
    env = {
        'CROS_WORKON_LOCALNAME': pkg_name,
        'CROS_WORKON_SUBDIR': '',
        'CROS_WORKON_ALWAYS_LIVE': '',
    }
    settings = osutils.SourceEnvironment(ebuild_path, workon_vars, env=env)
    # Try to detect problems extracting the variables by checking whether
    # CROS_WORKON_PROJECT is set. If it isn't, something went wrong, possibly
    # because we're simplistically sourcing the ebuild without most of portage
    # being available. That still breaks this script and needs to be flagged
    # as an error. We won't catch problems setting CROS_WORKON_LOCALNAME or
    # CROS_WORKON_SUBDIR or if CROS_WORKON_PROJECT is set to the wrong thing,
    # but at least this covers some types of failures.
    if 'CROS_WORKON_PROJECT' not in settings:
      raise EbuildFormatIncorrectException(
          ebuild_path, 'Unable to determine CROS_WORKON_PROJECT value.')
    localnames = settings['CROS_WORKON_LOCALNAME'].split(',')
    projects = settings['CROS_WORKON_PROJECT'].split(',')
    subdirs = settings['CROS_WORKON_SUBDIR'].split(',')
    live = settings['CROS_WORKON_ALWAYS_LIVE']

    return EBuild.CrosWorkonVars(localnames, projects, subdirs, live)

  def GetSourcePath(self, srcroot, manifest):
    """Get the project and path for this ebuild.

    The path is guaranteed to exist, be a directory, and be absolute.
    """

    localnames, projects, subdirs, always_live = EBuild.GetCrosWorkonVars(
        self._unstable_ebuild_path, self.pkgname)

    if always_live:
      return [], []

    # Sanity checks and completion.
    # Each project specification has to have the same amount of items.
    if len(projects) != len(localnames):
      raise EbuildFormatIncorrectException(
          self._unstable_ebuild_path,
          'Number of _PROJECT and _LOCALNAME items don\'t match.')
    # Subdir must be either 0,1 or len(project)
    if len(projects) != len(subdirs) and len(subdirs) > 1:
      raise EbuildFormatIncorrectException(
          self._unstable_ebuild_path, 'Incorrect number of _SUBDIR items.')
    # If there's one, apply it to all.
    if len(subdirs) == 1:
      subdirs = subdirs * len(projects)
    # If there is none, make an empty list to avoid exceptions later.
    if len(subdirs) == 0:
      subdirs = [''] * len(projects)

    # Calculate srcdir.
    if self.category in ('chromeos-base', 'brillo-base'):
      dir_ = '' # 'platform2'
    else:
      dir_ = 'third_party'

    # Once all targets are moved from platform to platform2, uncomment
    # the following lines as well as dir_ = 'platform2' above,
    # and delete the loop that builds |subdir_paths| below.

    # subdir_paths = [os.path.realpath(os.path.join(srcroot, dir_, l, s))
    #                for l, s in zip(localnames, subdirs)]

    subdir_paths = []
    for local, sub in zip(localnames, subdirs):
      subdir_path = os.path.realpath(os.path.join(srcroot, dir_, local, sub))
      if dir_ == '' and not os.path.isdir(subdir_path):
        subdir_path = os.path.realpath(os.path.join(srcroot, 'platform',
                                                    local, sub))
      subdir_paths.append(subdir_path)

    for subdir_path, project in zip(subdir_paths, projects):
      if not os.path.isdir(subdir_path):
        cros_build_lib.Die('Source repository %s '
                           'for project %s does not exist.' % (subdir_path,
                                                               self.pkgname))
      # Verify that we're grabbing the commit id from the right project name.
      real_project = manifest.FindCheckoutFromPath(subdir_path)['name']
      if project != real_project:
        cros_build_lib.Die('Project name mismatch for %s '
                           '(found %s, expected %s)' % (subdir_path,
                                                        real_project,
                                                        project))

    return projects, subdir_paths

  def GetCommitId(self, srcdir):
    """Get the commit id for this ebuild."""
    output = self._RunGit(srcdir, ['rev-parse', 'HEAD'])
    if not output:
      cros_build_lib.Die('Cannot determine HEAD commit for %s' % srcdir)
    return output.rstrip()

  def GetTreeId(self, srcdir):
    """Get the SHA1 of the source tree for this ebuild.

    Unlike the commit hash, the SHA1 of the source tree is unaffected by the
    history of the repository, or by commit messages.
    """
    output = self._RunGit(srcdir, ['log', '-1', '--format=%T'])
    if not output:
      cros_build_lib.Die('Cannot determine HEAD tree hash for %s' % srcdir)
    return output.rstrip()

  def GetVersion(self, srcroot, manifest, default):
    """Get the base version number for this ebuild.

    The version is provided by the ebuild through a specific script in
    the $FILESDIR (chromeos-version.sh).
    """
    vers_script = os.path.join(os.path.dirname(self._ebuild_path_no_version),
                               'files', 'chromeos-version.sh')

    if not os.path.exists(vers_script):
      return default

    if not self.is_workon:
      raise EbuildFormatIncorrectException(
          self._ebuild_path_no_version,
          'Package has a chromeos-version.sh script but is not workon-able.')

    srcdirs = self.GetSourcePath(srcroot, manifest)[1]

    # The chromeos-version script will output a usable raw version number,
    # or nothing in case of error or no available version
    try:
      output = self._RunCommand([vers_script] + srcdirs).strip()
    except cros_build_lib.RunCommandError as e:
      cros_build_lib.Die('Package %s chromeos-version.sh failed: %s' %
                         (self.pkgname, e))

    if not output:
      cros_build_lib.Die('Package %s has a chromeos-version.sh script but '
                         'it returned no valid version for "%s"' %
                         (self.pkgname, ' '.join(srcdirs)))

    return output

  @staticmethod
  def FormatBashArray(unformatted_list):
    """Returns a python list in a bash array format.

    If the list only has one item, format as simple quoted value.
    That is both backwards-compatible and more readable.

    Args:
      unformatted_list: an iterable to format as a bash array. This variable
        has to be sanitized first, as we don't do any safeties.

    Returns:
      A text string that can be used by bash as array declaration.
    """
    if len(unformatted_list) > 1:
      return '("%s")' % '" "'.join(unformatted_list)
    else:
      return '"%s"' % unformatted_list[0]

  def RevWorkOnEBuild(self, srcroot, manifest, redirect_file=None):
    """Revs a workon ebuild given the git commit hash.

    By default this class overwrites a new ebuild given the normal
    ebuild rev'ing logic.  However, a user can specify a redirect_file
    to redirect the new stable ebuild to another file.

    Args:
      srcroot: full path to the 'src' subdirectory in the source
        repository.
      manifest: git.ManifestCheckout object.
      redirect_file: Optional file to write the new ebuild.  By default
        it is written using the standard rev'ing logic.  This file must be
        opened and closed by the caller.

    Returns:
      If the revved package is different than the old ebuild, return the full
      revved package name, including the version number. Otherwise, return None.

    Raises:
      OSError: Error occurred while creating a new ebuild.
      IOError: Error occurred while writing to the new revved ebuild file.
    """

    if self.is_stable:
      stable_version_no_rev = self.GetVersion(srcroot, manifest,
                                              self.version_no_rev)
    else:
      # If given unstable ebuild, use preferred version rather than 9999.
      stable_version_no_rev = self.GetVersion(srcroot, manifest, '0.0.1')

    new_version = '%s-r%d' % (
        stable_version_no_rev, self.current_revision + 1)
    new_stable_ebuild_path = '%s-%s.ebuild' % (
        self._ebuild_path_no_version, new_version)

    self._Print('Creating new stable ebuild %s' % new_stable_ebuild_path)
    if not os.path.exists(self._unstable_ebuild_path):
      cros_build_lib.Die('Missing unstable ebuild: %s' %
                         self._unstable_ebuild_path)

    srcdirs = self.GetSourcePath(srcroot, manifest)[1]
    commit_ids = map(self.GetCommitId, srcdirs)
    tree_ids = map(self.GetTreeId, srcdirs)
    variables = dict(CROS_WORKON_COMMIT=self.FormatBashArray(commit_ids),
                     CROS_WORKON_TREE=self.FormatBashArray(tree_ids))
    self.MarkAsStable(self._unstable_ebuild_path, new_stable_ebuild_path,
                      variables, redirect_file)

    old_ebuild_path = self.ebuild_path
    if filecmp.cmp(old_ebuild_path, new_stable_ebuild_path, shallow=False):
      os.unlink(new_stable_ebuild_path)
      return None
    else:
      self._Print('Adding new stable ebuild to git')
      self._RunGit(self.overlay, ['add', new_stable_ebuild_path])

      if self.is_stable:
        self._Print('Removing old ebuild from git')
        self._RunGit(self.overlay, ['rm', old_ebuild_path])

      return '%s-%s' % (self.package, new_version)

  @classmethod
  def GitRepoHasChanges(cls, directory):
    """Returns True if there are changes in the given directory."""
    # Refresh the index first. This squashes just metadata changes.
    cls._RunGit(directory, ['update-index', '-q', '--refresh'])
    output = cls._RunGit(directory, ['diff-index', '--name-only', 'HEAD'])
    return output not in [None, '']

  @staticmethod
  def _GetSHA1ForPath(manifest, path):
    """Get the latest SHA1 for a given project from Gerrit.

    This function looks up the remote and branch for a given project in the
    manifest, and uses this to lookup the SHA1 from Gerrit. This only makes
    sense for unpinned manifests.

    Args:
      manifest: git.ManifestCheckout object.
      path: Path of project.

    Raises:
      Exception if the manifest is pinned.
    """
    checkout = manifest.FindCheckoutFromPath(path)
    project = checkout['name']
    helper = gerrit.GetGerritHelper(checkout['remote'])
    manifest_branch = checkout['revision']
    branch = git.StripRefsHeads(manifest_branch)
    return helper.GetLatestSHA1ForBranch(project, branch)

  @staticmethod
  def _GetEBuildPaths(buildroot, manifest, overlay_list, changes):
    """Calculate ebuild->path map for changed ebuilds.

    Args:
      buildroot: Path to root of build directory.
      manifest: git.ManifestCheckout object.
      overlay_list: List of all overlays.
      changes: Changes from Gerrit that are being pushed.

    Returns:
      A dictionary mapping changed ebuilds to lists of associated paths.
    """
    directory_src = os.path.join(buildroot, 'src')
    overlay_dict = dict((o, []) for o in overlay_list)
    BuildEBuildDictionary(overlay_dict, True, None)
    changed_paths = set(c.GetCheckout(manifest).GetPath(absolute=True)
                        for c in changes)
    ebuild_projects = {}
    for ebuilds in overlay_dict.itervalues():
      for ebuild in ebuilds:
        _projects, paths = ebuild.GetSourcePath(directory_src, manifest)
        if changed_paths.intersection(paths):
          ebuild_projects[ebuild] = paths

    return ebuild_projects

  @classmethod
  def UpdateCommitHashesForChanges(cls, changes, buildroot, manifest):
    """Updates the commit hashes for the EBuilds uprevved in changes.

    Args:
      changes: Changes from Gerrit that are being pushed.
      buildroot: Path to root of build directory.
      manifest: git.ManifestCheckout object.
    """
    path_sha1s = {}
    overlay_list = FindOverlays(constants.BOTH_OVERLAYS, buildroot=buildroot)
    ebuild_paths = cls._GetEBuildPaths(buildroot, manifest, overlay_list,
                                       changes)
    for ebuild, paths in ebuild_paths.iteritems():
      # Calculate any SHA1s that are not already in path_sha1s.
      for path in set(paths).difference(path_sha1s):
        path_sha1s[path] = cls._GetSHA1ForPath(manifest, path)

      sha1s = [path_sha1s[path] for path in paths]
      logging.info('Updating ebuild for package %s with commit hashes %r',
                   ebuild.package, sha1s)
      updates = dict(CROS_WORKON_COMMIT=cls.FormatBashArray(sha1s))
      EBuild.UpdateEBuild(ebuild.ebuild_path, updates)

    # Commit any changes to all overlays.
    for overlay in overlay_list:
      if EBuild.GitRepoHasChanges(overlay):
        EBuild.CommitChange('Updating commit hashes in ebuilds '
                            'to match remote repository.', overlay=overlay)


class PortageDBException(Exception):
  """Generic PortageDB error."""


class PortageDB(object):
  """Wrapper class to access the portage database located in var/db/pkg."""

  def __init__(self, root='/'):
    """Initialize the internal structure for the database in the given root.

    Args:
      root: The path to the root to inspect, for example "/build/foo".
    """
    self.root = root
    self.db_path = os.path.join(root, 'var/db/pkg')
    self._ebuilds = {}

  def GetInstalledPackage(self, category, pv):
    """Get the InstalledPackage instance for the passed package.

    Args:
      category: The category of the package. For example "chromeos-base".
      pv: The package name with the version (and revision) of the
          installed package. For example "libchrome-271506-r5".

    Returns:
      An InstalledPackage instance for the requested package or None if the
      requested package is not found.
    """
    pkg_key = '%s/%s' % (category, pv)
    if pkg_key in self._ebuilds:
      return self._ebuilds[pkg_key]

    # Create a new InstalledPackage instance and cache it.
    pkgdir = os.path.join(self.db_path, category, pv)
    try:
      pkg = InstalledPackage(self, pkgdir, category, pv)
    except PortageDBException:
      return None
    self._ebuilds[pkg_key] = pkg
    return pkg

  def InstalledPackages(self):
    """Lists all portage packages in the database.

    Returns:
      A list of InstalledPackage instances for each package in the database.
    """
    ebuild_pattern = os.path.join(self.db_path, '*/*/*.ebuild')
    packages = []

    for path in glob.glob(ebuild_pattern):
      category, pf, packagecheck = SplitEbuildPath(path)
      if not _category_re.match(category):
        continue
      if pf != packagecheck:
        continue
      pkg_key = '%s/%s' % (category, pf)
      if pkg_key not in self._ebuilds:
        self._ebuilds[pkg_key] = InstalledPackage(
            self, os.path.join(self.db_path, category, pf),
            category, pf)
      packages.append(self._ebuilds[pkg_key])

    return packages


class InstalledPackage(object):
  """Wrapper class for information about an installed package.

  This class accesses the information provided by var/db/pkg for an installed
  ebuild, such as the list of files installed by this package.
  """

  # "type" constants for the ListContents() return value.
  OBJ = 'obj'
  SYM = 'sym'
  DIR = 'dir'

  def __init__(self, portage_db, pkgdir, category=None, pf=None):
    """Initialize the installed ebuild wrapper.

    Args:
      portage_db: The PortageDB instance where the ebuild is installed. This
          is used to query the database about other installed ebuilds, for
          example, the ones listed in DEPEND, but otherwise it isn't used.
      pkgdir: The directory where the installed package resides. This could be
          for example a directory like "var/db/pkg/category/pf" or the
          "build-info" directory in the portage temporary directory where
          the package is being built.
      category: The category of the package. If omitted, it will be loaded from
          the package contents.
      pf: The package and version of the package. If omitted, it will be loaded
          from the package contents. This avoids unncessary lookup when this
          value is known.

    Raises:
      PortageDBException if the pkgdir doesn't contain a valid package.
    """
    self._portage_db = portage_db
    self.pkgdir = pkgdir
    self._fields = {}
    # Prepopulate the field cache with the category and pf (if provided).
    if not category is None:
      self._fields['CATEGORY'] = category
    if not pf is None:
      self._fields['PF'] = pf

    if self.pf is None:
      raise PortageDBException("Package doesn't contain package-version value.")

    # Check that the ebuild is present.
    ebuild_path = os.path.join(self.pkgdir, '%s.ebuild' % self.pf)
    if not os.path.exists(ebuild_path):
      raise PortageDBException("Package doesn't contain an ebuild file.")

    split_pv = SplitPV(self.pf)
    if split_pv is None:
      raise PortageDBException('Package and version "%s" doesn\'t have a valid '
                               'format.' % self.pf)
    self.package = split_pv.package
    self.version = split_pv.version

  def _ReadField(self, field_name):
    """Reads the contents of the file in the installed package directory.

    Args:
      field_name: The name of the field to read, for example, 'SLOT' or
          'LICENSE'.

    Returns:
      A string with the contents of the file. The contents of the file are
      cached in _fields. If the file doesn't exists returns None.
    """
    if field_name not in self._fields:
      try:
        value = osutils.ReadFile(os.path.join(self.pkgdir, field_name))
      except IOError as e:
        if e.errno != errno.ENOENT:
          raise
        value = None
      self._fields[field_name] = value
    return self._fields[field_name]

  @property
  def category(self):
    return self._ReadField('CATEGORY')

  @property
  def pf(self):
    return self._ReadField('PF')

  def ListContents(self):
    """List of files and directories installed by this package.

    Returns:
      A list of tuples (file_type, path) where the file_type is a string
      determining the type of the installed file: InstalledPackage.OBJ (regular
      files), InstalledPackage.SYM (symlinks) or InstalledPackage.DIR
      (directory), and path is the relative path of the file to the root like
      'usr/bin/ls'.
    """
    path = os.path.join(self.pkgdir, 'CONTENTS')
    if not os.path.exists(path):
      return []

    result = []
    for line in open(path):
      line = line.strip()
      # Line format is: "type file_path [more space-separated fields]".
      # Discard any other line without at least the first two fields. The
      # remaining fields depend on the type.
      typ, data = line.split(' ', 1)
      if typ == self.OBJ:
        file_path, _file_hash, _mtime = data.rsplit(' ', 2)
      elif typ == self.DIR:
        file_path = data
      elif typ == self.SYM:
        file_path, _ = data.split(' -> ', 1)
      else:
        # Unknown type.
        continue
      result.append((typ, file_path.lstrip('/')))

    return result


def BestEBuild(ebuilds):
  """Returns the newest EBuild from a list of EBuild objects."""
  from portage.versions import vercmp
  winner = ebuilds[0]
  for ebuild in ebuilds[1:]:
    if vercmp(winner.version, ebuild.version) < 0:
      winner = ebuild
  return winner


def _FindUprevCandidates(files):
  """Return the uprev candidate ebuild from a specified list of files.

  Usually an uprev candidate is a the stable ebuild in a cros_workon
  directory.  However, if no such stable ebuild exists (someone just
  checked in the 9999 ebuild), this is the unstable ebuild.

  If the package isn't a cros_workon package, return None.

  Args:
    files: List of files in a package directory.
  """
  stable_ebuilds = []
  unstable_ebuilds = []
  for path in files:
    if not path.endswith('.ebuild') or os.path.islink(path):
      continue
    ebuild = EBuild(path)
    if not ebuild.is_workon or ebuild.is_blacklisted:
      continue
    if ebuild.is_stable:
      if ebuild.version == WORKON_EBUILD_VERSION:
        cros_build_lib.Die('KEYWORDS in %s ebuild should not be stable %s'
                           % (WORKON_EBUILD_VERSION, path))
      stable_ebuilds.append(ebuild)
    else:
      unstable_ebuilds.append(ebuild)

  # If both ebuild lists are empty, the passed in file list was for
  # a non-workon package.
  if not unstable_ebuilds:
    if stable_ebuilds:
      path = os.path.dirname(stable_ebuilds[0].ebuild_path)
      cros_build_lib.Die(
          'Missing %s ebuild in %s' % (WORKON_EBUILD_VERSION, path))
    return None

  path = os.path.dirname(unstable_ebuilds[0].ebuild_path)
  if len(unstable_ebuilds) > 1:
    cros_build_lib.Die('Found multiple unstable ebuilds in %s' % path)

  if not stable_ebuilds:
    cros_build_lib.Warning('Missing stable ebuild in %s' % path)
    return unstable_ebuilds[0]

  if len(stable_ebuilds) == 1:
    return stable_ebuilds[0]

  stable_versions = set(ebuild.version_no_rev for ebuild in stable_ebuilds)
  if len(stable_versions) > 1:
    package = stable_ebuilds[0].package
    message = 'Found multiple stable ebuild versions in %s:' % path
    for version in stable_versions:
      message += '\n    %s-%s' % (package, version)
    cros_build_lib.Die(message)

  uprev_ebuild = max(stable_ebuilds, key=lambda eb: eb.current_revision)
  for ebuild in stable_ebuilds:
    if ebuild != uprev_ebuild:
      cros_build_lib.Warning('Ignoring stable ebuild revision %s in %s' %
                             (ebuild.version, path))
  return uprev_ebuild


def BuildEBuildDictionary(overlays, use_all, packages):
  """Build a dictionary of the ebuilds in the specified overlays.

  Args:
    overlays: A map which maps overlay directories to arrays of stable EBuilds
      inside said directories.
    use_all: Whether to include all ebuilds in the specified directories.
      If true, then we gather all packages in the directories regardless
      of whether they are in our set of packages.
    packages: A set of the packages we want to gather.  If use_all is
      True, this argument is ignored, and should be None.
  """
  for overlay in overlays:
    for package_dir, _dirs, files in os.walk(overlay):
      # Add stable ebuilds to overlays[overlay].
      paths = [os.path.join(package_dir, path) for path in files]
      ebuild = _FindUprevCandidates(paths)

      # If the --all option isn't used, we only want to update packages that
      # are in packages.
      if ebuild and (use_all or ebuild.package in packages):
        overlays[overlay].append(ebuild)


def RegenCache(overlay):
  """Regenerate the cache of the specified overlay.

  Args:
    overlay: The tree to regenerate the cache for.
  """
  repo_name = GetOverlayName(overlay)
  if not repo_name:
    return

  layout = cros_build_lib.LoadKeyValueFile('%s/metadata/layout.conf' % overlay,
                                           ignore_missing=True)
  if layout.get('cache-format') != 'md5-dict':
    return

  # Regen for the whole repo.
  cros_build_lib.RunCommand(['egencache', '--update', '--repo', repo_name,
                             '--jobs', str(multiprocessing.cpu_count())])
  # If there was nothing new generated, then let's just bail.
  result = git.RunGit(overlay, ['status', '-s', 'metadata/'])
  if not result.output:
    return
  # Explicitly add any new files to the index.
  git.RunGit(overlay, ['add', 'metadata/'])
  # Explicitly tell git to also include rm-ed files.
  git.RunGit(overlay, ['commit', '-m', 'regen cache', 'metadata/'])


def ParseBashArray(value):
  """Parse a valid bash array into python list."""
  # The syntax for bash arrays is nontrivial, so let's use bash to do the
  # heavy lifting for us.
  sep = ','
  # Because %s may contain bash comments (#), put a clever newline in the way.
  cmd = 'ARR=%s\nIFS=%s; echo -n "${ARR[*]}"' % (value, sep)
  return cros_build_lib.RunCommand(
      cmd, print_cmd=False, shell=True, capture_output=True).output.split(sep)


def WorkonEBuildGeneratorForDirectory(base_dir):
  """Yields cros_workon EBuilds in |base_dir|.

  Args:
    base_dir: Path to the base directory.

  Yields:
    A cros_workon EBuild instance.
  """
  for root, _, files in os.walk(base_dir):
    for filename in files:
      # Only look at *-9999.ebuild files.
      if filename.endswith(WORKON_EBUILD_SUFFIX):
        full_path = os.path.join(root, filename)
        ebuild = EBuild(full_path)
        if not ebuild.is_workon:
          continue
        yield ebuild


def WorkonEBuildGenerator(buildroot, overlay_type):
  """Scans all overlays and yields cros_workon EBuilds.

  Args:
    buildroot: Path to source root to find overlays.
    overlay_type: The type of overlay to use (one of
      constants.VALID_OVERLAYS).

  Yields:
    A cros_workon EBuild instance.
  """
  # Get the list of all overlays.
  overlays = FindOverlays(overlay_type, buildroot=buildroot)
  # Iterate through overlays and gather all workon ebuilds
  for overlay in overlays:
    for ebuild in WorkonEBuildGeneratorForDirectory(overlay):
      yield ebuild


def BuildFullWorkonPackageDictionary(buildroot, overlay_type, manifest):
  """Scans all cros_workon ebuilds and build a dictionary.

  Args:
    buildroot: Path to source root to find overlays.
    overlay_type: The type of overlay to use (one of
      constants.VALID_OVERLAYS).
    manifest: git.ManifestCheckout object.

  Returns:
    A dictionary mapping (project, branch) to a list of packages.
    E.g., {('chromiumos/third_party/kernel', 'chromeos-3.14'):
           ['sys-kernel/chromeos-kernel-3_14']}.
  """
  # we want (project, branch) -> package (CP or P?)
  directory_src = os.path.join(buildroot, 'src')

  pkg_map = dict()
  for ebuild in WorkonEBuildGenerator(buildroot, overlay_type):
    if ebuild.is_blacklisted:
      continue
    package = ebuild.package
    _, paths = ebuild.GetSourcePath(directory_src, manifest)
    for path in paths:
      checkout = manifest.FindCheckoutFromPath(path)
      project = checkout['name']
      branch = git.StripRefs(checkout['tracking_branch'])
      pkg_list = pkg_map.get((project, branch), [])
      pkg_list.append(package)
      pkg_map[(project, branch)] = pkg_list

  return pkg_map


def GetWorkonProjectMap(overlay, subdirectories):
  """Get the project -> ebuild mapping for cros_workon ebuilds.

  Args:
    overlay: Overlay to look at.
    subdirectories: List of subdirectories to look in on the overlay.

  Yields:
    A list of (filename, projects) tuples for cros-workon ebuilds in the
    given overlay under the given subdirectories.
  """
  # Search ebuilds for project names, ignoring non-existent directories.
  # Also filter out ebuilds which are not cros_workon.
  for subdir in subdirectories:
    base_dir = os.path.join(overlay, subdir)
    for ebuild in WorkonEBuildGeneratorForDirectory(base_dir):
      full_path = ebuild.ebuild_path
      _, projects, _, _ = EBuild.GetCrosWorkonVars(full_path,
                                                   ebuild.pkgname)
      relpath = os.path.relpath(full_path, start=overlay)
      yield relpath, projects


def SplitEbuildPath(path):
  """Split an ebuild path into its components.

  Given a specified ebuild filename, returns $CATEGORY, $PN, $P. It does not
  perform any check on ebuild name elements or their validity, merely splits
  a filename, absolute or relative, and returns the last 3 components.

  Example: For /any/path/chromeos-base/power_manager/power_manager-9999.ebuild,
  returns ('chromeos-base', 'power_manager', 'power_manager-9999').

  Args:
    path: Path to the ebuild.

  Returns:
    $CATEGORY, $PN, $P
  """
  return os.path.splitext(path)[0].rsplit('/', 3)[-3:]


def SplitPV(pv, strict=True):
  """Takes a PV value and splits it into individual components.

  Args:
    pv: Package name and version.
    strict: If True, returns None if version or package name is missing.
      Otherwise, only package name is mandatory.

  Returns:
    A collection with named members:
      pv, package, version, version_no_rev, rev
  """
  m = _pvr_re.match(pv)

  if m is None and strict:
    return None

  if m is None:
    return PV(**{'pv': None, 'package': pv, 'version': None,
                 'version_no_rev': None, 'rev': None})

  return PV(**m.groupdict())


def SplitCPV(cpv, strict=True):
  """Splits a CPV value into components.

  Args:
    cpv: Category, package name, and version of a package.
    strict: If True, returns None if any of the components is missing.
      Otherwise, only package name is mandatory.

  Returns:
    A collection with named members:
      category, pv, package, version, version_no_rev, rev
  """
  chunks = cpv.split('/')
  if len(chunks) > 2:
    raise ValueError('Unexpected package format %s' % cpv)
  if len(chunks) == 1:
    category = None
  else:
    category = chunks[0]

  m = SplitPV(chunks[-1], strict=strict)
  if strict and (category is None or m is None):
    return None
  return CPV(category=category, **m._asdict())


def FindWorkonProjects(packages):
  """Find the projects associated with the specified cros_workon packages.

  Args:
    packages: List of cros_workon packages.

  Returns:
    The set of projects associated with the specified cros_workon packages.
  """
  all_projects = set()
  buildroot, both = constants.SOURCE_ROOT, constants.BOTH_OVERLAYS
  for overlay in FindOverlays(both, buildroot=buildroot):
    for _, projects in GetWorkonProjectMap(overlay, packages):
      all_projects.update(projects)
  return all_projects


def ListInstalledPackages(sysroot):
  """[DEPRECATED] Lists all portage packages in a given portage-managed root.

  Assumes the existence of a /var/db/pkg package database.

  This function is DEPRECATED, please use PortageDB.InstalledPackages instead.

  Args:
    sysroot: The root directory being inspected.

  Returns:
    A list of (cp,v) tuples in the given sysroot.
  """
  return [('%s/%s' % (pkg.category, pkg.package), pkg.version)
          for pkg in PortageDB(sysroot).InstalledPackages()]


def BestVisible(atom, board=None, pkg_type='ebuild',
                buildroot=constants.SOURCE_ROOT):
  """Get the best visible ebuild CPV for the given atom.

  Args:
    atom: Portage atom.
    board: Board to look at. By default, look in chroot.
    pkg_type: Package type (ebuild, binary, or installed).
    buildroot: Directory

  Returns:
    A CPV object.
  """
  portageq = 'portageq' if board is None else 'portageq-%s' % board
  root = cros_build_lib.GetSysroot(board=board)
  cmd = [portageq, 'best_visible', root, pkg_type, atom]
  result = cros_build_lib.RunCommand(
      cmd, cwd=buildroot, enter_chroot=True, debug_level=logging.DEBUG,
      capture_output=True)
  return SplitCPV(result.output.strip())


def IsPackageInstalled(package, sysroot='/'):
  """Return whether a portage package is in a given portage-managed root.

  Args:
    package: The CP to look for.
    sysroot: The root being inspected.
  """
  for key, _version in ListInstalledPackages(sysroot):
    if key == package:
      return True

  return False


def FindPackageNameMatches(pkg_str, board=None):
  """Finds a list of installed packages matching |pkg_str|.

  Args:
    pkg_str: The package name with optional category, version, and slot.
    board: The board to insepct.

  Returns:
    A list of matched CPV objects.
  """
  cmd = ['equery']
  if board:
    cmd = ['equery-%s' % board]

  cmd += ['list', pkg_str]
  result = cros_build_lib.RunCommand(
      cmd, capture_output=True, error_code_ok=True)

  matches = []
  if result.returncode == 0:
    matches = [SplitCPV(x) for x in result.output.splitlines()]

  return matches


def GetInstalledPackageUseFlags(pkg_str, board=None):
  """Gets the list of USE flags for installed packages matching |pkg_str|.

  Args:
    pkg_str: The package name with optional category, version, and slot.
    board: The board to inspect.

  Returns:
    A dictionary with the key being a package CP and the value being the list
    of USE flags for that package.
  """
  cmd = ['qlist']
  if board:
    cmd = ['qlist-%s' % board]

  cmd += ['-CqU', pkg_str]
  result = cros_build_lib.RunCommand(
      cmd, enter_chroot=True, capture_output=True, error_code_ok=True)

  use_flags = {}
  if result.returncode == 0:
    for line in result.output.splitlines():
      tokens = line.split()
      use_flags[tokens[0]] = tokens[1:]

  return use_flags


def GetBinaryPackageDir(sysroot='/', packages_dir=None):
  """Returns the binary package directory of |sysroot|."""
  dir_name = packages_dir if packages_dir else 'packages'
  return os.path.join(sysroot, dir_name)


def GetBinaryPackagePath(c, p, v, sysroot='/', packages_dir=None):
  """Returns the path to the binary package.

  Args:
    c: category.
    p: package.
    v: version.
    sysroot: The root being inspected.
    packages_dir: Name of the packages directory in |sysroot|.

  Returns:
    The path to the binary package.
  """
  pkgdir = GetBinaryPackageDir(sysroot=sysroot, packages_dir=packages_dir)
  path = os.path.join(pkgdir, c, '%s-%s.tbz2' % (p, v))
  if not os.path.exists(path):
    raise ValueError('Cannot find the binary package %s!' % path)

  return path


def CleanOutdatedBinaryPackages(board):
  """Cleans outdated binary packages for |board|."""
  return cros_build_lib.RunCommand(['eclean-%s' % board, '-d', 'packages'])
