# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/sdk_cache_state.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/sdk_cache_state.proto',
  package='chromiumos',
  syntax='proto3',
  serialized_options=b'Z4go.chromium.org/chromiumos/infra/proto/go/chromiumos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n chromiumos/sdk_cache_state.proto\x12\nchromiumos\"f\n\rSdkCacheState\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x17\n\x0fmanifest_branch\x18\x02 \x01(\t\x12\x14\n\x0cmanifest_url\x18\x03 \x01(\t\x12\x15\n\rsnapshot_hash\x18\x04 \x01(\tB6Z4go.chromium.org/chromiumos/infra/proto/go/chromiumosb\x06proto3'
)




_SDKCACHESTATE = _descriptor.Descriptor(
  name='SdkCacheState',
  full_name='chromiumos.SdkCacheState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='chromiumos.SdkCacheState.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='manifest_branch', full_name='chromiumos.SdkCacheState.manifest_branch', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='manifest_url', full_name='chromiumos.SdkCacheState.manifest_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snapshot_hash', full_name='chromiumos.SdkCacheState.snapshot_hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=48,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['SdkCacheState'] = _SDKCACHESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SdkCacheState = _reflection.GeneratedProtocolMessageType('SdkCacheState', (_message.Message,), {
  'DESCRIPTOR' : _SDKCACHESTATE,
  '__module__' : 'chromiumos.sdk_cache_state_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.SdkCacheState)
  })
_sym_db.RegisterMessage(SdkCacheState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
