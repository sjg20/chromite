# -*- coding: utf-8 -*-
# Copyright 2019 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Deps analysis service."""

from __future__ import print_function

import functools
import os
from pathlib import Path
import re
from typing import List, Optional

from chromite.lib import build_target_lib
from chromite.lib import constants
from chromite.lib import cros_build_lib
from chromite.lib import cros_logging
from chromite.lib import git
from chromite.lib import osutils
from chromite.lib import portage_util
from chromite.scripts import cros_extract_deps


class Error(Exception):
  """Base error class for the module."""


class MissingCacheEntry(Error):
  """No on-disk cache entry could be found for a package."""


class NoMatchingFileForDigest(Error):
  """No ebuild or eclass file could be found with the given MD5 digest."""


def NormalizeSourcePaths(source_paths):
  """Return the "normalized" form of a list of source paths.

  Normalizing includes:
    * Sorting the source paths in alphabetical order.
    * Remove paths that are sub-path of others in the source paths.
    * Ensure all the directory path strings are ended with the trailing '/'.
    * Convert all the path from absolute paths to relative path (relative to
      the chroot source root).
  """
  for i, path in enumerate(source_paths):
    assert os.path.isabs(path), 'path %s is not an aboslute path' % path
    source_paths[i] = os.path.normpath(path)

  source_paths.sort()

  results = []

  for i, path in enumerate(source_paths):
    is_subpath_of_other = False
    for j, other in enumerate(source_paths):
      if j != i and osutils.IsSubPath(path, other):
        is_subpath_of_other = True
    if not is_subpath_of_other:
      if os.path.isdir(path) and not path.endswith('/'):
        path += '/'
      path = os.path.relpath(path, constants.CHROOT_SOURCE_ROOT)
      results.append(path)

  return results


def GetRelevantEclassesForEbuild(ebuild_path, path_cache, overlay_dirs):

  # Trim '.ebuild' from the tail of the path.
  ebuild_path_no_ext, _ = os.path.splitext(ebuild_path)

  # Ebuild paths look like:
  # {some_dir}/category/package/package-version
  # but cache entry paths look like:
  # {some_dir}/category/package-version
  # So we need to remove the second to last path element from the ebuild path
  # to construct the path to the matching edb cache entry.
  path_head, package_name = os.path.split(ebuild_path_no_ext)
  path_head, _ = os.path.split(path_head)
  overlay_head, category = os.path.split(path_head)
  fixed_path = os.path.join(overlay_head, category, package_name)

  cache_file_relpath = os.path.relpath(fixed_path, '/')

  edb_cache_file_path = os.path.join('/var/cache/edb/dep', cache_file_relpath)
  md5_cache_file_path = os.path.join(overlay_head, 'metadata', 'md5-cache',
                                     category, package_name)

  relevant_eclass_paths = []

  if os.path.isfile(edb_cache_file_path):
    cache_entries = parse_edb_cache_entry(edb_cache_file_path)
  elif os.path.isfile(md5_cache_file_path):
    cache_entries = parse_md5_cache_entry(md5_cache_file_path)
  else:
    raise MissingCacheEntry(
        'No cache entry found for package: %s' % package_name)

  for eclass, digest in cache_entries:
    if digest in path_cache:
      relevant_eclass_paths.append(path_cache[digest])
    else:
      try:
        eclass_path = find_matching_eclass_file(eclass, digest, overlay_dirs)
        path_cache[digest] = eclass_path
        relevant_eclass_paths.append(eclass_path)
      except NoMatchingFileForDigest:
        cros_logging.warning(
            ('Package %s has a reference to eclass %s with digest %s but no '
             'matching file could be found.'), package_name, eclass, digest)
        # If we can't find a matching eclass file then we don't know exactly
        # which overlay the eclass file is coming from, but we do know that it
        # has to be in one of the overlay_dirs. So as a fallback we will pretend
        # the eclass could be in any of them and add all of the paths that it
        # could possibly have.
        relevant_eclass_paths.extend([
            os.path.join(overlay, 'eclass', eclass) + '.eclass'
            for overlay in overlay_dirs
        ])

  return relevant_eclass_paths


