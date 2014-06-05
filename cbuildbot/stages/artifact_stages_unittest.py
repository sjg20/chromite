#!/usr/bin/python
# Copyright (c) 2012 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittests for the artifact stages."""

import mox
import os
import sys

sys.path.insert(0, os.path.abspath('%s/../../..' % os.path.dirname(__file__)))
from chromite.cbuildbot import commands
from chromite.cbuildbot import constants
from chromite.cbuildbot import failures_lib
from chromite.cbuildbot.stages import artifact_stages
from chromite.cbuildbot.stages import build_stages_unittest
from chromite.cbuildbot.stages import generic_stages_unittest
from chromite.lib import cros_build_lib
from chromite.lib import cros_build_lib_unittest
from chromite.lib import cros_test_lib
from chromite.lib import git
from chromite.lib import parallel
from chromite.lib import parallel_unittest
from chromite.lib import partial_mock

from chromite.cbuildbot.stages.generic_stages_unittest import BuilderRunMock
from chromite.cbuildbot.stages.generic_stages_unittest import patch
from chromite.cbuildbot.stages.generic_stages_unittest import patches


DEFAULT_CHROME_BRANCH = '27'


# pylint: disable=R0901,W0212
class ArchiveStageTest(generic_stages_unittest.AbstractStageTest):
  """Exercise ArchiveStage functionality."""
  RELEASE_TAG = ''
  VERSION = '3333.1.0'

  def _PatchDependencies(self):
    """Patch dependencies of ArchiveStage.PerformStage()."""
    to_patch = [
        (parallel, 'RunParallelSteps'), (commands, 'PushImages'),
        (commands, 'UploadArchivedFile')]
    self.AutoPatch(to_patch)

  def setUp(self):
    self.StartPatcher(BuilderRunMock())
    self._PatchDependencies()

    self._Prepare()

  def _Prepare(self, bot_id=None, **kwargs):
    extra_config = {'upload_symbols': True, 'push_image': True}
    super(ArchiveStageTest, self)._Prepare(bot_id, extra_config=extra_config,
                                           **kwargs)

  def ConstructStage(self):
    self._run.GetArchive().SetupArchivePath()
    return artifact_stages.ArchiveStage(self._run, self._current_board)

  def testArchive(self):
    """Simple did-it-run test."""
    # TODO(davidjames): Test the individual archive steps as well.
    self.RunStage()

  # TODO(build): This test is not actually testing anything real.  It confirms
  # that PushImages is not called, but the mock for RunParallelSteps already
  # prevents PushImages from being called, regardless of whether this is a
  # trybot flow.
  def testNoPushImagesForRemoteTrybot(self):
    """Test that remote trybot overrides work to disable push images."""
    self._Prepare('x86-mario-release',
                  cmd_args=['--remote-trybot', '-r', self.build_root,
                            '--buildnumber=1234'])
    self.RunStage()
    # pylint: disable=E1101
    self.assertEquals(commands.PushImages.call_count, 0)

  def ConstructStageForArchiveStep(self):
    """Stage construction for archive steps."""
    stage = self.ConstructStage()
    self.PatchObject(stage._upload_queue, 'put', autospec=True)
    self.PatchObject(git, 'ReinterpretPathForChroot', return_value='',
                     autospec=True)
    return stage

  def testBuildAndArchiveDeltaSysroot(self):
    """Test tarball is added to upload queue."""
    stage = self.ConstructStageForArchiveStep()
    with cros_build_lib_unittest.RunCommandMock() as rc:
      rc.SetDefaultCmdResult()
      stage.BuildAndArchiveDeltaSysroot()
    stage._upload_queue.put.assert_called_with([constants.DELTA_SYSROOT_TAR])

  def testBuildAndArchiveDeltaSysrootFailure(self):
    """Test tarball not added to upload queue on command exception."""
    stage = self.ConstructStageForArchiveStep()
    with cros_build_lib_unittest.RunCommandMock() as rc:
      rc.AddCmdResult(partial_mock.In('generate_delta_sysroot'), returncode=1,
                      error='generate_delta_sysroot: error')
      self.assertRaises2(cros_build_lib.RunCommandError,
                        stage.BuildAndArchiveDeltaSysroot)
    self.assertFalse(stage._upload_queue.put.called)


