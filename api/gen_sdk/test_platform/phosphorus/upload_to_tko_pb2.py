# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/phosphorus/upload_to_tko.proto

from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.test_platform.phosphorus import common_pb2 as test__platform_dot_phosphorus_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/phosphorus/upload_to_tko.proto',
  package='test_platform.phosphorus',
  syntax='proto3',
  serialized_options=b'ZBgo.chromium.org/chromiumos/infra/proto/go/test_platform/phosphorus',
  serialized_pb=b'\n,test_platform/phosphorus/upload_to_tko.proto\x12\x18test_platform.phosphorus\x1a%test_platform/phosphorus/common.proto\"F\n\x12UploadToTkoRequest\x12\x30\n\x06\x63onfig\x18\x01 \x01(\x0b\x32 .test_platform.phosphorus.ConfigBDZBgo.chromium.org/chromiumos/infra/proto/go/test_platform/phosphorusb\x06proto3'
  ,
  dependencies=[test__platform_dot_phosphorus_dot_common__pb2.DESCRIPTOR,])




_UPLOADTOTKOREQUEST = _descriptor.Descriptor(
  name='UploadToTkoRequest',
  full_name='test_platform.phosphorus.UploadToTkoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='test_platform.phosphorus.UploadToTkoRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=113,
  serialized_end=183,
)

_UPLOADTOTKOREQUEST.fields_by_name['config'].message_type = test__platform_dot_phosphorus_dot_common__pb2._CONFIG
DESCRIPTOR.message_types_by_name['UploadToTkoRequest'] = _UPLOADTOTKOREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadToTkoRequest = _reflection.GeneratedProtocolMessageType('UploadToTkoRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADTOTKOREQUEST,
  '__module__' : 'test_platform.phosphorus.upload_to_tko_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.phosphorus.UploadToTkoRequest)
  })
_sym_db.RegisterMessage(UploadToTkoRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
