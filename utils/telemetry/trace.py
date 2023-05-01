# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""The tracing library that provides the Tracer."""

from typing import Optional

from opentelemetry import trace as otel_trace
from opentelemetry.context.context import Context
from opentelemetry.propagators import textmap
from opentelemetry.trace.propagation.tracecontext import (
    TraceContextTextMapPropagator,
)


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

    return otel_trace.get_tracer(
        instrumenting_module_name,
        instrumenting_library_version,
    )


def extract_context(
    carrier: textmap.CarrierT,
    context: Optional[Context] = None,
    getter: textmap.Getter[textmap.CarrierT] = textmap.default_getter,
) -> Context:
    """Extracts SpanContext from carrier using w3c TraceContext's headers.

    See `opentelemetry.propagators.textmap.TextMapPropagator.extract`
    The extract function should retrieve values from the carrier
    object using getter, and use values to populate a
    Context value and return it.

    Args:
        carrier: and object which contains values that are
            used to construct a Context. This object
            must be paired with an appropriate getter
            which understands how to extract a value from it.
        context: an optional Context to use. Defaults to root
            context if not set.
        getter: a function that can retrieve zero
            or more values from the carrier. In the case that
            the value does not exist, return an empty list.

    Returns:
        A Context with configuration found in the carrier.
    """

    return TraceContextTextMapPropagator().extract(carrier, context, getter)


def inject_context(
    carrier: textmap.CarrierT,
    context: Optional[Context] = None,
    setter: textmap.Setter[textmap.CarrierT] = textmap.default_setter,
) -> None:
    """Injects SpanContext into carrier using w3c TraceContext's headers.

    inject enables the propagation of values into HTTP clients or
    other objects.
    See `opentelemetry.propagators.textmap.TextMapPropagator.inject`

    Examples:
        # Passing context to subprocess
        from chromite.utils.telemetry import trace

        tracer = trace.get_tracer(__name__)

        with tracer.start_as_current_span("start_child"):
            env = {}
            trace.inject_context(env)
            subprocess.run('ls', env=env)

    Args:
        carrier: An object that a place to define HTTP headers.
            Should be paired with setter, which should
            know how to set header values on the carrier.
        context: an optional Context to use. Defaults to current
            context if not set.
        setter: An optional `Setter` object that can set values
            on the carrier.
    """
    TraceContextTextMapPropagator().inject(carrier, context, setter)
