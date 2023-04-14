# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Defines the ResourceDetector to capture resource properties."""

import os
import platform
import sys
from typing import Sequence

from opentelemetry.sdk.resources import OS_DESCRIPTION
from opentelemetry.sdk.resources import OS_TYPE
from opentelemetry.sdk.resources import PROCESS_COMMAND
from opentelemetry.sdk.resources import PROCESS_COMMAND_ARGS
from opentelemetry.sdk.resources import PROCESS_EXECUTABLE_NAME
from opentelemetry.sdk.resources import PROCESS_EXECUTABLE_PATH
from opentelemetry.sdk.resources import PROCESS_OWNER
from opentelemetry.sdk.resources import PROCESS_PID
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.resources import ResourceDetector
import psutil


CPU_ARCHITECTURE = "cpu.architecture"
CPU_NAME = "cpu.name"
PROCESS_CWD = "process.cwd"
PROCESS_RUNTIME_API_VERSION = "process.runtime.apiversion"
PROCESS_ENV = "process.env"
OS_NAME = "os.name"


class ProcessDetector(ResourceDetector):
    """ResourceDetector to capture information about the process."""

    def __init__(self, allowed_env: Sequence[str] = None):
        self._allowed_env = allowed_env or ["USE"]

    def detect(self) -> Resource:
        p = psutil.Process()
        env = p.environ()
        resource = {
            PROCESS_PID: p.pid,
            PROCESS_CWD: p.cwd(),
            PROCESS_OWNER: p.uids().effective,
            PROCESS_RUNTIME_API_VERSION: sys.api_version,
            PROCESS_EXECUTABLE_NAME: p.name(),
            PROCESS_EXECUTABLE_PATH: p.exe(),
            PROCESS_COMMAND: p.cmdline()[0],
            PROCESS_COMMAND_ARGS: p.cmdline()[1:],
        }
        resource.update(
            {
                f"{PROCESS_ENV}.{k}": env[k]
                for k in self._allowed_env
                if k in env
            }
        )

        return Resource(resource)


class SystemDetector(ResourceDetector):
    """ResourceDetector to capture information about system."""

    def detect(self) -> Resource:
        resource = {
            OS_NAME: os.name,
            OS_TYPE: platform.system(),
            OS_DESCRIPTION: platform.platform(),
            CPU_ARCHITECTURE: platform.machine(),
            CPU_NAME: platform.processor(),
        }

        return Resource(resource)
