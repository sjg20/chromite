# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""The tracing library that provides the Tracer."""

from logging import ERROR
from logging import getLogger
from typing import Optional


# Disable warning log messages in opentelemetry
getLogger("opentelemetry.util._time").setLevel(ERROR)


_GET_TRACER_DELEGATE = None


if not _GET_TRACER_DELEGATE:
    from opentelemetry import trace
    from opentelemetry.sdk.resources import get_aggregated_resources
    from opentelemetry.sdk.resources import OTELResourceDetector
    from opentelemetry.sdk.resources import ProcessResourceDetector
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor

    from chromite.utils.telemetry.detector import ProcessDetector
    from chromite.utils.telemetry.detector import SystemDetector
    from chromite.utils.telemetry.exporter import ClearcutSpanExporter

    resource = get_aggregated_resources(
        [
            ProcessResourceDetector(),
            OTELResourceDetector(),
            ProcessDetector(),
            SystemDetector(),
        ]
    )
    trace.set_tracer_provider(TracerProvider(resource=resource))
    trace.get_tracer_provider().add_span_processor(
        BatchSpanProcessor(ClearcutSpanExporter())
    )
    _GET_TRACER_DELEGATE = trace.get_tracer


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
