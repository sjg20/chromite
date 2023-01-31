# Copyright 2016 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""This script performs an Android uprev.

After calling, it prints out a JSON representing the result, with the new
Android version atom string included. A caller could then use this atom with
emerge to build the newly uprevved version of Android e.g.

./cros_mark_android_as_stable \
    --android_build_branch=git_pi-arc \
    --android_package=android-container-pi

Returns {"android_atom": "chromeos-base/android-container-pi-6417892-r1"}

emerge-eve =chromeos-base/android-container-pi-6417892-r1
"""

import filecmp
import glob
import json
import logging
import os

from chromite.lib import commandline
from chromite.lib import constants
from chromite.lib import cros_build_lib
from chromite.lib import git
from chromite.lib import osutils
from chromite.lib import portage_util
from chromite.lib import repo_util
from chromite.scripts import cros_mark_as_stable
from chromite.service import android
from chromite.service import packages


# Dir where all the action happens.
_OVERLAY_DIR = "%(srcroot)s/private-overlays/project-cheets-private/"

_GIT_COMMIT_MESSAGE = """Marking latest for %(android_package)s ebuild with \
version %(android_version)s as stable.

BUG=None
TEST=CQ
"""

_RUNTIME_ARTIFACTS_BUCKET_URL = "gs://chromeos-arc-images/runtime_artifacts"


def FindAndroidCandidates(package_dir):
    """Return a tuple of Android's unstable ebuild and stable ebuilds.

    Args:
      package_dir: The path to where the package ebuild is stored.

    Returns:
      Tuple [unstable_ebuild, stable_ebuilds].

    Raises:
      Exception: if no unstable ebuild exists for Android.
    """
    stable_ebuilds = []
    unstable_ebuilds = []
    for path in glob.glob(os.path.join(package_dir, "*.ebuild")):
        ebuild = portage_util.EBuild(path)
        if ebuild.version == "9999":
            unstable_ebuilds.append(ebuild)
        else:
            stable_ebuilds.append(ebuild)

    # Apply some confidence checks.
    if not unstable_ebuilds:
        raise Exception("Missing 9999 ebuild for %s" % package_dir)
    if not stable_ebuilds:
        logging.warning("Missing stable ebuild for %s", package_dir)

    return portage_util.BestEBuild(unstable_ebuilds), stable_ebuilds


def UpdateDataCollectorArtifacts(
    android_version, runtime_artifacts_bucket_url, package_name
):
    r"""Finds and includes into variables artifacts from arc.DataCollector.

    This verifies default android version. In case artificts are not found for
    default Android version it tries to find artifacts for pinned version. If
    pinned version is provided, it is required artifacts exist for the pinned
    version.

    Args:
      android_version: The \d+ build id of Android.
      runtime_artifacts_bucket_url: root of runtime artifacts
      package_name: android package name. Used to determine the pinned version if exists.

    Returns:
      dictionary with filled ebuild variables.
    """
    # Check the existing version. If we find any artifacts, use them.
    variables = android.FindDataCollectorArtifacts(
        package_name,
        android_version,
        "${PV}",
        runtime_artifacts_bucket_url,
    )
    if variables:
        # Data artificts were found.
        return variables

    # Check pinned version for the current branch.
    milestone = packages.determine_milestone_version()
    pin_version = android.FindRuntimeArtifactsPin(
        package_name,
        milestone,
        runtime_artifacts_bucket_url,
    )
    if pin_version is None:
        # No pinned version.
        logging.warning(
            "No data collector artifacts were found for %s", android_version
        )
        return variables

    logging.info("Pinned version %s overrides %s", pin_version, android_version)
    variables = android.FindDataCollectorArtifacts(
        package_name,
        pin_version,
        pin_version,
        runtime_artifacts_bucket_url,
    )
    if not variables:
        # If pin version set it must contain data.
        raise Exception(
            f"Pinned version {pin_version} does not contain artifacts"
        )
    return variables


def MarkAndroidEBuildAsStable(
    stable_candidate,
    unstable_ebuild,
    android_package,
    android_version,
    package_dir,
    build_branch,
    arc_bucket_url,
    runtime_artifacts_bucket_url,
):
    r"""Uprevs the Android ebuild.

    This is the main function that uprevs from a stable candidate
    to its new version.

    Args:
      stable_candidate: ebuild that corresponds to the stable ebuild we are
        revving from.  If None, builds the a new ebuild given the version
        with revision set to 1.
      unstable_ebuild: ebuild corresponding to the unstable ebuild for Android.
      android_package: android package name.
      android_version: The \d+ build id of Android.
      package_dir: Path to the android-container package dir.
      build_branch: branch of Android builds.
      arc_bucket_url: URL of the target ARC build gs bucket.
      runtime_artifacts_bucket_url: root of runtime artifacts

    Returns:
      Tuple[str, List[str], List[str]] if revved, or None
      1. Full portage version atom (including rc's, etc) that was revved.
      2. List of files to be `git add`ed.
      3. List of files to be `git rm`ed.
    """

    def IsTheNewEBuildRedundant(new_ebuild, stable_ebuild):
        """Returns True if the new ebuild is redundant.

        This is True if there if the current stable ebuild is the exact same copy
        of the new one.
        """
        if not stable_ebuild:
            return False

        if stable_candidate.version_no_rev == new_ebuild.version_no_rev:
            return filecmp.cmp(
                new_ebuild.ebuild_path, stable_ebuild.ebuild_path, shallow=False
            )
        return False

    # Case where we have the last stable candidate with same version just rev.
    if stable_candidate and stable_candidate.version_no_rev == android_version:
        new_ebuild_path = "%s-r%d.ebuild" % (
            stable_candidate.ebuild_path_no_revision,
            stable_candidate.current_revision + 1,
        )
    else:
        pf = "%s-%s-r1" % (android_package, android_version)
        new_ebuild_path = os.path.join(package_dir, "%s.ebuild" % pf)

    build_targets = android.GetAndroidEbuildTargetsForPackage(android_package)
    variables = {"BASE_URL": arc_bucket_url}
    for var, target in build_targets.items():
        # TODO(b/255705023): Have MirrorArtifacts generate the mapping for us.
        variables[var] = f"{build_branch}-linux-{target}"

    variables.update(
        UpdateDataCollectorArtifacts(
            android_version,
            runtime_artifacts_bucket_url,
            android_package,
        )
    )

    portage_util.EBuild.MarkAsStable(
        unstable_ebuild.ebuild_path,
        new_ebuild_path,
        variables,
        make_stable=True,
    )
    new_ebuild = portage_util.EBuild(new_ebuild_path)

    # Determine whether this is ebuild is redundant.
    if IsTheNewEBuildRedundant(new_ebuild, stable_candidate):
        msg = "Previous ebuild with same version found and ebuild is redundant."
        logging.info(msg)
        osutils.SafeUnlink(new_ebuild_path)
        return None

    files_to_add = [new_ebuild_path]
    files_to_remove = []
    if stable_candidate and not stable_candidate.IsSticky():
        osutils.SafeUnlink(stable_candidate.ebuild_path)
        files_to_remove.append(stable_candidate.ebuild_path)

    # Update ebuild manifest and git add it.
    gen_manifest_cmd = ["ebuild", new_ebuild_path, "manifest", "--force"]
    cros_build_lib.run(gen_manifest_cmd, extra_env=None, print_cmd=True)
    files_to_add.append(os.path.join(package_dir, "Manifest"))

    return (
        f"{new_ebuild.package}-{new_ebuild.version}",
        files_to_add,
        files_to_remove,
    )


def _PrepareGitBranch(overlay_dir):
    """Prepares a git branch for the uprev commit.

    If the overlay project is currently on a branch (e.g. patches are being
    applied), rebase the new branch on top of it.

    Args:
      overlay_dir: The overlay directory.
    """
    existing_branch = git.GetCurrentBranch(overlay_dir)
    repo_util.Repository.MustFind(overlay_dir).StartBranch(
        constants.STABLE_EBUILD_BRANCH, projects=["."], cwd=overlay_dir
    )
    if existing_branch:
        git.RunGit(overlay_dir, ["rebase", existing_branch])


def _CommitChange(message, android_package_dir, files_to_add, files_to_remove):
    """Commit changes to git with list of files to add/remove."""
    git.RunGit(android_package_dir, ["add", "--"] + files_to_add)
    if files_to_remove:
        git.RunGit(android_package_dir, ["rm", "--"] + files_to_remove)

    portage_util.EBuild.CommitChange(message, android_package_dir)


def GetParser():
    """Creates the argument parser."""
    parser = commandline.ArgumentParser()
    parser.add_argument("-b", "--boards")
    parser.add_argument(
        "--android_bucket_url",
        default=android.ANDROID_BUCKET_URL,
        type="gs_path",
    )
    parser.add_argument(
        "--android_build_branch",
        help="Android branch to import from, overriding default",
    )
    parser.add_argument(
        "--android_package",
        required=True,
        choices=android.GetAllAndroidPackages(),
        help="Android package to uprev",
    )
    parser.add_argument(
        "--arc_bucket_url", default=constants.ARC_BUCKET_URL, type="gs_path"
    )
    parser.add_argument("-f", "--force_version", help="Android build id to use")
    parser.add_argument(
        "-s",
        "--srcroot",
        default=os.path.join(constants.SOURCE_ROOT, "src"),
        help="Path to the src directory",
    )
    parser.add_argument(
        "--runtime_artifacts_bucket_url",
        default=_RUNTIME_ARTIFACTS_BUCKET_URL,
        type="gs_path",
    )
    parser.add_argument(
        "--skip_commit",
        action="store_true",
        help="Skip commiting uprev changes to git",
    )
    return parser


def main(argv):
    parser = GetParser()
    options = parser.parse_args(argv)
    options.Freeze()

    overlay_dir = os.path.abspath(_OVERLAY_DIR % {"srcroot": options.srcroot})
    android_package_dir = android.GetAndroidPackageDir(
        options.android_package, overlay_dir=overlay_dir
    )

    if not options.skip_commit:
        _PrepareGitBranch(overlay_dir)

    # Use default Android branch if not overridden.
    android_build_branch = (
        options.android_build_branch
        or android.GetAndroidBranchForPackage(options.android_package)
    )

    (unstable_ebuild, stable_ebuilds) = FindAndroidCandidates(
        android_package_dir
    )
    # Mirror artifacts, i.e., images and some sdk tools (e.g., adb, aapt).
    version_to_uprev = android.MirrorArtifacts(
        options.android_package,
        options.android_bucket_url,
        android_build_branch,
        options.arc_bucket_url,
        android_package_dir,
        options.force_version,
    )

    stable_candidate = portage_util.BestEBuild(stable_ebuilds)

    if stable_candidate:
        logging.info("Stable candidate found %s", stable_candidate.version)
    else:
        logging.info("No stable candidate found.")

    revved = MarkAndroidEBuildAsStable(
        stable_candidate,
        unstable_ebuild,
        options.android_package,
        version_to_uprev,
        android_package_dir,
        android_build_branch,
        options.arc_bucket_url,
        options.runtime_artifacts_bucket_url,
    )

    output = dict(revved=bool(revved))

    if revved:
        android_atom, files_to_add, files_to_remove = revved
        if not options.skip_commit:
            _CommitChange(
                _GIT_COMMIT_MESSAGE
                % {
                    "android_package": options.android_package,
                    "android_version": version_to_uprev,
                },
                android_package_dir,
                files_to_add,
                files_to_remove,
            )
        if options.boards:
            cros_mark_as_stable.CleanStalePackages(
                options.srcroot, options.boards.split(":"), [android_atom]
            )

        output["android_atom"] = android_atom
        # This field is read by the PUpr uprev handler for creating CLs. We cannot
        # return absolute paths because this script runs inside chroot but the uprev
        # handler runs outside.
        # Here we return paths relative to |overlay_dir|.
        output["modified_files"] = [
            os.path.relpath(f, overlay_dir)
            for f in files_to_add + files_to_remove
        ]

    # The output is being parsed by service.packages.uprev_android and has to be
    # in its own single line. When invoked from chromite API endpoints, entering
    # chroot can generate junk messages on stdout, so we prefix our output with a
    # line break to further ensure that.
    print("\n" + json.dumps(output, sort_keys=True))
