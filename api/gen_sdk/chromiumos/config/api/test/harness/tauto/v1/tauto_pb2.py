# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/harness/tauto/v1/tauto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/test/harness/tauto/v1/tauto.proto',
  package='chromiumos.config.api.test.harness.tauto.v1',
  syntax='proto3',
  serialized_options=_b('ZDgo.chromium.org/chromiumos/config/go/api/test/harness/tauto/v1;tauto'),
  serialized_pb=_b('\n7chromiumos/config/api/test/harness/tauto/v1/tauto.proto\x12+chromiumos.config.api.test.harness.tauto.v1\"\x8f\x01\n\x0cTestMetadata\x12L\n\x04main\x18\x01 \x01(\x0b\x32>.chromiumos.config.api.test.harness.tauto.v1.TestMetadata.Main\x1a\x31\n\x04Main\x12\x16\n\x0epython_package\x18\x01 \x01(\t\x12\x11\n\ttest_args\x18\x02 \x03(\tBFZDgo.chromium.org/chromiumos/config/go/api/test/harness/tauto/v1;tautob\x06proto3')
)




_TESTMETADATA_MAIN = _descriptor.Descriptor(
  name='Main',
  full_name='chromiumos.config.api.test.harness.tauto.v1.TestMetadata.Main',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='python_package', full_name='chromiumos.config.api.test.harness.tauto.v1.TestMetadata.Main.python_package', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_args', full_name='chromiumos.config.api.test.harness.tauto.v1.TestMetadata.Main.test_args', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=248,
)

_TESTMETADATA = _descriptor.Descriptor(
  name='TestMetadata',
  full_name='chromiumos.config.api.test.harness.tauto.v1.TestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='main', full_name='chromiumos.config.api.test.harness.tauto.v1.TestMetadata.main', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TESTMETADATA_MAIN, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=248,
)

_TESTMETADATA_MAIN.containing_type = _TESTMETADATA
_TESTMETADATA.fields_by_name['main'].message_type = _TESTMETADATA_MAIN
DESCRIPTOR.message_types_by_name['TestMetadata'] = _TESTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestMetadata = _reflection.GeneratedProtocolMessageType('TestMetadata', (_message.Message,), dict(

  Main = _reflection.GeneratedProtocolMessageType('Main', (_message.Message,), dict(
    DESCRIPTOR = _TESTMETADATA_MAIN,
    __module__ = 'chromiumos.config.api.test.harness.tauto.v1.tauto_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.harness.tauto.v1.TestMetadata.Main)
    ))
  ,
  DESCRIPTOR = _TESTMETADATA,
  __module__ = 'chromiumos.config.api.test.harness.tauto.v1.tauto_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.harness.tauto.v1.TestMetadata)
  ))
_sym_db.RegisterMessage(TestMetadata)
_sym_db.RegisterMessage(TestMetadata.Main)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
