# -*- coding: utf-8 -*-
# Copyright 2019 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Tests for the validate module."""

from __future__ import print_function

import os
import sys

from chromite.api import api_config
from chromite.api import validate
from chromite.api.gen.chromite.api import build_api_test_pb2
from chromite.api.gen.chromiumos import common_pb2
from chromite.lib import cros_build_lib
from chromite.lib import cros_test_lib
from chromite.lib import osutils


assert sys.version_info >= (3, 6), 'This module requires Python 3.6+'


class ExistsTest(cros_test_lib.TempDirTestCase, api_config.ApiConfigMixin):
  """Tests for the exists validator."""

  def test_not_exists(self):
    """Test the validator fails when given a path that doesn't exist."""
    path = os.path.join(self.tempdir, 'DOES_NOT_EXIST')

    @validate.exists('path')
    def impl(_input_proto, _output_proto, _config):
      self.fail('Incorrectly allowed method to execute.')

    with self.assertRaises(cros_build_lib.DieSystemExit):
      impl(common_pb2.Chroot(path=path), None, self.api_config)

  def test_exists(self):
    """Test the validator fails when given a path that doesn't exist."""
    path = os.path.join(self.tempdir, 'chroot')
    osutils.SafeMakedirs(path)

    @validate.exists('path')
    def impl(_input_proto, _output_proto, _config):
      pass

    impl(common_pb2.Chroot(path=path), None, self.api_config)

  def test_skip_validation(self):
    """Test skipping validation case."""
    @validate.exists('path')
    def impl(_input_proto, _output_proto, _config):
      pass

    # This would otherwise raise an error for an invalid path.
    impl(common_pb2.Chroot(), None, self.no_validate_config)


class IsInTest(cros_test_lib.TestCase, api_config.ApiConfigMixin):
  """Tests for the is_in validator."""

  def test_in(self):
    """Test a valid value."""
    @validate.is_in('path', ['/chroot/path', '/other/chroot/path'])
    def impl(_input_proto, _output_proto, _config):
      pass

    # Make sure all of the values work.
    impl(common_pb2.Chroot(path='/chroot/path'), None, self.api_config)
    impl(common_pb2.Chroot(path='/other/chroot/path'), None, self.api_config)

  def test_not_in(self):
    """Test an invalid value."""
    @validate.is_in('path', ['/chroot/path', '/other/chroot/path'])
    def impl(_input_proto, _output_proto, _config):
      pass

    # Should be failing on the invalid value.
    with self.assertRaises(cros_build_lib.DieSystemExit):
      impl(common_pb2.Chroot(path='/bad/value'), None, self.api_config)

  def test_not_set(self):
    """Test an unset value."""
    @validate.is_in('path', ['/chroot/path', '/other/chroot/path'])
    def impl(_input_proto, _output_proto, _config):
      pass

    # Should be failing without a value set.
    with self.assertRaises(cros_build_lib.DieSystemExit):
      impl(common_pb2.Chroot(), None, self.api_config)

  def test_skip_validation(self):
    """Test skipping validation case."""
    @validate.is_in('path', ['/chroot/path', '/other/chroot/path'])
    def impl(_input_proto, _output_proto, _config):
      pass

    # This would otherwise raise an error for an invalid path.
    impl(common_pb2.Chroot(), None, self.no_validate_config)


class RequiredTest(cros_test_lib.TestCase, api_config.ApiConfigMixin):
  """Tests for the required validator."""

  def test_invalid_field(self):
    """Test validator fails when given an unset value."""

    @validate.require('does.not.exist')
    def impl(_input_proto, _output_proto, _config):
      self.fail('Incorrectly allowed method to execute.')

    with self.assertRaises(cros_build_lib.DieSystemExit):
      impl(common_pb2.Chroot(), None, self.api_config)

  def test_not_set(self):
    """Test validator fails when given an unset value."""

    @validate.require('env.use_flags')
    def impl(_input_proto, _output_proto, _config):
      self.fail('Incorrectly allowed method to execute.')

    with self.assertRaises(cros_build_lib.DieSystemExit):
      impl(common_pb2.Chroot(), None, self.api_config)

  def test_set(self):
    """Test validator passes when given set values."""

    @validate.require('path', 'env.use_flags')
    def impl(_input_proto, _output_proto, _config):
      pass

    in_proto = common_pb2.Chroot(path='/chroot/path',
                                 env={'use_flags': [{'flag': 'test'}]})
    impl(in_proto, None, self.api_config)

  def test_mixed(self):
    """Test validator passes when given a set value."""

    @validate.require('path', 'env.use_flags')
    def impl(_input_proto, _output_proto, _config):
      pass

    with self.assertRaises(cros_build_lib.DieSystemExit):
      impl(common_pb2.Chroot(path='/chroot/path'), None, self.api_config)

  def test_skip_validation(self):
    """Test skipping validation case."""
    @validate.require('path', 'env.use_flags')
    def impl(_input_proto, _output_proto, _config):
      pass

    # This would otherwise raise an error for an invalid path.
    impl(common_pb2.Chroot(), None, self.no_validate_config)


