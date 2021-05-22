# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/multibot/leader_transitions.proto

from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.test_platform.multibot import common_pb2 as test__platform_dot_multibot_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/multibot/leader_transitions.proto',
  package='test_platform.multibot',
  syntax='proto3',
  serialized_options=b'Z@go.chromium.org/chromiumos/infra/proto/go/test_platform/multibot',
  serialized_pb=b'\n/test_platform/multibot/leader_transitions.proto\x12\x16test_platform.multibot\x1a#test_platform/multibot/common.proto\"\xf1\x02\n\x17LeaderTransitionMessage\x12N\n\tnew_state\x18\x01 \x01(\x0e\x32;.test_platform.multibot.LeaderTransitionMessage.LeaderState\x12\x42\n\x12\x66ollower_gathering\x18\x02 \x01(\x0b\x32&.test_platform.multibot.FollowersState\"\xc1\x01\n\x0bLeaderState\x12\x13\n\x0fSTATE_UNDEFINED\x10\x00\x12\x14\n\x10STATE_SCHEDULING\x10\x10\x12\x18\n\x14STATE_RUNNING_PREJOB\x10 \x12\x1f\n\x1bSTATE_WAITING_FOR_FOLLOWERS\x10\x30\x12\x1d\n\x19STATE_NOTIFYING_FOLLOWERS\x10@\x12\x19\n\x15STATE_RUNNING_PAYLOAD\x10P\x12\x12\n\x0eSTATE_CLEANING\x10`\"o\n\x0e\x46ollowersState\x12\x1d\n\x15waiting_for_followers\x18\x01 \x01(\x05\x12>\n\x0f\x66ollowers_heard\x18\x02 \x01(\x0b\x32%.test_platform.multibot.HostInfoStoreBBZ@go.chromium.org/chromiumos/infra/proto/go/test_platform/multibotb\x06proto3'
  ,
  dependencies=[test__platform_dot_multibot_dot_common__pb2.DESCRIPTOR,])



_LEADERTRANSITIONMESSAGE_LEADERSTATE = _descriptor.EnumDescriptor(
  name='LeaderState',
  full_name='test_platform.multibot.LeaderTransitionMessage.LeaderState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_SCHEDULING', index=1, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_RUNNING_PREJOB', index=2, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_WAITING_FOR_FOLLOWERS', index=3, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_NOTIFYING_FOLLOWERS', index=4, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_RUNNING_PAYLOAD', index=5, number=80,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_CLEANING', index=6, number=96,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=289,
  serialized_end=482,
)
_sym_db.RegisterEnumDescriptor(_LEADERTRANSITIONMESSAGE_LEADERSTATE)


_LEADERTRANSITIONMESSAGE = _descriptor.Descriptor(
  name='LeaderTransitionMessage',
  full_name='test_platform.multibot.LeaderTransitionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_state', full_name='test_platform.multibot.LeaderTransitionMessage.new_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='follower_gathering', full_name='test_platform.multibot.LeaderTransitionMessage.follower_gathering', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEADERTRANSITIONMESSAGE_LEADERSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=482,
)


_FOLLOWERSSTATE = _descriptor.Descriptor(
  name='FollowersState',
  full_name='test_platform.multibot.FollowersState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='waiting_for_followers', full_name='test_platform.multibot.FollowersState.waiting_for_followers', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='followers_heard', full_name='test_platform.multibot.FollowersState.followers_heard', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=484,
  serialized_end=595,
)

_LEADERTRANSITIONMESSAGE.fields_by_name['new_state'].enum_type = _LEADERTRANSITIONMESSAGE_LEADERSTATE
_LEADERTRANSITIONMESSAGE.fields_by_name['follower_gathering'].message_type = _FOLLOWERSSTATE
_LEADERTRANSITIONMESSAGE_LEADERSTATE.containing_type = _LEADERTRANSITIONMESSAGE
_FOLLOWERSSTATE.fields_by_name['followers_heard'].message_type = test__platform_dot_multibot_dot_common__pb2._HOSTINFOSTORE
DESCRIPTOR.message_types_by_name['LeaderTransitionMessage'] = _LEADERTRANSITIONMESSAGE
DESCRIPTOR.message_types_by_name['FollowersState'] = _FOLLOWERSSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LeaderTransitionMessage = _reflection.GeneratedProtocolMessageType('LeaderTransitionMessage', (_message.Message,), {
  'DESCRIPTOR' : _LEADERTRANSITIONMESSAGE,
  '__module__' : 'test_platform.multibot.leader_transitions_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.multibot.LeaderTransitionMessage)
  })
_sym_db.RegisterMessage(LeaderTransitionMessage)

FollowersState = _reflection.GeneratedProtocolMessageType('FollowersState', (_message.Message,), {
  'DESCRIPTOR' : _FOLLOWERSSTATE,
  '__module__' : 'test_platform.multibot.leader_transitions_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.multibot.FollowersState)
  })
_sym_db.RegisterMessage(FollowersState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
