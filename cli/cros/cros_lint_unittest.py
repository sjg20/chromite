# Copyright 2014 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""This module tests the cros lint command."""

import os
from typing import List
from unittest import mock

from chromite.cli.cros import cros_lint
from chromite.lib import commandline
from chromite.lib import cros_test_lib
from chromite.lib import osutils


# pylint: disable=protected-access


class LintCommandTest(cros_test_lib.TestCase):
    """Test class for our LintCommand class."""

    def testOutputArgument(self):
        """Tests that the --output argument mapping for cpplint is complete."""
        self.assertEqual(
            set(cros_lint.LintCommand.OUTPUT_FORMATS),
            set(cros_lint.CPPLINT_OUTPUT_FORMAT_MAP.keys()) | {"default"},
        )


class JsonTest(cros_test_lib.TempDirTestCase):
    """Tests for _JsonLintFile."""

    def testValid(self):
        """Verify valid json file is accepted."""
        path = os.path.join(self.tempdir, "x.json")
        osutils.WriteFile(path, "{}\n")
        ret = cros_lint._JsonLintFile(path, None, None, False)
        self.assertEqual(ret.returncode, 0)

    def testInvalid(self):
        """Verify invalid json file is rejected."""
        path = os.path.join(self.tempdir, "x.json")
        osutils.WriteFile(path, "{")
        ret = cros_lint._JsonLintFile(path, None, None, False)
        self.assertEqual(ret.returncode, 1)

    def testUnicodeBom(self):
        """Verify we skip the Unicode BOM."""
        path = os.path.join(self.tempdir, "x.json")
        osutils.WriteFile(path, b"\xef\xbb\xbf{}\n", mode="wb")
        ret = cros_lint._JsonLintFile(path, None, None, False)
        self.assertEqual(ret.returncode, 0)


def test_non_exec(tmp_path):
    """Tests for _NonExecLintFile."""
    # Ignore dirs.
    ret = cros_lint._NonExecLintFile(tmp_path, False, False, False)
    assert ret.returncode == 0

    # Create a data file.
    path = tmp_path / "foo.txt"
    path.write_text("", encoding="utf-8")

    # -x data files are OK.
    path.chmod(0o644)
    ret = cros_lint._NonExecLintFile(path, False, False, False)
    assert ret.returncode == 0

    # +x data files are not OK.
    path.chmod(0o755)
    ret = cros_lint._NonExecLintFile(path, False, False, False)
    assert ret.returncode == 1

    # Ignore symlinks to bad files.
    sym_path = tmp_path / "sym.txt"
    sym_path.symlink_to(path.name)
    ret = cros_lint._NonExecLintFile(sym_path, False, False, False)
    assert ret.returncode == 0

    # Ignore broken symlinks.
    sym_path = tmp_path / "broken.txt"
    sym_path.symlink_to("asdfasdfasdfasdf")
    ret = cros_lint._NonExecLintFile(sym_path, False, False, False)
    assert ret.returncode == 0


def _call_cros_lint(args: List[str]) -> int:
    """Call "cros lint" with the given command line arguments.

    Args:
        args: The command line arguments.

    Returns:
        The return code of "cros lint".
    """
    parser = commandline.ArgumentParser()
    cros_lint.LintCommand.AddParser(parser)
    opts = parser.parse_args(args)
    cmd = cros_lint.LintCommand(opts)
    return cmd.Run()


def test_expand_dir(tmp_path):
    """Test the CLI expands directories when given one."""
    files = [tmp_path / "foo.txt", tmp_path / "bar.txt"]
    for file in files:
        osutils.Touch(file)
    with mock.patch(
        "chromite.cli.cros.cros_lint._BreakoutFilesByTool", spec=True
    ) as breakout_files:
        assert _call_cros_lint([str(tmp_path)]) == 0
    assert set(breakout_files.call_args.args[0]) == set(files)
