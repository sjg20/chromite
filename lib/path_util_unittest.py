# -*- coding: utf-8 -*-
# Copyright 2015 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Test the path_util module."""

from __future__ import print_function

import itertools
import os
import tempfile

from chromite.lib import constants
from chromite.lib import cros_test_lib
from chromite.lib import git
from chromite.lib import partial_mock
from chromite.lib import path_util
from chromite.third_party import mock


FAKE_SOURCE_PATH = '/path/to/source/tree'
FAKE_REPO_PATH = '/path/to/repo'
CUSTOM_SOURCE_PATH = '/custom/source/path'


class DetermineCheckoutTest(cros_test_lib.MockTempDirTestCase):
  """Verify functionality for figuring out what checkout we're in."""

  def setUp(self):
    self.rc_mock = cros_test_lib.RunCommandMock()
    self.StartPatcher(self.rc_mock)
    self.rc_mock.SetDefaultCmdResult()

  def RunTest(self, dir_struct, cwd, expected_root, expected_type,
              expected_src):
    """Run a test with specific parameters and expected results."""
    cros_test_lib.CreateOnDiskHierarchy(self.tempdir, dir_struct)
    cwd = os.path.join(self.tempdir, cwd)
    checkout_info = path_util.DetermineCheckout(cwd)
    full_root = expected_root
    if expected_root is not None:
      full_root = os.path.join(self.tempdir, expected_root)
    full_src = expected_src
    if expected_src is not None:
      full_src = os.path.join(self.tempdir, expected_src)

    self.assertEqual(checkout_info.root, full_root)
    self.assertEqual(checkout_info.type, expected_type)
    self.assertEqual(checkout_info.chrome_src_dir, full_src)

  def testGclientRepo(self):
    """Recognizes a GClient repo checkout."""
    dir_struct = [
        'a/.gclient',
        'a/b/.repo/',
        'a/b/c/.gclient',
        'a/b/c/d/somefile',
    ]
    self.RunTest(dir_struct, 'a/b/c', 'a/b/c',
                 path_util.CHECKOUT_TYPE_GCLIENT,
                 'a/b/c/src')
    self.RunTest(dir_struct, 'a/b/c/d', 'a/b/c',
                 path_util.CHECKOUT_TYPE_GCLIENT,
                 'a/b/c/src')
    self.RunTest(dir_struct, 'a/b', 'a/b',
                 path_util.CHECKOUT_TYPE_REPO,
                 None)
    self.RunTest(dir_struct, 'a', 'a',
                 path_util.CHECKOUT_TYPE_GCLIENT,
                 'a/src')

  def testGitUnderGclient(self):
    """Recognizes a chrome git checkout by gclient."""
    self.rc_mock.AddCmdResult(
        partial_mock.In('config'), output=constants.CHROMIUM_GOB_URL)
    dir_struct = [
        'a/.gclient',
        'a/src/.git/',
    ]
    self.RunTest(dir_struct, 'a/src', 'a',
                 path_util.CHECKOUT_TYPE_GCLIENT,
                 'a/src')

  def testGitUnderRepo(self):
    """Recognizes a chrome git checkout by repo."""
    self.rc_mock.AddCmdResult(
        partial_mock.In('config'), output=constants.CHROMIUM_GOB_URL)
    dir_struct = [
        'a/.repo/',
        'a/b/.git/',
    ]
    self.RunTest(dir_struct, 'a/b', 'a',
                 path_util.CHECKOUT_TYPE_REPO,
                 None)

  def testBadGit1(self):
    """.git is not a directory."""
    self.RunTest(['a/.git'], 'a', None,
                 path_util.CHECKOUT_TYPE_UNKNOWN, None)

  def testBadGit2(self):
    """'git config' returns nothing."""
    self.RunTest(['a/.repo/', 'a/b/.git/'], 'a/b', 'a',
                 path_util.CHECKOUT_TYPE_REPO, None)

  def testBadGit3(self):
    """'git config' returns error."""
    self.rc_mock.AddCmdResult(partial_mock.In('config'), returncode=5)
    self.RunTest(['a/.git/'], 'a', None,
                 path_util.CHECKOUT_TYPE_UNKNOWN, None)