class UploadPrebuiltsStageTest(
    generic_stages_unittest.RunCommandAbstractStageTest):
  """Tests for the UploadPrebuilts stage."""

  CMD = './upload_prebuilts'
  RELEASE_TAG = ''

  def setUp(self):
    self.StartPatcher(BuilderRunMock())

  def _Prepare(self, bot_id=None, **kwargs):
    super(UploadPrebuiltsStageTest, self)._Prepare(bot_id, **kwargs)

    self._run.options.prebuilts = True

  def ConstructStage(self):
    return artifact_stages.UploadPrebuiltsStage(self._run,
                                                self._run.config.boards[-1])

  def _VerifyBoardMap(self, bot_id, count, board_map, public_args=None,
                      private_args=None):
    """Verify that the prebuilts are uploaded for the specified bot.

    Args:
      bot_id: Bot to upload prebuilts for.
      count: Number of assert checks that should be performed.
      board_map: Map from slave boards to whether the bot is public.
      public_args: List of extra arguments for public boards.
      private_args: List of extra arguments for private boards.
    """
    self._Prepare(bot_id)
    self.RunStage()
    public_prefix = [self.CMD] + (public_args or [])
    private_prefix = [self.CMD] + (private_args or [])
    for board, public in board_map.iteritems():
      if public or public_args:
        public_cmd = public_prefix + ['--slave-board', board]
        self.assertCommandContains(public_cmd, expected=public)
        count -= 1
      private_cmd = private_prefix + ['--slave-board', board, '--private']
      self.assertCommandContains(private_cmd, expected=not public)
      count -= 1
    if board_map:
      self.assertCommandContains([self.CMD, '--set-version',
                                  self._run.GetVersion()])
      count -= 1
    self.assertEqual(count, 0,
        'Number of asserts performed does not match (%d remaining)' % count)

  def testFullPrebuiltsUpload(self):
    """Test uploading of full builder prebuilts."""
    self._VerifyBoardMap('x86-generic-full', 0, {})
    self.assertCommandContains([self.CMD, '--git-sync'])

  def testIncorrectCount(self):
    """Test that _VerifyBoardMap asserts when the count is wrong."""
    self.assertRaises(AssertionError, self._VerifyBoardMap, 'x86-generic-full',
                      1, {})

  def testChromeUpload(self):
    """Test uploading of prebuilts for chrome build."""
    board_map = {'amd64-generic': True, 'daisy': True,
                 'x86-alex': False, 'lumpy': False}
    self._VerifyBoardMap('x86-generic-chromium-pfq', 9, board_map,
                         public_args=['--board', 'x86-generic'])


