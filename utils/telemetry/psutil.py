# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Provides utils to get information about process"""

import os
from typing import Optional, Sequence

from chromite.lib import cros_build_lib


class Process(object):
    """Class allows to read process related data."""

    def __init__(self, pid: Optional[int] = None):
        self._pid = pid or os.getpid()
        self._exe = os.readlink(f"/proc/{self._pid}/exe")
        self._cmdline = self._os_read_cmdline()
        self._status = self._os_read_status()

    def _os_read_cmdline(self) -> Sequence[str]:
        with open(f"/proc/{self._pid}/cmdline", "r", encoding="utf-8") as f:
            line = f.readline()
            return cros_build_lib.CmdToStr(line.split("\0"))

    def _os_read_status(self):
        status = dict()
        for line in open(f"/proc/{self._pid}/status", "r", encoding="utf-8"):
            key, value = line.split(":", 2)
            status[key] = value.strip()
        return status

    @property
    def pid(self) -> int:
        """The pid for the process."""
        return self._pid

    def name(self) -> str:
        """The name for the process."""
        return self._status["Name"]

    def exe(self) -> str:
        """The path to the executable."""
        return self._exe

    def cmdline(self) -> str:
        """The cmdline used to run the process."""
        return self._cmdline

    def tracer_pid(self) -> str:
        """TracerPid for the process."""
        return self._status["TracerPid"]
