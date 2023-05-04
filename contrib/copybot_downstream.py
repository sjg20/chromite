#!/usr/bin/env python3
# Copyright 2022 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""CR and CQ +2 copybot project commits for downstreaming.

See go/copybot

For Zephyr Downstreaming Rotation: go/zephyr-downstreaming-guide
For coreboot Downstreaming Rotation: go/coreboot:downstreaming
"""

from collections import defaultdict
import logging
import re
from typing import Dict, List, NamedTuple, Optional

from chromite.lib import commandline
from chromite.lib import config_lib
from chromite.lib import gerrit


# Gerrit will merge a max of 240 dependencies. Leave some room
# for dependencies from the platform/ec repo.
MAX_GERRIT_CHANGES = 225


class PathDomains(NamedTuple):
    """A filepath and the domains that must review it."""

    path: str
    domains: List[str]


site_params = config_lib.GetSiteParams()
gerrit_helper = gerrit.GetGerritHelper(site_params.EXTERNAL_REMOTE)

REVIEWER_KEY_TEXT = "Original-Reviewed-by"


def project_passed_googler_review_paths_check(
    cl: dict, paths: List[str]
) -> List[str]:
    """Check paths that require further Googler review.

    * Require additional review from any paths specified by paths.

    Args:
        cl: gerrit CL dict for use in parsing.
        paths: paths to check for this project.

    Returns:
        warning_strings a list of strings to be printed for this CL.
            * This must match the expected prototype used in check_func_dict.
    """
    warning_strings = []
    revision = cl["revisions"][cl["current_revision"]]
    for path in paths:
        if any(path in s for s in revision["files"]):
            warning_strings.append(
                f"Found filepath({path}) which requires Googler review"
            )
    return warning_strings


def project_passed_domain_restricted_paths_check(
    cl: dict, path_domains: List[PathDomains]
) -> List[str]:
    """Check paths that require further Googler review.

    * Require additional review if changes to paths specified by paths
        are not reviewed by anyone in the domain list specified by paths.

    Args:
        cl: gerrit CL dict for use in parsing.
        path_domains: list of tuples(path, restricted_domains), where path is the path to
            be restricted, and restricted_domains is a list of domains that should
            have been a part of the review.

    Returns:
        warning_strings a list of strings to be printed for this CL.
            * This must match the expected prototype used in check_func_dict.
    """
    warning_strings = []
    revision = cl["revisions"][cl["current_revision"]]
    reviewers = []
    for line in revision["commit"]["message"].splitlines():
        if REVIEWER_KEY_TEXT in line:
            reviewers.append(line[(len(REVIEWER_KEY_TEXT) + 1) :])
    for path_domain in path_domains:
        if any(path_domain[0] in s for s in revision["files"]):
            reviewer_found = False
            for domain in path_domain[1]:
                if any(domain in s for s in reviewers):
                    reviewer_found = True
            if not reviewer_found:
                warning_strings.append(
                    f"Found filepath({path_domain[0]}) which requires Googler review from domain(s) {str(path_domain[1])}"
                )
    return warning_strings


def check_commit_message(cl: dict, args: List[str]) -> List[str]:
    """Check commit message for keywords.

    * Throw warning if keywords found in commit message.
        This can be useful for banned words as well as logistical issues
            such as CL's with CQ-Depend.

    Args:
        cl: gerrit CL dict for use in parsing.
        args: list of keywords to flag.

    Returns:
        warning_strings a list of strings to be printed for this CL.
            * This must match the expected prototype used in check_func_dict.
    """
    warning_strings = []
    for banned_term in args:
        if re.search(
            banned_term,
            cl["revisions"][cl["current_revision"]]["commit"]["message"],
        ):
            printable_term = "".join(banned_term.splitlines())
            warning_strings.append(f"Found {printable_term} in change!")
    return warning_strings


def check_hashtags(cl: dict, args: List[str]) -> List[str]:
    """Check hashtags for keywords.

    * Throw warning if keywords found in hashtags..

    Args:
        cl: gerrit CL dict for use in parsing.
        args: list of keywords to flag.

    Returns:
        warning_strings a list of strings to be printed for this CL.
            * This must match the expected prototype used in check_func_dict.
    """
    warning_strings = []
    for banned_hashtag in args:
        if banned_hashtag in cl["hashtags"]:
            warning_strings.append(
                f"Change marked with hashtag {banned_hashtag}"
            )
    return warning_strings


# Map of function pointers to be called when the project in the key is encountered.
#
#    Map format:
#       Key:
#           project name
#       Value:
#           List of tuples(function pointer, list of arguments) where the format of the list
#               can vary across functions.
#
#    Functions should take a CL and perform any additional checks required by the project
#    prior to downstreaming.
#
#    Args:
#        gerrit CL dict for use in parsing
#        dynamic args for use in parsing
#    Returns:
#        List of warning strings to be printed for this CL
check_func_dict = {
    "test": [
        [project_passed_googler_review_paths_check, [".md"]],
        [project_passed_domain_restricted_paths_check, [(".md", ["@md.com"])]],
        [check_commit_message, ["\nC[Qq]-Depend:.*"]],
        [check_hashtags, ["copybot-skip"]],
    ],
}


def _find_cls_to_downstream(project: str) -> List[Dict]:
    """Find all CLs to downstream for the given project.

    Args:
        project: The name of the project.

    Returns:
        A list of Gerrit CL dicts to downstream, including those which
        have the {project}-downstream topic and the CLs to which they
        are related.
    """
    copybot_downstream_cls = gerrit_helper.Query(
        topic=f"{project}-downstream",
        status="open",
        raw=True,
        verbose=True,
        convert_results=False,
    )
    return copybot_downstream_cls


def _check_cl(downstream_candidate_cl: Dict, project: str) -> List[str]:
    """Check whether the given CL is OK to downstream.

    Args:
        downstream_candidate_cl: Dict representing the CL that we want to downstream.
        project: The name of the project.

    Returns:
        warnings: A list of warning strings stating problems with the CL.
            If empty, that means there are no problems.
    """
    warnings = []
    logging.info("Processing %s", downstream_candidate_cl["_number"])
    logging.debug(
        "change info:\n\t%s",
        "\n\t".join(f"{k}:{v}" for k, v in downstream_candidate_cl.items()),
    )
    for check_func in check_func_dict.get(project, []):
        tmp_warnings = check_func[0](downstream_candidate_cl, check_func[1])
        if tmp_warnings:
            warnings.extend(tmp_warnings)

    return warnings


def _filter_cls(
    cls_to_downstream: List[Dict], limit: Optional[int] = 0, stop_at: str = None
) -> List[Dict]:
    """Filter full CL list based on the limit and/or CL the chain should stop at.

    Args:
        cls_to_downstream: Ordered list of all CL candidates to be downstreamed.
        limit: Maximum number of CLs to downstream.
        stop_at: CL in chain that downstreaming should stop at.

    Returns:
        Tuple(cls_to_downstream, all_warnings)
        cls_to_downstream: Ordered list of filtered CLs to be downstreamed.
    """
    filtered_cls = []
    if limit is None or limit > MAX_GERRIT_CHANGES:
        logging.info(
            "Limiting to maximum Gerrit changes (%d)", MAX_GERRIT_CHANGES
        )
        limit = MAX_GERRIT_CHANGES
    cls_to_downstream = cls_to_downstream[:limit]
    for change_num in cls_to_downstream:
        if stop_at and stop_at == change_num:
            logging.info(
                "Matched change: %s, stop processing other changes", change_num
            )
            break
        filtered_cls.append(change_num)
    return filtered_cls


def _get_related_cls(change_number: str) -> List[str]:
    """Get the list of related CLs for the passed in CL number.

    Args:
        change_number: CL to find relationships of.

    Returns:
        List of strings containing related CL numbers.
    """
    return [
        x["_change_number"]
        for x in gerrit_helper.GetRelatedChangesInfo(change_number)["changes"]
        if x["status"] == "NEW"
    ]


def _act_on_cls(
    cls_to_downstream: List[Dict], dry_run: bool, cq_dry_run: bool
) -> None:
    """Perform Gerrit updates on the CLs to downstream.

    Args:
        cls_to_downstream: Ordered list of all CL candidates to be downstreamed.
        dry_run: If we're dry running the script.
        cq_dry_run: If we're dry running the CQ.

    Returns:
        None
    """
    # TODO(b/278748163): Investigate bulk changes instead.
    for i, change_num in enumerate(cls_to_downstream):
        logging.info(
            "Downstreaming %s: %d/%d", change_num, i + 1, len(cls_to_downstream)
        )

        gerrit_helper.SetReviewers(
            change=change_num, dryrun=dry_run, notify="NONE"
        )
        gerrit_helper.SetReview(
            change=change_num,
            dryrun=dry_run,
            # Add Verified label because client POST removes it.
            labels={
                "Verified": "1",
                "Code-Review": "2",
                "Commit-Queue": "1" if cq_dry_run else "2",
            },
        )


def _handle_checks_results(
    all_warnings: List[str], ignore_warnings: bool
) -> int:
    """Perform Gerrit updates on the CLs to downstream.

    Args:
        all_warnings: A dictionary of lists of warning strings stating problems with these CLs.
            Key: CL number with warnings
            Value: List of warnings (str) found in the CL associated with the key.
            If empty, that means there are no problems.
        ignore_warnings: If false, treat warnings as errors.

    Returns:
        0 if warnings are acceptable/ignored.
        1 if the script should exit due to warnings.
    """
    if all_warnings:
        for cl_num, warnings in all_warnings.items():
            logging.warning(
                "http://crrev/c/%s Found warnings in change:\n\t%s",
                cl_num,
                "\n\t".join(warning for warning in warnings),
            )
        if not ignore_warnings:
            logging.error(
                "Warnings detected in this run.  Please address them.\n\t\tTo ignore the listed warnings, rerun with --ignore-warnings"
            )
            return 1
    return 0


def cmd_downstream(opts):
    """Downstream copybot project CLs."""

    copybot_downstream_cls = _find_cls_to_downstream(opts.project)

    if not copybot_downstream_cls:
        logging.info("No %s CLs to downstream!", opts.project)
        return 0

    all_warnings = defaultdict(list)
    cls_to_downstream = []
    full_cl_list = []

    for change in copybot_downstream_cls:
        logging.debug("Top level Change: %s", change["_number"])
        if change["_number"] not in cls_to_downstream:
            cls_to_downstream.append(change["_number"])
            full_cl_list.append(change)
            logging.debug("\tAdded to list")
        for related_change_number in _get_related_cls(change["_number"]):
            logging.debug("\trelated Change: %s", related_change_number)
            if related_change_number in cls_to_downstream:
                logging.debug("\t\tSkipping this one since it already exists")
                continue
            full_cl_list.append(
                gerrit_helper.GetChangeDetail(
                    related_change_number, verbose=True
                )
            )
            cls_to_downstream.append(related_change_number)

    for change in full_cl_list:
        warnings = _check_cl(change, opts.project)
        if warnings:
            all_warnings[change["_number"]] = warnings

    # CL dependencies come in with newest first, so do reverse.
    cls_to_downstream.reverse()
    result = _handle_checks_results(all_warnings, opts.ignore_warnings)
    if result != 0:
        return result
    cls_to_downstream = _filter_cls(cls_to_downstream, opts.limit, opts.stop_at)
    logging.info(
        "Downstreaming the following CLs:\n%s",
        "\n".join(str(change_num) for change_num in cls_to_downstream),
    )

    _act_on_cls(cls_to_downstream, opts.dry_run, opts.cq_dry_run)

    logging.info("All finished! Remember to monitor the CQ!")
    return 0


def cmd_clear_attention(opts):
    """Remove user from attention set on merged CLs"""

    cls_to_modify = gerrit_helper.Query(
        topic=f"{opts.project}-downstream",
        status="merged",
        attention="me",
        raw=True,
    )
    cls_to_modify.sort(key=lambda patch: patch["number"])

    if opts.limit:
        cls_to_modify = cls_to_modify[: opts.limit]

    counter = 0
    for cl in cls_to_modify:
        logging.info(
            "Updating attention set on CL %s (%d/%d)",
            cl["number"],
            counter + 1,
            len(cls_to_modify),
        )

        gerrit_helper.SetAttentionSet(
            change=cl["number"],
            remove=("me",),
            dryrun=opts.dry_run,
            notify="NONE",
        )
        counter += 1

        if opts.stop_at and opts.stop_at == cl["number"]:
            break

    logging.info("Total CLs affected: %d", counter)
    return 0


def main(args):
    """Main entry point for CLI"""
    # TODO(b/278748731): Add option to rebase CLs.
    parser = commandline.ArgumentParser(__doc__)
    parser.add_argument(
        "--dry-run", action="store_true", help="Dry run, no updates to Gerrit."
    )
    parser.add_argument(
        "--cq-dry-run",
        action="store_true",
        help="Label the patches for dry run (CQ+1) instead of merge (CQ+2, "
        "default behavior).",
    )
    parser.add_argument(
        "--limit", type=int, help="How many changes to modify, from the oldest."
    )
    parser.add_argument(
        "--stop-at", type=str, help="Stop at the specified change number."
    )
    parser.add_argument(
        "--project", type=str, default="zephyr", help="Project to downstream."
    )
    parser.add_argument(
        "--ignore-warnings",
        action="store_true",
        default=False,
        help="Ignore warnings and proceed with downstreaming action.",
    )

    #
    # Subcommands
    #
    # Used to extend the functionality of the script. If none is specified,
    # default to the main downstreaming program (original behavior)
    #

    # Utility to remove the current user from the attention set on merged CLs,
    # as this sometimes does not happen automatically and leaves the user's
    # Gerrit dashboard cluttered.
    subparser_clear_attention = parser.add_subparsers(
        title="Subcommands", dest="cmd"
    )
    subparser_clear_attention.add_parser(
        "clear_attention",
        help="Remove current user from attention set on merged downstreaming "
        "CLs",
    )

    opts = parser.parse_args(args)

    if opts.project == "test":
        opts.cq_dry_run = True
    if opts.cmd is None:
        return cmd_downstream(opts)
    if opts.cmd == "clear_attention":
        return cmd_clear_attention(opts)

    logging.error("Unknown subcommand %s", opts.cmd)
    return 1