class MasterUploadPrebuiltsStageTest(
    generic_stages_unittest.RunCommandAbstractStageTest):
  """Tests for the MasterUploadPrebuilts stage."""

  CMD = './upload_prebuilts'
  RELEASE_TAG = '1234.5.6'
  VERSION = 'R%s-%s' % (DEFAULT_CHROME_BRANCH, RELEASE_TAG)

  def setUp(self):
    self.StartPatcher(BuilderRunMock())

  def _Prepare(self, bot_id=None, **kwargs):
    super(MasterUploadPrebuiltsStageTest, self)._Prepare(bot_id, **kwargs)

    self._run.options.prebuilts = True

  def ConstructStage(self):
    return artifact_stages.MasterUploadPrebuiltsStage(self._run)

  def _RunStage(self, bot_id):
    """Run the stage under test with the given |bot_id| config.

    Args:
      bot_id: Builder config target name.
    """
    self._Prepare(bot_id)
    self.RunStage()

  def _VerifyResults(self, public_slave_boards=(), private_slave_boards=()):
    """Verify that the expected prebuilt commands were run.

    Do various assertions on the two RunCommands that were run by stage.
    There should be one private (--private) and one public (default) run.

    Args:
      public_slave_boards: List of public slave boards.
      private_slave_boards: List of private slave boards.
    """
    # TODO(mtennant): Add functionality in partial_mock to support more flexible
    # asserting.  For example here, asserting that '--sync-host' appears in
    # the command that did not include '--public'.

    # Some args are expected for any public run.
    if public_slave_boards:
      # It would be nice to confirm that --private is not in command, but note
      # that --sync-host should not appear in the --private command.
      cmd = [self.CMD, '--sync-binhost-conf', '--sync-host']
      self.assertCommandContains(cmd, expected=True)

    # Some args are expected for any private run.
    if private_slave_boards:
      cmd = [self.CMD, '--sync-binhost-conf', '--private']
      self.assertCommandContains(cmd, expected=True)

    # Assert public slave boards are mentioned in public run.
    for board in public_slave_boards:
      # This check does not actually confirm that this board was in the public
      # run rather than the private run, unfortunately.
      cmd = [self.CMD, '--slave-board', board]
      self.assertCommandContains(cmd, expected=True)

    # Assert private slave boards are mentioned in private run.
    for board in private_slave_boards:
      cmd = [self.CMD, '--slave-board', board, '--private']
      self.assertCommandContains(cmd, expected=True)

    # We expect --set-version so long as build config has manifest_version=True.
    self.assertCommandContains([self.CMD, '--set-version', self.VERSION],
                               expected=self._run.config.manifest_version)

  def testMasterPaladinUpload(self):
    self._RunStage('master-paladin')

    # Provide a sample of private/public slave boards that are expected.
    public_slave_boards = ('amd64-generic', 'x86-generic')
    private_slave_boards = ('x86-mario', 'x86-alex', 'lumpy', 'daisy_spring')

    self._VerifyResults(public_slave_boards=public_slave_boards,
                        private_slave_boards=private_slave_boards)


class UploadDevInstallerPrebuiltsStageTest(
    generic_stages_unittest.AbstractStageTest):
  """Tests for the UploadDevInstallerPrebuilts stage."""

  RELEASE_TAG = 'RT'

  def setUp(self):
    self.mox.StubOutWithMock(commands, 'UploadDevInstallerPrebuilts')

    self.StartPatcher(BuilderRunMock())

    self._Prepare()

  def _Prepare(self, bot_id=None, **kwargs):
    super(UploadDevInstallerPrebuiltsStageTest, self)._Prepare(bot_id, **kwargs)

    self._run.options.chrome_rev = None
    self._run.options.prebuilts = True
    self._run.config['dev_installer_prebuilts'] = True
    self._run.config['binhost_bucket'] = 'gs://testbucket'
    self._run.config['binhost_key'] = 'dontcare'
    self._run.config['binhost_base_url'] = 'https://dontcare/here'

  def ConstructStage(self):
    return artifact_stages.DevInstallerPrebuiltsStage(self._run,
                                                      self._current_board)

  def testDevInstallerUpload(self):
    """Basic sanity test testing uploads of dev installer prebuilts."""
    version = 'R%s-%s' % (DEFAULT_CHROME_BRANCH, self.RELEASE_TAG)

    commands.UploadDevInstallerPrebuilts(
        binhost_bucket=self._run.config.binhost_bucket,
        binhost_key=self._run.config.binhost_key,
        binhost_base_url=self._run.config.binhost_base_url,
        buildroot=self.build_root,
        board=self._current_board,
        extra_args=mox.And(mox.IsA(list),
                           mox.In(version)))

    self.mox.ReplayAll()
    self.RunStage()
    self.mox.VerifyAll()


