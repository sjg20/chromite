# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""The tests for resource detector classes."""

import os
import platform
import random
import sys

from chromite.lib import cros_build_lib
from chromite.utils.telemetry import detector
from chromite.utils.telemetry import psutil


def test_process_info_capture():
    """Test that ProcessDetector captures correct process info."""
    p = psutil.Process()
    d = detector.ProcessDetector()
    attrs = d.detect()

    assert attrs[detector.PROCESS_PID] == p.pid
    assert attrs[detector.PROCESS_CWD] == os.getcwd()
    assert (
        attrs[detector.PROCESS_RUNTIME_NAME] == platform.python_implementation()
    )
    assert attrs[detector.PROCESS_RUNTIME_VERSION] == platform.python_version()
    assert attrs[detector.PROCESS_RUNTIME_DESCRIPTION] == sys.version
    assert attrs[detector.PROCESS_COMMAND_NAME] == sys.argv[0]
    assert attrs[detector.PROCESS_COMMAND_ARGS] == p.cmdline()
    assert attrs[detector.PROCESS_EXECUTABLE_NAME] == p.name()
    assert attrs[detector.PROCESS_EXECUTABLE_PATH] == p.exe()


def test_process_info_immutability():
    """Test that ProcessDetector returns copy of dict."""
    p = psutil.Process()
    d = detector.ProcessDetector()
    attrs = d.detect()

    attrs[detector.PROCESS_PID] = p.pid + random.randint(10, 1000)

    assert attrs[detector.PROCESS_PID] != p.pid
    assert d.detect()[detector.PROCESS_PID] == p.pid


def test_system_info_captured():
    """Test that SystemDetector captures the correct system info."""
    d = detector.SystemDetector()
    attrs = d.detect()

    assert attrs[detector.OS_NAME] == platform.system()
    assert attrs[detector.OS_TYPE] == platform.system()
    assert attrs[detector.OS_DESCRIPTION] == platform.platform()
    assert attrs[detector.CPU_ARCHITECTURE] == platform.machine()
    assert attrs[detector.CPU_NAME] == platform.processor()


def test_system_info_immutability():
    """Test that SystemDetector returns copy of dict."""
    d = detector.SystemDetector()
    attrs = d.detect()

    attrs[detector.OS_NAME] = f"cool-os-{cros_build_lib.GetRandomString()}"

    assert attrs[detector.OS_NAME] != platform.system()
    assert d.detect()[detector.OS_NAME] == platform.system()
