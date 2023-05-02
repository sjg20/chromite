# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""A cros command used to retrieve firmware archives from Google Storage."""

import logging

from chromite.cli import command
from chromite.lib.fwbuddy import fwbuddy


@command.command_decorator("fwget")
class FwgetCommand(command.CliCommand):
    """Downloads firmware archives from Google Storage"""

    EPILOG = f"""
ATTENTION: fwget is still under heavy development and not to be relied on for
anything serious. YOU HAVE BEEN WARNED. For questions/concerns/suggestions
please create a bug at {fwbuddy.BUG_SUBMIT_URL}

Downloads and extracts the firmware archive identified by a given fwbuddy URI
to a local folder.

{fwbuddy.USAGE}

Examples:
    cros fwget fwbuddy://dedede/galnat360/galtic/latest/signed path/to/put/extracted/archive
    cros fwget fwbuddy://dedede/galnat360/galtic/latest/signed path/to/put/ec.bin
"""

    @classmethod
    def AddParser(cls, parser):
        """Add parser arguments."""
        super(FwgetCommand, cls).AddParser(parser)
        parser.add_argument(
            "uri",
            nargs=1,
            help="The fwbuddy URI that identifies the firmware archive.",
        )
        parser.add_argument(
            "path",
            nargs=1,
            type="dir_exists",
            help="The path to the local folder where the firmware archive will "
            "be extracted to.",
        )

    def Run(self):
        """Downloads the firmware archive and extract its contents to path"""
        logging.notice(self.options.uri[0])
        logging.notice(self.options.path[0])