class FindCacheDirTest(cros_test_lib.MockTempDirTestCase):
  """Test cache dir specification and finding functionality."""

  def setUp(self):
    dir_struct = [
        'repo/.repo/',
        'repo/manifest/',
        'gclient/.gclient',
    ]
    cros_test_lib.CreateOnDiskHierarchy(self.tempdir, dir_struct)
    self.repo_root = os.path.join(self.tempdir, 'repo')
    self.gclient_root = os.path.join(self.tempdir, 'gclient')
    self.nocheckout_root = os.path.join(self.tempdir, 'nothing')

    self.rc_mock = self.StartPatcher(cros_test_lib.RunCommandMock())
    self.cwd_mock = self.PatchObject(os, 'getcwd')

  def testRepoRoot(self):
    """Test when we are inside a repo checkout."""
    self.cwd_mock.return_value = self.repo_root
    self.assertEqual(
        path_util.FindCacheDir(),
        os.path.join(self.repo_root, path_util.GENERAL_CACHE_DIR))

  def testGclientRoot(self):
    """Test when we are inside a gclient checkout."""
    self.cwd_mock.return_value = self.gclient_root
    self.assertEqual(
        path_util.FindCacheDir(),
        os.path.join(self.gclient_root, 'src', 'build',
                     path_util.CHROME_CACHE_DIR))

  def testTempdir(self):
    """Test when we are not in any checkout."""
    self.cwd_mock.return_value = self.nocheckout_root
    self.assertStartsWith(
        path_util.FindCacheDir(),
        os.path.join(tempfile.gettempdir(), ''))


