# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Attempt automated fixes on the specified files."""

import logging
from pathlib import Path

from chromite.cli import command
from chromite.cli.cros import cros_format


@command.command_decorator("fix")
class FixCommand(command.CliCommand):
    """Automatically fix format/lint/etc... issues."""

    use_dryrun_options = True
    # Override base class property to use path filter options.
    use_filter_options = True

    @classmethod
    def AddParser(cls, parser):
        super().AddParser(parser)
        parser.add_argument(
            "--check",
            dest="dryrun",
            action="store_true",
            help="Display files with errors & exit non-zero",
        )
        parser.add_argument(
            "--diff",
            action="store_true",
            help="Display diff instead of fixed content",
        )
        parser.add_argument(
            "--stdout",
            dest="inplace",
            action="store_false",
            help="Write to stdout",
        )
        parser.add_argument(
            "-i",
            "--inplace",
            default=True,
            action="store_true",
            help="Fix files inplace (default)",
        )
        parser.add_argument(
            "--commit",
            type=str,
            help="Use files from git commit instead of on disk.",
        )
        parser.add_argument(
            "files",
            nargs="*",
            type=Path,
            help=(
                "Files to fix. Directories will be expanded, and if in a "
                "git repository, the .gitignore will be respected."
            ),
        )

    def Run(self):
        files = self.options.files
        if not files:
            # Running with no arguments is allowed to make the repo upload hook
            # simple, but print a warning so that if someone runs this manually
            # they are aware that nothing was changed.
            logging.warning("No files provided.  Doing nothing.")
            return 0

        # TODO(build): Integrate linters that have a --fix option.
        cmd = cros_format.FormatCommand(self.options)
        return cmd.Run()
