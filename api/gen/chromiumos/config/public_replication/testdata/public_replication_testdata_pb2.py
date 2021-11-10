# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/public_replication/testdata/public_replication_testdata.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromiumos.config.public_replication import public_replication_pb2 as chromiumos_dot_config_dot_public__replication_dot_public__replication__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/public_replication/testdata/public_replication_testdata.proto',
  package='chromiumos.config.public_replication.testdata',
  syntax='proto3',
  serialized_options=b'Z@go.chromium.org/chromiumos/config/go/public_replication/testdata',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nOchromiumos/config/public_replication/testdata/public_replication_testdata.proto\x12-chromiumos.config.public_replication.testdata\x1a=chromiumos/config/public_replication/public_replication.proto\"\x9b\x02\n\x19PublicReplicationTestdata\x12S\n\x12public_replication\x18\x01 \x01(\x0b\x32\x37.chromiumos.config.public_replication.PublicReplication\x12\x0c\n\x04str1\x18\x02 \x01(\t\x12\x0c\n\x04str2\x18\x03 \x01(\t\x12`\n\x04map1\x18\x04 \x03(\x0b\x32R.chromiumos.config.public_replication.testdata.PublicReplicationTestdata.Map1Entry\x1a+\n\tMap1Entry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\xe5\x01\n\x10WrapperTestdata1\x12\n\n\x02n1\x18\x01 \x01(\x05\x12]\n\x0bpr_testdata\x18\x02 \x01(\x0b\x32H.chromiumos.config.public_replication.testdata.PublicReplicationTestdata\x12\x66\n\x14repeated_pr_testdata\x18\x03 \x03(\x0b\x32H.chromiumos.config.public_replication.testdata.PublicReplicationTestdata\"n\n\x10WrapperTestdata2\x12Z\n\x11wrapper_testdata1\x18\x01 \x01(\x0b\x32?.chromiumos.config.public_replication.testdata.WrapperTestdata1\"\xd2\x01\n\x10WrapperTestdata3\x12S\n\x12public_replication\x18\x01 \x01(\x0b\x32\x37.chromiumos.config.public_replication.PublicReplication\x12\n\n\x02\x62\x31\x18\x02 \x01(\x08\x12]\n\x0bpr_testdata\x18\x03 \x01(\x0b\x32H.chromiumos.config.public_replication.testdata.PublicReplicationTestdata\"z\n\x10RecursiveMessage\x12\n\n\x02\x62\x31\x18\x01 \x01(\x08\x12Z\n\x11recursive_message\x18\x02 \x01(\x0b\x32?.chromiumos.config.public_replication.testdata.RecursiveMessage\"\xe3\x01\n\x0ePrivateMessage\x12T\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x44.chromiumos.config.public_replication.testdata.PrivateMessage.Config\x1a{\n\x06\x43onfig\x12Z\n\x07payload\x18\x01 \x03(\x0b\x32I.chromiumos.config.public_replication.testdata.PrivateMessage.Config.Test\x1a\x15\n\x04Test\x12\r\n\x05\x62ools\x18\x01 \x01(\x08\"n\n\x14NestedPrivateMessage\x12V\n\x0fnested_messages\x18\x01 \x01(\x0b\x32=.chromiumos.config.public_replication.testdata.PrivateMessage\"v\n\x1cNestedRepeatedPrivateMessage\x12V\n\x0fnested_messages\x18\x01 \x03(\x0b\x32=.chromiumos.config.public_replication.testdata.PrivateMessageBBZ@go.chromium.org/chromiumos/config/go/public_replication/testdatab\x06proto3'
  ,
  dependencies=[chromiumos_dot_config_dot_public__replication_dot_public__replication__pb2.DESCRIPTOR,])




_PUBLICREPLICATIONTESTDATA_MAP1ENTRY = _descriptor.Descriptor(
  name='Map1Entry',
  full_name='chromiumos.config.public_replication.testdata.PublicReplicationTestdata.Map1Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='chromiumos.config.public_replication.testdata.PublicReplicationTestdata.Map1Entry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.config.public_replication.testdata.PublicReplicationTestdata.Map1Entry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=477,
)

_PUBLICREPLICATIONTESTDATA = _descriptor.Descriptor(
  name='PublicReplicationTestdata',
  full_name='chromiumos.config.public_replication.testdata.PublicReplicationTestdata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_replication', full_name='chromiumos.config.public_replication.testdata.PublicReplicationTestdata.public_replication', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='str1', full_name='chromiumos.config.public_replication.testdata.PublicReplicationTestdata.str1', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='str2', full_name='chromiumos.config.public_replication.testdata.PublicReplicationTestdata.str2', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map1', full_name='chromiumos.config.public_replication.testdata.PublicReplicationTestdata.map1', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PUBLICREPLICATIONTESTDATA_MAP1ENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=477,
)


