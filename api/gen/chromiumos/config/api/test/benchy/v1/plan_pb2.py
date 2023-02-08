# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/benchy/v1/plan.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/test/benchy/v1/plan.proto',
  package='chromium.config.api.test.benchy.v1',
  syntax='proto3',
  serialized_options=b'Z>go.chromium.org/chromiumos/config/go/api/test/benchy/v1;benchy',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/chromiumos/config/api/test/benchy/v1/plan.proto\x12\"chromium.config.api.test.benchy.v1\"<\n\x07Payload\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x03 \x01(\t\"8\n\x06\x44\x65vice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\thost_name\x18\x02 \x01(\t\x12\r\n\x05\x62oard\x18\x03 \x01(\t\"&\n\x05\x42uild\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\x85\x02\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\x12\x14\n\x0c\x63ommand_line\x18\x03 \x01(\t\x12S\n\x0e\x65xecution_mode\x18\x04 \x01(\x0e\x32;.chromium.config.api.test.benchy.v1.Parameter.ExecutionMode\"o\n\rExecutionMode\x12\x19\n\x15\x45XECUTION_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x45XECUTION_LOCAL\x10\x01\x12\x11\n\rEXECUTION_DUT\x10\x02\x12\x1b\n\x17\x45XECUTION_TAST_VARIABLE\x10\x03\"]\n\x08Workload\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63ommand_line\x18\x02 \x01(\t\x12\x17\n\x0flocal_execution\x18\x03 \x01(\x08\x12\x14\n\x0crepeat_count\x18\x04 \x01(\r\"\xcf\x02\n\x04Plan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12=\n\x08payloads\x18\x02 \x03(\x0b\x32+.chromium.config.api.test.benchy.v1.Payload\x12;\n\x07\x64\x65vices\x18\x03 \x03(\x0b\x32*.chromium.config.api.test.benchy.v1.Device\x12\x39\n\x06\x62uilds\x18\x04 \x03(\x0b\x32).chromium.config.api.test.benchy.v1.Build\x12?\n\tworkloads\x18\x05 \x03(\x0b\x32,.chromium.config.api.test.benchy.v1.Workload\x12\x41\n\nparameters\x18\x06 \x03(\x0b\x32-.chromium.config.api.test.benchy.v1.ParameterB@Z>go.chromium.org/chromiumos/config/go/api/test/benchy/v1;benchyb\x06proto3'
)



_PARAMETER_EXECUTIONMODE = _descriptor.EnumDescriptor(
  name='ExecutionMode',
  full_name='chromium.config.api.test.benchy.v1.Parameter.ExecutionMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXECUTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXECUTION_LOCAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXECUTION_DUT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXECUTION_TAST_VARIABLE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=398,
  serialized_end=509,
)
_sym_db.RegisterEnumDescriptor(_PARAMETER_EXECUTIONMODE)


_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='chromium.config.api.test.benchy.v1.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromium.config.api.test.benchy.v1.Payload.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='chromium.config.api.test.benchy.v1.Payload.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination', full_name='chromium.config.api.test.benchy.v1.Payload.destination', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=87,
  serialized_end=147,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='chromium.config.api.test.benchy.v1.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromium.config.api.test.benchy.v1.Device.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host_name', full_name='chromium.config.api.test.benchy.v1.Device.host_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='board', full_name='chromium.config.api.test.benchy.v1.Device.board', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=149,
  serialized_end=205,
)


_BUILD = _descriptor.Descriptor(
  name='Build',
  full_name='chromium.config.api.test.benchy.v1.Build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromium.config.api.test.benchy.v1.Build.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='chromium.config.api.test.benchy.v1.Build.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=207,
  serialized_end=245,
)


_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='chromium.config.api.test.benchy.v1.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromium.config.api.test.benchy.v1.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='chromium.config.api.test.benchy.v1.Parameter.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command_line', full_name='chromium.config.api.test.benchy.v1.Parameter.command_line', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='execution_mode', full_name='chromium.config.api.test.benchy.v1.Parameter.execution_mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PARAMETER_EXECUTIONMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=509,
)


