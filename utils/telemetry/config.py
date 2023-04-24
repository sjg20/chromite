# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Provides telemetry configuration utilities."""

import configparser
import os


ENABLED_KEY = "enabled"
TRACE_KEY = "trace"
DEFAULT_CONFIG = {TRACE_KEY: {ENABLED_KEY: False}}


class TraceConfig:
    """Tracing specific config in Telemetry config."""

    def __init__(self, config):
        self._enabled = config.getboolean(ENABLED_KEY, False)

    @property
    def enabled(self) -> bool:
        """Value of trace.enabled property in telemetry.cfg."""

        return self._enabled


class Config:
    """Telemetry configuration."""

    def __init__(self, path: os.PathLike):
        self._config = configparser.ConfigParser()

        if not os.path.exists(path):
            self._config.read_dict(DEFAULT_CONFIG)
            with open(path, "w", encoding="utf-8") as configfile:
                self._config.write(configfile)
        else:
            with open(path, "r", encoding="utf-8") as configfile:
                self._config.read_file(configfile)

        self._trace_config = TraceConfig(self._config[TRACE_KEY])

    @property
    def trace_config(self) -> TraceConfig:
        """The trace config in telemetry."""

        return self._trace_config
