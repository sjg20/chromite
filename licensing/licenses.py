# Copyright 2012 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Generate an HTML file containing license info for all installed packages.

Documentation on this script is also available here:
https://dev.chromium.org/chromium-os/licensing/licensing-for-chromiumos-developers

End user (i.e. package owners) documentation is here:
https://dev.chromium.org/chromium-os/licensing/licensing-for-chromiumos-package-owners

Usage:
For this script to work, you must have built the architecture
this is being run against, _after_ you've last run repo sync.
Otherwise, it will query newer source code and then fail to work on packages
that are out of date in your build.

Recommended build:
  cros_sdk
  export BOARD=x86-alex
  sudo rm -rf /build/$BOARD
  cd ~/chromiumos/src/scripts
  # If you wonder why we need to build Chromium OS just to run
  # `emerge -p -v virtual/target-os` on it, we don't.
  # However, later we run ebuild unpack, and this will apply patches and run
  # configure. Configure will fail due to aclocal macros missing in
  # /build/x86-alex/usr/share/aclocal (those are generated during build).
  # This will take about 10mn on a Z620.
  build_packages --board=$BOARD --no-withautotest --no-withtest --no-withdev \
                   --no-withfactory
  cd ~/chromiumos/chromite/licensing
  # This removes left over packages from an earlier build that could cause
  # conflicts.
  eclean-$BOARD packages
  %(prog)s [--debug] [--all-packages] --board $BOARD [-o o.html] 2>&1 | tee out

The workflow above is what you would do to generate a licensing file by hand
given a chromeos tree.
Note that building packages now creates a license.yaml fork in the package
which you can see with
qtbz2 -x -O  /build/x86-alex/packages/dev-util/libc-bench-0.0.1-r8.tbz2 |
     qxpak -x -O - license.yaml
This gets automatically installed in
/build/x86-alex/var/db/pkg/dev-util/libc-bench-0.0.1-r8/license.yaml

Unless you run with --generate-licenses, the script will now gather those
license bits and generate a license file from there.
License bits for each package are generated by default from
src/scripts/hooks/install/gen-package-licenses.sh which gets run automatically
by emerge as part of a package build (by running this script with
--hook /path/to/tmp/portage/build/tree/for/that/package

If license bits are missing, they are generated on the fly if you were running
with sudo. If you didn't use sudo, this on the fly late generation will fail
and act as a warning that your prebuilts were missing package build time
licenses.

You can check the licenses and/or generate a HTML file for a list of
packages using --package or -p:
  %(prog)s --package "dev-libs/libatomic_ops-7.2d" --package \
  "net-misc/wget-1.14" --board $BOARD -o out.html

Note that you'll want to use --generate-licenses to force regeneration of the
licensing bits from a package source you may have just modified but not rebuilt.

If you want to check licensing against all ChromeOS packages, you should
run `build_packages --board=$BOARD` to build everything and then run this script
with --all-packages.

By default, when no package is specified, this script processes all
packages for $BOARD.
"""

import logging
import os

from chromite.lib import build_target_lib
from chromite.lib import commandline
from chromite.lib import cros_build_lib
from chromite.licensing import licenses_lib


def LoadPackageInfo(sysroot, all_packages, generateMissing, packages):
    """Do the work when we're not called as a hook."""
    logging.info("Processing sysroot %s", sysroot)

    detect_packages = not packages
    if detect_packages:
        # If no packages were specified, we look up the full list.
        packages = licenses_lib.ListInstalledPackages(sysroot, all_packages)

    assert packages, f"{sysroot}: could not find any packages"

    logging.debug(
        "Initial Package list to work through:\n%s", "\n".join(sorted(packages))
    )
    licensing = licenses_lib.Licensing(sysroot, packages, generateMissing)

    licensing.LoadPackageInfo()
    logging.debug(
        "Package list to skip:\n%s",
        "\n".join([p for p in sorted(packages) if licensing.packages[p].skip]),
    )
    logging.debug(
        "Package list left to work through:\n%s",
        "\n".join(
            [p for p in sorted(packages) if not licensing.packages[p].skip]
        ),
    )
    licensing.ProcessPackageLicenses()

    return licensing


def get_parser() -> commandline.ArgumentParser:
    """Return a command line parser."""
    parser = commandline.ArgumentParser(usage=__doc__)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-b", "--board", help="which board to run for, like x86-alex"
    )
    group.add_argument(
        "--sysroot",
        type="path",
        help="which sysroot to run on (e.g. /build/eve)",
    )

    parser.add_argument(
        "-p",
        "--package",
        action="append",
        default=[],
        dest="packages",
        help="check the license of the package, e.g.,"
        "dev-libs/libatomic_ops-7.2d",
    )
    parser.add_argument(
        "-a",
        "--all-packages",
        action="store_true",
        help="Run licensing against all packages in the "
        "build tree, instead of just virtual/target-os "
        "dependencies.",
    )
    parser.add_argument(
        "-g",
        "--generate-licenses",
        action="store_true",
        dest="gen_licenses",
        help="Generate license information, if missing.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type="path",
        help="which html file to create with output",
    )
    parser.add_argument(
        "-c",
        "--compress-output",
        action="store_true",
        help="whether to compress the html output. If true, output must end in "
        "an appropriate extension.",
    )
    return parser


def main(args):
    parser = get_parser()
    opts = parser.parse_args(args)

    if not opts.output and not opts.gen_licenses:
        parser.error("You must specify --output and/or --generate-licenses")

    sysroot = opts.sysroot or build_target_lib.get_default_sysroot_path(
        opts.board
    )

    if (
        opts.output
        and os.path.exists(opts.output)
        and not os.path.isfile(opts.output)
    ):
        parser.error(f"--output must point to a file: {opts.output}")

    if opts.compress_output:
        if not opts.output:
            parser.error("--compress-output requires --output")
        if (
            cros_build_lib.CompressionExtToType(opts.output)
            == cros_build_lib.CompressionType.NONE
        ):
            parser.error(
                "if --compress-output is specified, --output must end in "
                f"appropriate compression format but is: {opts.output}"
            )

    licensing = LoadPackageInfo(
        sysroot, opts.all_packages, opts.gen_licenses, opts.packages
    )

    if opts.output:
        licensing.GenerateHTMLLicenseOutput(
            opts.output, compress_output=opts.compress_output
        )
