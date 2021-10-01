# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/phosphorus/runtest.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromiumos.build.api import container_metadata_pb2 as chromiumos_dot_build_dot_api_dot_container__metadata__pb2
from chromite.third_party.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from chromite.api.gen.test_platform.phosphorus import common_pb2 as test__platform_dot_phosphorus_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/phosphorus/runtest.proto',
  package='test_platform.phosphorus',
  syntax='proto3',
  serialized_options=b'ZBgo.chromium.org/chromiumos/infra/proto/go/test_platform/phosphorus',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&test_platform/phosphorus/runtest.proto\x12\x18test_platform.phosphorus\x1a-chromiumos/build/api/container_metadata.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a%test_platform/phosphorus/common.proto\"\xbf\x04\n\x0eRunTestRequest\x12\x30\n\x06\x63onfig\x18\x01 \x01(\x0b\x32 .test_platform.phosphorus.Config\x12\x15\n\rdut_hostnames\x18\x02 \x03(\t\x12\x45\n\x08\x61utotest\x18\x03 \x01(\x0b\x32\x31.test_platform.phosphorus.RunTestRequest.AutotestH\x00\x12,\n\x08\x64\x65\x61\x64line\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x46\n\x14\x63ontainer_image_info\x18\x06 \x01(\x0b\x32(.chromiumos.build.api.ContainerImageInfo\x1a\x8b\x02\n\x08\x41utotest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\ttest_args\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x16\n\x0eis_client_test\x18\x04 \x01(\x08\x12O\n\x07keyvals\x18\x05 \x03(\x0b\x32>.test_platform.phosphorus.RunTestRequest.Autotest.KeyvalsEntry\x12\x11\n\tpeer_duts\x18\x06 \x03(\t\x12\x1c\n\x14image_storage_server\x18\x07 \x01(\t\x1a.\n\x0cKeyvalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x06\n\x04testJ\x04\x08\x04\x10\x05R\x0b\x65nvironment\"\xbd\x01\n\x0fRunTestResponse\x12>\n\x05state\x18\x01 \x01(\x0e\x32/.test_platform.phosphorus.RunTestResponse.State\x12\x13\n\x0bresults_dir\x18\x02 \x01(\t\"U\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\r\n\tTIMED_OUT\x10\x03\x12\x0b\n\x07\x41\x42ORTED\x10\x04\x42\x44ZBgo.chromium.org/chromiumos/infra/proto/go/test_platform/phosphorusb\x06proto3'
  ,
  dependencies=[chromiumos_dot_build_dot_api_dot_container__metadata__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,test__platform_dot_phosphorus_dot_common__pb2.DESCRIPTOR,])



_RUNTESTRESPONSE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='test_platform.phosphorus.RunTestResponse.State',
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
      name='TIMED_OUT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ABORTED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=870,
  serialized_end=955,
)
_sym_db.RegisterEnumDescriptor(_RUNTESTRESPONSE_STATE)


_RUNTESTREQUEST_AUTOTEST_KEYVALSENTRY = _descriptor.Descriptor(
  name='KeyvalsEntry',
  full_name='test_platform.phosphorus.RunTestRequest.Autotest.KeyvalsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.phosphorus.RunTestRequest.Autotest.KeyvalsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.phosphorus.RunTestRequest.Autotest.KeyvalsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=690,
  serialized_end=736,
)

_RUNTESTREQUEST_AUTOTEST = _descriptor.Descriptor(
  name='Autotest',
  full_name='test_platform.phosphorus.RunTestRequest.Autotest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test_platform.phosphorus.RunTestRequest.Autotest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_args', full_name='test_platform.phosphorus.RunTestRequest.Autotest.test_args', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='test_platform.phosphorus.RunTestRequest.Autotest.display_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_client_test', full_name='test_platform.phosphorus.RunTestRequest.Autotest.is_client_test', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keyvals', full_name='test_platform.phosphorus.RunTestRequest.Autotest.keyvals', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peer_duts', full_name='test_platform.phosphorus.RunTestRequest.Autotest.peer_duts', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_storage_server', full_name='test_platform.phosphorus.RunTestRequest.Autotest.image_storage_server', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RUNTESTREQUEST_AUTOTEST_KEYVALSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=469,
  serialized_end=736,
)

