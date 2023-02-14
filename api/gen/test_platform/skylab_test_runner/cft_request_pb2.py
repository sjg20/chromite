# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_test_runner/cft_request.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.third_party.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from chromite.api.gen.test_platform import request_pb2 as test__platform_dot_request__pb2
from chromite.api.gen.chromiumos.test.api import provision_state_pb2 as chromiumos_dot_test_dot_api_dot_provision__state__pb2
from chromite.api.gen.chromiumos.test.api import test_suite_pb2 as chromiumos_dot_test_dot_api_dot_test__suite__pb2
from chromite.api.gen.chromiumos.test.lab.api import dut_pb2 as chromiumos_dot_test_dot_lab_dot_api_dot_dut__pb2
from chromite.api.gen.chromiumos.build.api import container_metadata_pb2 as chromiumos_dot_build_dot_api_dot_container__metadata__pb2
from chromite.api.gen.test_platform.common import cft_steps_config_pb2 as test__platform_dot_common_dot_cft__steps__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/skylab_test_runner/cft_request.proto',
  package='test_platform.skylab_test_runner',
  syntax='proto3',
  serialized_options=b'ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runner',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2test_platform/skylab_test_runner/cft_request.proto\x12 test_platform.skylab_test_runner\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1btest_platform/request.proto\x1a)chromiumos/test/api/provision_state.proto\x1a$chromiumos/test/api/test_suite.proto\x1a!chromiumos/test/lab/api/dut.proto\x1a-chromiumos/build/api/container_metadata.proto\x1a+test_platform/common/cft_steps_config.proto\"\x8a\x07\n\x0e\x43\x46TTestRequest\x12L\n\x0bprimary_dut\x18\x01 \x01(\x0b\x32\x37.test_platform.skylab_test_runner.CFTTestRequest.Device\x12O\n\x0e\x63ompanion_duts\x18\x02 \x03(\x0b\x32\x37.test_platform.skylab_test_runner.CFTTestRequest.Device\x12\x33\n\x0btest_suites\x18\x03 \x03(\x0b\x32\x1e.chromiumos.test.api.TestSuite\x12,\n\x08\x64\x65\x61\x64line\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x12parent_request_uid\x18\x05 \x01(\t\x12\x17\n\x0fparent_build_id\x18\x06 \x01(\x03\x12_\n\x10\x61utotest_keyvals\x18\x07 \x03(\x0b\x32\x45.test_platform.skylab_test_runner.CFTTestRequest.AutotestKeyvalsEntry\x12\\\n\x1f\x64\x65\x66\x61ult_test_execution_behavior\x18\x08 \x01(\x0e\x32\x33.test_platform.Request.Params.TestExecutionBehavior\x12\x43\n\x12\x63ontainer_metadata\x18\t \x01(\x0b\x32\'.chromiumos.build.api.ContainerMetadata\x12\x14\n\x0cretry_number\x18\n \x01(\x05\x12:\n\x0csteps_config\x18\x0b \x01(\x0b\x32$.test_platform.common.CftStepsConfig\x12\x14\n\x0crun_via_trv2\x18\x0c \x01(\x08\x1a\x36\n\x14\x41utotestKeyvalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x9c\x01\n\x06\x44\x65vice\x12\x34\n\tdut_model\x18\x01 \x01(\x0b\x32!.chromiumos.test.lab.api.DutModel\x12<\n\x0fprovision_state\x18\x02 \x01(\x0b\x32#.chromiumos.test.api.ProvisionState\x12\x1e\n\x16\x63ontainer_metadata_key\x18\x03 \x01(\tBLZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runnerb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,test__platform_dot_request__pb2.DESCRIPTOR,chromiumos_dot_test_dot_api_dot_provision__state__pb2.DESCRIPTOR,chromiumos_dot_test_dot_api_dot_test__suite__pb2.DESCRIPTOR,chromiumos_dot_test_dot_lab_dot_api_dot_dut__pb2.DESCRIPTOR,chromiumos_dot_build_dot_api_dot_container__metadata__pb2.DESCRIPTOR,test__platform_dot_common_dot_cft__steps__config__pb2.DESCRIPTOR,])




_CFTTESTREQUEST_AUTOTESTKEYVALSENTRY = _descriptor.Descriptor(
  name='AutotestKeyvalsEntry',
  full_name='test_platform.skylab_test_runner.CFTTestRequest.AutotestKeyvalsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.skylab_test_runner.CFTTestRequest.AutotestKeyvalsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.skylab_test_runner.CFTTestRequest.AutotestKeyvalsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1052,
  serialized_end=1106,
)

_CFTTESTREQUEST_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='test_platform.skylab_test_runner.CFTTestRequest.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dut_model', full_name='test_platform.skylab_test_runner.CFTTestRequest.Device.dut_model', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provision_state', full_name='test_platform.skylab_test_runner.CFTTestRequest.Device.provision_state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='container_metadata_key', full_name='test_platform.skylab_test_runner.CFTTestRequest.Device.container_metadata_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1109,
  serialized_end=1265,
)

