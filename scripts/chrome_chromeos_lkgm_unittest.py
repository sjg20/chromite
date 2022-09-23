# Copyright 2017 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unit tests for the chrome_chromeos_lkgm program."""

from unittest import mock

from chromite.lib import cros_test_lib
from chromite.scripts import chrome_chromeos_lkgm


class StubGerritChange:
    """Stab class corresponding to cros_patch.GerritChange."""

    def __init__(
        self,
        gerrit_number,
        file_content,
        subject,
        mergeable=True,
        original_file_content=None,
    ):
        self._gerrit_number = gerrit_number
        self._subject = subject
        self._file_content = file_content
        self._mergeable = mergeable
        self._original_file_content = original_file_content or file_content

    @property
    def subject(self):
        return self._subject

    @property
    def gerrit_number(self):
        return self._gerrit_number

    def GetFileContents(self, _path: str):
        return self._file_content

    def GetOriginalFileContents(self, _path: str):
        return self._original_file_content

    def IsMergeable(self):
        return self._mergeable

    def Rebase(self, allow_conflicts: bool = False):
        pass


# pylint: disable=protected-access
class ChromeLKGMCommitterTester(
    cros_test_lib.RunCommandTestCase, cros_test_lib.MockTempDirTestCase
):
    """Test cros_chromeos_lkgm.Committer."""

    def setUp(self):
        """Common set up method for all tests."""
        self.committer = chrome_chromeos_lkgm.ChromeLKGMCommitter(
            "1001.0.0", "main"
        )

    @mock.patch("chromite.lib.gob_util.GetFileContents")
    def testCommitNewLKGM(self, mock_get_file):
        """Tests that we can commit a new LKGM file."""
        mock_get_file.return_value = "999.0.0"
        with mock.patch.object(
            self.committer._gerrit_helper, "CreateChange"
        ) as cg:
            cg.return_value = mock.MagicMock(gerrit_number=123456)
            with mock.patch.object(
                self.committer._gerrit_helper, "ChangeEdit"
            ) as ce:
                with mock.patch.object(
                    self.committer._gerrit_helper, "SetReview"
                ) as bc:
                    with mock.patch.object(
                        self.committer._gerrit_helper, "SetHashtags"
                    ):
                        self.committer.UpdateLKGM()
                        ce.assert_called_once_with(
                            123456, "chromeos/CHROMEOS_LKGM", "1001.0.0"
                        )
                        bc.assert_called_once_with(
                            123456,
                            labels={"Bot-Commit": 1, "Commit-Queue": 2},
                            notify="NONE",
                            ready=True,
                            reviewers=[
                                "chrome-os-gardeners-reviews@google.com"
                            ],
                        )

    @mock.patch("chromite.lib.gob_util.GetFileContents")
    def testOlderLKGMFails(self, mock_get_file):
        """Tests that trying to update to an older lkgm version fails."""
        mock_get_file.return_value = "1002.0.0"
        with mock.patch.object(
            self.committer._gerrit_helper, "CreateChange"
        ) as cg:
            cg.return_value = mock.MagicMock(gerrit_number=123456)
            with mock.patch.object(
                self.committer._gerrit_helper, "ChangeEdit"
            ) as ce:
                self.assertRaises(
                    chrome_chromeos_lkgm.LKGMNotValid, self.committer.UpdateLKGM
                )
                ce.assert_not_called()

    @mock.patch("chromite.lib.gob_util.GetFileContents")
    def testAbandonObsoleteLKGMs(self, mock_get_file):
        """Tests that trying to abandon the obsolete lkgm CLs."""
        mock_get_file.return_value = "10002.0.0"

        older_change = StubGerritChange(
            3876550, "10001.0.0", "10001.0.0", mergeable=False
        )
        newer_change = StubGerritChange(3876551, "10003.0.0", "10003.0.0")
        open_issues = [older_change, newer_change]

        with mock.patch.object(
            self.committer._gerrit_helper, "Query", return_value=open_issues
        ) as mock_query:
            with mock.patch.object(
                self.committer._gerrit_helper, "AbandonChange"
            ) as ac:
                self.committer.ProcessObsoleteLKGMRolls()
                mock_query.assert_called_once()
                ac.assert_called_once_with((older_change), msg=mock.ANY)

    @mock.patch("chromite.lib.gob_util.GetFileContents")
    def testRebaseObsoleteLKGMs(self, mock_get_file):
        """Tests that trying to abandon the obsolete lkgm CLs."""
        mock_get_file.return_value = "10002.0.0"

        # LKGM Roll CL from "10001.0.0" to "10003.0.0" should be in the
        # merge-conflict state, since the current LKGM version is "10002.0.0".
        ROLL_FROM = "10001.0.0"
        ROLL_TO = "10003.0.0"
        GERRIT_NUM = 3876551
        roll = StubGerritChange(
            GERRIT_NUM,
            ROLL_TO,
            ROLL_TO,
            mergeable=False,
            original_file_content=ROLL_FROM,
        )

        with mock.patch.object(
            self.committer._gerrit_helper, "Query", return_value=[roll]
        ) as mock_query:
            with mock.patch.object(roll, "Rebase") as rebase:
                with mock.patch.object(
                    self.committer._gerrit_helper, "ChangeEdit"
                ) as ce:
                    self.committer.ProcessObsoleteLKGMRolls()
                    mock_query.assert_called_once()

                    # Confirm that it does rebasing.
                    rebase.assert_called_once_with(allow_conflicts=True)
                    ce.assert_called_once_with(GERRIT_NUM, mock.ANY, ROLL_TO)

    @mock.patch("chromite.lib.gob_util.GetFileContents")
    def testDoNothingObsoleteLKGMs(self, mock_get_file):
        """Tests that trying to abandon the obsolete lkgm CLs."""
        mock_get_file.return_value = "10002.0.0"

        # LKGM Roll CL from "10002.0.0" to "10003.0.0" should NOT be in the
        # merge-conflict state, since the current LKGM version is "10002.0.0".
        ROLL_FROM = "10002.0.0"
        ROLL_TO = "10003.0.0"
        GERRIT_NUM = 3876551
        # Even if mergeable=False, the logic should not do nothing.
        roll = StubGerritChange(
            GERRIT_NUM,
            ROLL_TO,
            ROLL_TO,
            mergeable=False,
            original_file_content=ROLL_FROM,
        )

        with mock.patch.object(
            self.committer._gerrit_helper, "Query", return_value=[roll]
        ) as mock_query:
            with mock.patch.object(roll, "Rebase") as rebase:
                with mock.patch.object(
                    self.committer._gerrit_helper, "ChangeEdit"
                ) as ce:
                    self.committer.ProcessObsoleteLKGMRolls()
                    mock_query.assert_called_once()

                    # Confirm that it does nothing.
                    rebase.assert_not_called()
                    ce.assert_not_called()

    @mock.patch("chromite.lib.gob_util.GetFileContents")
    def testVersionWithChromeBranch(self, mock_get_file):
        """Tests passing a version with a chrome branch strips the branch."""
        branch = "refs/branch-heads/5000"
        self.committer = chrome_chromeos_lkgm.ChromeLKGMCommitter(
            "1003.0.0-rc2", branch
        )
        mock_get_file.return_value = "1002.0.0"

        with mock.patch.object(
            self.committer._gerrit_helper, "CreateChange"
        ) as cg:
            cg.return_value = mock.MagicMock(gerrit_number=123456)
            with mock.patch.object(
                self.committer._gerrit_helper, "ChangeEdit"
            ) as ce:
                with mock.patch.object(
                    self.committer._gerrit_helper, "SetReview"
                ) as bc:
                    with mock.patch.object(
                        self.committer._gerrit_helper, "SetHashtags"
                    ):
                        # Check the file was actually written out correctly.
                        self.committer.UpdateLKGM()
                        cg.assert_called_once_with(
                            "chromium/src", branch, mock.ANY, False
                        )
                        ce.assert_called_once_with(
                            123456, "chromeos/CHROMEOS_LKGM", "1003.0.0"
                        )
                        bc.assert_called_once_with(
                            123456,
                            labels={"Bot-Commit": 1, "Commit-Queue": 2},
                            notify="NONE",
                            ready=True,
                            reviewers=[
                                "chrome-os-gardeners-reviews@google.com"
                            ],
                        )

    def testCommitMsg(self):
        """Tests format of the commit message."""
        self.committer._PRESUBMIT_BOTS = ["bot1", "bot2"]
        self.committer._buildbucket_id = "some-build-id"
        commit_msg_lines = self.committer.ComposeCommitMsg().splitlines()
        self.assertIn(
            "Automated Commit: LKGM 1001.0.0 for chromeos.", commit_msg_lines
        )
        self.assertIn(
            "Uploaded by https://ci.chromium.org/b/some-build-id",
            commit_msg_lines,
        )
        self.assertIn(
            "CQ_INCLUDE_TRYBOTS=luci.chrome.try:bot1", commit_msg_lines
        )
        self.assertIn(
            "CQ_INCLUDE_TRYBOTS=luci.chrome.try:bot2", commit_msg_lines
        )
