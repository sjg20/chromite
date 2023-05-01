# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Defines the ResourceDetector to capture resource properties."""

import getpass
import os
from pathlib import Path
import platform
import sys
from typing import Sequence

from opentelemetry.sdk import resources
import psutil


CPU_ARCHITECTURE = "cpu.architecture"
CPU_NAME = "cpu.name"
CPU_COUNT = "cpu.count"
HOST_TYPE = "host.type"
MEMORY_SWAP_TOTAL = "memory.swap.total"
MEMORY_TOTAL = "memory.total"
PROCESS_CWD = "process.cwd"
PROCESS_RUNTIME_API_VERSION = "process.runtime.apiversion"
PROCESS_ENV = "process.env"
OS_NAME = "os.name"
DMI_PATH = Path("/sys/class/dmi/id/product_name")
GCE_DMI = "Google Compute Engine"
CROS_BOT_USER = "chromeos-bot"


class ProcessDetector(resources.ResourceDetector):
    """ResourceDetector to capture information about the process."""

    def __init__(self, allowed_env: Sequence[str] = None):
        self._allowed_env = allowed_env or ["USE"]

    def detect(self) -> resources.Resource:
        p = psutil.Process()
        env = p.environ()
        resource = {
            PROCESS_CWD: p.cwd(),
            PROCESS_RUNTIME_API_VERSION: sys.api_version,
            resources.PROCESS_PID: p.pid,
            resources.PROCESS_OWNER: p.uids().effective,
            resources.PROCESS_EXECUTABLE_NAME: p.name(),
            resources.PROCESS_EXECUTABLE_PATH: p.exe(),
            resources.PROCESS_COMMAND: p.cmdline()[0],
            resources.PROCESS_COMMAND_ARGS: p.cmdline()[1:],
        }
        resource.update(
            {
                f"{PROCESS_ENV}.{k}": env[k]
                for k in self._allowed_env
                if k in env
            }
        )

        return resources.Resource(resource)


class SystemDetector(resources.ResourceDetector):
    """ResourceDetector to capture information about system."""

    def detect(self) -> resources.Resource:
        host_type = "UNKNOWN"

        if DMI_PATH.exists():
            host_type = DMI_PATH.read_text(encoding="utf-8")

        if host_type == GCE_DMI and getpass.getuser() == CROS_BOT_USER:
            host_type = "chromeos-bot"

        resource = {
            CPU_ARCHITECTURE: platform.machine(),
            CPU_COUNT: psutil.cpu_count(),
            CPU_NAME: platform.processor(),
            HOST_TYPE: host_type,
            MEMORY_SWAP_TOTAL: psutil.swap_memory().total,
            MEMORY_TOTAL: psutil.virtual_memory().total,
            OS_NAME: os.name,
            resources.OS_TYPE: platform.system(),
            resources.OS_DESCRIPTION: platform.platform(),
        }

        return resources.Resource(resource)
