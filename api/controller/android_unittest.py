# -*- coding: utf-8 -*-
# Copyright 2019 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittests for Android operations."""

from __future__ import print_function

from chromite.api import api_config
from chromite.api.controller import android
from chromite.api.gen.chromite.api import android_pb2
from chromite.api.gen.chromiumos import common_pb2
from chromite.lib import build_target_lib
from chromite.lib import constants
from chromite.lib import cros_build_lib
from chromite.lib import cros_test_lib
from chromite.lib import osutils
from chromite.service import android as service_android
from chromite.service import packages
from chromite.third_party import mock


class GetLatestBuildTest(cros_test_lib.MockTestCase, api_config.ApiConfigMixin):
  """Unittests for GetLatestBuild."""

  def setUp(self):
    self._mock = self.PatchObject(service_android, 'GetLatestBuild')
    self._mock.return_value = ('7123456', {})
    self._input_proto = android_pb2.GetLatestBuildRequest()
    self._input_proto.android_build_branch = 'git_rvc-arc'
    self._output_proto = android_pb2.GetLatestBuildResponse()

  def testValidateOnly(self):
    """Test that a validate only call does not execute any logic."""
    android.GetLatestBuild(self._input_proto, self._output_proto,
                           self.validate_only_config)
    self._mock.assert_not_called()

  def testMockCall(self):
    """Test that a mock call does not execute logic, returns mocked value."""
    android.GetLatestBuild(self._input_proto, self._output_proto,
                           self.mock_call_config)
    self._mock.assert_not_called()
    self.assertEqual(self._output_proto.android_version, '7123456')

  def testFailsIfAndroidBuildBranchMissing(self):
    """Fails if package_name is missing."""
    self._input_proto.android_build_branch = ''
    with self.assertRaises(cros_build_lib.DieSystemExit):
      android.GetLatestBuild(self._input_proto, self._output_proto,
                             self.api_config)
    self._mock.assert_not_called()

  def testActualCall(self):
    """Test that the underlying method is being called in the usual case."""
    android.GetLatestBuild(self._input_proto, self._output_proto,
                           self.api_config)
    self._mock.assert_called_once_with('git_rvc-arc')
    self.assertEqual(self._output_proto.android_version, '7123456')


