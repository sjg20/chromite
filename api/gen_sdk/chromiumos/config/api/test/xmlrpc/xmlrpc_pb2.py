# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/xmlrpc/xmlrpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/test/xmlrpc/xmlrpc.proto',
  package='chromiumos.config.api.test.xmlrpc',
  syntax='proto3',
  serialized_options=_b('Z4go.chromium.org/chromiumos/config/go/api/test/xmlrpc'),
  serialized_pb=_b('\n.chromiumos/config/api/test/xmlrpc/xmlrpc.proto\x12!chromiumos.config.api.test.xmlrpc\"\xfb\x01\n\x05Value\x12\r\n\x03int\x18\x02 \x01(\x11H\x00\x12\x11\n\x07\x62oolean\x18\x03 \x01(\x08H\x00\x12\x10\n\x06string\x18\x04 \x01(\tH\x00\x12\x10\n\x06\x64ouble\x18\x05 \x01(\x01H\x00\x12\x12\n\x08\x64\x61tetime\x18\x06 \x01(\tH\x00\x12\x10\n\x06\x62\x61se64\x18\x07 \x01(\x0cH\x00\x12;\n\x06struct\x18\x08 \x01(\x0b\x32).chromiumos.config.api.test.xmlrpc.StructH\x00\x12\x39\n\x05\x61rray\x18\t \x01(\x0b\x32(.chromiumos.config.api.test.xmlrpc.ArrayH\x00\x42\x0e\n\x0cscalar_oneof\"\xab\x01\n\x06Struct\x12G\n\x07members\x18\x01 \x03(\x0b\x32\x36.chromiumos.config.api.test.xmlrpc.Struct.MembersEntry\x1aX\n\x0cMembersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.chromiumos.config.api.test.xmlrpc.Value:\x02\x38\x01\"A\n\x05\x41rray\x12\x38\n\x06values\x18\x01 \x03(\x0b\x32(.chromiumos.config.api.test.xmlrpc.ValueB6Z4go.chromium.org/chromiumos/config/go/api/test/xmlrpcb\x06proto3')
)




_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='chromiumos.config.api.test.xmlrpc.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int', full_name='chromiumos.config.api.test.xmlrpc.Value.int', index=0,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolean', full_name='chromiumos.config.api.test.xmlrpc.Value.boolean', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string', full_name='chromiumos.config.api.test.xmlrpc.Value.string', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double', full_name='chromiumos.config.api.test.xmlrpc.Value.double', index=3,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='chromiumos.config.api.test.xmlrpc.Value.datetime', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base64', full_name='chromiumos.config.api.test.xmlrpc.Value.base64', index=5,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='struct', full_name='chromiumos.config.api.test.xmlrpc.Value.struct', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='array', full_name='chromiumos.config.api.test.xmlrpc.Value.array', index=7,
      number=9, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='scalar_oneof', full_name='chromiumos.config.api.test.xmlrpc.Value.scalar_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=86,
  serialized_end=337,
)


_STRUCT_MEMBERSENTRY = _descriptor.Descriptor(
  name='MembersEntry',
  full_name='chromiumos.config.api.test.xmlrpc.Struct.MembersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='chromiumos.config.api.test.xmlrpc.Struct.MembersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.config.api.test.xmlrpc.Struct.MembersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=511,
)

_STRUCT = _descriptor.Descriptor(
  name='Struct',
  full_name='chromiumos.config.api.test.xmlrpc.Struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='members', full_name='chromiumos.config.api.test.xmlrpc.Struct.members', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STRUCT_MEMBERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=511,
)


_ARRAY = _descriptor.Descriptor(
  name='Array',
  full_name='chromiumos.config.api.test.xmlrpc.Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='chromiumos.config.api.test.xmlrpc.Array.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=513,
  serialized_end=578,
)

_VALUE.fields_by_name['struct'].message_type = _STRUCT
_VALUE.fields_by_name['array'].message_type = _ARRAY
_VALUE.oneofs_by_name['scalar_oneof'].fields.append(
  _VALUE.fields_by_name['int'])
_VALUE.fields_by_name['int'].containing_oneof = _VALUE.oneofs_by_name['scalar_oneof']
_VALUE.oneofs_by_name['scalar_oneof'].fields.append(
  _VALUE.fields_by_name['boolean'])
_VALUE.fields_by_name['boolean'].containing_oneof = _VALUE.oneofs_by_name['scalar_oneof']
_VALUE.oneofs_by_name['scalar_oneof'].fields.append(
  _VALUE.fields_by_name['string'])
_VALUE.fields_by_name['string'].containing_oneof = _VALUE.oneofs_by_name['scalar_oneof']
_VALUE.oneofs_by_name['scalar_oneof'].fields.append(
  _VALUE.fields_by_name['double'])
_VALUE.fields_by_name['double'].containing_oneof = _VALUE.oneofs_by_name['scalar_oneof']
_VALUE.oneofs_by_name['scalar_oneof'].fields.append(
  _VALUE.fields_by_name['datetime'])
_VALUE.fields_by_name['datetime'].containing_oneof = _VALUE.oneofs_by_name['scalar_oneof']
_VALUE.oneofs_by_name['scalar_oneof'].fields.append(
  _VALUE.fields_by_name['base64'])
_VALUE.fields_by_name['base64'].containing_oneof = _VALUE.oneofs_by_name['scalar_oneof']
_VALUE.oneofs_by_name['scalar_oneof'].fields.append(
  _VALUE.fields_by_name['struct'])
_VALUE.fields_by_name['struct'].containing_oneof = _VALUE.oneofs_by_name['scalar_oneof']
_VALUE.oneofs_by_name['scalar_oneof'].fields.append(
  _VALUE.fields_by_name['array'])
_VALUE.fields_by_name['array'].containing_oneof = _VALUE.oneofs_by_name['scalar_oneof']
_STRUCT_MEMBERSENTRY.fields_by_name['value'].message_type = _VALUE
_STRUCT_MEMBERSENTRY.containing_type = _STRUCT
_STRUCT.fields_by_name['members'].message_type = _STRUCT_MEMBERSENTRY
_ARRAY.fields_by_name['values'].message_type = _VALUE
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['Struct'] = _STRUCT
DESCRIPTOR.message_types_by_name['Array'] = _ARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'chromiumos.config.api.test.xmlrpc.xmlrpc_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.xmlrpc.Value)
  ))
_sym_db.RegisterMessage(Value)

Struct = _reflection.GeneratedProtocolMessageType('Struct', (_message.Message,), dict(

  MembersEntry = _reflection.GeneratedProtocolMessageType('MembersEntry', (_message.Message,), dict(
    DESCRIPTOR = _STRUCT_MEMBERSENTRY,
    __module__ = 'chromiumos.config.api.test.xmlrpc.xmlrpc_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.xmlrpc.Struct.MembersEntry)
    ))
  ,
  DESCRIPTOR = _STRUCT,
  __module__ = 'chromiumos.config.api.test.xmlrpc.xmlrpc_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.xmlrpc.Struct)
  ))
_sym_db.RegisterMessage(Struct)
_sym_db.RegisterMessage(Struct.MembersEntry)

Array = _reflection.GeneratedProtocolMessageType('Array', (_message.Message,), dict(
  DESCRIPTOR = _ARRAY,
  __module__ = 'chromiumos.config.api.test.xmlrpc.xmlrpc_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.xmlrpc.Array)
  ))
_sym_db.RegisterMessage(Array)


DESCRIPTOR._options = None
_STRUCT_MEMBERSENTRY._options = None
# @@protoc_insertion_point(module_scope)
