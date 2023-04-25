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
from typing import Dict, List

from chromite.lib import commandline
from chromite.lib import config_lib
from chromite.lib import gerrit


# Gerrit will merge a max of 240 dependencies. Leave some room
# for dependencies from the platform/ec repo.
MAX_GERRIT_CHANGES = 225

site_params = config_lib.GetSiteParams()
gerrit_helper = gerrit.GetGerritHelper(site_params.EXTERNAL_REMOTE)


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


def _check_cl(
    downstream_candidate_cl: Dict,
) -> List[str]:
    """Check whether the given CL is OK to downstream.

    Args:
        downstream_candidate_cl: Dict representing the CL that we want to downstream.

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
    if "copybot-skip" in downstream_candidate_cl["hashtags"]:
        warnings.append("Change marked with copybot-skip")
    if re.search(
        "\nC[Qq]-Depend:",
        downstream_candidate_cl["revisions"][
            downstream_candidate_cl["current_revision"]
        ]["commit"]["message"],
    ):
        warnings.append("Found Cq-Depend in change!")

    return warnings


def _filter_cls(
    cls_to_downstream: List[Dict], limit: int = None, stop_at: str = None
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
    if limit > MAX_GERRIT_CHANGES or not limit:
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
        warnings = _check_cl(change)
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
