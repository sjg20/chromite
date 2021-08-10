# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/steps/execute/build.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/steps/execute/build.proto',
  package='test_platform.steps.execute',
  syntax='proto3',
  serialized_options=b'ZEgo.chromium.org/chromiumos/infra/proto/go/test_platform/steps/execute',
  serialized_pb=b'\n\'test_platform/steps/execute/build.proto\x12\x1btest_platform.steps.execute\x1a\x1fgoogle/protobuf/timestamp.proto\"D\n\x05\x42uild\x12/\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\n\n\x02id\x18\x02 \x01(\x03\x42GZEgo.chromium.org/chromiumos/infra/proto/go/test_platform/steps/executeb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BUILD = _descriptor.Descriptor(
  name='Build',
  full_name='test_platform.steps.execute.Build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create_time', full_name='test_platform.steps.execute.Build.create_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='test_platform.steps.execute.Build.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=105,
  serialized_end=173,
)

_BUILD.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Build'] = _BUILD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Build = _reflection.GeneratedProtocolMessageType('Build', (_message.Message,), {
  'DESCRIPTOR' : _BUILD,
  '__module__' : 'test_platform.steps.execute.build_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.steps.execute.Build)
  })
_sym_db.RegisterMessage(Build)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