_WRAPPERTESTDATA1 = _descriptor.Descriptor(
  name='WrapperTestdata1',
  full_name='chromiumos.config.public_replication.testdata.WrapperTestdata1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='chromiumos.config.public_replication.testdata.WrapperTestdata1.n1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pr_testdata', full_name='chromiumos.config.public_replication.testdata.WrapperTestdata1.pr_testdata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repeated_pr_testdata', full_name='chromiumos.config.public_replication.testdata.WrapperTestdata1.repeated_pr_testdata', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=480,
  serialized_end=709,
)


_WRAPPERTESTDATA2 = _descriptor.Descriptor(
  name='WrapperTestdata2',
  full_name='chromiumos.config.public_replication.testdata.WrapperTestdata2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='wrapper_testdata1', full_name='chromiumos.config.public_replication.testdata.WrapperTestdata2.wrapper_testdata1', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=711,
  serialized_end=821,
)


_WRAPPERTESTDATA3 = _descriptor.Descriptor(
  name='WrapperTestdata3',
  full_name='chromiumos.config.public_replication.testdata.WrapperTestdata3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_replication', full_name='chromiumos.config.public_replication.testdata.WrapperTestdata3.public_replication', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b1', full_name='chromiumos.config.public_replication.testdata.WrapperTestdata3.b1', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pr_testdata', full_name='chromiumos.config.public_replication.testdata.WrapperTestdata3.pr_testdata', index=2,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=824,
  serialized_end=1034,
)


_RECURSIVEMESSAGE = _descriptor.Descriptor(
  name='RecursiveMessage',
  full_name='chromiumos.config.public_replication.testdata.RecursiveMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='b1', full_name='chromiumos.config.public_replication.testdata.RecursiveMessage.b1', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recursive_message', full_name='chromiumos.config.public_replication.testdata.RecursiveMessage.recursive_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1036,
  serialized_end=1158,
)


_PRIVATEMESSAGE_CONFIG_TEST = _descriptor.Descriptor(
  name='Test',
  full_name='chromiumos.config.public_replication.testdata.PrivateMessage.Config.Test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bools', full_name='chromiumos.config.public_replication.testdata.PrivateMessage.Config.Test.bools', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1367,
  serialized_end=1388,
)

_PRIVATEMESSAGE_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='chromiumos.config.public_replication.testdata.PrivateMessage.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='chromiumos.config.public_replication.testdata.PrivateMessage.Config.payload', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PRIVATEMESSAGE_CONFIG_TEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1265,
  serialized_end=1388,
)

_PRIVATEMESSAGE = _descriptor.Descriptor(
  name='PrivateMessage',
  full_name='chromiumos.config.public_replication.testdata.PrivateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='chromiumos.config.public_replication.testdata.PrivateMessage.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PRIVATEMESSAGE_CONFIG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1161,
  serialized_end=1388,
)


_NESTEDPRIVATEMESSAGE = _descriptor.Descriptor(
  name='NestedPrivateMessage',
  full_name='chromiumos.config.public_replication.testdata.NestedPrivateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nested_messages', full_name='chromiumos.config.public_replication.testdata.NestedPrivateMessage.nested_messages', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1390,
  serialized_end=1500,
)


_NESTEDREPEATEDPRIVATEMESSAGE = _descriptor.Descriptor(
  name='NestedRepeatedPrivateMessage',
  full_name='chromiumos.config.public_replication.testdata.NestedRepeatedPrivateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nested_messages', full_name='chromiumos.config.public_replication.testdata.NestedRepeatedPrivateMessage.nested_messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1502,
  serialized_end=1620,
)

