# Copyright 2017 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Tests for cros_sdk."""

import os
import re
import sys

from chromite.lib import constants
from chromite.lib import cros_build_lib
from chromite.lib import cros_test_lib
from chromite.lib import retry_util
from chromite.scripts import cros_sdk


class CrosSdkUtilsTest(cros_test_lib.MockTempDirTestCase):
    """Tests for misc util funcs."""

    def testGetArchStageTarballs(self):
        """Basic test of GetArchStageTarballs."""
        self.assertCountEqual(
            [
                "https://storage.googleapis.com/chromiumos-sdk/cros-sdk-123.tar.xz",
            ],
            cros_sdk.GetArchStageTarballs("123"),
        )

    def testFetchRemoteTarballsEmpty(self):
        """Test FetchRemoteTarballs with no results."""
        m = self.PatchObject(retry_util, "RunCurl")
        with self.assertRaises(ValueError):
            cros_sdk.FetchRemoteTarballs(self.tempdir, [])
        m.return_value = cros_build_lib.CompletedProcess(stdout=b"Foo: bar\n")
        with self.assertRaises(ValueError):
            cros_sdk.FetchRemoteTarballs(self.tempdir, ["gs://x.tar"])

    def testFetchRemoteTarballsSuccess(self):
        """Test FetchRemoteTarballs with a successful download."""
        curl = cros_build_lib.CompletedProcess(
            stdout=(b"HTTP/1.0 200\n" b"Foo: bar\n" b"Content-Length: 100\n")
        )
        self.PatchObject(retry_util, "RunCurl", return_value=curl)
        self.assertEqual(
            os.path.join(self.tempdir, "tar"),
            cros_sdk.FetchRemoteTarballs(self.tempdir, ["gs://x/tar"]),
        )


class CrosSdkParserCommandLineTest(cros_test_lib.MockTestCase):
    """Tests involving the CLI."""

    # pylint: disable=protected-access

    # A typical sys.argv[0] that cros_sdk sees.
    ARGV0 = "/home/chronos/chromiumos/chromite/bin/cros_sdk"

    def setUp(self):
        self.parser, _ = cros_sdk._CreateParser("1", "2")

    def testSudoCommand(self):
        """Verify basic sudo command building works."""
        # Stabilize the env for testing.
        for v in (
            constants.CHROOT_ENVIRONMENT_ALLOWLIST + constants.ENV_PASSTHRU
        ):
            os.environ[v] = "value"
        os.environ["PATH"] = "path"

        cmd = cros_sdk._SudoCommand()
        assert cmd[0] == "sudo"
        assert "CHROMEOS_SUDO_PATH=path" in cmd
        rlimits = [x for x in cmd if x.startswith("CHROMEOS_SUDO_RLIMITS=")]
        assert len(rlimits) == 1

        # Spot check some pass thru vars.
        assert "GIT_AUTHOR_EMAIL=value" in cmd
        assert "https_proxy=value" in cmd

        # Make sure we only pass vars after `sudo`.
        for i in range(1, len(cmd)):
            assert "=" in cmd[i]
            v = cmd[i].split("=", 1)[0]
            assert re.match(r"^[A-Za-z0-9_]+$", v) is not None

    def testReexecCommand(self):
        """Verify reexec command line building."""
        # Stub sudo logic since we tested it above already.
        self.PatchObject(cros_sdk, "_SudoCommand", return_value=["sudo"])
        opts = self.parser.parse_args([])
        new_cmd = cros_sdk._BuildReExecCommand([self.ARGV0], opts)
        assert new_cmd == ["sudo", "--", sys.executable, self.ARGV0]

    def testReexecCommandStrace(self):
        """Verify reexec command line building w/strace."""
        # Stub sudo logic since we tested it above already.
        self.PatchObject(cros_sdk, "_SudoCommand", return_value=["sudo"])

        # Strace args passed, but not enabled.
        opts = self.parser.parse_args(["--strace-arguments=-s4096 -v"])
        new_cmd = cros_sdk._BuildReExecCommand([self.ARGV0], opts)
        assert new_cmd == ["sudo", "--", sys.executable, self.ARGV0]

        # Strace enabled.
        opts = self.parser.parse_args(["--strace"])
        new_cmd = cros_sdk._BuildReExecCommand([self.ARGV0], opts)
        assert new_cmd == [
            "sudo",
            "--",
            "strace",
            "--",
            sys.executable,
            self.ARGV0,
        ]

        # Strace enabled w/args.
        opts = self.parser.parse_args(
            ["--strace", "--strace-arguments=-s4096 -v"]
        )
        new_cmd = cros_sdk._BuildReExecCommand([self.ARGV0], opts)
        assert new_cmd == [
            "sudo",
            "--",
            "strace",
            "-s4096",
            "-v",
            "--",
            sys.executable,
            self.ARGV0,
        ]
