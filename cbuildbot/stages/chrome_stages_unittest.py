#!/usr/bin/python
# Copyright (c) 2012 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittests for chrome stages."""

from __future__ import print_function

import os
import sys

sys.path.insert(0, os.path.abspath('%s/../../..' % os.path.dirname(__file__)))
from chromite.cbuildbot import commands
from chromite.cbuildbot import constants
from chromite.cbuildbot.cbuildbot_unittest import BuilderRunMock
from chromite.cbuildbot.stages import chrome_stages
from chromite.cbuildbot.stages import generic_stages_unittest
from chromite.lib import cidb
from chromite.lib import cros_build_lib
from chromite.lib import cros_build_lib_unittest
from chromite.lib import cros_test_lib
from chromite.lib import osutils
from chromite.lib import parallel_unittest

# TODO(build): Finish test wrapper (http://crosbug.com/37517).
# Until then, this has to be after the chromite imports.
import mock


class ChromeSDKStageTest(generic_stages_unittest.AbstractStageTest,
                         cros_test_lib.LoggingTestCase):
  """Verify stage that creates the chrome-sdk and builds chrome with it."""
  BOT_ID = 'link-paladin'
  RELEASE_TAG = ''

  # pylint: disable=protected-access

  def setUp(self):
    self.StartPatcher(BuilderRunMock())
    self.StartPatcher(parallel_unittest.ParallelMock())

    # Set up a general purpose cidb mock. Tests with more specific
    # mock requirements can replace this with a separate call to
    # SetupMockCidb
    cidb.CIDBConnectionFactory.SetupMockCidb(mock.MagicMock())

    self._Prepare()

  def _Prepare(self, bot_id=None, **kwargs):
    super(ChromeSDKStageTest, self)._Prepare(bot_id, **kwargs)

    self._run.options.chrome_root = '/tmp/non-existent'
    self._run.attrs.metadata.UpdateWithDict({'toolchain-tuple': ['target'],
                                             'toolchain-url' : 'some-url'})

  def ConstructStage(self):
    self._run.GetArchive().SetupArchivePath()
    return chrome_stages.ChromeSDKStage(self._run, self._current_board)

  def testIt(self):
    """A simple run-through test."""
    rc_mock = self.StartPatcher(cros_build_lib_unittest.RunCommandMock())
    rc_mock.SetDefaultCmdResult()
    self.PatchObject(chrome_stages.ChromeSDKStage, '_ArchiveChromeEbuildEnv',
                     autospec=True)
    self.PatchObject(chrome_stages.ChromeSDKStage, '_VerifyChromeDeployed',
                     autospec=True)
    self.PatchObject(chrome_stages.ChromeSDKStage, '_VerifySDKEnvironment',
                     autospec=True)
    self.RunStage()

  def testChromeEnvironment(self):
    """Test that the Chrome environment is built."""
    # Create the chrome environment compressed file.
    stage = self.ConstructStage()
    chrome_env_dir = os.path.join(
        stage._pkg_dir, constants.CHROME_CP + '-25.3643.0_rc1')
    env_file = os.path.join(chrome_env_dir, 'environment')
    osutils.Touch(env_file, makedirs=True)

    cros_build_lib.RunCommand(['bzip2', env_file])

    # Run the code.
    stage._ArchiveChromeEbuildEnv()

    env_tar_base = stage._upload_queue.get()[0]
    env_tar = os.path.join(stage.archive_path, env_tar_base)
    self.assertTrue(os.path.exists(env_tar))
    cros_test_lib.VerifyTarball(env_tar, ['./', 'environment'])


class PatchChromeStageTest(generic_stages_unittest.AbstractStageTest):
  """Tests for PatchChromeStage."""

  def setUp(self):
    self._Prepare(cmd_args=[
        '-r', self.build_root,
        '--rietveld-patches=1234',
        '--rietveld-patches=555:adir',
    ])
    self.PatchObject(commands, 'PatchChrome')

  def ConstructStage(self):
    return chrome_stages.PatchChromeStage(self._run)

  def testBasic(self):
    """Verify requested patches are applied."""
    stage = self.ConstructStage()
    stage.PerformStage()


if __name__ == '__main__':
  cros_test_lib.main()