def find_matching_eclass_file(eclass, digest, overlay_dirs):
  for overlay in overlay_dirs:
    path = os.path.join(overlay, 'eclass', eclass) + '.eclass'
    if os.path.isfile(path) and digest == osutils.MD5HashFile(path):
      return path
  raise NoMatchingFileForDigest(
      'No matching eclass file found: %s %s' % (eclass, digest))


def parse_edb_cache_entry(edb_cache_file_path):
  ECLASS_REGEX = re.compile(r'_eclasses_=(.*)')
  ECLASS_CLAUSE_REGEX = (r'(?P<eclass>[^\s]+)\s+(?P<overlay_path>[^\s]+)\s+'
                         r'(?P<digest>[\da-fA-F]+)\s?')

  cachefile = osutils.ReadFile(edb_cache_file_path)
  m = ECLASS_REGEX.search(cachefile)
  if not m:
    return []

  start, end = m.start(1), m.end(1)
  entries = re.finditer(ECLASS_CLAUSE_REGEX, cachefile[start:end])
  return [(c.group('eclass'), c.group('digest')) for c in entries]


def parse_md5_cache_entry(md5_cache_file_path):
  ECLASS_REGEX = re.compile(r'_eclasses_=(.*)')
  ECLASS_CLAUSE_REGEX = r'(?P<eclass>[^\s]+)\s+(?P<digest>[\da-fA-F]+)\s?'

  cachefile = osutils.ReadFile(md5_cache_file_path)
  m = ECLASS_REGEX.search(cachefile)
  if not m:
    return []

  start, end = m.start(1), m.end(1)
  entries = re.finditer(ECLASS_CLAUSE_REGEX, cachefile[start:end])
  return [(c.group('eclass'), c.group('digest')) for c in entries]


def GenerateSourcePathMapping(packages, sysroot_path, board):
  """Returns a map from each package to the source paths it depends on.

  A source path is considered dependency of a package if modifying files in that
  path might change the content of the resulting package.

  Notes:
    1) This method errs on the side of returning unneeded dependent paths.
       i.e: for a given package X, some of its dependency source paths may
       contain files which doesn't affect the content of X.

       On the other hands, any missing dependency source paths for package X is
       considered a bug.
    2) This only outputs the direct dependency source paths for a given package
       and does not takes include the dependency source paths of dependency
       packages.
       e.g: if package A depends on B (DEPEND=B), then results of computing
       dependency source paths of A doesn't include dependency source paths
       of B.

  Args:
    packages: The list of packages CPV names (str)
    sysroot_path (str): The path to the sysroot.  If the packages are board
      agnostic, then this should be '/'.
    board (str): The name of the board if packages are dependency of board. If
      the packages are board agnostic, then this should be None.

  Returns:
    Map from each package to the source path (relative to the repo checkout
      root, i.e: ~/trunk/ in your cros_sdk) it depends on.
    For each source path which is a directory, the string is ended with a
      trailing '/'.
  """

  results = {}

  packages_to_ebuild_paths = portage_util.FindEbuildsForPackages(
      packages, sysroot=sysroot_path, check=True)

  # Source paths which are the directory of ebuild files.
  for package, ebuild_path in packages_to_ebuild_paths.items():
    # Include the entire directory that contains the ebuild as the package's
    # FILESDIR probably lives there too.
    results[package] = [os.path.dirname(ebuild_path)]

  # Source paths which are cros workon source paths.
  buildroot = os.path.join(constants.CHROOT_SOURCE_ROOT, 'src')
  manifest = git.ManifestCheckout.Cached(buildroot)
  for package, ebuild_path in packages_to_ebuild_paths.items():
    attrs = portage_util.EBuild.Classify(ebuild_path)
    if (not attrs.is_workon or
        # Blacklisted ebuild is pinned to a specific git sha1, so change in
        # that repo matter to the ebuild.
        attrs.is_blacklisted):
      continue
    ebuild = portage_util.EBuild(ebuild_path)
    workon_subtrees = ebuild.GetSourceInfo(buildroot, manifest).subtrees
    for path in workon_subtrees:
      results[package].append(path)

  if board:
    overlay_directories = portage_util.FindOverlays(
        overlay_type='both', board=board)
  else:
    # If a board is not specified we assume the package is intended for the SDK
    # and so we use the overlays for the SDK builder.
    overlay_directories = portage_util.FindOverlays(
        overlay_type='both', board=constants.CHROOT_BUILDER_BOARD)

  eclass_path_cache = {}

  for package, ebuild_path in packages_to_ebuild_paths.items():
    eclass_paths = GetRelevantEclassesForEbuild(ebuild_path, eclass_path_cache,
                                                overlay_directories)
    results[package].extend(eclass_paths)

  # Source paths which are the overlay directories for the given board
  # (packages are board specific).

  # The only parts of the overlay that affect every package are the current
  # profile (which lives somewhere in the profiles/ subdir) and a top-level
  # make.conf (if it exists).
  profile_directories = [
      os.path.join(x, 'profiles') for x in overlay_directories
  ]
  make_conf_paths = [os.path.join(x, 'make.conf') for x in overlay_directories]

  # These directories *might* affect a build, so we include them for now to
  # be safe.
  metadata_directories = [
      os.path.join(x, 'metadata') for x in overlay_directories
  ]
  scripts_directories = [
      os.path.join(x, 'scripts') for x in overlay_directories
  ]

  for package in results:
    results[package].extend(profile_directories)
    results[package].extend(make_conf_paths)
    results[package].extend(metadata_directories)
    results[package].extend(scripts_directories)
    # The 'crosutils' repo potentially affects the build of every package.
    results[package].append(constants.CROSUTILS_DIR)

  # chromiumos-overlay specifies default settings for every target in
  # chromeos/config  and so can potentially affect every board.
  for package in results:
    results[package].append(
        os.path.join(constants.CHROOT_SOURCE_ROOT,
                     constants.CHROMIUMOS_OVERLAY_DIR, 'chromeos', 'config'))

  for p in results:
    results[p] = NormalizeSourcePaths(results[p])

  return results


