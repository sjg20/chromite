# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittests for SpanExporter classes."""

import datetime
import sys
from unittest import mock
import urllib.request

from chromite.third_party.google.protobuf import json_format

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


def test_export_to_console_contents(capsys):
    """Test ConsoleSpanExporter to export to sys.stdout."""
    span = trace_span_pb2.TraceSpan()
    span.name = "name"
    expected = json_format.MessageToJson(span)

    e = exporter.ConsoleSpanExporter(out=sys.stdout)
    assert e.export([span])
    result = capsys.readouterr().out
    assert result == expected


@mock.patch("sys.stdout.flush")
def test_export_to_console_flush(flush_mocker):
    """Test ConsoleSpanExporter to export to sys.stdout."""
    span = trace_span_pb2.TraceSpan()
    span.name = "name"

    e = exporter.ConsoleSpanExporter(out=sys.stdout)
    assert e.export([span])
    flush_mocker.assert_called_once()


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

    span = trace_span_pb2.TraceSpan()
    span.name = "name"
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

    span = trace_span_pb2.TraceSpan()
    span.name = "name"

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
