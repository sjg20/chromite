# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_test_runner/cft_steps_config.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/skylab_test_runner/cft_steps_config.proto',
  package='test_platform.skylab_test_runner',
  syntax='proto3',
  serialized_options=b'ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runner',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7test_platform/skylab_test_runner/cft_steps_config.proto\x12 test_platform.skylab_test_runner\"i\n\x0e\x43\x66tStepsConfig\x12H\n\x0ehw_test_config\x18\x01 \x01(\x0b\x32..test_platform.skylab_test_runner.HwTestConfigH\x00\x42\r\n\x0b\x63onfig_type\"\xb2\x01\n\x0cHwTestConfig\x12\x16\n\x0eskip_provision\x18\x01 \x01(\x08\x12\x1b\n\x13skip_test_execution\x18\x02 \x01(\x08\x12\x1f\n\x17skip_all_result_publish\x18\x03 \x01(\x08\x12\x18\n\x10skip_gcs_publish\x18\x04 \x01(\x08\x12\x18\n\x10skip_rdb_publish\x18\x05 \x01(\x08\x12\x18\n\x10skip_tko_publish\x18\x06 \x01(\x08\x42LZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runnerb\x06proto3'
)




_CFTSTEPSCONFIG = _descriptor.Descriptor(
  name='CftStepsConfig',
  full_name='test_platform.skylab_test_runner.CftStepsConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hw_test_config', full_name='test_platform.skylab_test_runner.CftStepsConfig.hw_test_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='config_type', full_name='test_platform.skylab_test_runner.CftStepsConfig.config_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=93,
  serialized_end=198,
)


_HWTESTCONFIG = _descriptor.Descriptor(
  name='HwTestConfig',
  full_name='test_platform.skylab_test_runner.HwTestConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='skip_provision', full_name='test_platform.skylab_test_runner.HwTestConfig.skip_provision', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skip_test_execution', full_name='test_platform.skylab_test_runner.HwTestConfig.skip_test_execution', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skip_all_result_publish', full_name='test_platform.skylab_test_runner.HwTestConfig.skip_all_result_publish', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skip_gcs_publish', full_name='test_platform.skylab_test_runner.HwTestConfig.skip_gcs_publish', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skip_rdb_publish', full_name='test_platform.skylab_test_runner.HwTestConfig.skip_rdb_publish', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skip_tko_publish', full_name='test_platform.skylab_test_runner.HwTestConfig.skip_tko_publish', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=201,
  serialized_end=379,
)

_CFTSTEPSCONFIG.fields_by_name['hw_test_config'].message_type = _HWTESTCONFIG
_CFTSTEPSCONFIG.oneofs_by_name['config_type'].fields.append(
  _CFTSTEPSCONFIG.fields_by_name['hw_test_config'])
_CFTSTEPSCONFIG.fields_by_name['hw_test_config'].containing_oneof = _CFTSTEPSCONFIG.oneofs_by_name['config_type']
DESCRIPTOR.message_types_by_name['CftStepsConfig'] = _CFTSTEPSCONFIG
DESCRIPTOR.message_types_by_name['HwTestConfig'] = _HWTESTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CftStepsConfig = _reflection.GeneratedProtocolMessageType('CftStepsConfig', (_message.Message,), {
  'DESCRIPTOR' : _CFTSTEPSCONFIG,
  '__module__' : 'test_platform.skylab_test_runner.cft_steps_config_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.CftStepsConfig)
  })
_sym_db.RegisterMessage(CftStepsConfig)

HwTestConfig = _reflection.GeneratedProtocolMessageType('HwTestConfig', (_message.Message,), {
  'DESCRIPTOR' : _HWTESTCONFIG,
  '__module__' : 'test_platform.skylab_test_runner.cft_steps_config_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.HwTestConfig)
  })
_sym_db.RegisterMessage(HwTestConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
