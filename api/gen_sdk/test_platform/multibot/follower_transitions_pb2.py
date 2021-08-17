# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/multibot/follower_transitions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.test_platform.skylab_local_state import multihost_pb2 as test__platform_dot_skylab__local__state_dot_multihost__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/multibot/follower_transitions.proto',
  package='test_platform.multibot',
  syntax='proto3',
  serialized_options=_b('Z@go.chromium.org/chromiumos/infra/proto/go/test_platform/multibot'),
  serialized_pb=_b('\n1test_platform/multibot/follower_transitions.proto\x12\x16test_platform.multibot\x1a\x30test_platform/skylab_local_state/multihost.proto\"\xee\x01\n\x13\x46ollowerStateChange\x12L\n\tnew_state\x18\x01 \x01(\x0e\x32\x39.test_platform.multibot.FollowerStateChange.FollowerState\"\x88\x01\n\rFollowerState\x12\x13\n\x0fSTATE_UNDEFINED\x10\x00\x12\x11\n\rSTATE_STARTED\x10\x10\x12 \n\x1cSTATE_WAITING_TO_RUN_PAYLOAD\x10 \x12\x19\n\x15STATE_RUNNING_PAYLOAD\x10\x30\x12\x12\n\x0eSTATE_CLEANING\x10@\"\xd2\x01\n\rFollowerEvent\x12O\n\x0f\x66inished_prejob\x18\x01 \x01(\x0b\x32\x34.test_platform.multibot.FollowerEvent.FinishedPrejobH\x00\x12\x0e\n\x04\x64ied\x18\x02 \x01(\x08H\x00\x1aW\n\x0e\x46inishedPrejob\x12\x45\n\thost_info\x18\x01 \x01(\x0b\x32\x32.test_platform.skylab_local_state.MultiBotHostInfoB\x07\n\x05\x65ventBBZ@go.chromium.org/chromiumos/infra/proto/go/test_platform/multibotb\x06proto3')
  ,
  dependencies=[test__platform_dot_skylab__local__state_dot_multihost__pb2.DESCRIPTOR,])



_FOLLOWERSTATECHANGE_FOLLOWERSTATE = _descriptor.EnumDescriptor(
  name='FollowerState',
  full_name='test_platform.multibot.FollowerStateChange.FollowerState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_STARTED', index=1, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_WAITING_TO_RUN_PAYLOAD', index=2, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_RUNNING_PAYLOAD', index=3, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_CLEANING', index=4, number=64,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=230,
  serialized_end=366,
)
_sym_db.RegisterEnumDescriptor(_FOLLOWERSTATECHANGE_FOLLOWERSTATE)


_FOLLOWERSTATECHANGE = _descriptor.Descriptor(
  name='FollowerStateChange',
  full_name='test_platform.multibot.FollowerStateChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_state', full_name='test_platform.multibot.FollowerStateChange.new_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FOLLOWERSTATECHANGE_FOLLOWERSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=366,
)


_FOLLOWEREVENT_FINISHEDPREJOB = _descriptor.Descriptor(
  name='FinishedPrejob',
  full_name='test_platform.multibot.FollowerEvent.FinishedPrejob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_info', full_name='test_platform.multibot.FollowerEvent.FinishedPrejob.host_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=483,
  serialized_end=570,
)

_FOLLOWEREVENT = _descriptor.Descriptor(
  name='FollowerEvent',
  full_name='test_platform.multibot.FollowerEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='finished_prejob', full_name='test_platform.multibot.FollowerEvent.finished_prejob', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='died', full_name='test_platform.multibot.FollowerEvent.died', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FOLLOWEREVENT_FINISHEDPREJOB, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='event', full_name='test_platform.multibot.FollowerEvent.event',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=369,
  serialized_end=579,
)

_FOLLOWERSTATECHANGE.fields_by_name['new_state'].enum_type = _FOLLOWERSTATECHANGE_FOLLOWERSTATE
_FOLLOWERSTATECHANGE_FOLLOWERSTATE.containing_type = _FOLLOWERSTATECHANGE
_FOLLOWEREVENT_FINISHEDPREJOB.fields_by_name['host_info'].message_type = test__platform_dot_skylab__local__state_dot_multihost__pb2._MULTIBOTHOSTINFO
_FOLLOWEREVENT_FINISHEDPREJOB.containing_type = _FOLLOWEREVENT
_FOLLOWEREVENT.fields_by_name['finished_prejob'].message_type = _FOLLOWEREVENT_FINISHEDPREJOB
_FOLLOWEREVENT.oneofs_by_name['event'].fields.append(
  _FOLLOWEREVENT.fields_by_name['finished_prejob'])
_FOLLOWEREVENT.fields_by_name['finished_prejob'].containing_oneof = _FOLLOWEREVENT.oneofs_by_name['event']
_FOLLOWEREVENT.oneofs_by_name['event'].fields.append(
  _FOLLOWEREVENT.fields_by_name['died'])
_FOLLOWEREVENT.fields_by_name['died'].containing_oneof = _FOLLOWEREVENT.oneofs_by_name['event']
DESCRIPTOR.message_types_by_name['FollowerStateChange'] = _FOLLOWERSTATECHANGE
DESCRIPTOR.message_types_by_name['FollowerEvent'] = _FOLLOWEREVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FollowerStateChange = _reflection.GeneratedProtocolMessageType('FollowerStateChange', (_message.Message,), dict(
  DESCRIPTOR = _FOLLOWERSTATECHANGE,
  __module__ = 'test_platform.multibot.follower_transitions_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.multibot.FollowerStateChange)
  ))
_sym_db.RegisterMessage(FollowerStateChange)

FollowerEvent = _reflection.GeneratedProtocolMessageType('FollowerEvent', (_message.Message,), dict(

  FinishedPrejob = _reflection.GeneratedProtocolMessageType('FinishedPrejob', (_message.Message,), dict(
    DESCRIPTOR = _FOLLOWEREVENT_FINISHEDPREJOB,
    __module__ = 'test_platform.multibot.follower_transitions_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.multibot.FollowerEvent.FinishedPrejob)
    ))
  ,
  DESCRIPTOR = _FOLLOWEREVENT,
  __module__ = 'test_platform.multibot.follower_transitions_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.multibot.FollowerEvent)
  ))
_sym_db.RegisterMessage(FollowerEvent)
_sym_db.RegisterMessage(FollowerEvent.FinishedPrejob)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
