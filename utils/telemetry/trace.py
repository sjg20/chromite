# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""The tracing library that provides the Tracer."""

import logging
from typing import Optional


# Disable warning log messages in opentelemetry
logging.getLogger("opentelemetry.util._time").setLevel(logging.ERROR)


_GET_TRACER_DELEGATE = None


if not _GET_TRACER_DELEGATE:
    from opentelemetry import trace as otel_trace_api
    from opentelemetry.sdk import resources as otel_resources
    from opentelemetry.sdk import trace as otel_trace
    from opentelemetry.sdk.trace import export as otel_export

    from chromite.utils.telemetry import detector
    from chromite.utils.telemetry import exporter

    resource = otel_resources.get_aggregated_resources(
        [
            otel_resources.ProcessResourceDetector(),
            otel_resources.OTELResourceDetector(),
            detector.ProcessDetector(),
            detector.SystemDetector(),
        ]
    )
    otel_trace_api.set_tracer_provider(
        otel_trace.TracerProvider(resource=resource)
    )
    otel_trace_api.get_tracer_provider().add_span_processor(
        otel_export.BatchSpanProcessor(exporter.ClearcutSpanExporter())
    )
    _GET_TRACER_DELEGATE = otel_trace_api.get_tracer


def get_tracer(
    instrumenting_module_name: str,
    instrumenting_library_version: Optional[str] = None,
):
    """Returns a `Tracer` for use in instrumentation library.

    Examples:
        from chromite.utils.telemetry import trace

        tracer = trace.get_tracer(__name__)

        def somefunction():
            with tracer.start_as_current_span("greet"):
                print("Hello")

    Args:
        instrumenting_module_name: Name of the module being instrumented.
            typically set to __name__
        instrumenting_library_version: Optional version information for the
            instrumented module.

    Returns:
        An instance of tracer.
    """

    return _GET_TRACER_DELEGATE(
        instrumenting_module_name,
        instrumenting_library_version,
    )
