# Copyright 2022 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Internal helper for attaching & detaching disk images.

We have a long history of the kernel flaking when working with loopback devices,
so this helper takes care of setting up & tearing it down reliably.
"""

import os
from pathlib import Path
import sys
from typing import List, Optional

from chromite.lib import commandline
from chromite.lib import constants
from chromite.lib import cros_build_lib
from chromite.lib import image_lib
from chromite.lib import osutils
from chromite.utils import pformat


def get_parser() -> commandline.ArgumentParser:
    """Return a command line parser."""
    parser = commandline.ArgumentParser(description=__doc__)

    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True

    subparser = subparsers.add_parser(
        "attach", help="Attach a disk image to a loopback device."
    )
    subparser.add_argument(
        "path",
        type=Path,
        help="Disk image to attach.",
    )

    subparser = subparsers.add_parser(
        "detach", help="Detach a loopback device."
    )
    subparser.add_argument(
        "path",
        type=Path,
        help="Loopback device to free.",
    )

    return parser


def main(argv: Optional[List[str]] = None) -> Optional[int]:
    parser = get_parser()
    opts = parser.parse_args(argv)

    if not osutils.IsRootUser():
        result = cros_build_lib.sudo_run(
            [os.path.join(constants.CHROMITE_SCRIPTS_DIR, "cros_losetup")]
            + argv,
            check=False,
        )
        return result.returncode

    if opts.subcommand == "attach":
        loop_path = image_lib.LoopbackPartitions.attach_image(opts.path)
        print(
            pformat.json(
                {
                    "path": loop_path,
                },
                compact=not sys.stdin.isatty(),
            ),
            end="",
        )
    elif opts.subcommand == "detach":
        if not image_lib.LoopbackPartitions.detach_loopback(opts.path):
            return 1
    else:
        raise RuntimeError(f"Unknown command: {opts.subcommand}")

    return 0
