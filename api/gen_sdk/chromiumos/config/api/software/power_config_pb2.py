# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/software/power_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/software/power_config.proto',
  package='chromiumos.config.api.software',
  syntax='proto3',
  serialized_options=_b('Z1go.chromium.org/chromiumos/config/go/api/software'),
  serialized_pb=_b('\n1chromiumos/config/api/software/power_config.proto\x12\x1e\x63hromiumos.config.api.software\"\x94\x01\n\x0bPowerConfig\x12Q\n\x0bpreferences\x18\x01 \x03(\x0b\x32<.chromiumos.config.api.software.PowerConfig.PreferencesEntry\x1a\x32\n\x10PreferencesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x33Z1go.chromium.org/chromiumos/config/go/api/softwareb\x06proto3')
)




_POWERCONFIG_PREFERENCESENTRY = _descriptor.Descriptor(
  name='PreferencesEntry',
  full_name='chromiumos.config.api.software.PowerConfig.PreferencesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='chromiumos.config.api.software.PowerConfig.PreferencesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.config.api.software.PowerConfig.PreferencesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=234,
)

_POWERCONFIG = _descriptor.Descriptor(
  name='PowerConfig',
  full_name='chromiumos.config.api.software.PowerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='preferences', full_name='chromiumos.config.api.software.PowerConfig.preferences', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POWERCONFIG_PREFERENCESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=234,
)

_POWERCONFIG_PREFERENCESENTRY.containing_type = _POWERCONFIG
_POWERCONFIG.fields_by_name['preferences'].message_type = _POWERCONFIG_PREFERENCESENTRY
DESCRIPTOR.message_types_by_name['PowerConfig'] = _POWERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PowerConfig = _reflection.GeneratedProtocolMessageType('PowerConfig', (_message.Message,), dict(

  PreferencesEntry = _reflection.GeneratedProtocolMessageType('PreferencesEntry', (_message.Message,), dict(
    DESCRIPTOR = _POWERCONFIG_PREFERENCESENTRY,
    __module__ = 'chromiumos.config.api.software.power_config_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.software.PowerConfig.PreferencesEntry)
    ))
  ,
  DESCRIPTOR = _POWERCONFIG,
  __module__ = 'chromiumos.config.api.software.power_config_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.software.PowerConfig)
  ))
_sym_db.RegisterMessage(PowerConfig)
_sym_db.RegisterMessage(PowerConfig.PreferencesEntry)


DESCRIPTOR._options = None
_POWERCONFIG_PREFERENCESENTRY._options = None
# @@protoc_insertion_point(module_scope)