_RUNTESTREQUEST = _descriptor.Descriptor(
  name='RunTestRequest',
  full_name='test_platform.phosphorus.RunTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='test_platform.phosphorus.RunTestRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dut_hostnames', full_name='test_platform.phosphorus.RunTestRequest.dut_hostnames', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autotest', full_name='test_platform.phosphorus.RunTestRequest.autotest', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deadline', full_name='test_platform.phosphorus.RunTestRequest.deadline', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='container_image_info', full_name='test_platform.phosphorus.RunTestRequest.container_image_info', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RUNTESTREQUEST_AUTOTEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='test', full_name='test_platform.phosphorus.RunTestRequest.test',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=188,
  serialized_end=763,
)


_RUNTESTRESPONSE = _descriptor.Descriptor(
  name='RunTestResponse',
  full_name='test_platform.phosphorus.RunTestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='test_platform.phosphorus.RunTestResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results_dir', full_name='test_platform.phosphorus.RunTestResponse.results_dir', index=1,
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
    _RUNTESTRESPONSE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=766,
  serialized_end=955,
)

_RUNTESTREQUEST_AUTOTEST_KEYVALSENTRY.containing_type = _RUNTESTREQUEST_AUTOTEST
_RUNTESTREQUEST_AUTOTEST.fields_by_name['keyvals'].message_type = _RUNTESTREQUEST_AUTOTEST_KEYVALSENTRY
_RUNTESTREQUEST_AUTOTEST.containing_type = _RUNTESTREQUEST
_RUNTESTREQUEST.fields_by_name['config'].message_type = test__platform_dot_phosphorus_dot_common__pb2._CONFIG
_RUNTESTREQUEST.fields_by_name['autotest'].message_type = _RUNTESTREQUEST_AUTOTEST
_RUNTESTREQUEST.fields_by_name['deadline'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RUNTESTREQUEST.fields_by_name['container_image_info'].message_type = chromiumos_dot_build_dot_api_dot_container__metadata__pb2._CONTAINERIMAGEINFO
_RUNTESTREQUEST.oneofs_by_name['test'].fields.append(
  _RUNTESTREQUEST.fields_by_name['autotest'])
_RUNTESTREQUEST.fields_by_name['autotest'].containing_oneof = _RUNTESTREQUEST.oneofs_by_name['test']
_RUNTESTRESPONSE.fields_by_name['state'].enum_type = _RUNTESTRESPONSE_STATE
_RUNTESTRESPONSE_STATE.containing_type = _RUNTESTRESPONSE
DESCRIPTOR.message_types_by_name['RunTestRequest'] = _RUNTESTREQUEST
DESCRIPTOR.message_types_by_name['RunTestResponse'] = _RUNTESTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunTestRequest = _reflection.GeneratedProtocolMessageType('RunTestRequest', (_message.Message,), {

  'Autotest' : _reflection.GeneratedProtocolMessageType('Autotest', (_message.Message,), {

    'KeyvalsEntry' : _reflection.GeneratedProtocolMessageType('KeyvalsEntry', (_message.Message,), {
      'DESCRIPTOR' : _RUNTESTREQUEST_AUTOTEST_KEYVALSENTRY,
      '__module__' : 'test_platform.phosphorus.runtest_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.phosphorus.RunTestRequest.Autotest.KeyvalsEntry)
      })
    ,
    'DESCRIPTOR' : _RUNTESTREQUEST_AUTOTEST,
    '__module__' : 'test_platform.phosphorus.runtest_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.phosphorus.RunTestRequest.Autotest)
    })
  ,
  'DESCRIPTOR' : _RUNTESTREQUEST,
  '__module__' : 'test_platform.phosphorus.runtest_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.phosphorus.RunTestRequest)
  })
_sym_db.RegisterMessage(RunTestRequest)
_sym_db.RegisterMessage(RunTestRequest.Autotest)
_sym_db.RegisterMessage(RunTestRequest.Autotest.KeyvalsEntry)

RunTestResponse = _reflection.GeneratedProtocolMessageType('RunTestResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNTESTRESPONSE,
  '__module__' : 'test_platform.phosphorus.runtest_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.phosphorus.RunTestResponse)
  })
_sym_db.RegisterMessage(RunTestResponse)


DESCRIPTOR._options = None
_RUNTESTREQUEST_AUTOTEST_KEYVALSENTRY._options = None
# @@protoc_insertion_point(module_scope)
