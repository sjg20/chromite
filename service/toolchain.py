# Copyright 2022 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Toolchain-related operations."""

import logging
import os
from pathlib import Path
import re
import subprocess
from typing import Dict, Iterable, List, NamedTuple, Text, Tuple

from chromite.lib import chroot_util
from chromite.lib import cros_build_lib
from chromite.lib import osutils
from chromite.lib import portage_util
from chromite.lib.parser import package_info


if cros_build_lib.IsInsideChroot():
    # Only used for linting in chroot and requires yaml which is only in chroot
    from chromite.scripts import tricium_cargo_clippy
    from chromite.scripts import tricium_clang_tidy

    # TODO(b/229665884): Move the implementation details for parsing lints to
    # a new lib module. Scripts should not have to import scripts.


class ToolchainServiceError(Exception):
    """Base module error."""


class NotChrootError(ToolchainServiceError):
    """An error raised when linting endpoints are invoked outside the chroot."""


class ParsingError(ToolchainServiceError):
    """An error raised when parsing lint files in an unexpected format."""


class CodeLocation(NamedTuple):
    """Holds the code location of a linter finding."""

    filepath: str
    contents: str
    line_start: int
    line_end: int
    col_start: int
    col_end: int


class SuggestedFix(NamedTuple):
    """Holds information about a linter finding."""

    replacement: str
    location: CodeLocation


class LinterFinding(NamedTuple):
    """Holds information about a linter finding."""

    name: str
    message: str
    locations: List[CodeLocation]
    linter: str
    suggested_fixes: List[SuggestedFix]