class CPEExportStageTest(generic_stages_unittest.AbstractStageTest):
  """Test CPEExportStage"""

  def setUp(self):
    self.StartPatcher(BuilderRunMock())
    self.StartPatcher(generic_stages_unittest.ArchivingStageMixinMock())
    self.StartPatcher(parallel_unittest.ParallelMock())

    self.rc_mock = self.StartPatcher(cros_build_lib_unittest.RunCommandMock())
    self.rc_mock.SetDefaultCmdResult(output='')

    self.stage = None

  def ConstructStage(self):
    """Create a CPEExportStage instance for testing"""
    self._run.GetArchive().SetupArchivePath()
    return artifact_stages.CPEExportStage(self._run, self._current_board)

  def assertBoardAttrEqual(self, attr, expected_value):
    """Assert the value of a board run |attr| against |expected_value|."""
    value = self.stage.board_runattrs.GetParallel(attr)
    self.assertEqual(expected_value, value)

  def _TestPerformStage(self):
    """Run PerformStage for the stage."""
    self._Prepare()
    self._run.attrs.release_tag = BuilderRunMock.VERSION

    self.stage = self.ConstructStage()
    self.stage.PerformStage()

  def testCPEExport(self):
    """Test that CPEExport stage runs without syntax errors."""
    self._TestPerformStage()


class DebugSymbolsStageTest(generic_stages_unittest.AbstractStageTest):
  """Test DebugSymbolsStage"""

  def setUp(self):
    self.StartPatcher(BuilderRunMock())
    self.StartPatcher(generic_stages_unittest.ArchivingStageMixinMock())
    self.StartPatcher(parallel_unittest.ParallelMock())

    self.gen_mock = self.PatchObject(commands, 'GenerateBreakpadSymbols')
    self.upload_mock = self.PatchObject(commands, 'UploadSymbols')
    self.tar_mock = self.PatchObject(commands, 'GenerateDebugTarball')

    self.rc_mock = self.StartPatcher(cros_build_lib_unittest.RunCommandMock())
    self.rc_mock.SetDefaultCmdResult(output='')

    self.stage = None

  def ConstructStage(self):
    """Create a DebugSymbolsStage instance for testing"""
    self._run.GetArchive().SetupArchivePath()
    return artifact_stages.DebugSymbolsStage(self._run, self._current_board)

  def assertBoardAttrEqual(self, attr, expected_value):
    """Assert the value of a board run |attr| against |expected_value|."""
    value = self.stage.board_runattrs.GetParallel(attr)
    self.assertEqual(expected_value, value)

  def _TestPerformStage(self, extra_config=None):
    """Run PerformStage for the stage with the given extra config."""
    if not extra_config:
      extra_config = {
          'archive_build_debug': True,
          'vm_tests': True,
          'upload_symbols': True,
      }

    self._Prepare(extra_config=extra_config)
    self._run.attrs.release_tag = BuilderRunMock.VERSION

    self.tar_mock.side_effect = '/my/tar/ball'
    self.stage = self.ConstructStage()
    try:
      self.stage.PerformStage()
    except Exception:
      self.stage._HandleStageException(sys.exc_info())
      raise

  def testPerformStageWithSymbols(self):
    """Smoke test for an PerformStage when debugging is enabled"""
    self._TestPerformStage()

    self.assertEqual(self.gen_mock.call_count, 1)
    self.assertEqual(self.upload_mock.call_count, 1)
    self.assertEqual(self.tar_mock.call_count, 1)

    self.assertBoardAttrEqual('breakpad_symbols_generated', True)
    self.assertBoardAttrEqual('debug_tarball_generated', True)

  def testPerformStageNoSymbols(self):
    """Smoke test for an PerformStage when debugging is disabled"""
    extra_config = {
        'archive_build_debug': False,
        'vm_tests': False,
        'upload_symbols': False,
    }
    self._TestPerformStage(extra_config)

    self.assertEqual(self.gen_mock.call_count, 1)
    self.assertEqual(self.upload_mock.call_count, 0)
    self.assertEqual(self.tar_mock.call_count, 1)

    self.assertBoardAttrEqual('breakpad_symbols_generated', True)
    self.assertBoardAttrEqual('debug_tarball_generated', True)

  def testGenerateCrashStillNotifies(self):
    """Crashes in symbol generation should still notify external events."""
    self.skipTest('Test skipped due to crbug.com/363339')
    class TestError(Exception):
      """Unique test exception"""

    self.gen_mock.side_effect = TestError('mew')
    self.assertRaises(TestError, self._TestPerformStage)

    self.assertEqual(self.gen_mock.call_count, 1)
    self.assertEqual(self.upload_mock.call_count, 0)
    self.assertEqual(self.tar_mock.call_count, 0)

    self.assertBoardAttrEqual('breakpad_symbols_generated', False)
    self.assertBoardAttrEqual('debug_tarball_generated', False)

  def testUploadCrashStillNotifies(self):
    """Crashes in symbol upload should still notify external events."""
    class TestError(failures_lib.CrashCollectionFailure):
      """Unique test exception"""

    self.upload_mock.side_effect = TestError('mew')
    self.assertRaises(TestError, self._TestPerformStage)

    self.assertEqual(self.gen_mock.call_count, 1)
    self.assertEqual(self.upload_mock.call_count, 1)
    self.assertEqual(self.tar_mock.call_count, 1)

    self.assertBoardAttrEqual('breakpad_symbols_generated', True)
    self.assertBoardAttrEqual('debug_tarball_generated', True)


