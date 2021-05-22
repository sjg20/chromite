# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/build_api_config.proto

from chromite.third_party.google.protobuf.internal import enum_type_wrapper
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromite/api/build_api_config.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api',
  serialized_pb=b'\n#chromite/api/build_api_config.proto\x12\x0c\x63hromite.api\"M\n\x0e\x42uildApiConfig\x12\x10\n\x08log_path\x18\x01 \x01(\t\x12)\n\tcall_type\x18\x02 \x01(\x0e\x32\x16.chromite.api.CallType*\xa6\x01\n\x08\x43\x61llType\x12\x12\n\x0e\x43\x41LL_TYPE_NONE\x10\x00\x12\x15\n\x11\x43\x41LL_TYPE_EXECUTE\x10\x01\x12\x1b\n\x17\x43\x41LL_TYPE_VALIDATE_ONLY\x10\x02\x12\x1a\n\x16\x43\x41LL_TYPE_MOCK_SUCCESS\x10\x03\x12\x1a\n\x16\x43\x41LL_TYPE_MOCK_FAILURE\x10\x04\x12\x1a\n\x16\x43\x41LL_TYPE_MOCK_INVALID\x10\x05\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3'
)

_CALLTYPE = _descriptor.EnumDescriptor(
  name='CallType',
  full_name='chromite.api.CallType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CALL_TYPE_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_TYPE_EXECUTE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_TYPE_VALIDATE_ONLY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_TYPE_MOCK_SUCCESS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_TYPE_MOCK_FAILURE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_TYPE_MOCK_INVALID', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=133,
  serialized_end=299,
)
_sym_db.RegisterEnumDescriptor(_CALLTYPE)

CallType = enum_type_wrapper.EnumTypeWrapper(_CALLTYPE)
CALL_TYPE_NONE = 0
CALL_TYPE_EXECUTE = 1
CALL_TYPE_VALIDATE_ONLY = 2
CALL_TYPE_MOCK_SUCCESS = 3
CALL_TYPE_MOCK_FAILURE = 4
CALL_TYPE_MOCK_INVALID = 5



_BUILDAPICONFIG = _descriptor.Descriptor(
  name='BuildApiConfig',
  full_name='chromite.api.BuildApiConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_path', full_name='chromite.api.BuildApiConfig.log_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_type', full_name='chromite.api.BuildApiConfig.call_type', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=130,
)

_BUILDAPICONFIG.fields_by_name['call_type'].enum_type = _CALLTYPE
DESCRIPTOR.message_types_by_name['BuildApiConfig'] = _BUILDAPICONFIG
DESCRIPTOR.enum_types_by_name['CallType'] = _CALLTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildApiConfig = _reflection.GeneratedProtocolMessageType('BuildApiConfig', (_message.Message,), {
  'DESCRIPTOR' : _BUILDAPICONFIG,
  '__module__' : 'chromite.api.build_api_config_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BuildApiConfig)
  })
_sym_db.RegisterMessage(BuildApiConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