class MarkStableTest(cros_test_lib.MockTestCase, api_config.ApiConfigMixin):
  """Unittests for MarkStable."""

  def setUp(self):
    self.uprev = self.PatchObject(packages, 'uprev_android')

    self.input_proto = android_pb2.MarkStableRequest()
    self.input_proto.package_name = 'android-package-name'
    self.input_proto.android_build_branch = 'android_build_branch'
    self.input_proto.build_targets.add().name = 'foo'
    self.input_proto.build_targets.add().name = 'bar'
    self.input_proto.skip_commit = True

    self.build_targets = [build_target_lib.BuildTarget('foo'),
                          build_target_lib.BuildTarget('bar')]

    self.response = android_pb2.MarkStableResponse()

  def testValidateOnly(self):
    """Sanity check that a validate only call does not execute any logic."""
    android.MarkStable(self.input_proto, self.response,
                       self.validate_only_config)
    self.uprev.assert_not_called()

  def testMockCall(self):
    """Test that a mock call does not execute logic, returns mocked value."""
    android.MarkStable(self.input_proto, self.response,
                       self.mock_call_config)
    self.uprev.assert_not_called()
    self.assertEqual(self.response.status,
                     android_pb2.MARK_STABLE_STATUS_SUCCESS)
    self.assertEqual(self.response.android_atom.category, 'category')
    self.assertEqual(self.response.android_atom.package_name,
                     'android-package-name')
    self.assertEqual(self.response.android_atom.version, '1.2')

  def testFailsIfPackageNameMissing(self):
    """Fails if package_name is missing."""
    self.input_proto.package_name = ''
    with self.assertRaises(cros_build_lib.DieSystemExit):
      android.MarkStable(self.input_proto, self.response, self.api_config)
    self.uprev.assert_not_called()

  def testFailsIfAndroidBuildBranchMissing(self):
    """Fails if android_build_branch is missing."""
    self.input_proto.android_build_branch = ''
    with self.assertRaises(cros_build_lib.DieSystemExit):
      android.MarkStable(self.input_proto, self.response, self.api_config)
    self.uprev.assert_not_called()

  def testCallsCommandCorrectly(self):
    """Test that commands.MarkAndroidAsStable is called correctly."""
    self.input_proto.android_version = 'android-version'
    self.uprev.return_value = 'cat/android-1.2.3'
    atom = common_pb2.PackageInfo()
    atom.category = 'cat'
    atom.package_name = 'android'
    atom.version = '1.2.3'
    android.MarkStable(self.input_proto, self.response, self.api_config)
    self.uprev.assert_called_once_with(
        android_package=self.input_proto.package_name,
        android_build_branch=self.input_proto.android_build_branch,
        chroot=mock.ANY,
        build_targets=self.build_targets,
        android_version=self.input_proto.android_version,
        skip_commit=self.input_proto.skip_commit,
    )
    self.assertEqual(self.response.android_atom, atom)
    self.assertEqual(self.response.status,
                     android_pb2.MARK_STABLE_STATUS_SUCCESS)

  def testHandlesEarlyExit(self):
    """Test that early exit is handled correctly."""
    self.input_proto.android_version = 'android-version'
    self.uprev.return_value = ''
    android.MarkStable(self.input_proto, self.response, self.api_config)
    self.uprev.assert_called_once_with(
        android_package=self.input_proto.package_name,
        android_build_branch=self.input_proto.android_build_branch,
        chroot=mock.ANY,
        build_targets=self.build_targets,
        android_version=self.input_proto.android_version,
        skip_commit=self.input_proto.skip_commit,
    )
    self.assertEqual(self.response.status,
                     android_pb2.MARK_STABLE_STATUS_EARLY_EXIT)

  def testHandlesPinnedUprevError(self):
    """Test that pinned error is handled correctly."""
    self.input_proto.android_version = 'android-version'
    self.uprev.side_effect = packages.AndroidIsPinnedUprevError('pin/xx-1.1')
    atom = common_pb2.PackageInfo()
    atom.category = 'pin'
    atom.package_name = 'xx'
    atom.version = '1.1'
    android.MarkStable(self.input_proto, self.response, self.api_config)
    self.uprev.assert_called_once_with(
        android_package=self.input_proto.package_name,
        android_build_branch=self.input_proto.android_build_branch,
        chroot=mock.ANY,
        build_targets=self.build_targets,
        android_version=self.input_proto.android_version,
        skip_commit=self.input_proto.skip_commit,
    )
    self.assertEqual(self.response.android_atom, atom)
    self.assertEqual(self.response.status,
                     android_pb2.MARK_STABLE_STATUS_PINNED)


class UnpinVersionTest(cros_test_lib.MockTestCase, api_config.ApiConfigMixin):
  """Unittests for UnpinVersion."""

  def testCallsUnlink(self):
    """SetAndroid calls service with correct args."""
    safeunlink = self.PatchObject(osutils, 'SafeUnlink')
    self.PatchObject(constants, '_FindSourceRoot', return_value='SRCROOT')

    # This has the side effect of making sure that input and output proto are
    # not actually used.
    android.UnpinVersion(None, None, self.api_config)
    safeunlink.assert_called_once_with(android.ANDROIDPIN_MASK_PATH)

  def testValidateOnly(self):
    """Sanity check that a validate only call does not execute any logic."""
    safeunlink = self.PatchObject(osutils, 'SafeUnlink')

    android.UnpinVersion(None, None, self.validate_only_config)
    safeunlink.assert_not_called()

  def testMockCall(self):
    """Test that a mock call does not execute logic."""
    safeunlink = self.PatchObject(osutils, 'SafeUnlink')

    android.UnpinVersion(None, None, self.mock_call_config)
    safeunlink.assert_not_called()
    # android.UnpinVersion does not modify the response.
