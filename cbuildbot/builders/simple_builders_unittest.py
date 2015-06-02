# Copyright 2015 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittests for simpler builders."""

from __future__ import print_function

import copy
import os

from chromite.cbuildbot import cbuildbot_config
from chromite.cbuildbot import cbuildbot_run
from chromite.cbuildbot import constants
from chromite.cbuildbot.builders import generic_builders
from chromite.cbuildbot.builders import simple_builders
from chromite.lib import cros_test_lib
from chromite.lib import osutils
from chromite.lib import parallel
from chromite.lib import parallel_unittest
from chromite.scripts import cbuildbot


# pylint: disable=protected-access


class SimpleBuilderTest(cros_test_lib.MockTempDirTestCase):
  """Tests for the main code paths in simple_builders.SimpleBuilder"""

  def setUp(self):
    self.buildroot = os.path.join(self.tempdir, 'buildroot')
    chroot_path = os.path.join(self.buildroot, constants.DEFAULT_CHROOT_DIR)
    osutils.SafeMakedirs(os.path.join(chroot_path, 'tmp'))

    self.PatchObject(generic_builders.Builder, '_RunStage')
    self.PatchObject(simple_builders.SimpleBuilder, '_RunParallelStages')
    self.PatchObject(cbuildbot_run._BuilderRunBase, 'GetVersion',
                     return_value='R32-1234.0.0')
    self.StartPatcher(parallel_unittest.ParallelMock())

    self._manager = parallel.Manager()
    self._manager.__enter__()

  def tearDown(self):
    # Mimic exiting a 'with' statement.
    self._manager.__exit__(None, None, None)

  def _initConfig(self, bot_id, extra_argv=None):
    """Return normal options/build_config for |bot_id|"""
    site_config = cbuildbot_config.GetConfig()
    build_config = copy.deepcopy(site_config[bot_id])
    build_config['master'] = False
    build_config['important'] = False

    # Use the cbuildbot parser to create properties and populate default values.
    parser = cbuildbot._CreateParser()
    argv = (['-r', self.buildroot, '--buildbot', '--debug', '--nochromesdk'] +
            (extra_argv if extra_argv else []) + [bot_id])
    options, _ = cbuildbot._ParseCommandLine(parser, argv, site_config)

    # Yikes.
    options.managed_chrome = build_config['sync_chrome']

    return cbuildbot_run.BuilderRun(
        options, site_config, build_config, self._manager)

  def testRunStagesPreCQ(self):
    """Verify RunStages for PRE_CQ_LAUNCHER_TYPE builders"""
    builder_run = self._initConfig('pre-cq-launcher')
    simple_builders.SimpleBuilder(builder_run).RunStages()

  def testRunStagesBranchUtil(self):
    """Verify RunStages for CREATE_BRANCH_TYPE builders"""
    extra_argv = ['--branch-name', 'foo', '--version', '1234']
    builder_run = self._initConfig(constants.BRANCH_UTIL_CONFIG,
                                   extra_argv=extra_argv)
    simple_builders.SimpleBuilder(builder_run).RunStages()

  def testRunStagesChrootBuilder(self):
    """Verify RunStages for CHROOT_BUILDER_TYPE builders"""
    builder_run = self._initConfig('chromiumos-sdk')
    simple_builders.SimpleBuilder(builder_run).RunStages()

  def testRunStagesRefreshPackages(self):
    """Verify RunStages for REFRESH_PACKAGES_TYPE builders"""
    builder_run = self._initConfig('refresh-packages')
    simple_builders.SimpleBuilder(builder_run).RunStages()

  def testRunStagesDefaultBuild(self):
    """Verify RunStages for standard board builders"""
    builder_run = self._initConfig('x86-generic-full')
    builder_run.attrs.chrome_version = 'TheChromeVersion'
    simple_builders.SimpleBuilder(builder_run).RunStages()

  def testRunStagesDefaultBuildCompileCheck(self):
    """Verify RunStages for standard board builders (compile only)"""
    extra_argv = ['--compilecheck']
    builder_run = self._initConfig('x86-generic-full', extra_argv=extra_argv)
    builder_run.attrs.chrome_version = 'TheChromeVersion'
    simple_builders.SimpleBuilder(builder_run).RunStages()

  def testRunStagesDefaultBuildHwTests(self):
    """Verify RunStages for boards w/hwtests"""
    extra_argv = ['--hwtest']
    builder_run = self._initConfig('lumpy-release', extra_argv=extra_argv)
    builder_run.attrs.chrome_version = 'TheChromeVersion'
    simple_builders.SimpleBuilder(builder_run).RunStages()
