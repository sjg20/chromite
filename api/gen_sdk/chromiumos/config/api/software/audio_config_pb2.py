# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/software/audio_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.config.public_replication import public_replication_pb2 as chromiumos_dot_config_dot_public__replication_dot_public__replication__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/software/audio_config.proto',
  package='chromiumos.config.api.software',
  syntax='proto3',
  serialized_options=_b('Z1go.chromium.org/chromiumos/config/go/api/software'),
  serialized_pb=_b('\n1chromiumos/config/api/software/audio_config.proto\x12\x1e\x63hromiumos.config.api.software\x1a=chromiumos/config/public_replication/public_replication.proto\"\xb8\x02\n\x0b\x41udioConfig\x12S\n\x12public_replication\x18\t \x01(\x0b\x32\x37.chromiumos.config.public_replication.PublicReplication\x12\x11\n\tcard_name\x18\x01 \x01(\t\x12\x18\n\x10\x63\x61rd_config_file\x18\x02 \x01(\t\x12\x10\n\x08\x64sp_file\x18\x03 \x01(\t\x12\x10\n\x08ucm_file\x18\x04 \x01(\t\x12\x17\n\x0fucm_master_file\x18\x05 \x01(\t\x12\x12\n\nucm_suffix\x18\x06 \x01(\t\x12\x13\n\x0bmodule_file\x18\x07 \x01(\t\x12\x12\n\nboard_file\x18\x08 \x01(\t\x12\x1c\n\x14sound_card_init_file\x18\n \x01(\t\x12\x0f\n\x07\x63\x61rd_id\x18\x0b \x01(\tB3Z1go.chromium.org/chromiumos/config/go/api/softwareb\x06proto3')
  ,
  dependencies=[chromiumos_dot_config_dot_public__replication_dot_public__replication__pb2.DESCRIPTOR,])




_AUDIOCONFIG = _descriptor.Descriptor(
  name='AudioConfig',
  full_name='chromiumos.config.api.software.AudioConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_replication', full_name='chromiumos.config.api.software.AudioConfig.public_replication', index=0,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_name', full_name='chromiumos.config.api.software.AudioConfig.card_name', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_config_file', full_name='chromiumos.config.api.software.AudioConfig.card_config_file', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dsp_file', full_name='chromiumos.config.api.software.AudioConfig.dsp_file', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ucm_file', full_name='chromiumos.config.api.software.AudioConfig.ucm_file', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ucm_master_file', full_name='chromiumos.config.api.software.AudioConfig.ucm_master_file', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ucm_suffix', full_name='chromiumos.config.api.software.AudioConfig.ucm_suffix', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module_file', full_name='chromiumos.config.api.software.AudioConfig.module_file', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='board_file', full_name='chromiumos.config.api.software.AudioConfig.board_file', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sound_card_init_file', full_name='chromiumos.config.api.software.AudioConfig.sound_card_init_file', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_id', full_name='chromiumos.config.api.software.AudioConfig.card_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=149,
  serialized_end=461,
)

_AUDIOCONFIG.fields_by_name['public_replication'].message_type = chromiumos_dot_config_dot_public__replication_dot_public__replication__pb2._PUBLICREPLICATION
DESCRIPTOR.message_types_by_name['AudioConfig'] = _AUDIOCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AudioConfig = _reflection.GeneratedProtocolMessageType('AudioConfig', (_message.Message,), dict(
  DESCRIPTOR = _AUDIOCONFIG,
  __module__ = 'chromiumos.config.api.software.audio_config_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.software.AudioConfig)
  ))
_sym_db.RegisterMessage(AudioConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