_CFTTESTREQUEST = _descriptor.Descriptor(
  name='CFTTestRequest',
  full_name='test_platform.skylab_test_runner.CFTTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='primary_dut', full_name='test_platform.skylab_test_runner.CFTTestRequest.primary_dut', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='companion_duts', full_name='test_platform.skylab_test_runner.CFTTestRequest.companion_duts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_suites', full_name='test_platform.skylab_test_runner.CFTTestRequest.test_suites', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deadline', full_name='test_platform.skylab_test_runner.CFTTestRequest.deadline', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_request_uid', full_name='test_platform.skylab_test_runner.CFTTestRequest.parent_request_uid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_build_id', full_name='test_platform.skylab_test_runner.CFTTestRequest.parent_build_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autotest_keyvals', full_name='test_platform.skylab_test_runner.CFTTestRequest.autotest_keyvals', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_test_execution_behavior', full_name='test_platform.skylab_test_runner.CFTTestRequest.default_test_execution_behavior', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='container_metadata', full_name='test_platform.skylab_test_runner.CFTTestRequest.container_metadata', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='retry_number', full_name='test_platform.skylab_test_runner.CFTTestRequest.retry_number', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='steps_config', full_name='test_platform.skylab_test_runner.CFTTestRequest.steps_config', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='run_via_trv2', full_name='test_platform.skylab_test_runner.CFTTestRequest.run_via_trv2', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CFTTESTREQUEST_AUTOTESTKEYVALSENTRY, _CFTTESTREQUEST_DEVICE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=359,
  serialized_end=1265,
)

_CFTTESTREQUEST_AUTOTESTKEYVALSENTRY.containing_type = _CFTTESTREQUEST
_CFTTESTREQUEST_DEVICE.fields_by_name['dut_model'].message_type = chromiumos_dot_test_dot_lab_dot_api_dot_dut__pb2._DUTMODEL
_CFTTESTREQUEST_DEVICE.fields_by_name['provision_state'].message_type = chromiumos_dot_test_dot_api_dot_provision__state__pb2._PROVISIONSTATE
_CFTTESTREQUEST_DEVICE.containing_type = _CFTTESTREQUEST
_CFTTESTREQUEST.fields_by_name['primary_dut'].message_type = _CFTTESTREQUEST_DEVICE
_CFTTESTREQUEST.fields_by_name['companion_duts'].message_type = _CFTTESTREQUEST_DEVICE
_CFTTESTREQUEST.fields_by_name['test_suites'].message_type = chromiumos_dot_test_dot_api_dot_test__suite__pb2._TESTSUITE
_CFTTESTREQUEST.fields_by_name['deadline'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CFTTESTREQUEST.fields_by_name['autotest_keyvals'].message_type = _CFTTESTREQUEST_AUTOTESTKEYVALSENTRY
_CFTTESTREQUEST.fields_by_name['default_test_execution_behavior'].enum_type = test__platform_dot_request__pb2._REQUEST_PARAMS_TESTEXECUTIONBEHAVIOR
_CFTTESTREQUEST.fields_by_name['container_metadata'].message_type = chromiumos_dot_build_dot_api_dot_container__metadata__pb2._CONTAINERMETADATA
_CFTTESTREQUEST.fields_by_name['steps_config'].message_type = test__platform_dot_common_dot_cft__steps__config__pb2._CFTSTEPSCONFIG
DESCRIPTOR.message_types_by_name['CFTTestRequest'] = _CFTTESTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CFTTestRequest = _reflection.GeneratedProtocolMessageType('CFTTestRequest', (_message.Message,), {

  'AutotestKeyvalsEntry' : _reflection.GeneratedProtocolMessageType('AutotestKeyvalsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CFTTESTREQUEST_AUTOTESTKEYVALSENTRY,
    '__module__' : 'test_platform.skylab_test_runner.cft_request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.CFTTestRequest.AutotestKeyvalsEntry)
    })
  ,

  'Device' : _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
    'DESCRIPTOR' : _CFTTESTREQUEST_DEVICE,
    '__module__' : 'test_platform.skylab_test_runner.cft_request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.CFTTestRequest.Device)
    })
  ,
  'DESCRIPTOR' : _CFTTESTREQUEST,
  '__module__' : 'test_platform.skylab_test_runner.cft_request_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.CFTTestRequest)
  })
_sym_db.RegisterMessage(CFTTestRequest)
_sym_db.RegisterMessage(CFTTestRequest.AutotestKeyvalsEntry)
_sym_db.RegisterMessage(CFTTestRequest.Device)


DESCRIPTOR._options = None
_CFTTESTREQUEST_AUTOTESTKEYVALSENTRY._options = None
# @@protoc_insertion_point(module_scope)
