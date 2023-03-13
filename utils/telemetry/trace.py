# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""The tracing library that provides the Tracer."""

import contextlib
import datetime
import time
from typing import Dict, Optional, Union
import uuid

# Required due to incomplete proto support in chromite. This proto usage is not
# tied to the Build API, so delegating the proto handling to api/ does not make
# sense. When proto is better supported in chromite, the protos could, for
# example, live somewhere in utils/ instead.
from chromite.api.gen.chromite.telemetry import trace_span_pb2


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


class PocSpan:
    """Simple proof of concept span implementation."""

    def __init__(self, name: str, trace_id=None):
        self._msg = trace_span_pb2.TraceSpan()
        self._msg.name = name
        self._msg.context.trace_id = trace_id or str(uuid.uuid4())
        self._msg.context.span_id = str(uuid.uuid4())

    def __enter__(self):
        self._msg.start_time_millis = round(time.time() * 1000)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._msg.end_time_millis = round(time.time() * 1000)

    def as_proto(self):
        """Return the proto representation of the span."""
        return self._msg

    def set_attribute(self, attr: str, val):
        """Set an attribute."""
        self._msg.attributes[attr] = val

    def add_event(
        self,
        name: str,
        attrs: Optional[Dict] = None,
        when: Optional[Union[int, datetime.datetime]] = None,
    ):
        """Add an event."""
        attrs = attrs or {}
        when = when or round(time.time() * 1000)
        if isinstance(when, datetime.datetime):
            when = round(when.timestamp() * 1000)

        event = self._msg.events.add()
        event.name = name
        event.event_time_millis = when
        for k, v in attrs.items():
            event.attributes[k] = v

    def set_status(self, code=None, message=None):
        """Set the status."""
        if code is None:
            status_code = trace_span_pb2.TraceSpan.Status.STATUS_CODE_UNSET
        elif not code:
            status_code = trace_span_pb2.TraceSpan.Status.STATUS_CODE_OK
        else:
            status_code = trace_span_pb2.TraceSpan.Status.STATUS_CODE_ERROR

        self._msg.status.status_code = status_code
        self._msg.status.message = message or ""


class PocTracer:
    """Simple proof of concept tracer."""

    def __init__(self):
        self._trace_id = str(uuid.uuid4())
        self._spans = []
        self.exporters = []

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        for exporter in self.exporters:
            exporter.export(self.spans_as_proto())

    @contextlib.contextmanager
    def start_as_current_span(self, name: str):
        """Provides a new span to used as context."""
        span = PocSpan(name, self._trace_id)
        self._spans.append(span)
        with span:
            yield span

    def spans_as_proto(self):
        """Get the spans as proto messages."""
        return [x.as_proto() for x in self._spans]
