# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_test_runner/steps/test_execution.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.test_platform.skylab_test_runner import config_pb2 as test__platform_dot_skylab__test__runner_dot_config__pb2
from chromite.api.gen_sdk.test_platform.skylab_test_runner import request_pb2 as test__platform_dot_skylab__test__runner_dot_request__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/skylab_test_runner/steps/test_execution.proto',
  package='test_platform.skylab_test_runner.steps',
  syntax='proto3',
  serialized_options=_b('ZPgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runner/steps'),
  serialized_pb=_b('\n;test_platform/skylab_test_runner/steps/test_execution.proto\x12&test_platform.skylab_test_runner.steps\x1a-test_platform/skylab_test_runner/config.proto\x1a.test_platform/skylab_test_runner/request.proto\"\x87\x01\n\x0fRunTestsRequest\x12:\n\x07request\x18\x01 \x01(\x0b\x32).test_platform.skylab_test_runner.Request\x12\x38\n\x06\x63onfig\x18\x02 \x01(\x0b\x32(.test_platform.skylab_test_runner.Config\"2\n\x10RunTestsResponse\x12\x1e\n\x16\x65rror_summary_markdown\x18\x01 \x01(\tBRZPgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runner/stepsb\x06proto3')
  ,
  dependencies=[test__platform_dot_skylab__test__runner_dot_config__pb2.DESCRIPTOR,test__platform_dot_skylab__test__runner_dot_request__pb2.DESCRIPTOR,])




_RUNTESTSREQUEST = _descriptor.Descriptor(
  name='RunTestsRequest',
  full_name='test_platform.skylab_test_runner.steps.RunTestsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='test_platform.skylab_test_runner.steps.RunTestsRequest.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='test_platform.skylab_test_runner.steps.RunTestsRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=334,
)


_RUNTESTSRESPONSE = _descriptor.Descriptor(
  name='RunTestsResponse',
  full_name='test_platform.skylab_test_runner.steps.RunTestsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_summary_markdown', full_name='test_platform.skylab_test_runner.steps.RunTestsResponse.error_summary_markdown', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=386,
)

_RUNTESTSREQUEST.fields_by_name['request'].message_type = test__platform_dot_skylab__test__runner_dot_request__pb2._REQUEST
_RUNTESTSREQUEST.fields_by_name['config'].message_type = test__platform_dot_skylab__test__runner_dot_config__pb2._CONFIG
DESCRIPTOR.message_types_by_name['RunTestsRequest'] = _RUNTESTSREQUEST
DESCRIPTOR.message_types_by_name['RunTestsResponse'] = _RUNTESTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunTestsRequest = _reflection.GeneratedProtocolMessageType('RunTestsRequest', (_message.Message,), dict(
  DESCRIPTOR = _RUNTESTSREQUEST,
  __module__ = 'test_platform.skylab_test_runner.steps.test_execution_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.steps.RunTestsRequest)
  ))
_sym_db.RegisterMessage(RunTestsRequest)

RunTestsResponse = _reflection.GeneratedProtocolMessageType('RunTestsResponse', (_message.Message,), dict(
  DESCRIPTOR = _RUNTESTSRESPONSE,
  __module__ = 'test_platform.skylab_test_runner.steps.test_execution_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.steps.RunTestsResponse)
  ))
_sym_db.RegisterMessage(RunTestsResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
