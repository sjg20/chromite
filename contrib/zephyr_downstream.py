#!/usr/bin/env python3
# Copyright 2022 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""CR and CQ +2 Zephyr commits for downstreaming.

For Zephyr Downstreaming Rotation: go/zephyr-downstreaming-guide
"""

import logging

from chromite.lib import commandline
from chromite.lib import config_lib
from chromite.lib import gerrit


# Gerrit will merge a max of 240 dependencies. Leave some room
# for dependencies from the platform/ec repo.
MAX_GERRIT_CHANGES = 225


def cmd_downstream(opts):
    """Downstream Zephyr CLs."""
    dry_run = opts.dry_run

    site_params = config_lib.GetSiteParams()
    cros = gerrit.GetGerritHelper(site_params.EXTERNAL_REMOTE)

    cls_to_downstream = cros.Query(
        topic="zephyr-downstream", status="open", raw=True
    )
    cls_to_downstream.sort(key=lambda patch: patch["number"])

    if opts.limit:
        cls_to_downstream = cls_to_downstream[: opts.limit]

    logging.info(
        "Downstreaming the following CLs:\n%s",
        "\n".join((patch["number"] for patch in cls_to_downstream)),
    )

    cq_level = "1" if opts.cq_dry_run else "2"

    stop_at = opts.stop_at
    # TODO(aaronmassey): Investigate bulk changes from Gerrit lib API instead.
    for i, patch in enumerate(cls_to_downstream):
        change_num = patch["number"]

        if stop_at and stop_at == change_num:
            logging.info(
                "Matched change: %s, stop processing other changes", change_num
            )
            break

        if i + 1 > MAX_GERRIT_CHANGES:
            logging.info(
                "Maximum Gerrit limit reached at change: %s,"
                " stop processing other changes",
                change_num,
            )
            break

        logging.info(
            "Downstreaming %s: %d/%d", change_num, i + 1, len(cls_to_downstream)
        )

        cros.SetReviewers(change=change_num, dryrun=dry_run, notify="NONE")
        cros.SetReview(
            change=change_num,
            dryrun=dry_run,
            # Add Verified label because client POST removes it.
            labels={
                "Verified": "1",
                "Code-Review": "2",
                "Commit-Queue": cq_level,
            },
        )

    logging.info("All finished! Remember to monitor the CQ!")
    return 0


def cmd_clear_attention(opts):
    """Remove user from attention set on merged CLs"""

    site_params = config_lib.GetSiteParams()
    cros = gerrit.GetGerritHelper(site_params.EXTERNAL_REMOTE)

    cls_to_modify = cros.Query(
        topic="zephyr-downstream", status="merged", attention="me", raw=True
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

        cros.SetAttentionSet(
            change=cl["number"], remove=("me",), dryrun=opts.dry_run
        )
        counter += 1

        if opts.stop_at and opts.stop_at == cl["number"]:
            break

    logging.info("Total CLs affected: %d", counter)
    return 0


def main(args):
    """Main entry point for CLI"""
    # TODO(aaronmassey): Add option to rebase CLs.
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

    if opts.cmd is None:
        return cmd_downstream(opts)
    if opts.cmd == "clear_attention":
        return cmd_clear_attention(opts)

    logging.error("Unknown subcommand %s", opts.cmd)
    return 1
