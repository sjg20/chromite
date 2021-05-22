# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_local_state/load.proto

from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.test_platform.skylab_local_state import common_pb2 as test__platform_dot_skylab__local__state_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/skylab_local_state/load.proto',
  package='test_platform.skylab_local_state',
  syntax='proto3',
  serialized_options=b'ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_local_state',
  serialized_pb=b'\n+test_platform/skylab_local_state/load.proto\x12 test_platform.skylab_local_state\x1a-test_platform/skylab_local_state/common.proto\"\x9d\x01\n\x0bLoadRequest\x12\x38\n\x06\x63onfig\x18\x01 \x01(\x0b\x32(.test_platform.skylab_local_state.Config\x12\x10\n\x08\x64ut_name\x18\x03 \x01(\t\x12\x0e\n\x06run_id\x18\x04 \x01(\t\x12\x0e\n\x06\x64ut_id\x18\x05 \x01(\t\x12\x0f\n\x07test_id\x18\x06 \x01(\tJ\x04\x08\x02\x10\x03R\x0bresults_dir\"\xdb\x01\n\x0cLoadResponse\x12\x65\n\x14provisionable_labels\x18\x01 \x03(\x0b\x32G.test_platform.skylab_local_state.LoadResponse.ProvisionableLabelsEntry\x12\x13\n\x0bresults_dir\x18\x02 \x01(\t\x1a:\n\x18ProvisionableLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x03\x10\x04R\rasync_resultsBLZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_local_stateb\x06proto3'
  ,
  dependencies=[test__platform_dot_skylab__local__state_dot_common__pb2.DESCRIPTOR,])




_LOADREQUEST = _descriptor.Descriptor(
  name='LoadRequest',
  full_name='test_platform.skylab_local_state.LoadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='test_platform.skylab_local_state.LoadRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dut_name', full_name='test_platform.skylab_local_state.LoadRequest.dut_name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_id', full_name='test_platform.skylab_local_state.LoadRequest.run_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dut_id', full_name='test_platform.skylab_local_state.LoadRequest.dut_id', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_id', full_name='test_platform.skylab_local_state.LoadRequest.test_id', index=4,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=129,
  serialized_end=286,
)


_LOADRESPONSE_PROVISIONABLELABELSENTRY = _descriptor.Descriptor(
  name='ProvisionableLabelsEntry',
  full_name='test_platform.skylab_local_state.LoadResponse.ProvisionableLabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.skylab_local_state.LoadResponse.ProvisionableLabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.skylab_local_state.LoadResponse.ProvisionableLabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=429,
  serialized_end=487,
)

_LOADRESPONSE = _descriptor.Descriptor(
  name='LoadResponse',
  full_name='test_platform.skylab_local_state.LoadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provisionable_labels', full_name='test_platform.skylab_local_state.LoadResponse.provisionable_labels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results_dir', full_name='test_platform.skylab_local_state.LoadResponse.results_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOADRESPONSE_PROVISIONABLELABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=508,
)

_LOADREQUEST.fields_by_name['config'].message_type = test__platform_dot_skylab__local__state_dot_common__pb2._CONFIG
_LOADRESPONSE_PROVISIONABLELABELSENTRY.containing_type = _LOADRESPONSE
_LOADRESPONSE.fields_by_name['provisionable_labels'].message_type = _LOADRESPONSE_PROVISIONABLELABELSENTRY
DESCRIPTOR.message_types_by_name['LoadRequest'] = _LOADREQUEST
DESCRIPTOR.message_types_by_name['LoadResponse'] = _LOADRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoadRequest = _reflection.GeneratedProtocolMessageType('LoadRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOADREQUEST,
  '__module__' : 'test_platform.skylab_local_state.load_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_local_state.LoadRequest)
  })
_sym_db.RegisterMessage(LoadRequest)

LoadResponse = _reflection.GeneratedProtocolMessageType('LoadResponse', (_message.Message,), {

  'ProvisionableLabelsEntry' : _reflection.GeneratedProtocolMessageType('ProvisionableLabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LOADRESPONSE_PROVISIONABLELABELSENTRY,
    '__module__' : 'test_platform.skylab_local_state.load_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_local_state.LoadResponse.ProvisionableLabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LOADRESPONSE,
  '__module__' : 'test_platform.skylab_local_state.load_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_local_state.LoadResponse)
  })
_sym_db.RegisterMessage(LoadResponse)
_sym_db.RegisterMessage(LoadResponse.ProvisionableLabelsEntry)


DESCRIPTOR._options = None
_LOADRESPONSE_PROVISIONABLELABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
