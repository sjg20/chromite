# Copyright 2014 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittests for gob_util.py"""

import base64
import http.client
import json
import tempfile
import time

from chromite.lib import config_lib
from chromite.lib import cros_test_lib
from chromite.lib import gob_util
from chromite.lib import timeout_util


gob_util.TRY_LIMIT = 1


class FakeHTTPResponse(object):
  """Enough of a HTTPResponse for FetchUrl.

  See https://docs.python.org/3/library/http.client.html#httpresponse-objects
  for more details.
  """

  def __init__(self, body=b'', headers=(), reason=None, status=200, version=11):
    if reason is None:
      reason = http.client.responses[status]

    self.body = body
    self.headers = dict(headers)
    self.msg = None
    self.reason = reason
    self.status = status
    self.version = version

  def read(self):
    return self.body

  def getheader(self, name, default=None):
    return self.headers.get(name, default)

  def getheaders(self):
    return tuple(self.headers.items())


class FakeHTTPConnection(object):
  """Enough of a HTTPConnection result for FetchUrl."""

  def __init__(self, req_url='/', req_method='GET', req_headers=None,
               req_body=None, **kwargs):
    self.kwargs = kwargs.copy()
    self.req_params = {
        'url': req_url,
        'method': req_method,
        'headers': req_headers,
        'body': req_body,
    }

  def getresponse(self):
    return FakeHTTPResponse(**self.kwargs)


class GobTest(cros_test_lib.MockTestCase):
  """Unittests that use mocks."""

  UTF8_DATA = b'That\xe2\x80\x99s an error. That\xe2\x80\x99s all we know.'

  def setUp(self):
    self.conn = self.PatchObject(gob_util, 'CreateHttpConn', autospec=False)

  def testUtf8Response(self):
    """Handle gerrit responses w/UTF8 in them."""
    self.conn.return_value = FakeHTTPConnection(body=self.UTF8_DATA)
    gob_util.FetchUrl('', '')

  def testUtf8Response502(self):
    self.conn.return_value = FakeHTTPConnection(body=self.UTF8_DATA, status=502)

    with self.assertRaises(gob_util.InternalGOBError):
      gob_util.FetchUrl('', '')

  def testConnectionTimeout(self):
    """Exercise the timeout process."""
    # To finish the test quickly, we need to shorten the timeout.
    self.PatchObject(gob_util, 'REQUEST_TIMEOUT_SECONDS', 1)

    # Setup a 'hanging' network connection.
    def simulateHang(*_args, **_kwargs):
      time.sleep(30)
      self.fail('Would hang forever.')

    self.conn.side_effect = simulateHang

    # Verify that we fail, with expected timeout error.
    with self.assertRaises(timeout_util.TimeoutError):
      gob_util.FetchUrl('', '')

  def testHtmlParser(self):
    """Verify that GOB error message is parsed properly."""
    html_data = """
<!DOCTYPE html>
 <html lang=en>
 <meta charset=utf-8>
 <meta name=viewport>
 <title>Error 403 (Forbidden)!!1</title>
 <style>"*{margin:0;padding:0}"</style>
 <div id="af-error-container">
 <a href=//www.google.com><span id=logo aria-label=Google></span></a>

 <p>Error <b>403.</b><br><ins>That's an error.<p>Too bad...</ins>
 </div>
 <div id="come other stuff">
    some other stuff
 </div>
<html>"""
    expected_parsed_data = """Error 403.
That's an error.

Too bad..."""
    ep = gob_util.ErrorParser()
    ep.feed(html_data)
    ep.close()
    self.assertEqual(expected_parsed_data, ep.ParsedDiv())

  def testCreateChange(self):
    body = json.dumps({'change_num': 123456}).encode()
    xss_protection_prefix = b")]}'\n"
    body = xss_protection_prefix + body
    self.conn.return_value = FakeHTTPConnection(body=body, status=200)
    change_json = gob_util.CreateChange(
        'some.git.url', 'project', 'branch', 'subject', True)
    self.assertEqual(change_json['change_num'], 123456)

  def testChangeEdit(self):
    self.conn.return_value = FakeHTTPConnection(body={}, status=204)
    gob_util.ChangeEdit('some.git.url', 123456, 'some/file/path',
                        'some file contents')

  def testPublishChangeEdit(self):
    self.conn.return_value = FakeHTTPConnection(body={}, status=204)
    gob_util.PublishChangeEdit('some.git.url', 123456)

  def testGetFileContents(self):
    expected_contents = 'some file contents'
    body = base64.b64encode(expected_contents.encode())
    self.conn.return_value = FakeHTTPConnection(body=body, status=200)
    contents = gob_util.GetFileContentsOnHead('some.git.url',
                                              'some/file/path')
    self.assertEqual(contents, expected_contents)


class GetCookieTests(cros_test_lib.TestCase):
  """Unittests for GetCookies()"""

  def testSimple(self):
    f = tempfile.NamedTemporaryFile(mode='w+')
    f.write('.googlesource.com\tTRUE\t/f\tTRUE\t2147483647\to\tfoo=bar')
    f.flush()
    cookies = gob_util.GetCookies('foo.googlesource.com', '/foo', [f.name])
    self.assertEqual(cookies, {'o': 'foo=bar'})
    cookies = gob_util.GetCookies('google.com', '/foo', [f.name])
    self.assertEqual(cookies, {})
    cookies = gob_util.GetCookies('foo.googlesource.com', '/', [f.name])
    self.assertEqual(cookies, {})


@cros_test_lib.pytestmark_network_test
class NetworkGobTest(cros_test_lib.TestCase):
  """Unittests that talk to real Gerrit."""

  def test200(self):
    """Test successful loading of change."""
    gob_util.FetchUrlJson(config_lib.GetSiteParams().EXTERNAL_GOB_HOST,
                          'changes/227254/detail')

  def test404(self):
    gob_util.FetchUrlJson(config_lib.GetSiteParams().EXTERNAL_GOB_HOST,
                          'foo/bar/baz')

  def test404Exception(self):
    with self.assertRaises(gob_util.GOBError) as ex:
      gob_util.FetchUrlJson(config_lib.GetSiteParams().EXTERNAL_GOB_HOST,
                            'foo/bar/baz', ignore_404=False)
    self.assertEqual(ex.exception.http_status, 404)
