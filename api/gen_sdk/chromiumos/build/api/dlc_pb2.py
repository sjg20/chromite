# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/build/api/dlc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/build/api/dlc.proto',
  package='chromiumos.build.api',
  syntax='proto3',
  serialized_options=b'Z.go.chromium.org/chromiumos/config/go/build/api',
  serialized_pb=b'\n\x1e\x63hromiumos/build/api/dlc.proto\x12\x14\x63hromiumos.build.api\"D\n\x03\x44lc\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.chromiumos.build.api.Dlc.Id\x1a\x13\n\x02Id\x12\r\n\x05value\x18\x01 \x01(\tB0Z.go.chromium.org/chromiumos/config/go/build/apib\x06proto3'
)




_DLC_ID = _descriptor.Descriptor(
  name='Id',
  full_name='chromiumos.build.api.Dlc.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.build.api.Dlc.Id.value', index=0,
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
  serialized_start=105,
  serialized_end=124,
)

_DLC = _descriptor.Descriptor(
  name='Dlc',
  full_name='chromiumos.build.api.Dlc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chromiumos.build.api.Dlc.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DLC_ID, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=124,
)

_DLC_ID.containing_type = _DLC
_DLC.fields_by_name['id'].message_type = _DLC_ID
DESCRIPTOR.message_types_by_name['Dlc'] = _DLC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dlc = _reflection.GeneratedProtocolMessageType('Dlc', (_message.Message,), {

  'Id' : _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
    'DESCRIPTOR' : _DLC_ID,
    '__module__' : 'chromiumos.build.api.dlc_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.build.api.Dlc.Id)
    })
  ,
  'DESCRIPTOR' : _DLC,
  '__module__' : 'chromiumos.build.api.dlc_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.build.api.Dlc)
  })
_sym_db.RegisterMessage(Dlc)
_sym_db.RegisterMessage(Dlc.Id)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