@functools.lru_cache()
def GetBuildDependency(sysroot_path, board=None, packages=None):
  """Return the build dependency and package -> source path map for |board|.

  Args:
    sysroot_path (str): The path to the sysroot, or None if no sysroot is being
        used.
    board (str): The name of the board whose artifacts are being created, or
        None if no sysroot is being used.
    packages (tuple[CPV]): The packages that need to be built, or empty / None
        to use the default list.

  Returns:
    JSON build dependencies report for the given board which includes:
      - Package level deps graph from portage
      - Map from each package to the source path
      (relative to the repo checkout root, i.e: ~/trunk/ in your cros_sdk) it
      depends on
  """
  results = {
      'sysroot_path': sysroot_path,
      'target_board': board,
      'package_deps': {},
      'source_path_mapping': {},
  }

  sdk_sysroot = cros_build_lib.GetSysroot(None)
  sdk_results = {
      'sysroot_path': sdk_sysroot,
      'target_board': 'sdk',
      'package_deps': {},
      'source_path_mapping': {},
  }

  if sysroot_path != sdk_sysroot:
    board_packages = []
    if packages:
      board_packages.extend([cpv.cp for cpv in packages])
    else:
      board_packages.extend([
          'virtual/target-os', 'virtual/target-os-dev',
          'virtual/target-os-test', 'virtual/target-os-factory'
      ])
      # Since we don’t have a clear mapping from autotests to git repos
      # and/or portage packages, we assume every board run all autotests.
      board_packages += ['chromeos-base/autotest-all']

    board_deps, board_bdeps = cros_extract_deps.ExtractDeps(
        sysroot=sysroot_path,
        package_list=board_packages,
        include_bdepend=False,
        backtrack=False)

    results['package_deps'].update(board_deps)
    results['package_deps'].update(board_bdeps)
    sdk_results['package_deps'].update(board_bdeps)

  indep_packages = [
      'virtual/target-sdk', 'chromeos-base/chromite',
      'virtual/target-sdk-post-cross'
  ]

  indep_deps, _ = cros_extract_deps.ExtractDeps(
      sysroot=sdk_results['sysroot_path'], package_list=indep_packages)

  indep_map = GenerateSourcePathMapping(list(indep_deps), sdk_sysroot, None)
  results['package_deps'].update(indep_deps)
  results['source_path_mapping'].update(indep_map)

  sdk_results['package_deps'].update(indep_deps)
  sdk_results['source_path_mapping'].update(indep_map)

  if sysroot_path != sdk_sysroot:
    bdep_map = GenerateSourcePathMapping(list(board_bdeps), sdk_sysroot, None)
    board_map = GenerateSourcePathMapping(list(board_deps), sysroot_path, board)
    results['source_path_mapping'].update(bdep_map)
    results['source_path_mapping'].update(board_map)
    sdk_results['source_path_mapping'].update(bdep_map)

  return results, sdk_results