class RequireEachTest(cros_test_lib.TestCase, api_config.ApiConfigMixin):
  """Tests for the require_each validator."""

  def _multi_field_message(self, msg_id=None, name=None, flag=None):
    msg = build_api_test_pb2.MultiFieldMessage()
    if msg_id is not None:
      msg.id = int(msg_id)
    if name is not None:
      msg.name = str(name)
    if flag is not None:
      msg.flag = bool(flag)
    return msg

  def _request(self, messages=None, count=0):
    """Build the request."""
    if messages is None:
      messages = [self._multi_field_message() for _ in range(count)]

    request = build_api_test_pb2.TestRequestMessage()
    for message in messages:
      msg = request.messages.add()
      msg.CopyFrom(message)

    return request

  def test_invalid_field(self):
    """Test validator fails when given an invalid field."""

    @validate.require_each('does.not', ['exist'])
    def impl(_input_proto, _output_proto, _config):
      self.fail('Incorrectly allowed method to execute.')

    with self.assertRaises(cros_build_lib.DieSystemExit):
      impl(self._request(), None, self.api_config)

  def test_invalid_call_no_subfields(self):
    """Test validator fails when given no subfields."""

    with self.assertRaises(AssertionError):
      @validate.require_each('does.not', [])
      def _(_input_proto, _output_proto, _config):
        pass

  def test_invalid_call_invalid_subfields(self):
    """Test validator fails when given subfields incorrectly."""

    with self.assertRaises(AssertionError):
      @validate.require_each('does.not', 'exist')
      def _(_input_proto, _output_proto, _config):
        pass

  def test_not_set(self):
    """Test validator fails when given an unset value."""

    @validate.require_each('messages', ['id'])
    def impl(_input_proto, _output_proto, _config):
      self.fail('Incorrectly allowed method to execute.')

    with self.assertRaises(cros_build_lib.DieSystemExit):
      impl(self._request(count=2), None, self.api_config)

  def test_no_elements_success(self):
    """Test validator fails when given no messages in the repeated field."""

    @validate.require_each('messages', ['id'])
    def impl(_input_proto, _output_proto, _config):
      pass

    impl(self._request(), None, self.api_config)

  def test_no_elements_failure(self):
    """Test validator fails when given no messages in the repeated field."""

    @validate.require_each('messages', ['id'], allow_empty=False)
    def impl(_input_proto, _output_proto, _config):
      self.fail('Incorrectly allowed method to execute.')

    with self.assertRaises(cros_build_lib.DieSystemExit):
      impl(self._request(), None, self.api_config)

  def test_set(self):
    """Test validator passes when given set values."""

    @validate.require_each('messages', ['id'])
    def impl(_input_proto, _output_proto, _config):
      pass

    messages = [self._multi_field_message(msg_id=i) for i in range(1, 5)]
    impl(self._request(messages=messages), None, self.api_config)

  def test_one_set_fails(self):
    """Test validator passes when given set values."""

    @validate.require_each('messages', ['id', 'name'])
    def impl(_input_proto, _output_proto, _config):
      pass

    messages = [self._multi_field_message(msg_id=i) for i in range(1, 5)]
    with self.assertRaises(cros_build_lib.DieSystemExit):
      impl(self._request(messages=messages), None, self.api_config)

  def test_multi_set(self):
    """Test validator passes when all values set."""

    @validate.require_each('messages', ['id', 'name'])
    def impl(_input_proto, _output_proto, _config):
      pass

    messages = [self._multi_field_message(msg_id=i, name=i)
                for i in range(1, 5)]
    impl(self._request(messages=messages), None, self.api_config)

  def test_skip_validation(self):
    """Test skipping validation case."""
    @validate.require_each('messages', ['id'], allow_empty=False)
    def impl(_input_proto, _output_proto, _config):
      pass

    impl(self._request(), None, self.no_validate_config)


class ValidateOnlyTest(cros_test_lib.TestCase, api_config.ApiConfigMixin):
  """validate_only decorator tests."""

  def test_validate_only(self):
    """Test validate only."""
    @validate.require('path')
    @validate.validation_complete
    def impl(_input_proto, _output_proto, _config):
      self.fail('Implementation was called.')
      return 1

    # Just using arbitrary messages, we just need the
    # (request, response, config) arguments so it can check the config.
    rc = impl(common_pb2.Chroot(path='/chroot/path'), common_pb2.Chroot(),
              self.validate_only_config)

    self.assertEqual(0, rc)

  def test_no_validate_only(self):
    """Test no use of validate only."""
    @validate.validation_complete
    def impl(_input_proto, _output_proto, _config):
      self.fail('Incorrectly allowed method to execute.')

    # We will get an assertion error unless validate_only prevents the function
    # from being called.
    with self.assertRaises(AssertionError):
      impl(common_pb2.Chroot(), common_pb2.Chroot(), self.api_config)
