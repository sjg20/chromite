# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/results/v1/machine_id.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/test/results/v1/machine_id.proto',
  package='chromiumos.config.api.test.results.v1',
  syntax='proto3',
  serialized_options=_b('Z@go.chromium.org/chromiumos/config/go/api/test/results/v1;results'),
  serialized_pb=_b('\n6chromiumos/config/api/test/results/v1/machine_id.proto\x12%chromiumos.config.api.test.results.v1\"\x1a\n\tMachineId\x12\r\n\x05value\x18\x01 \x01(\tBBZ@go.chromium.org/chromiumos/config/go/api/test/results/v1;resultsb\x06proto3')
)




_MACHINEID = _descriptor.Descriptor(
  name='MachineId',
  full_name='chromiumos.config.api.test.results.v1.MachineId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.config.api.test.results.v1.MachineId.value', index=0,
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
  serialized_start=97,
  serialized_end=123,
)

DESCRIPTOR.message_types_by_name['MachineId'] = _MACHINEID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MachineId = _reflection.GeneratedProtocolMessageType('MachineId', (_message.Message,), dict(
  DESCRIPTOR = _MACHINEID,
  __module__ = 'chromiumos.config.api.test.results.v1.machine_id_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.results.v1.MachineId)
  ))
_sym_db.RegisterMessage(MachineId)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
