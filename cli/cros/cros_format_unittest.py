# Copyright 2022 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""This module tests the cros format command."""

from pathlib import Path

from chromite.cli.cros import cros_format
from chromite.format import formatters
from chromite.lib import commandline
from chromite.lib import cros_test_lib
from chromite.lib import osutils


# pylint: disable=protected-access


class FormatCommandTest(cros_test_lib.TestCase):
    """Tests that don't involve real files."""

    def setUp(self):
        # Set up default options for tests to play with for running cros format.
        self.parser = commandline.ArgumentParser(filter=True)
        cros_format.FormatCommand.AddParser(self.parser)
        self.options = self.parser.parse_args([])

    def testBreakoutFilesByTool(self):
        """Check extension<->tool mapping."""
        self.assertEqual({}, cros_format._BreakoutFilesByTool([]))
        self.assertEqual(
            {},
            cros_format._BreakoutFilesByTool([Path("foo"), Path("blah.xxx")]),
        )

        tool_map = cros_format._BreakoutFilesByTool([Path("foo.md")])
        self.assertEqual(
            {formatters.whitespace.Data: [Path("foo.md")]}, tool_map
        )

    def testCliNoFiles(self):
        """Check cros format handling with no files."""
        cmd = cros_format.FormatCommand(self.options)
        self.assertEqual(0, cmd.Run())

    def testCliNoMatchedFiles(self):
        """Check cros format handling with no matched files."""
        self.options.files = [Path("foo")]
        cmd = cros_format.FormatCommand(self.options)
        self.assertEqual(0, cmd.Run())


class FormatCommandTempDirTests(cros_test_lib.TempDirTestCase):
    """Tests that use real files."""

    def setUp(self):
        # Set up default parser for tests to play with for running cros format.
        self.parser = commandline.ArgumentParser(filter=True)
        cros_format.FormatCommand.AddParser(self.parser)

    def testCliOneFile(self):
        """Check behavior with one file."""
        file = self.tempdir / "foo.txt"
        osutils.Touch(file)
        opts = self.parser.parse_args([str(file)])
        cmd = cros_format.FormatCommand(opts)
        self.assertEqual(0, cmd.Run())

    def testCliDir(self):
        """Test the CLI expands directories when given one."""
        files = [self.tempdir / "foo.txt", self.tempdir / "bar.txt"]
        for file in files:
            osutils.Touch(file)
        opts = self.parser.parse_args([str(self.tempdir)])
        cmd = cros_format.FormatCommand(opts)
        self.assertEqual(0, cmd.Run())

    def testCliManyFile(self):
        """Check behavior with many files."""
        files = []
        for n in range(0, 10):
            file = self.tempdir / f"foo.{n}.txt"
            osutils.Touch(file)
            files.append(str(file))
        opts = self.parser.parse_args(files)
        cmd = cros_format.FormatCommand(opts)
        self.assertEqual(0, cmd.Run())

    def testDiffFile(self):
        """Check behavior with --diff file."""
        file = self.tempdir / "foo.txt"
        file.write_text(" ", encoding="utf-8")
        opts = self.parser.parse_args(["--diff", str(file)])
        cmd = cros_format.FormatCommand(opts)
        self.assertEqual(1, cmd.Run())
        self.assertEqual(" ", file.read_text(encoding="utf-8"))

    def testCheckFile(self):
        """Check behavior with --check file."""
        file = self.tempdir / "foo.txt"
        file.write_text(" ", encoding="utf-8")
        for arg in ("-n", "--dry-run", "--check"):
            opts = self.parser.parse_args([arg, str(file)])
            cmd = cros_format.FormatCommand(opts)
            self.assertEqual(1, cmd.Run())
            self.assertEqual(" ", file.read_text(encoding="utf-8"))

    def testStdoutFile(self):
        """Check behavior with --stdout file."""
        file = self.tempdir / "foo.txt"
        file.write_text(" ", encoding="utf-8")
        opts = self.parser.parse_args(["--stdout", str(file)])
        cmd = cros_format.FormatCommand(opts)
        self.assertEqual(1, cmd.Run())
        self.assertEqual(" ", file.read_text(encoding="utf-8"))

    def testInplaceFile(self):
        """Check behavior with --inplace file."""
        file = self.tempdir / "foo.txt"
        file.write_text(" ", encoding="utf-8")
        opts = self.parser.parse_args([str(file)])
        cmd = cros_format.FormatCommand(opts)
        self.assertEqual(0, cmd.Run())
        self.assertEqual("", file.read_text(encoding="utf-8"))
