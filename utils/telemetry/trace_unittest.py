# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Test the trace module in telemetry library"""


from opentelemetry import trace as otel_trace_api
from opentelemetry.sdk import trace as otel_trace_sdk

from chromite.utils.telemetry import trace


tracer = otel_trace_sdk.TracerProvider().get_tracer(__name__)


def test_inject_context():
    """Test inject_context to set traceparent in passed carrier."""

    with tracer.start_as_current_span("test_inject_context") as span:
        carrier = {}
        trace.inject_context(carrier)

        span_context = span.get_span_context()
        traceparent = "-".join(
            [
                "00",
                otel_trace_api.format_trace_id(span_context.trace_id),
                otel_trace_api.format_span_id(span_context.span_id),
                f"{span_context.trace_flags:02x}",
            ]
        )

        print(traceparent)
        print(span_context.trace_id)
        print(span_context.span_id)

        assert carrier["traceparent"] == traceparent


def test_extract_context():
    """Test extract_context to parse context from traceparent."""

    carrier = {
        "traceparent": "00-e698aa36475e5b53f745b9cf2180e678-079bca6fdcd6bc42-01"
    }

    context = trace.extract_context(carrier)

    span_context = otel_trace_api.propagation.get_current_span(
        context
    ).get_span_context()

    assert span_context.trace_id == 306515120463068847130265386468134413944
    assert span_context.span_id == 548254361450888258
