# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device/brand_id.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='device/brand_id.proto',
  package='device',
  syntax='proto3',
  serialized_options=b'Z0go.chromium.org/chromiumos/infra/proto/go/device',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x64\x65vice/brand_id.proto\x12\x06\x64\x65vice\"\x18\n\x07\x42randId\x12\r\n\x05value\x18\x01 \x01(\tB2Z0go.chromium.org/chromiumos/infra/proto/go/deviceb\x06proto3'
)




_BRANDID = _descriptor.Descriptor(
  name='BrandId',
  full_name='device.BrandId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='device.BrandId.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=33,
  serialized_end=57,
)

DESCRIPTOR.message_types_by_name['BrandId'] = _BRANDID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BrandId = _reflection.GeneratedProtocolMessageType('BrandId', (_message.Message,), {
  'DESCRIPTOR' : _BRANDID,
  '__module__' : 'device.brand_id_pb2'
  # @@protoc_insertion_point(class_scope:device.BrandId)
  })
_sym_db.RegisterMessage(BrandId)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
