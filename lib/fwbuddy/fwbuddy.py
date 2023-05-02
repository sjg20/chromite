# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Main module for finding and retrieving firmware archives"""

import re
from typing import NamedTuple


USAGE = """
fwbuddy://<board>/<model>/<firmware-name>/<version>/<image-type>/<firmware-type>
        board: {dedede, atlas, etc}
        model: {galnat360, drawcia, etc.}
        firmware-name: {galtic, dood, etc.}
        version: {stable|stable-ro|latest|R99-123.456.0}
        image-type: {signed|unsigned}
        firmware-type: {serial, dev, etc} OPTIONAL
"""

BUG_SUBMIT_URL = "https://issuetracker.google.com/issues/new?component=1094001&template=1670797"

# Example: fwbuddy://dedede/galtic/latest/signed
# Example: fwbuddy://dedede/galtic/latest/signed/serial
FWBUDDY_URI_REGEX_PATTERN = re.compile(
    r"fwbuddy:\/\/(\w+)\/(\w+)\/(\w+)\/([\w\-\.]+)\/(\w+)\/?(\w+)?"
)


class FwBuddyException(Exception):
    """Exception class used by this module."""


class URI(NamedTuple):
    """All fwbuddy parameters in tuple form"""

    board: str
    model: str
    firmware_name: str
    version: str
    image_type: str
    firmware_type: str


class FwBuddy:
    """Class that manages firmware archive retrieval from Google Storage"""

    def __init__(self, uri: str):
        """Initialize fwbuddy from an fwbuddy URI

        This constructor performs all manner of URI validation and resolves
        any ambiguous version identifiers (such as "stable") to locate the
        Google Storage path for the firmware archive. This constructor calls
        out to DLM and Google Storage to accomplish this.

        This constructor will error if it is unable to determine the
        complete Google Storage path defined by the fwbuddy URI for any reason.

        Args:
            uri: An fwbuddy URI used to identify a specific firmware archive.
        """
        self.uri = parse_uri(uri)


def parse_uri(uri: str) -> URI:
    """Creates a new URI object from an fwbuddy URI string

    Args:
        uri: The fwbuddy uri in string format.

    Returns:
        A URI object with all of the fields from the fwbuddy uri string.

    Raises:
        FwBuddyException: If the fwbuddy uri is malformed.
    """

    fields = FWBUDDY_URI_REGEX_PATTERN.findall(uri)
    if len(fields) == 0 or (len(fields) == 1 and (len(fields[0]) < 5)):
        raise FwBuddyException(
            f"Unable to parse fwbuddy URI: {uri} Expected something "
            f"matching the following format: {USAGE}"
        )

    board = fields[0][0]
    model = fields[0][1]
    firmware_name = fields[0][2]
    version = fields[0][3]
    image_type = fields[0][4]
    firmware_type = None
    if len(fields[0]) == 6 and fields[0][5] != "":
        firmware_type = fields[0][5]

    return URI(
        board=board,
        model=model,
        firmware_name=firmware_name,
        version=version,
        image_type=image_type,
        firmware_type=firmware_type,
    )
