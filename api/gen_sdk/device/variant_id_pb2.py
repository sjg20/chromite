# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device/variant_id.proto

from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='device/variant_id.proto',
  package='device',
  syntax='proto3',
  serialized_options=b'Z0go.chromium.org/chromiumos/infra/proto/go/device',
  serialized_pb=b'\n\x17\x64\x65vice/variant_id.proto\x12\x06\x64\x65vice\"\x1a\n\tVariantId\x12\r\n\x05value\x18\x01 \x01(\tB2Z0go.chromium.org/chromiumos/infra/proto/go/deviceb\x06proto3'
)




_VARIANTID = _descriptor.Descriptor(
  name='VariantId',
  full_name='device.VariantId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='device.VariantId.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=61,
)

DESCRIPTOR.message_types_by_name['VariantId'] = _VARIANTID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VariantId = _reflection.GeneratedProtocolMessageType('VariantId', (_message.Message,), {
  'DESCRIPTOR' : _VARIANTID,
  '__module__' : 'device.variant_id_pb2'
  # @@protoc_insertion_point(class_scope:device.VariantId)
  })
_sym_db.RegisterMessage(VariantId)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