_WORKLOAD = _descriptor.Descriptor(
  name='Workload',
  full_name='chromium.config.api.test.benchy.v1.Workload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromium.config.api.test.benchy.v1.Workload.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command_line', full_name='chromium.config.api.test.benchy.v1.Workload.command_line', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='local_execution', full_name='chromium.config.api.test.benchy.v1.Workload.local_execution', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repeat_count', full_name='chromium.config.api.test.benchy.v1.Workload.repeat_count', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=511,
  serialized_end=604,
)


_PLAN = _descriptor.Descriptor(
  name='Plan',
  full_name='chromium.config.api.test.benchy.v1.Plan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromium.config.api.test.benchy.v1.Plan.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payloads', full_name='chromium.config.api.test.benchy.v1.Plan.payloads', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='devices', full_name='chromium.config.api.test.benchy.v1.Plan.devices', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='builds', full_name='chromium.config.api.test.benchy.v1.Plan.builds', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workloads', full_name='chromium.config.api.test.benchy.v1.Plan.workloads', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='chromium.config.api.test.benchy.v1.Plan.parameters', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=607,
  serialized_end=942,
)

_PARAMETER.fields_by_name['execution_mode'].enum_type = _PARAMETER_EXECUTIONMODE
_PARAMETER_EXECUTIONMODE.containing_type = _PARAMETER
_PLAN.fields_by_name['payloads'].message_type = _PAYLOAD
_PLAN.fields_by_name['devices'].message_type = _DEVICE
_PLAN.fields_by_name['builds'].message_type = _BUILD
_PLAN.fields_by_name['workloads'].message_type = _WORKLOAD
_PLAN.fields_by_name['parameters'].message_type = _PARAMETER
DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['Build'] = _BUILD
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['Workload'] = _WORKLOAD
DESCRIPTOR.message_types_by_name['Plan'] = _PLAN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOAD,
  '__module__' : 'chromiumos.config.api.test.benchy.v1.plan_pb2'
  # @@protoc_insertion_point(class_scope:chromium.config.api.test.benchy.v1.Payload)
  })
_sym_db.RegisterMessage(Payload)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'chromiumos.config.api.test.benchy.v1.plan_pb2'
  # @@protoc_insertion_point(class_scope:chromium.config.api.test.benchy.v1.Device)
  })
_sym_db.RegisterMessage(Device)

Build = _reflection.GeneratedProtocolMessageType('Build', (_message.Message,), {
  'DESCRIPTOR' : _BUILD,
  '__module__' : 'chromiumos.config.api.test.benchy.v1.plan_pb2'
  # @@protoc_insertion_point(class_scope:chromium.config.api.test.benchy.v1.Build)
  })
_sym_db.RegisterMessage(Build)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETER,
  '__module__' : 'chromiumos.config.api.test.benchy.v1.plan_pb2'
  # @@protoc_insertion_point(class_scope:chromium.config.api.test.benchy.v1.Parameter)
  })
_sym_db.RegisterMessage(Parameter)

Workload = _reflection.GeneratedProtocolMessageType('Workload', (_message.Message,), {
  'DESCRIPTOR' : _WORKLOAD,
  '__module__' : 'chromiumos.config.api.test.benchy.v1.plan_pb2'
  # @@protoc_insertion_point(class_scope:chromium.config.api.test.benchy.v1.Workload)
  })
_sym_db.RegisterMessage(Workload)

Plan = _reflection.GeneratedProtocolMessageType('Plan', (_message.Message,), {
  'DESCRIPTOR' : _PLAN,
  '__module__' : 'chromiumos.config.api.test.benchy.v1.plan_pb2'
  # @@protoc_insertion_point(class_scope:chromium.config.api.test.benchy.v1.Plan)
  })
_sym_db.RegisterMessage(Plan)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
