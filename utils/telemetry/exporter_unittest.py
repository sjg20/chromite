# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittests for SpanExporter classes."""

import datetime
import time
import urllib.request

from opentelemetry.sdk import trace
from opentelemetry.sdk.trace.export import SpanExportResult

from chromite.api.gen.chromite.telemetry import clientanalytics_pb2
from chromite.api.gen.chromite.telemetry import trace_span_pb2
from chromite.utils.telemetry import exporter


class MockResponse(object):
    """Mock requests.Response."""

    def __init__(self, status, text):
        self._status = status
        self._text = text

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def read(self):
        return self._text


tracer = trace.TracerProvider().get_tracer(__name__)


def test_otel_span_translation(monkeypatch):
    """Test ClearcutSpanExporter to translate otel spans to TraceSpan."""
    requests = []

    def mock_urlopen(request, timeout=0):
        requests.append((request, timeout))
        resp = clientanalytics_pb2.LogResponse()
        resp.next_request_wait_millis = 1
        body = resp.SerializeToString()
        return MockResponse(200, body)

    monkeypatch.setattr(urllib.request, "urlopen", mock_urlopen)

    span = tracer.start_span("name")
    span.end()

    e = exporter.ClearcutSpanExporter()

    assert e.export([span]) == SpanExportResult.SUCCESS
    req, _ = requests[0]
    log_request = clientanalytics_pb2.LogRequest()
    log_request.ParseFromString(req.data)

    assert log_request.request_time_ms <= int(time.time() * 1000)
    assert len(log_request.log_event) == 1

    # The following constants are defined in chromite.utils.telemetry.exporter
    # as _CLIENT_TYPE and _LOG_SOURCE respectively.
    assert log_request.client_info.client_type == 33
    assert log_request.log_source == 2044

    tspan = trace_span_pb2.TraceSpan()
    tspan.ParseFromString(log_request.log_event[0].source_extension)

    assert tspan.name == span.name
    assert tspan.start_time_millis == int(span.start_time / 10e6)
    assert tspan.end_time_millis == int(span.end_time / 10e6)


def test_export_to_http_api(monkeypatch):
    """Test ClearcutSpanExporter to export spans over http."""
    requests = []

    def mock_urlopen(request, timeout=0):
        requests.append((request, timeout))
        resp = clientanalytics_pb2.LogResponse()
        resp.next_request_wait_millis = 1
        body = resp.SerializeToString()
        return MockResponse(200, body)

    monkeypatch.setattr(urllib.request, "urlopen", mock_urlopen)

    span = tracer.start_span("name")
    span.end()
    endpoint = "http://domain.com/path"

    e = exporter.ClearcutSpanExporter(endpoint=endpoint, timeout=7)

    assert e.export([span])
    req, timeout = requests[0]
    assert req.full_url == endpoint
    assert timeout == 7


def test_export_to_http_api_throttle(monkeypatch):
    """Test ClearcutSpanExporter to throttle based on prev response."""
    mock_open_times = []

    # pylint: disable=unused-argument
    def mock_urlopen(request, timeout=0):
        nonlocal mock_open_times
        mock_open_times.append(datetime.datetime.now())
        resp = clientanalytics_pb2.LogResponse()
        resp.next_request_wait_millis = 1000
        body = resp.SerializeToString()
        return MockResponse(200, body)

    monkeypatch.setattr(urllib.request, "urlopen", mock_urlopen)

    span = tracer.start_span("name")
    span.end()

    e = exporter.ClearcutSpanExporter()

    assert e.export([span])
    assert e.export([span])

    # We've called export() on the same exporter instance twice, so we expect
    # the following things to be true:
    #   1. The request.urlopen() function has been called exactly twice, and
    #   2. The calls to urlopen() are more than 1000 ms apart (due to the
    #      value in the mock_urlopen response).
    # The mock_open_times list is a proxy for observing this behavior directly.
    assert len(mock_open_times) == 2
    assert (mock_open_times[1] - mock_open_times[0]).total_seconds() > 1
