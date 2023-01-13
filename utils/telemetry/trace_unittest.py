# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Test for telemetry trace."""

from chromite.utils.telemetry import trace


def test_no_op_tracer():
    """Test the NoOp tracer to work as desired in spec."""
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("name") as span:
        assert span.__class__.__name__ == "NoOpSpan"

    assert tracer.__class__.__name__ == "NoOpTracer"
