# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_test_runner/request.proto

from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.third_party.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from chromite.api.gen_sdk.test_platform.execution import param_pb2 as test__platform_dot_execution_dot_param__pb2
from chromite.api.gen_sdk.test_platform import request_pb2 as test__platform_dot_request__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/skylab_test_runner/request.proto',
  package='test_platform.skylab_test_runner',
  syntax='proto3',
  serialized_options=b'ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runner',
  serialized_pb=b'\n.test_platform/skylab_test_runner/request.proto\x12 test_platform.skylab_test_runner\x1a\x1fgoogle/protobuf/timestamp.proto\x1a#test_platform/execution/param.proto\x1a\x1btest_platform/request.proto\"\xa3\t\n\x07Request\x12@\n\x06prejob\x18\x01 \x01(\x0b\x32\x30.test_platform.skylab_test_runner.Request.Prejob\x12<\n\x04test\x18\x02 \x01(\x0b\x32..test_platform.skylab_test_runner.Request.Test\x12,\n\x08\x64\x65\x61\x64line\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x12parent_request_uid\x18\x04 \x01(\t\x12\x17\n\x0fparent_build_id\x18\x05 \x01(\x03\x12\x43\n\x05tests\x18\x06 \x03(\x0b\x32\x34.test_platform.skylab_test_runner.Request.TestsEntry\x12\x37\n\x0f\x65xecution_param\x18\x07 \x01(\x0b\x32\x1e.test_platform.execution.Param\x1a\x93\x02\n\x06Prejob\x12O\n\x15software_dependencies\x18\x01 \x03(\x0b\x32\x30.test_platform.Request.Params.SoftwareDependency\x12k\n\x14provisionable_labels\x18\x02 \x03(\x0b\x32I.test_platform.skylab_test_runner.Request.Prejob.ProvisionableLabelsEntryB\x02\x18\x01\x12\x0f\n\x07use_tls\x18\x03 \x01(\x08\x1a:\n\x18ProvisionableLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xc2\x03\n\x04Test\x12K\n\x08\x61utotest\x18\x01 \x01(\x0b\x32\x37.test_platform.skylab_test_runner.Request.Test.AutotestH\x00\x12N\n\x07offload\x18\x02 \x01(\x0b\x32=.test_platform.skylab_test_runner.Request.Test.OffloadOptions\x1a\xe0\x01\n\x08\x41utotest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\ttest_args\x18\x02 \x01(\t\x12U\n\x07keyvals\x18\x03 \x03(\x0b\x32\x44.test_platform.skylab_test_runner.Request.Test.Autotest.KeyvalsEntry\x12\x16\n\x0eis_client_test\x18\x04 \x01(\x08\x12\x14\n\x0c\x64isplay_name\x18\x05 \x01(\t\x1a.\n\x0cKeyvalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\x0eOffloadOptions\x12\x1d\n\x15synchronous_gs_enable\x18\x01 \x01(\x08\x42\t\n\x07harness\x1a\\\n\nTestsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b\x32..test_platform.skylab_test_runner.Request.Test:\x02\x38\x01\x42LZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runnerb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,test__platform_dot_execution_dot_param__pb2.DESCRIPTOR,test__platform_dot_request__pb2.DESCRIPTOR,])




_REQUEST_PREJOB_PROVISIONABLELABELSENTRY = _descriptor.Descriptor(
  name='ProvisionableLabelsEntry',
  full_name='test_platform.skylab_test_runner.Request.Prejob.ProvisionableLabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.skylab_test_runner.Request.Prejob.ProvisionableLabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.skylab_test_runner.Request.Prejob.ProvisionableLabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=766,
  serialized_end=824,
)

_REQUEST_PREJOB = _descriptor.Descriptor(
  name='Prejob',
  full_name='test_platform.skylab_test_runner.Request.Prejob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='software_dependencies', full_name='test_platform.skylab_test_runner.Request.Prejob.software_dependencies', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provisionable_labels', full_name='test_platform.skylab_test_runner.Request.Prejob.provisionable_labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_tls', full_name='test_platform.skylab_test_runner.Request.Prejob.use_tls', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_PREJOB_PROVISIONABLELABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=549,
  serialized_end=824,
)