class TestPathResolver(cros_test_lib.MockTestCase):
  """Tests of ChrootPathResolver class."""

  def setUp(self):
    self.PatchObject(constants, 'SOURCE_ROOT', new=FAKE_SOURCE_PATH)
    self.PatchObject(path_util, 'GetCacheDir', return_value='/path/to/cache')
    self.PatchObject(
        path_util.ChrootPathResolver,
        '_GetCachePath',
        return_value='/path/to/cache')
    self.PatchObject(
        git,
        'FindRepoDir',
        return_value=os.path.join(FAKE_REPO_PATH, '.fake_repo'))
    self.chroot_path = None

  def FakeCwd(self, base_path):
    return os.path.join(base_path, 'somewhere/in/there')

  def SetChrootPath(self, source_path):
    """Set and fake the chroot path."""
    self.chroot_path = os.path.join(source_path, constants.DEFAULT_CHROOT_DIR)

  @mock.patch('chromite.lib.cros_build_lib.IsInsideChroot', return_value=True)
  def testInsideChroot(self, _):
    """Tests {To,From}Chroot() call from inside the chroot."""
    self.SetChrootPath(constants.SOURCE_ROOT)
    resolver = path_util.ChrootPathResolver()

    self.assertEqual(os.path.realpath('some/path'),
                     resolver.ToChroot('some/path'))
    self.assertEqual(os.path.realpath('/some/path'),
                     resolver.ToChroot('/some/path'))
    self.assertEqual(os.path.realpath('some/path'),
                     resolver.FromChroot('some/path'))
    self.assertEqual(os.path.realpath('/some/path'),
                     resolver.FromChroot('/some/path'))

  @mock.patch('chromite.lib.cros_build_lib.IsInsideChroot', return_value=False)
  def testOutsideChrootInbound(self, _):
    """Tests ToChroot() calls from outside the chroot."""
    for source_path, source_from_path_repo in itertools.product(
        (None, CUSTOM_SOURCE_PATH), (False, True)):
      if source_from_path_repo:
        actual_source_path = FAKE_REPO_PATH
      else:
        actual_source_path = source_path or constants.SOURCE_ROOT

      fake_cwd = self.FakeCwd(actual_source_path)
      self.PatchObject(os, 'getcwd', return_value=fake_cwd)
      self.SetChrootPath(actual_source_path)
      resolver = path_util.ChrootPathResolver(
          source_path=source_path,
          source_from_path_repo=source_from_path_repo)
      self.PatchObject(resolver, '_ReadChrootLink', return_value=None)
      source_rel_cwd = os.path.relpath(fake_cwd, actual_source_path)

      # Case: path inside the chroot space.
      self.assertEqual(
          '/some/path',
          resolver.ToChroot(os.path.join(self.chroot_path, 'some/path')))

      # Case: path inside the cache directory.
      self.assertEqual(
          os.path.join(constants.CHROOT_CACHE_ROOT, 'some/path'),
          resolver.ToChroot(os.path.join(path_util.GetCacheDir(),
                                         'some/path')))

      # Case: absolute path inside the source tree.
      if source_from_path_repo:
        self.assertEqual(
            os.path.join(constants.CHROOT_SOURCE_ROOT, 'some/path'),
            resolver.ToChroot(os.path.join(FAKE_REPO_PATH, 'some/path')))
      else:
        self.assertEqual(
            os.path.join(constants.CHROOT_SOURCE_ROOT, 'some/path'),
            resolver.ToChroot(os.path.join(actual_source_path, 'some/path')))

      # Case: relative path inside the source tree.
      if source_from_path_repo:
        self.assertEqual(
            os.path.join(constants.CHROOT_SOURCE_ROOT, source_rel_cwd,
                         'some/path'),
            resolver.ToChroot('some/path'))
      else:
        self.assertEqual(
            os.path.join(constants.CHROOT_SOURCE_ROOT, source_rel_cwd,
                         'some/path'),
            resolver.ToChroot('some/path'))

      # Case: unreachable, path with improper source root prefix.
      with self.assertRaises(ValueError):
        resolver.ToChroot(os.path.join(actual_source_path + '-foo',
                                       'some/path'))

      # Case: unreachable (random).
      with self.assertRaises(ValueError):
        resolver.ToChroot('/some/path')

  @mock.patch('chromite.lib.cros_build_lib.IsInsideChroot', return_value=False)
  def testOutsideChrootOutbound(self, _):
    """Tests FromChroot() calls from outside the chroot."""
    self.PatchObject(os, 'getcwd', return_value=self.FakeCwd(FAKE_SOURCE_PATH))
    self.SetChrootPath(constants.SOURCE_ROOT)
    resolver = path_util.ChrootPathResolver()
    # These two patches are only necessary or have any affect on the test when
    # the test is run inside of a symlinked chroot. The _ReadChrootLink patch
    # ensures it runs as if it is not in a symlinked chroot. The realpath
    # patch is necessary to make it actually behave as if that's the case.
    # In both instances the effective return value are as if it was not in a
    # symlinked chroot.
    # TODO(saklein) Rewrite these tests so this isn't necessary.
    self.PatchObject(resolver, '_ReadChrootLink', return_value=None)
    self.PatchObject(os.path, 'realpath', side_effect=lambda x: x)

    # Case: source root path.
    self.assertEqual(
        os.path.join(constants.SOURCE_ROOT, 'some/path'),
        resolver.FromChroot(os.path.join(constants.CHROOT_SOURCE_ROOT,
                                         'some/path')))

    # Case: cyclic source/chroot sub-path elimination.
    self.assertEqual(
        os.path.join(constants.SOURCE_ROOT, 'some/path'),
        resolver.FromChroot(os.path.join(
            constants.CHROOT_SOURCE_ROOT,
            constants.DEFAULT_CHROOT_DIR,
            constants.CHROOT_SOURCE_ROOT.lstrip(os.path.sep),
            constants.DEFAULT_CHROOT_DIR,
            constants.CHROOT_SOURCE_ROOT.lstrip(os.path.sep),
            'some/path')))

    # Case: path inside the cache directory.
    self.assertEqual(
        os.path.join(path_util.GetCacheDir(), 'some/path'),
        resolver.FromChroot(os.path.join(constants.CHROOT_CACHE_ROOT,
                                         'some/path')))

    # Case: non-rooted chroot paths.
    self.assertEqual(
        os.path.join(self.chroot_path, 'some/path'),
        resolver.FromChroot('/some/path'))

  @mock.patch('chromite.lib.cros_build_lib.IsInsideChroot', return_value=False)
  def testSymlinkedChroot(self, _):
    self.SetChrootPath(constants.SOURCE_ROOT)
    resolver = path_util.ChrootPathResolver()
    self.PatchObject(resolver, '_ReadChrootLink', return_value='/another/path')

    # Should still resolve paths from the chroot to the default location.
    self.assertEqual(
        os.path.join(constants.SOURCE_ROOT, constants.DEFAULT_CHROOT_DIR,
                     'some/path'),
        resolver.FromChroot('/some/path'))

    # Should be able to handle translating the linked location to a chroot path.
    self.assertEqual('/some/path',
                     resolver.ToChroot('/another/path/some/path'))