class BuildLinter:
    """Provides functions to support endpoints for the Build Linters recipe."""

    # FIXME(b/229769929): move linting artifiacts out of /tmp when
    TIDY_BASE_DIR = Path("/tmp/linting_output/clang-tidy")
    CARGO_BASE_DIR = Path("/tmp/cargo_clippy")
    BASE_DIR = Path("var/lib/chromeos/package-artifacts")
    GOLINT_TIMESTAMP_PATTERN = re.compile(r"(\d+).txt")
    GOLINT_PKG_PATTERN = re.compile(r"(.+)-")
    GOLINT_LINT_PATTERN = re.compile(
        r"(?P<file_path>[^\s]+\.go):(?P<line>\d+):\d+:\s+(?P<message>.*)"
    )
    # FIXME(b/195056381): default git-repo should be replaced with logic in
    # build_linters recipe to detect the repo path for applied patches.
    # As of 2021/5/1 only platform2 is supported so this value works temporarily.
    GIT_REPO_PATH = "/mnt/host/source/src/platform2/"

    def __init__(
        self,
        packages: List[package_info.PackageInfo],
        sysroot: Text,
        differential: bool = False,
    ):
        self.packages: List[package_info.PackageInfo] = packages
        self.sysroot: Text = sysroot
        self.differential: bool = differential

        self.package_atoms: List[str] = [package.atom for package in packages]

        if not cros_build_lib.IsInsideChroot():
            raise NotChrootError()

    def emerge_with_linting(
        self,
        use_clippy: bool = True,
        use_tidy: bool = True,
        use_golint: bool = True,
    ) -> List[LinterFinding]:
        """Emerge packages with linter features enabled and fetch the lints.

        Args:
            use_clippy: whether to set environment variables for Cargo Clippy
            use_tidy: whether to set environment variables for Clang Tidy
            use_golint: whether to set environment variables for Golint

        Returns:
            Linter findings from packages generated by emerge in a List of
            LinterFinding named tuples. These lints will be filtered if
            differential linting is enabled.
        """
        if not (use_clippy or use_tidy or use_golint):
            return []

        self._reset_temporary_files_for_linting()

        # First build the dependencies separately without linting flags to
        # prevent unsupported packages from being linted.
        emerge = chroot_util.GetEmergeCommand(self.sysroot)
        cros_build_lib.sudo_run(
            emerge + ["--onlydeps"] + self.package_atoms, preserve_env=True
        )

        # Packages outside of platform2 are currently only supported for golint
        platform2_packages = [
            p for p in self.package_atoms if self.is_package_platform2(p)
        ]
        nonplatform2_packages = [
            p for p in self.package_atoms if p not in platform2_packages
        ]

        for pkg in nonplatform2_packages:
            if use_clippy:
                logging.warning(
                    "Not using Clippy to lint %s since it's not in platform2.",
                    pkg,
                )
            if use_tidy:
                logging.warning(
                    "Not using Tidy to lint %s since it's not in platform2.",
                    pkg,
                )

        extra_env = {}
        if use_golint:
            extra_env["ENABLE_GO_LINT"] = "1"
            if nonplatform2_packages:
                cros_build_lib.sudo_run(
                    emerge + nonplatform2_packages,
                    preserve_env=True,
                    extra_env=extra_env,
                )
        if platform2_packages:
            if use_clippy:
                extra_env["ENABLE_RUST_CLIPPY"] = "1"
            if use_tidy:
                extra_env["WITH_TIDY"] = "tricium"
            cros_build_lib.sudo_run(
                emerge + platform2_packages,
                preserve_env=True,
                extra_env=extra_env,
            )

        return self.fetch_findings(use_clippy, use_tidy, use_golint)

    def fetch_findings(
        self,
        use_clippy: bool = True,
        use_tidy: bool = True,
        use_golint: bool = True,
    ) -> List[LinterFinding]:
        """Fetch lints from clippy and tidy after previously emerging with linting.

        Args:
            use_clippy: whether or not to look for lints from Cargo Clippy
            use_tidy: whether or not to look for lints from Clang Tidy
            use_golint: whether or not to look for lints from Golint

        Returns:
            Any linter findings found from the artifacts of a previous
            call to emerge as a list of LinterFinding named tuples. These
            lints will be filtered if differential linting is enabled.
        """
        findings = []
        if use_clippy:
            findings.extend(self._fetch_clippy_lints())
        if use_tidy:
            findings.extend(self._fetch_tidy_lints())
        if use_golint:
            findings.extend(self._fetch_golint_lints())
        if self.differential:
            findings = self._filter_linter_findings(findings)
        return findings

    def _reset_temporary_files_for_linting(self) -> None:
        """Prepares for linting by rming prior linter findings and caches."""
        # rm any existing lints from clang tidy
        osutils.RmDir(BuildLinter.TIDY_BASE_DIR, ignore_missing=True, sudo=True)
        osutils.SafeMakedirs(BuildLinter.TIDY_BASE_DIR, 0o777, sudo=True)

        # rm any existing temporary portage files from builds of affected packages:
        # this is required to make sure lints are always regenerated
        for package in self.package_atoms:
            cache_files_dir = f"{self.sysroot}/var/cache/portage/{package}"
            osutils.RmDir(cache_files_dir, ignore_missing=True, sudo=True)

    def _filter_linter_findings(
        self, findings: List[LinterFinding]
    ) -> List[LinterFinding]:
        """Filters findings to keep only those concerning modified lines."""
        repo_paths = self._get_git_repo_paths()
        if not repo_paths:
            # If sources aren't found for one or more packages,
            # return unfiltered findings.
            return findings
        repo_paths_dict = {repo_path: "HEAD" for repo_path in repo_paths}

        new_findings = []
        new_lines = self._get_added_lines(repo_paths_dict)
        for finding in findings:
            for loc in finding.locations:
                for (addition_start, addition_end) in new_lines.get(
                    loc.filepath, []
                ):
                    if addition_start <= loc.line_start < addition_end:
                        new_findings.append(finding)
        return new_findings

    def _get_added_lines(
        self, git_repos: Dict[Text, str]
    ) -> Dict[Text, Tuple[int, int]]:
        """Parses the lines with additions from git diff for the provided repos.

        Args:
            git_repos: a dictionary mapping repo paths to hashes for `git diff`

        Returns:
            A dictionary mapping modified filepaths to sets of tuples where each
            tuple is a (start_line, end_line) pair noting which lines were
            modified. Note that start_line is inclusive, and end_line is
            exclusive.
        """
        # TODO(b/230400788): Support differential linting of arbitrary CLs or
        #   contiguous chains of CLs

        new_lines = {}

        # Example File Paths in Git Logs:
        #   --- a/api/controller/toolchain.py
        #   +++ b/api/controller/toolchain.py
        # where we want: filename = api/controller/toolchain.py
        file_path_pattern = re.compile(r"^\+\+\+ b/(?P<file_path>.*)$")

        # Example Addition Position in git logs:
        #   @@ -20 +21,4 @@ if cros_build_lib.IsInsideChroot():
        # where we want to see that:
        #   *  line number = 21
        #   *  lines added = 4
        position_pattern = re.compile(
            r"^@@ -\d+(?:,\d+)? \+(?P<line_num>\d+)(?:,(?P<lines_added>\d+))? @@"
        )

        for git_repo, git_hash in git_repos.items():
            cmd = f"git -C {git_repo} diff -U0 {git_hash}^...{git_hash}"
            diff = cros_build_lib.run(
                cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8"
            ).stdout
            current_file = ""
            for line in diff.splitlines():
                file_path_match = re.match(file_path_pattern, str(line))
                if file_path_match:
                    current_file = file_path_match.group("file_path")
                    continue
                position_match = re.match(position_pattern, str(line))
                if position_match:
                    if current_file not in new_lines:
                        new_lines[current_file] = set()
                    line_num = int(position_match.group("line_num"))
                    line_count = position_match.group("lines_added")
                    line_count = (
                        int(line_count) if line_count is not None else 1
                    )
                    new_lines[current_file].add(
                        (line_num, line_num + line_count)
                    )
        return new_lines

    def _fetch_clippy_lints(self) -> List[LinterFinding]:
        """Get lints created by Cargo Clippy during emerge."""
        cros_build_lib.AssertInsideChroot()

        findings = tricium_cargo_clippy.parse_files(
            BuildLinter.CARGO_BASE_DIR, BuildLinter.GIT_REPO_PATH
        )
        findings = tricium_cargo_clippy.filter_diagnostics(findings)
        findings_tuples = []
        for finding in findings:
            locations = []
            for location in finding.locations:
                locations.append(
                    CodeLocation(
                        filepath=location.file_path,
                        line_start=location.line_start,
                        line_end=location.line_end,
                        # FIXME(b/244362509): Extend more details support to Rust
                        contents="",
                        col_start=None,
                        col_end=None,
                    )
                )
            findings_tuples.append(
                LinterFinding(
                    message=finding.message,
                    locations=locations,
                    linter="cargo_clippy",
                    suggested_fixes=[],
                    # FIXME(b/244362509): Extend more details support to Rust
                    name="",
                )
            )
        return findings_tuples

    def _fetch_tidy_lints(self) -> List[LinterFinding]:
        """Get lints created by Clang Tidy during emerge."""
        cros_build_lib.AssertInsideChroot()

        diagnostics = set()
        for filename in os.listdir(BuildLinter.TIDY_BASE_DIR):
            if filename.endswith(".json"):
                invocation_result = tricium_clang_tidy.parse_tidy_invocation(
                    BuildLinter.TIDY_BASE_DIR / filename
                )
                if isinstance(
                    invocation_result, tricium_clang_tidy.ExceptionData
                ):
                    logging.exception(invocation_result)
                    continue
                meta, complaints = invocation_result
                if meta.exit_code:
                    logging.warning(
                        "Invoking clang-tidy on %s with flags %s exited with "
                        "code %s; output:\n%s",
                        meta.lint_target,
                        meta.invocation,
                        meta.exit_code,
                        meta.stdstreams,
                    )
                    continue
                diagnostics.update(complaints)
        diagnostics = tricium_clang_tidy.filter_tidy_lints(
            None, None, diagnostics
        )

        return self._parse_tidy_diagnostics(diagnostics)

    def _parse_tidy_diagnostics(
        self, diagnostics: List["tricium_clang_tidy.TidyDiagnostic"]
    ) -> List[LinterFinding]:
        """Parse diagnostics created by Clang Tidy into LinterFindings objects."""
        findings = []
        for diag in diagnostics:
            filepath = self._clean_file_path(diag.file_path)
            suggested_fixes = []
            for replacement in diag.replacements:
                contents_to_replace = self._get_file_contents(
                    diag.file_path,
                    replacement.start_line,
                    replacement.end_line,
                    replacement.start_char,
                    replacement.end_char,
                )
                fix_location = CodeLocation(
                    filepath=filepath,
                    contents=contents_to_replace,
                    line_start=replacement.start_line,
                    line_end=replacement.end_line,
                    col_start=replacement.start_char,
                    col_end=replacement.end_char,
                )
                suggested_fix = SuggestedFix(
                    replacement=replacement.new_text, location=fix_location
                )
                suggested_fixes.append(suggested_fix)
            original_contents = self._get_file_contents(
                diag.file_path,
                diag.line_number,
                diag.line_number,
            )
            locations = [
                CodeLocation(
                    filepath=filepath,
                    contents=original_contents,
                    line_start=diag.line_number,
                    line_end=diag.line_number,
                    # FIXME(b/244362509): Add column data to claang tidy
                    # parsing scripts
                    col_start=None,
                    col_end=None,
                )
            ]
            finding = LinterFinding(
                name=diag.diag_name,
                message=diag.message,
                locations=locations,
                suggested_fixes=suggested_fixes,
                linter="clang_tidy",
            )
            findings.append(finding)
        return findings

    def _fetch_golint_lints(self) -> List[LinterFinding]:
        """Get lints created by Golint during emerge."""
        cros_build_lib.AssertInsideChroot()

        findings = []
        for files in self._fetch_from_linting_artifacts("go_lint").values():
            findings.extend(list(self._parse_golint_files(files)))

        return findings

    def _parse_golint_files(self, files: List[Text]) -> Iterable[LinterFinding]:
        """Parse files in the given directory for Golint lints."""
        packages_seen = set()

        # Sort files based on the timestamp appended to the file name
        files.sort(reverse=True, key=self._get_sorting_key)

        for file_path in files:
            package_match = BuildLinter.GOLINT_PKG_PATTERN.search(file_path)
            if not package_match:
                # File names are created using the package name,
                # so package_match should not be None
                raise ParsingError(
                    f"Could not parse package name from {file_path}"
                )

            package_name = package_match.group(1)
            if package_name in packages_seen:
                continue

            with Path(file_path).open(encoding="utf-8") as diagnostics:
                file_contents = diagnostics.readlines()

            # Lines should be formatted as <file>:<line>:<column>: <message>
            for line in file_contents:
                lint = BuildLinter.GOLINT_LINT_PATTERN.search(line)
                if not lint:
                    raise ParsingError(
                        "Lint line does not follow format"
                        "<file>:<line>:<column>: <message>"
                    )

                file_location = self._clean_file_path(lint.group("file_path"))
                lint_line_number = int(lint.group("line"))
                message = lint.group("message")
                location = CodeLocation(
                    filepath=file_location,
                    line_start=lint_line_number,
                    line_end=lint_line_number,
                    # FIXME(b/244362509): Extend more details support to Golang
                    contents="",
                    col_start=None,
                    col_end=None,
                )
                yield LinterFinding(
                    message=message,
                    locations=[location],
                    linter="go_lint",
                    # FIXME(b/244362509): Extend more details support to Golang
                    name="",
                    suggested_fixes=[],
                )

            packages_seen.add(package_name)

    def _fetch_from_linting_artifacts(self, subdir) -> Dict[Text, List[Text]]:
        """Get file from emerge artifact directory."""
        cros_build_lib.AssertInsideChroot()
        findings = {}
        base_dir = Path(self.sysroot) / BuildLinter.BASE_DIR
        for dirpath, _, files in os.walk(base_dir):
            path = Path(dirpath)
            if path.match(f"{base_dir}/*/*/linting_output/{subdir}"):
                package_path = path.parent.parent
                category = path.parent.name
                package = package_path.name.rsplit("-", 1)[0]
                package_atom = f"{category}/{package}"

                if not self.packages or package_atom in self.package_atoms:
                    findings[package_atom] = files

        return findings

    def _get_sorting_key(self, file_name: Text) -> int:
        """Returns integer value of timestamp used to sort Golint files."""
        return (
            0
            if not BuildLinter.GOLINT_TIMESTAMP_PATTERN.search(file_name)
            else int(
                BuildLinter.GOLINT_TIMESTAMP_PATTERN.search(file_name).group(1)
            )
        )

    def _clean_file_path(self, file_path: Text) -> str:
        """Remove git repo and work directories from file_paths."""
        file_path = re.sub("^" + BuildLinter.GIT_REPO_PATH, "", str(file_path))
        # Remove ebuild work directories from prefix
        # Such as: "**/<package>-9999/work/<package>-9999/"
        #      or: "**/<package>-0.24.52-r9/work/<package>-0.24.52/"
        return re.sub(r"(.*/)?[^/]+/work/[^/]+/+", "", file_path)

    def _get_git_repo_paths(self) -> Iterable[str]:
        """Gets the Git repo paths needed for performing differential linting."""
        repo_paths = []
        package_names = [pkg_info.package for pkg_info in self.packages]
        ebuild_paths = portage_util.FindEbuildsForPackages(
            package_names, self.sysroot
        )
        for pkg, ebuild_path in ebuild_paths.items():
            sources = [
                repo.srcdir
                for repo in portage_util.GetRepositoryForEbuild(
                    ebuild_path, self.sysroot
                )
            ]
            if not sources:
                logging.warning(
                    "Differential linting not possible for %s."
                    "Skipping differential linting.",
                    pkg.package,
                )
                return set()

            repo_paths.extend(sources)

        # Remove duplicates from different packages having the same source repo
        return set(repo_paths)

    def is_package_platform2(self, package_atom: Text) -> bool:
        """Returns whether or not a package is part of platform2.

        This is done by inspecting the output of ebuild $(equery w <package>) info.
        """
        cros_build_lib.AssertInsideChroot()

        ebuild = portage_util.FindEbuildForPackage(package_atom, self.sysroot)
        cmd = ["ebuild", ebuild, "info"]
        output = cros_build_lib.run(
            cmd, stdout=subprocess.PIPE, encoding="utf-8"
        ).stdout

        # Example output:
        #   CROS_WORKON_SRCDIR=("/mnt/host/source/src/platform2")
        #   CROS_WORKON_PROJECT=("chromiumos/platform2")
        for line in output.split():
            if line in [
                'CROS_WORKON_SRCDIR=("/mnt/host/source/src/platform2")',
                'CROS_WORKON_PROJECT=("chromiumos/platform2")',
            ]:
                return True
        return False

    def _get_file_contents(
        self,
        path: Text,
        line_start: int,
        line_end: int,
        col_start: int = None,
        col_end: int = None,
    ):
        """Attempt to get the contents of a file."""
        try:
            with Path(path).open(encoding="utf-8") as file_reader:
                file_contents = file_reader.readlines()
        except FileNotFoundError:
            return []
        # Note: line numbers are 1 indexed
        lines = file_contents[line_start - 1 : line_end]
        if lines and col_start is not None and col_end is not None:
            if col_start < len(lines[0]):
                lines[0] = lines[0][col_start:]
                lines[-1] = lines[-1][: col_end + 1]
        return "\n".join(lines)