_REQUEST_TEST_AUTOTEST_KEYVALSENTRY = _descriptor.Descriptor(
  name='KeyvalsEntry',
  full_name='test_platform.skylab_test_runner.Request.Test.Autotest.KeyvalsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.skylab_test_runner.Request.Test.Autotest.KeyvalsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.skylab_test_runner.Request.Test.Autotest.KeyvalsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1171,
  serialized_end=1217,
)

_REQUEST_TEST_AUTOTEST = _descriptor.Descriptor(
  name='Autotest',
  full_name='test_platform.skylab_test_runner.Request.Test.Autotest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test_platform.skylab_test_runner.Request.Test.Autotest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_args', full_name='test_platform.skylab_test_runner.Request.Test.Autotest.test_args', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyvals', full_name='test_platform.skylab_test_runner.Request.Test.Autotest.keyvals', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_client_test', full_name='test_platform.skylab_test_runner.Request.Test.Autotest.is_client_test', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='test_platform.skylab_test_runner.Request.Test.Autotest.display_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_TEST_AUTOTEST_KEYVALSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=993,
  serialized_end=1217,
)

_REQUEST_TEST_OFFLOADOPTIONS = _descriptor.Descriptor(
  name='OffloadOptions',
  full_name='test_platform.skylab_test_runner.Request.Test.OffloadOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='synchronous_gs_enable', full_name='test_platform.skylab_test_runner.Request.Test.OffloadOptions.synchronous_gs_enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1219,
  serialized_end=1266,
)

_REQUEST_TEST = _descriptor.Descriptor(
  name='Test',
  full_name='test_platform.skylab_test_runner.Request.Test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='autotest', full_name='test_platform.skylab_test_runner.Request.Test.autotest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offload', full_name='test_platform.skylab_test_runner.Request.Test.offload', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_TEST_AUTOTEST, _REQUEST_TEST_OFFLOADOPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='harness', full_name='test_platform.skylab_test_runner.Request.Test.harness',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=827,
  serialized_end=1277,
)

_REQUEST_TESTSENTRY = _descriptor.Descriptor(
  name='TestsEntry',
  full_name='test_platform.skylab_test_runner.Request.TestsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.skylab_test_runner.Request.TestsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.skylab_test_runner.Request.TestsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1279,
  serialized_end=1371,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='test_platform.skylab_test_runner.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prejob', full_name='test_platform.skylab_test_runner.Request.prejob', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test', full_name='test_platform.skylab_test_runner.Request.test', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deadline', full_name='test_platform.skylab_test_runner.Request.deadline', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_request_uid', full_name='test_platform.skylab_test_runner.Request.parent_request_uid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_build_id', full_name='test_platform.skylab_test_runner.Request.parent_build_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tests', full_name='test_platform.skylab_test_runner.Request.tests', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execution_param', full_name='test_platform.skylab_test_runner.Request.execution_param', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_PREJOB, _REQUEST_TEST, _REQUEST_TESTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=1371,
)

_REQUEST_PREJOB_PROVISIONABLELABELSENTRY.containing_type = _REQUEST_PREJOB
_REQUEST_PREJOB.fields_by_name['software_dependencies'].message_type = test__platform_dot_request__pb2._REQUEST_PARAMS_SOFTWAREDEPENDENCY
_REQUEST_PREJOB.fields_by_name['provisionable_labels'].message_type = _REQUEST_PREJOB_PROVISIONABLELABELSENTRY
_REQUEST_PREJOB.containing_type = _REQUEST
_REQUEST_TEST_AUTOTEST_KEYVALSENTRY.containing_type = _REQUEST_TEST_AUTOTEST
_REQUEST_TEST_AUTOTEST.fields_by_name['keyvals'].message_type = _REQUEST_TEST_AUTOTEST_KEYVALSENTRY
_REQUEST_TEST_AUTOTEST.containing_type = _REQUEST_TEST
_REQUEST_TEST_OFFLOADOPTIONS.containing_type = _REQUEST_TEST
_REQUEST_TEST.fields_by_name['autotest'].message_type = _REQUEST_TEST_AUTOTEST
_REQUEST_TEST.fields_by_name['offload'].message_type = _REQUEST_TEST_OFFLOADOPTIONS
_REQUEST_TEST.containing_type = _REQUEST
_REQUEST_TEST.oneofs_by_name['harness'].fields.append(
  _REQUEST_TEST.fields_by_name['autotest'])
