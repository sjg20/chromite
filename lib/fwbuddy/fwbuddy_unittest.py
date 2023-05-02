# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unit tests for fwbuddy.py."""

import pytest

from chromite.lib.fwbuddy import fwbuddy


def test_parse_uri():
    """Tests that we can properly convert a uri string into a URI object"""
    assert fwbuddy.parse_uri(
        "fwbuddy://dedede/galnat360/galtic/R99-123.456.0/signed/serial"
    ) == fwbuddy.URI(
        board="dedede",
        model="galnat360",
        firmware_name="galtic",
        version="R99-123.456.0",
        image_type="signed",
        firmware_type="serial",
    )

    assert fwbuddy.parse_uri(
        "fwbuddy://dedede/galnat360/galtic/R99-123.456.0/signed"
    ) == fwbuddy.URI(
        board="dedede",
        model="galnat360",
        firmware_name="galtic",
        version="R99-123.456.0",
        image_type="signed",
        firmware_type=None,
    )

    # Missing image_type
    with pytest.raises(fwbuddy.FwBuddyException):
        fwbuddy.parse_uri("fwbuddy://dedede/galtic/R99-123.456.0")

    # Wrong header
    with pytest.raises(fwbuddy.FwBuddyException):
        fwbuddy.parse_uri(
            "fwbozo://dedede/galnat360/galtic/R99-123.456.0/unsigned"
        )
