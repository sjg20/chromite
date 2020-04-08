# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_test_runner/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/skylab_test_runner/config.proto',
  package='test_platform.skylab_test_runner',
  syntax='proto3',
  serialized_options=_b('ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runner'),
  serialized_pb=_b('\n-test_platform/skylab_test_runner/config.proto\x12 test_platform.skylab_test_runner\"\xc3\x02\n\x06\x43onfig\x12\x39\n\x03lab\x18\x01 \x01(\x0b\x32,.test_platform.skylab_test_runner.Config.Lab\x12\x41\n\x07harness\x18\x02 \x01(\x0b\x32\x30.test_platform.skylab_test_runner.Config.Harness\x12?\n\x06output\x18\x03 \x01(\x0b\x32/.test_platform.skylab_test_runner.Config.Output\x1a\x1c\n\x03Lab\x12\x15\n\radmin_service\x18\x01 \x01(\t\x1a=\n\x07Harness\x12\x14\n\x0c\x61utotest_dir\x18\x01 \x01(\t\x12\x1c\n\x14synch_offload_subdir\x18\x02 \x01(\t\x1a\x1d\n\x06Output\x12\x13\n\x0bgs_root_dir\x18\x01 \x01(\tBLZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runnerb\x06proto3')
)




_CONFIG_LAB = _descriptor.Descriptor(
  name='Lab',
  full_name='test_platform.skylab_test_runner.Config.Lab',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='admin_service', full_name='test_platform.skylab_test_runner.Config.Lab.admin_service', index=0,
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
  serialized_start=285,
  serialized_end=313,
)

_CONFIG_HARNESS = _descriptor.Descriptor(
  name='Harness',
  full_name='test_platform.skylab_test_runner.Config.Harness',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='autotest_dir', full_name='test_platform.skylab_test_runner.Config.Harness.autotest_dir', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='synch_offload_subdir', full_name='test_platform.skylab_test_runner.Config.Harness.synch_offload_subdir', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=315,
  serialized_end=376,
)

_CONFIG_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='test_platform.skylab_test_runner.Config.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gs_root_dir', full_name='test_platform.skylab_test_runner.Config.Output.gs_root_dir', index=0,
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
  serialized_start=378,
  serialized_end=407,
)

_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='test_platform.skylab_test_runner.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lab', full_name='test_platform.skylab_test_runner.Config.lab', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='harness', full_name='test_platform.skylab_test_runner.Config.harness', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='test_platform.skylab_test_runner.Config.output', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONFIG_LAB, _CONFIG_HARNESS, _CONFIG_OUTPUT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=407,
)

_CONFIG_LAB.containing_type = _CONFIG
_CONFIG_HARNESS.containing_type = _CONFIG
_CONFIG_OUTPUT.containing_type = _CONFIG
_CONFIG.fields_by_name['lab'].message_type = _CONFIG_LAB
_CONFIG.fields_by_name['harness'].message_type = _CONFIG_HARNESS
_CONFIG.fields_by_name['output'].message_type = _CONFIG_OUTPUT
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(

  Lab = _reflection.GeneratedProtocolMessageType('Lab', (_message.Message,), dict(
    DESCRIPTOR = _CONFIG_LAB,
    __module__ = 'test_platform.skylab_test_runner.config_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Config.Lab)
    ))
  ,

  Harness = _reflection.GeneratedProtocolMessageType('Harness', (_message.Message,), dict(
    DESCRIPTOR = _CONFIG_HARNESS,
    __module__ = 'test_platform.skylab_test_runner.config_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Config.Harness)
    ))
  ,

  Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), dict(
    DESCRIPTOR = _CONFIG_OUTPUT,
    __module__ = 'test_platform.skylab_test_runner.config_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Config.Output)
    ))
  ,
  DESCRIPTOR = _CONFIG,
  __module__ = 'test_platform.skylab_test_runner.config_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Config)
  ))
_sym_db.RegisterMessage(Config)
_sym_db.RegisterMessage(Config.Lab)
_sym_db.RegisterMessage(Config.Harness)
_sym_db.RegisterMessage(Config.Output)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
