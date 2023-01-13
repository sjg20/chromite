# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Defines span exporters to be used with tracer."""

import abc
import datetime
import logging
import sys
import time
from typing import IO, Sequence
import urllib.request

from chromite.third_party.google.protobuf import json_format
from chromite.third_party.google.protobuf import message as proto_msg

# Required due to incomplete proto support in chromite. This proto usage is not
# tied to the Build API, so delegating the proto handling to api/ does not make
# sense. When proto is better supported in chromite, the protos could, for
# example, live somewhere in utils/ instead.
from chromite.api.gen.chromite.telemetry import clientanalytics_pb2
from chromite.api.gen.chromite.telemetry import trace_span_pb2


DEFAULT_ENDPOINT = "https://play.googleapis.com/log"
DEFAULT_TIMEOUT = 5
_DEFAULT_FLUSH_TIMEOUT = 30000
# Preallocated in Clearcut proto to Build.
_DEFAULT_LOG_SOURCE = 2044
# Preallocated in Clearcut proto to Python clients.
_CLIENT_TYPE = 33


class SpanExporter(abc.ABC):
    """Export the generated spans."""

    @abc.abstractmethod
    def export(self, spans: Sequence[trace_span_pb2.TraceSpan]) -> bool:
        """Export the batch of spans."""

    @abc.abstractmethod
    def shutdown(self) -> None:
        """Shutdown any open resources."""

    @abc.abstractmethod
    def force_flush(self, timeout_millis: int = _DEFAULT_FLUSH_TIMEOUT) -> bool:
        """Force flush all received spans.

        This is a hint to ensure that any received spans should be exported
        as soon as possible, preferably before returning this method.
        """


class ConsoleSpanExporter(SpanExporter):
    """Exports the spans to stdout."""

    def __init__(self, out: IO = sys.stdout):
        self._out = out

    def export(self, spans: Sequence[trace_span_pb2.TraceSpan]) -> bool:
        for span in spans:
            self._out.write(json_format.MessageToJson(span))

        self._out.flush()
        return True

    def shutdown(self) -> None:
        pass

    def force_flush(self, timeout_millis: int = 30000) -> bool:
        return True


class ClearcutSpanExporter(SpanExporter):
    """Exports the spans to google http endpoint."""

    def __init__(
        self,
        endpoint: str = DEFAULT_ENDPOINT,
        timeout: int = DEFAULT_TIMEOUT,
    ):
        self._endpoint = endpoint
        self._timeout = timeout
        self._log_source = _DEFAULT_LOG_SOURCE
        self._next_request_dt = datetime.datetime.now()

    def export(self, spans: Sequence[trace_span_pb2.TraceSpan]) -> bool:
        """Export the spans to clearcut via http api."""
        while True:
            wait_delta = self._next_request_dt - datetime.datetime.now()
            wait_time = wait_delta.total_seconds()
            if wait_time > 0:
                time.sleep(wait_time)
                continue

            logrequest = self._prepare_request_body(spans)

            req = urllib.request.Request(
                self._endpoint,
                data=logrequest.SerializeToString(),
                method="POST",
            )

            logresponse = clientanalytics_pb2.LogResponse()

            try:
                with urllib.request.urlopen(req, timeout=self._timeout) as f:
                    logresponse.ParseFromString(f.read())
            except urllib.error.URLError as e:
                logging.warning(e)
                return False
            except proto_msg.DecodeError as e:
                logging.warning("could not decode data into proto: %s", e)
                return False

            now = datetime.datetime.now()
            delta = datetime.timedelta(
                milliseconds=logresponse.next_request_wait_millis
            )
            self._next_request_dt = now + delta
            return True

    def shutdown(self) -> None:
        pass

    def force_flush(self, timeout_millis: int = 30000) -> bool:
        return True

    def _prepare_request_body(self, spans) -> clientanalytics_pb2.LogRequest:
        log_request = clientanalytics_pb2.LogRequest()
        log_request.request_time_ms = int(time.time() * 1000)
        log_request.client_info.client_type = _CLIENT_TYPE
        log_request.log_source = self._log_source

        events = []
        for span in spans:
            log_event = clientanalytics_pb2.LogEvent()
            log_event.event_time_ms = int(time.time() * 1000)
            log_event.source_extension = span.SerializeToString()
            events.append(log_event)

        log_request.log_event.extend(events)
        return log_request
