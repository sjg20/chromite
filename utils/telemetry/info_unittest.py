# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Test the config and anonymizer utils."""

import getpass
import re

from chromite.lib import cros_build_lib
from chromite.utils.telemetry import info


def test_is_enabled_for_invalid_host():
    """Test that tracer is disabled for random hostname."""
    c = info.Config(hostname="hello.some-cloud.com")

    assert not c.is_enabled()


def test_is_enabled_for_valid_host():
    """Test that tracer is enabled for *.googlers.com hostname."""
    c = info.Config(hostname=f"{cros_build_lib.GetRandomString()}.googlers.com")

    assert c.is_enabled()


def test_has_opt_in_config():
    """Test that opt is returns true always."""
    c = info.Config()

    assert c.has_opt_in_config()


def test_default_anonymizer_to_remove_username_from_path():
    """Test that default Anonymizer redacts username."""
    text = "/home/%s/docs" % getpass.getuser()

    a = info.Anonymizer()

    output = a.apply(text)
    assert output == "/home/${USER}/docs"


def test_anonymizer_to_apply_passed_replacements():
    """Test anonymizer to apply the requested replacements."""
    text = "/home/%s/docs" % getpass.getuser()

    replacements = [(re.escape(getpass.getuser()), "<user>")]
    a = info.Anonymizer(replacements=replacements)
    output = a.apply(text)

    assert output == "/home/<user>/docs"


def test_anonymizer_to_apply_multiple_replacements():
    """Test anonymizer to apply the passed replacements in order."""
    replacements = [(re.escape("abc"), "x"), (re.escape("xyz"), "t")]
    text = "hello abcd. how is xyz. abcyz"

    a = info.Anonymizer(replacements=replacements)
    output = a.apply(text)

    assert output == "hello xd. how is t. t"
