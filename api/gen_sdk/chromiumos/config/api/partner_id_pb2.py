# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/partner_id.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/partner_id.proto',
  package='chromiumos.config.api',
  syntax='proto3',
  serialized_options=_b('Z(go.chromium.org/chromiumos/config/go/api'),
  serialized_pb=_b('\n&chromiumos/config/api/partner_id.proto\x12\x15\x63hromiumos.config.api\"\x1a\n\tPartnerId\x12\r\n\x05value\x18\x01 \x01(\tB*Z(go.chromium.org/chromiumos/config/go/apib\x06proto3')
)




_PARTNERID = _descriptor.Descriptor(
  name='PartnerId',
  full_name='chromiumos.config.api.PartnerId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.config.api.PartnerId.value', index=0,
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
  serialized_start=65,
  serialized_end=91,
)

DESCRIPTOR.message_types_by_name['PartnerId'] = _PARTNERID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PartnerId = _reflection.GeneratedProtocolMessageType('PartnerId', (_message.Message,), dict(
  DESCRIPTOR = _PARTNERID,
  __module__ = 'chromiumos.config.api.partner_id_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.PartnerId)
  ))
_sym_db.RegisterMessage(PartnerId)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)