_REQUEST_TEST.fields_by_name['autotest'].containing_oneof = _REQUEST_TEST.oneofs_by_name['harness']
_REQUEST_TESTSENTRY.fields_by_name['value'].message_type = _REQUEST_TEST
_REQUEST_TESTSENTRY.containing_type = _REQUEST
_REQUEST.fields_by_name['prejob'].message_type = _REQUEST_PREJOB
_REQUEST.fields_by_name['test'].message_type = _REQUEST_TEST
_REQUEST.fields_by_name['deadline'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REQUEST.fields_by_name['tests'].message_type = _REQUEST_TESTSENTRY
_REQUEST.fields_by_name['execution_param'].message_type = test__platform_dot_execution_dot_param__pb2._PARAM
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {

  'Prejob' : _reflection.GeneratedProtocolMessageType('Prejob', (_message.Message,), {

    'ProvisionableLabelsEntry' : _reflection.GeneratedProtocolMessageType('ProvisionableLabelsEntry', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PREJOB_PROVISIONABLELABELSENTRY,
      '__module__' : 'test_platform.skylab_test_runner.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Request.Prejob.ProvisionableLabelsEntry)
      })
    ,
    'DESCRIPTOR' : _REQUEST_PREJOB,
    '__module__' : 'test_platform.skylab_test_runner.request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Request.Prejob)
    })
  ,

  'Test' : _reflection.GeneratedProtocolMessageType('Test', (_message.Message,), {

    'Autotest' : _reflection.GeneratedProtocolMessageType('Autotest', (_message.Message,), {

      'KeyvalsEntry' : _reflection.GeneratedProtocolMessageType('KeyvalsEntry', (_message.Message,), {
        'DESCRIPTOR' : _REQUEST_TEST_AUTOTEST_KEYVALSENTRY,
        '__module__' : 'test_platform.skylab_test_runner.request_pb2'
        # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Request.Test.Autotest.KeyvalsEntry)
        })
      ,
      'DESCRIPTOR' : _REQUEST_TEST_AUTOTEST,
      '__module__' : 'test_platform.skylab_test_runner.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Request.Test.Autotest)
      })
    ,

    'OffloadOptions' : _reflection.GeneratedProtocolMessageType('OffloadOptions', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_TEST_OFFLOADOPTIONS,
      '__module__' : 'test_platform.skylab_test_runner.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Request.Test.OffloadOptions)
      })
    ,
    'DESCRIPTOR' : _REQUEST_TEST,
    '__module__' : 'test_platform.skylab_test_runner.request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Request.Test)
    })
  ,

  'TestsEntry' : _reflection.GeneratedProtocolMessageType('TestsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_TESTSENTRY,
    '__module__' : 'test_platform.skylab_test_runner.request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Request.TestsEntry)
    })
  ,
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'test_platform.skylab_test_runner.request_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Request)
  })
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.Prejob)
_sym_db.RegisterMessage(Request.Prejob.ProvisionableLabelsEntry)
_sym_db.RegisterMessage(Request.Test)
_sym_db.RegisterMessage(Request.Test.Autotest)
_sym_db.RegisterMessage(Request.Test.Autotest.KeyvalsEntry)
_sym_db.RegisterMessage(Request.Test.OffloadOptions)
_sym_db.RegisterMessage(Request.TestsEntry)


DESCRIPTOR._options = None
_REQUEST_PREJOB_PROVISIONABLELABELSENTRY._options = None
_REQUEST_PREJOB.fields_by_name['provisionable_labels']._options = None
_REQUEST_TEST_AUTOTEST_KEYVALSENTRY._options = None
_REQUEST_TESTSENTRY._options = None
# @@protoc_insertion_point(module_scope)
