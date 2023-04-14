# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""The tests for resource detector classes."""

import os
import platform

import psutil

from chromite.utils.telemetry import detector


def test_process_info_capture():
    """Test that ProcessDetector captures correct process info."""
    p = psutil.Process()
    env_var = list(p.environ().keys())[0]

    d = detector.ProcessDetector(allowed_env=[env_var])
    attrs = d.detect().attributes

    assert attrs[detector.PROCESS_PID] == p.pid
    assert attrs[detector.PROCESS_CWD] == os.getcwd()
    assert attrs[detector.PROCESS_COMMAND] == p.cmdline()[0]
    assert attrs[detector.PROCESS_COMMAND_ARGS] == tuple(p.cmdline()[1:])
    assert attrs[detector.PROCESS_EXECUTABLE_NAME] == p.name()
    assert attrs[detector.PROCESS_EXECUTABLE_PATH] == p.exe()
    assert attrs[f"process.env.{env_var}"] == p.environ()[env_var]


def test_system_info_captured():
    """Test that SystemDetector captures the correct system info."""
    d = detector.SystemDetector()
    attrs = d.detect().attributes

    assert attrs[detector.OS_NAME] == os.name
    assert attrs[detector.OS_TYPE] == platform.system()
    assert attrs[detector.OS_DESCRIPTION] == platform.platform()
    assert attrs[detector.CPU_ARCHITECTURE] == platform.machine()
    assert attrs[detector.CPU_NAME] == platform.processor()
