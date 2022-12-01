# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/software/ui_config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/software/ui_config.proto',
  package='chromiumos.config.api.software',
  syntax='proto3',
  serialized_options=b'Z1go.chromium.org/chromiumos/config/go/api/software',
  serialized_pb=b'\n.chromiumos/config/api/software/ui_config.proto\x12\x1e\x63hromiumos.config.api.software\"\xcf\x01\n\x08UiConfig\x12\x1a\n\x12\x65xtra_web_apps_dir\x18\x01 \x01(\t\x12I\n\x0brequisition\x18\x02 \x01(\x0e\x32\x34.chromiumos.config.api.software.UiConfig.Requisition\"\\\n\x0bRequisition\x12\x1b\n\x17REQUISITION_UNSPECIFIED\x10\x00\x12\x18\n\x14REQUISITION_CHROMEOS\x10\x01\x12\x16\n\x12REQUISITION_MEETHW\x10\x02\x42\x33Z1go.chromium.org/chromiumos/config/go/api/softwareb\x06proto3'
)



_UICONFIG_REQUISITION = _descriptor.EnumDescriptor(
  name='Requisition',
  full_name='chromiumos.config.api.software.UiConfig.Requisition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQUISITION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUISITION_CHROMEOS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUISITION_MEETHW', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=198,
  serialized_end=290,
)
_sym_db.RegisterEnumDescriptor(_UICONFIG_REQUISITION)


_UICONFIG = _descriptor.Descriptor(
  name='UiConfig',
  full_name='chromiumos.config.api.software.UiConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='extra_web_apps_dir', full_name='chromiumos.config.api.software.UiConfig.extra_web_apps_dir', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requisition', full_name='chromiumos.config.api.software.UiConfig.requisition', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UICONFIG_REQUISITION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=290,
)

_UICONFIG.fields_by_name['requisition'].enum_type = _UICONFIG_REQUISITION
_UICONFIG_REQUISITION.containing_type = _UICONFIG
DESCRIPTOR.message_types_by_name['UiConfig'] = _UICONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UiConfig = _reflection.GeneratedProtocolMessageType('UiConfig', (_message.Message,), {
  'DESCRIPTOR' : _UICONFIG,
  '__module__' : 'chromiumos.config.api.software.ui_config_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.software.UiConfig)
  })
_sym_db.RegisterMessage(UiConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