def determine_package_relevance(dep_src_paths: List[str],
                                src_paths: Optional[List[str]] = None) -> bool:
  """Determine if the package is relevant to the given source paths.

  A package is relevant if any of its dependent source paths is in the given
  list of source paths. If no source paths are given, the default is True.

  Args:
    dep_src_paths: List of source paths the package depends on.
    src_paths: List of source paths of interest.
  """
  if not src_paths:
    return True
  for src_path in (Path(x) for x in src_paths):
    for dep_src_path in (Path(x) for x in dep_src_paths):
      try:
        # Will throw an error if src_path isn't under dep_src_path.
        src_path.relative_to(dep_src_path)
        return True
      except ValueError:
        pass
  return False


def GetDependencies(sysroot_path: str,
                    build_target: build_target_lib.BuildTarget,
                    src_paths: Optional[List[str]] = None,
                    packages: Optional[List[str]] = None) -> List[str]:
  """Return the packages dependent on the given source paths for |board|.

  Args:
    sysroot_path: The path to the sysroot.
    build_target: The build_target whose dependencies are being calculated.
    src_paths: List of paths for which to get a list of dependent packages. If
      empty / None returns all package dependencies.
    packages: The packages that need to be built, or empty / None to use the
      default list.

  Returns:
    The relevant package dependencies based on the given list of packages and
      src_paths.
  """
  pkgs = tuple(packages) if packages else None
  json_deps, _sdk_json_deps = GetBuildDependency(
      sysroot_path, build_target.name, packages=pkgs)

  relevant_packages = set()
  for cpv, dep_src_paths in json_deps['source_path_mapping'].items():
    if determine_package_relevance(dep_src_paths, src_paths):
      relevant_packages.add(cpv)

  relevant_package_deps = set()
  for cpv in relevant_packages:
    relevant_package_deps.update(json_deps['package_deps'][cpv]['deps'])
  return relevant_packages | relevant_package_deps


def DetermineToolchainSourcePaths():
  """Returns a list of all source paths relevant to toolchain packages.

  A package is a 'toolchain package' if it is listed as a direct dependency
  of virtual/toolchain-packages. This function deliberately does not return
  deeper transitive dependencies so that only direct changes to toolchain
  packages trigger the expensive full re-compilation required to test toolchain
  changes. Eclasses & overlays are not returned as relevant paths for the same
  reason.

  Returned paths are relative to the root of the project checkout.

  Returns:
    List[str]: A list of paths considered relevant to toolchain packages.
  """
  source_paths = set()
  toolchain_pkgs = portage_util.GetFlattenedDepsForPackage(
      'virtual/toolchain-packages', depth=1)
  toolchain_pkg_ebuilds = portage_util.FindEbuildsForPackages(
      toolchain_pkgs, sysroot='/', check=True)

  # Include the entire directory containing the toolchain ebuild, as the
  # package's FILESDIR and patches also live there.
  source_paths.update(
      os.path.dirname(ebuild_path)
      for ebuild_path in toolchain_pkg_ebuilds.values())

  # Source paths which are cros workon source paths.
  buildroot = os.path.join(constants.CHROOT_SOURCE_ROOT, 'src')
  manifest = git.ManifestCheckout.Cached(buildroot)
  for ebuild_path in toolchain_pkg_ebuilds.values():
    attrs = portage_util.EBuild.Classify(ebuild_path)
    if (not attrs.is_workon or
        # Blacklisted ebuild is pinned to a specific git sha1, so change in
        # that repo matter to the ebuild.
        attrs.is_blacklisted):
      continue
    ebuild = portage_util.EBuild(ebuild_path)
    workon_subtrees = ebuild.GetSourceInfo(buildroot, manifest).subtrees
    for path in workon_subtrees:
      source_paths.add(path)

  return NormalizeSourcePaths(list(source_paths))
