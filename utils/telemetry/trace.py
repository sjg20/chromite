# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""The tracing library that provides the Tracer."""

import contextlib
from typing import Optional


_GET_TRACER_DELEGATE = None


if not _GET_TRACER_DELEGATE:
    _GET_TRACER_DELEGATE = lambda _n, _v: NoOpTracer()


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


class NoOpSpan:
    """NoOp Span."""

    def __init__(self, name):
        self._name = name


class NoOpTracer:
    """NoOp tracer."""

    @contextlib.contextmanager
    def start_as_current_span(self, name):
        """Provides a new span to used as context."""
        yield NoOpSpan(name)