class UploadTestArtifactsStageMock(
    generic_stages_unittest.ArchivingStageMixinMock):
  """Partial mock for BuildImageStage."""

  TARGET = 'chromite.cbuildbot.stages.artifact_stages.UploadTestArtifactsStage'
  ATTRS = (generic_stages_unittest.ArchivingStageMixinMock.ATTRS +
           ('BuildAutotestTarballs',))

  def BuildAutotestTarballs(self, *args, **kwargs):
    with patches(
        patch(commands, 'BuildTarball'),
        patch(commands, 'FindFilesWithPattern', return_value=['foo.txt'])):
      self.backup['BuildAutotestTarballs'](*args, **kwargs)


class UploadTestArtifactsStageTest(
    build_stages_unittest.BuildPackagesStageTest):
  """Tests UploadTestArtifactsStage."""

  def setUp(self):
    self.StartPatcher(UploadTestArtifactsStageMock())

  def ConstructStage(self):
    return artifact_stages.UploadTestArtifactsStage(self._run,
                                                    self._current_board)

  def RunTestsWithBotId(self, bot_id, options_tests=True):
    """Test with the config for the specified bot_id."""
    self._Prepare(bot_id)
    self._run.options.tests = options_tests
    self._run.attrs.release_tag = '0.0.1'

    # Simulate images being ready.
    board_runattrs = self._run.GetBoardRunAttrs(self._current_board)
    board_runattrs.SetParallel('images_generated', True)

    with parallel_unittest.ParallelMock():
      with self.RunStageWithConfig() as rc:
        cfg = self._run.config
        hw = cfg['upload_hw_test_artifacts']
        rc.assertCommandContains(['--full_payload'], expected=hw)
        rc.assertCommandContains(['--nplus1'], expected=hw)


# TODO: Delete ArchivingMock once ArchivingStage is deprecated.
class ArchivingMock(partial_mock.PartialMock):
  """Partial mock for ArchivingStage."""

  TARGET = 'chromite.cbuildbot.stages.artifact_stages.ArchivingStage'
  ATTRS = ('UploadArtifact',)

  def UploadArtifact(self, *args, **kwargs):
    with patch(commands, 'ArchiveFile', return_value='foo.txt'):
      with patch(commands, 'UploadArchivedFile'):
        self.backup['UploadArtifact'](*args, **kwargs)


# TODO: Delete ArchivingStageTest once ArchivingStage is deprecated.
class ArchivingStageTest(generic_stages_unittest.AbstractStageTest):
  """Excerise ArchivingStage functionality."""
  RELEASE_TAG = ''

  def setUp(self):
    self.StartPatcher(BuilderRunMock())
    self.StartPatcher(ArchivingMock())

    self._Prepare()

  def ConstructStage(self):
    self._run.GetArchive().SetupArchivePath()
    archive_stage = artifact_stages.ArchiveStage(
        self._run, self._current_board)
    return artifact_stages.ArchivingStage(
        self._run, self._current_board, archive_stage)


if __name__ == '__main__':
  cros_test_lib.main()
