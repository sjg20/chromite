# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Defines the ResourceDetector to capture resource properties."""

import os
import platform
import sys
from typing import Sequence

from opentelemetry.sdk import resources
import psutil


CPU_ARCHITECTURE = "cpu.architecture"
CPU_NAME = "cpu.name"
PROCESS_CWD = "process.cwd"
PROCESS_RUNTIME_API_VERSION = "process.runtime.apiversion"
PROCESS_ENV = "process.env"
OS_NAME = "os.name"


class ProcessDetector(resources.ResourceDetector):
    """ResourceDetector to capture information about the process."""

    def __init__(self, allowed_env: Sequence[str] = None):
        self._allowed_env = allowed_env or ["USE"]

    def detect(self) -> resources.Resource:
        p = psutil.Process()
        env = p.environ()
        resource = {
            resources.PROCESS_PID: p.pid,
            PROCESS_CWD: p.cwd(),
            resources.PROCESS_OWNER: p.uids().effective,
            PROCESS_RUNTIME_API_VERSION: sys.api_version,
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
        resource = {
            OS_NAME: os.name,
            resources.OS_TYPE: platform.system(),
            resources.OS_DESCRIPTION: platform.platform(),
            CPU_ARCHITECTURE: platform.machine(),
            CPU_NAME: platform.processor(),
        }

        return resources.Resource(resource)
