# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Provides info related utils."""

import getpass
import re
import socket
from typing import Optional, Pattern, Sequence, Text, Tuple


class Config:
    """Telemetry configuration."""

    def __init__(self, hostname: Optional[Text] = None):
        hostname = hostname or socket.gethostname()

        self._is_google = False
        if hostname.endswith("googlers.com"):
            self._is_google = True

        self._opt_in = True

    def has_opt_in_config(self):
        """Checks whether the user answered telemetry opt in."""
        return self._opt_in is not None

    def is_enabled(self):
        """Checks if the telemetry is enabled."""
        return self._is_google and self._opt_in


class Anonymizer:
    """Redact the personally indentifiable information."""

    def __init__(
        self, replacements: Optional[Sequence[Tuple[Pattern[str], Text]]] = None
    ):
        self._replacements = replacements or []
        self._replacements.append((re.escape(getpass.getuser()), "${USER}"))

    def apply(self, data: Text) -> Text:
        """Applies the replacement rules to data text."""
        if not data:
            return data

        for repl_from, repl_to in self._replacements:
            data, _ = re.subn(repl_from, repl_to, data)

        return data
