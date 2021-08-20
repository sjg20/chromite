# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/results/v2/result.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.third_party.google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/test/results/v2/result.proto',
  package='chromiumos.config.api.test.results.v2',
  syntax='proto3',
  serialized_options=b'Z@go.chromium.org/chromiumos/config/go/api/test/results/v2;results',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2chromiumos/config/api/test/results/v2/result.proto\x12%chromiumos.config.api.test.results.v2\x1a\x1cgoogle/protobuf/struct.proto\"\xc5\x04\n\x06Result\x12\x42\n\x05state\x18\x01 \x01(\x0e\x32\x33.chromiumos.config.api.test.results.v2.Result.State\x12\x43\n\x06\x65rrors\x18\x02 \x03(\x0b\x32\x33.chromiumos.config.api.test.results.v2.Result.Error\x1a\xe9\x02\n\x05\x45rror\x12J\n\x06source\x18\x01 \x01(\x0e\x32:.chromiumos.config.api.test.results.v2.Result.Error.Source\x12N\n\x08severity\x18\x02 \x01(\x0e\x32<.chromiumos.config.api.test.results.v2.Result.Error.Severity\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"Y\n\x06Source\x12\x16\n\x12SOURCE_UNSPECIFIED\x10\x00\x12\x08\n\x04TEST\x10\x01\x12\x16\n\x12REMOTE_TEST_DRIVER\x10\x02\x12\x15\n\x11TEST_LAB_SERVICES\x10\x03\"?\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43RITICAL\x10\x01\x12\x0b\n\x07WARNING\x10\x02\"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\x0b\n\x07SKIPPED\x10\x03\x42\x42Z@go.chromium.org/chromiumos/config/go/api/test/results/v2;resultsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])



_RESULT_ERROR_SOURCE = _descriptor.EnumDescriptor(
  name='Source',
  full_name='chromiumos.config.api.test.results.v2.Result.Error.Source',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SOURCE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_TEST_DRIVER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEST_LAB_SERVICES', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=479,
  serialized_end=568,
)
_sym_db.RegisterEnumDescriptor(_RESULT_ERROR_SOURCE)

_RESULT_ERROR_SEVERITY = _descriptor.EnumDescriptor(
  name='Severity',
  full_name='chromiumos.config.api.test.results.v2.Result.Error.Severity',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CRITICAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=570,
  serialized_end=633,
)
_sym_db.RegisterEnumDescriptor(_RESULT_ERROR_SEVERITY)

_RESULT_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='chromiumos.config.api.test.results.v2.Result.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SKIPPED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=635,
  serialized_end=705,
)
_sym_db.RegisterEnumDescriptor(_RESULT_STATE)


_RESULT_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='chromiumos.config.api.test.results.v2.Result.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='chromiumos.config.api.test.results.v2.Result.Error.source', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='severity', full_name='chromiumos.config.api.test.results.v2.Result.Error.severity', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='chromiumos.config.api.test.results.v2.Result.Error.details', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESULT_ERROR_SOURCE,
    _RESULT_ERROR_SEVERITY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=633,
)

_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='chromiumos.config.api.test.results.v2.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='chromiumos.config.api.test.results.v2.Result.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='chromiumos.config.api.test.results.v2.Result.errors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESULT_ERROR, ],
  enum_types=[
    _RESULT_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=705,
)

_RESULT_ERROR.fields_by_name['source'].enum_type = _RESULT_ERROR_SOURCE
_RESULT_ERROR.fields_by_name['severity'].enum_type = _RESULT_ERROR_SEVERITY
_RESULT_ERROR.fields_by_name['details'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RESULT_ERROR.containing_type = _RESULT
_RESULT_ERROR_SOURCE.containing_type = _RESULT_ERROR
_RESULT_ERROR_SEVERITY.containing_type = _RESULT_ERROR
_RESULT.fields_by_name['state'].enum_type = _RESULT_STATE
_RESULT.fields_by_name['errors'].message_type = _RESULT_ERROR
_RESULT_STATE.containing_type = _RESULT
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {

  'Error' : _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
    'DESCRIPTOR' : _RESULT_ERROR,
    '__module__' : 'chromiumos.config.api.test.results.v2.result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.results.v2.Result.Error)
    })
  ,
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'chromiumos.config.api.test.results.v2.result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.results.v2.Result)
  })
_sym_db.RegisterMessage(Result)
_sym_db.RegisterMessage(Result.Error)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)