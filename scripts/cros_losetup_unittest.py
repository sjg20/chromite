# Copyright 2022 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Test the cros_losetup module."""

import json

import pytest

from chromite.lib import image_lib
from chromite.lib import osutils
from chromite.scripts import cros_losetup


@pytest.fixture(autouse=True)
def is_root_fixture(monkeypatch):
    """We don't want the code re-execing itself using sudo."""
    monkeypatch.setattr(osutils, "IsRootUser", lambda: True)


@pytest.fixture(autouse=True)
def stub_image_lib(monkeypatch):
    """Make sure these APIs aren't used by default."""

    def fail(path):
        raise RuntimeError("test is missing a mock")

    monkeypatch.setattr(image_lib.LoopbackPartitions, "detach_loopback", fail)
    monkeypatch.setattr(image_lib.LoopbackPartitions, "attach_image", fail)


def test_parser():
    """Basic tests for the parser interface."""
    parser = cros_losetup.get_parser()

    # Missing subcommand.
    with pytest.raises(SystemExit):
        parser.parse_args([])

    # Unknown subcommand.
    with pytest.raises(SystemExit):
        parser.parse_args(["asdfadsf"])

    # Missing path.
    with pytest.raises(SystemExit):
        parser.parse_args(["attach"])
    with pytest.raises(SystemExit):
        parser.parse_args(["detach"])

    # Valid commands.
    parser.parse_args(["attach", "disk.bin"])
    parser.parse_args(["detach", "/dev/loop0"])


def test_attach(monkeypatch, capsys):
    """Verify attaching runs lower APIs."""
    monkeypatch.setattr(
        image_lib.LoopbackPartitions, "attach_image", lambda x: "/dev/loop0"
    )
    assert cros_losetup.main(["attach", "disk.bin"]) == 0

    # Stdout should be JSON.
    captured = capsys.readouterr()
    data = json.loads(captured.out)
    assert "path" in data
    assert data["path"] == "/dev/loop0"


def test_detach_success(monkeypatch):
    """Verify detaching runs lower APIs."""
    monkeypatch.setattr(
        image_lib.LoopbackPartitions, "detach_loopback", lambda x: True
    )
    assert cros_losetup.main(["detach", "/dev/loop0"]) == 0


def test_detach_failure(monkeypatch):
    """Verify detaching runs lower APIs."""
    monkeypatch.setattr(
        image_lib.LoopbackPartitions, "detach_loopback", lambda x: False
    )
    assert cros_losetup.main(["detach", "/dev/loop0"]) == 1
