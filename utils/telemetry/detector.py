# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Defines the ResourceDetector to capture resource properties."""

import abc
import os
import platform
import sys
from typing import Dict

from chromite.utils.telemetry import psutil


CPU_NAME = "cpu.name"
CPU_ARCHITECTURE = "cpu.architecture"
PROCESS_CWD = "process.cwd"
PROCESS_EXECUTABLE_NAME = "process.executable.name"
PROCESS_EXECUTABLE_PATH = "process.executabe.path"
PROCESS_COMMAND_NAME = "process.command.name"
PROCESS_COMMAND_ARGS = "process.command.args"
PROCESS_PID = "process.pid"
PROCESS_OWNER = "process.owner"
PROCESS_RUNTIME_NAME = "process.runtime.name"
PROCESS_RUNTIME_DESCRIPTION = "process.runtime.description"
PROCESS_RUNTIME_VERSION = "process.runtime.version"
PROCESS_RUNTIME_API_VERSION = "process.runtime.apiversion"
OS_NAME = "os.name"
OS_TYPE = "os.type"
OS_DESCRIPTION = "os.description"


class ResourceDetector(abc.ABC):
    """The primary interface for resource detectors."""

    @abc.abstractmethod
    def detect(self) -> Dict:
        """Captures and returns the information about the resource."""

        raise NotImplementedError()


class ProcessDetector(ResourceDetector):
    """ResourceDetector to capture information about the process."""

    def __init__(self):
        self._resource = {}

    def detect(self) -> Dict:
        if not self._resource:
            p = psutil.Process()
            self._resource = {
                PROCESS_PID: os.getpid(),
                PROCESS_CWD: os.getcwd(),
                PROCESS_OWNER: os.geteuid(),
                PROCESS_RUNTIME_NAME: platform.python_implementation(),
                PROCESS_RUNTIME_VERSION: platform.python_version(),
                PROCESS_RUNTIME_DESCRIPTION: sys.version,
                PROCESS_RUNTIME_API_VERSION: sys.api_version,
                PROCESS_EXECUTABLE_NAME: p.name(),
                PROCESS_EXECUTABLE_PATH: p.exe(),
                PROCESS_COMMAND_NAME: sys.argv[0],
                PROCESS_COMMAND_ARGS: p.cmdline(),
            }

        return self._resource.copy()


class SystemDetector(ResourceDetector):
    """ResourceDetector to capture information about system."""

    def __init__(self):
        self._resource = {}

    def detect(self) -> Dict:
        if not self._resource:
            self._resource = {
                OS_NAME: platform.system(),
                OS_TYPE: platform.system(),
                OS_DESCRIPTION: platform.platform(),
                CPU_ARCHITECTURE: platform.machine(),
                CPU_NAME: platform.processor(),
            }

        return self._resource.copy()