_PUBLICREPLICATIONTESTDATA_MAP1ENTRY.containing_type = _PUBLICREPLICATIONTESTDATA
_PUBLICREPLICATIONTESTDATA.fields_by_name['public_replication'].message_type = chromiumos_dot_config_dot_public__replication_dot_public__replication__pb2._PUBLICREPLICATION
_PUBLICREPLICATIONTESTDATA.fields_by_name['map1'].message_type = _PUBLICREPLICATIONTESTDATA_MAP1ENTRY
_WRAPPERTESTDATA1.fields_by_name['pr_testdata'].message_type = _PUBLICREPLICATIONTESTDATA
_WRAPPERTESTDATA1.fields_by_name['repeated_pr_testdata'].message_type = _PUBLICREPLICATIONTESTDATA
_WRAPPERTESTDATA2.fields_by_name['wrapper_testdata1'].message_type = _WRAPPERTESTDATA1
_WRAPPERTESTDATA3.fields_by_name['public_replication'].message_type = chromiumos_dot_config_dot_public__replication_dot_public__replication__pb2._PUBLICREPLICATION
_WRAPPERTESTDATA3.fields_by_name['pr_testdata'].message_type = _PUBLICREPLICATIONTESTDATA
_RECURSIVEMESSAGE.fields_by_name['recursive_message'].message_type = _RECURSIVEMESSAGE
_PRIVATEMESSAGE_CONFIG_TEST.containing_type = _PRIVATEMESSAGE_CONFIG
_PRIVATEMESSAGE_CONFIG.fields_by_name['payload'].message_type = _PRIVATEMESSAGE_CONFIG_TEST
_PRIVATEMESSAGE_CONFIG.containing_type = _PRIVATEMESSAGE
_PRIVATEMESSAGE.fields_by_name['config'].message_type = _PRIVATEMESSAGE_CONFIG
_NESTEDPRIVATEMESSAGE.fields_by_name['nested_messages'].message_type = _PRIVATEMESSAGE
_NESTEDREPEATEDPRIVATEMESSAGE.fields_by_name['nested_messages'].message_type = _PRIVATEMESSAGE
DESCRIPTOR.message_types_by_name['PublicReplicationTestdata'] = _PUBLICREPLICATIONTESTDATA
DESCRIPTOR.message_types_by_name['WrapperTestdata1'] = _WRAPPERTESTDATA1
DESCRIPTOR.message_types_by_name['WrapperTestdata2'] = _WRAPPERTESTDATA2
DESCRIPTOR.message_types_by_name['WrapperTestdata3'] = _WRAPPERTESTDATA3
DESCRIPTOR.message_types_by_name['RecursiveMessage'] = _RECURSIVEMESSAGE
DESCRIPTOR.message_types_by_name['PrivateMessage'] = _PRIVATEMESSAGE
DESCRIPTOR.message_types_by_name['NestedPrivateMessage'] = _NESTEDPRIVATEMESSAGE
DESCRIPTOR.message_types_by_name['NestedRepeatedPrivateMessage'] = _NESTEDREPEATEDPRIVATEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PublicReplicationTestdata = _reflection.GeneratedProtocolMessageType('PublicReplicationTestdata', (_message.Message,), {

  'Map1Entry' : _reflection.GeneratedProtocolMessageType('Map1Entry', (_message.Message,), {
    'DESCRIPTOR' : _PUBLICREPLICATIONTESTDATA_MAP1ENTRY,
    '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.PublicReplicationTestdata.Map1Entry)
    })
  ,
  'DESCRIPTOR' : _PUBLICREPLICATIONTESTDATA,
  '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.PublicReplicationTestdata)
  })
_sym_db.RegisterMessage(PublicReplicationTestdata)
_sym_db.RegisterMessage(PublicReplicationTestdata.Map1Entry)

WrapperTestdata1 = _reflection.GeneratedProtocolMessageType('WrapperTestdata1', (_message.Message,), {
  'DESCRIPTOR' : _WRAPPERTESTDATA1,
  '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.WrapperTestdata1)
  })
_sym_db.RegisterMessage(WrapperTestdata1)

WrapperTestdata2 = _reflection.GeneratedProtocolMessageType('WrapperTestdata2', (_message.Message,), {
  'DESCRIPTOR' : _WRAPPERTESTDATA2,
  '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.WrapperTestdata2)
  })
_sym_db.RegisterMessage(WrapperTestdata2)

WrapperTestdata3 = _reflection.GeneratedProtocolMessageType('WrapperTestdata3', (_message.Message,), {
  'DESCRIPTOR' : _WRAPPERTESTDATA3,
  '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.WrapperTestdata3)
  })
_sym_db.RegisterMessage(WrapperTestdata3)

RecursiveMessage = _reflection.GeneratedProtocolMessageType('RecursiveMessage', (_message.Message,), {
  'DESCRIPTOR' : _RECURSIVEMESSAGE,
  '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.RecursiveMessage)
  })
_sym_db.RegisterMessage(RecursiveMessage)

PrivateMessage = _reflection.GeneratedProtocolMessageType('PrivateMessage', (_message.Message,), {

  'Config' : _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {

    'Test' : _reflection.GeneratedProtocolMessageType('Test', (_message.Message,), {
      'DESCRIPTOR' : _PRIVATEMESSAGE_CONFIG_TEST,
      '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
      # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.PrivateMessage.Config.Test)
      })
    ,
    'DESCRIPTOR' : _PRIVATEMESSAGE_CONFIG,
    '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.PrivateMessage.Config)
    })
  ,
  'DESCRIPTOR' : _PRIVATEMESSAGE,
  '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.PrivateMessage)
  })
_sym_db.RegisterMessage(PrivateMessage)
_sym_db.RegisterMessage(PrivateMessage.Config)
_sym_db.RegisterMessage(PrivateMessage.Config.Test)

NestedPrivateMessage = _reflection.GeneratedProtocolMessageType('NestedPrivateMessage', (_message.Message,), {
  'DESCRIPTOR' : _NESTEDPRIVATEMESSAGE,
  '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.NestedPrivateMessage)
  })
_sym_db.RegisterMessage(NestedPrivateMessage)

NestedRepeatedPrivateMessage = _reflection.GeneratedProtocolMessageType('NestedRepeatedPrivateMessage', (_message.Message,), {
  'DESCRIPTOR' : _NESTEDREPEATEDPRIVATEMESSAGE,
  '__module__' : 'chromiumos.config.public_replication.testdata.public_replication_testdata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.public_replication.testdata.NestedRepeatedPrivateMessage)
  })
_sym_db.RegisterMessage(NestedRepeatedPrivateMessage)


DESCRIPTOR._options = None
_PUBLICREPLICATIONTESTDATA_MAP1ENTRY._options = None
# @@protoc_insertion_point(module_scope)
