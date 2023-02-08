# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/multibot/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.test_platform import request_pb2 as test__platform_dot_request__pb2
from chromite.api.gen_sdk.test_platform.skylab_local_state import host_info_pb2 as test__platform_dot_skylab__local__state_dot_host__info__pb2
from chromite.api.gen_sdk.test_platform.skylab_test_runner import request_pb2 as test__platform_dot_skylab__test__runner_dot_request__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#test_platform/multibot/common.proto\x12\x16test_platform.multibot\x1a\x1btest_platform/request.proto\x1a\x30test_platform/skylab_local_state/host_info.proto\x1a.test_platform/skylab_test_runner/request.proto\"\x1f\n\x0eMultiBotConfig\x12\r\n\x05topic\x18\x01 \x01(\t\"\xbf\x01\n\rHostInfoStore\x12H\n\nhost_infos\x18\x01 \x03(\x0b\x32\x34.test_platform.multibot.HostInfoStore.HostInfosEntry\x1a\x64\n\x0eHostInfosEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.test_platform.skylab_local_state.AutotestHostInfo:\x02\x38\x01\"\xe4\x02\n\x0c\x46ollowerSpec\x12P\n\x11static_attributes\x18\x01 \x01(\x0b\x32\x35.test_platform.multibot.FollowerSpec.StaticAttributes\x12@\n\x06prejob\x18\x02 \x01(\x0b\x32\x30.test_platform.skylab_test_runner.Request.Prejob\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x1a\xb0\x01\n\x10StaticAttributes\x12M\n\x13hardware_attributes\x18\x01 \x01(\x0b\x32\x30.test_platform.Request.Params.HardwareAttributes\x12M\n\x13software_attributes\x18\x02 \x01(\x0b\x32\x30.test_platform.Request.Params.SoftwareAttributesBBZ@go.chromium.org/chromiumos/infra/proto/go/test_platform/multibotb\x06proto3')



_MULTIBOTCONFIG = DESCRIPTOR.message_types_by_name['MultiBotConfig']
_HOSTINFOSTORE = DESCRIPTOR.message_types_by_name['HostInfoStore']
_HOSTINFOSTORE_HOSTINFOSENTRY = _HOSTINFOSTORE.nested_types_by_name['HostInfosEntry']
_FOLLOWERSPEC = DESCRIPTOR.message_types_by_name['FollowerSpec']
_FOLLOWERSPEC_STATICATTRIBUTES = _FOLLOWERSPEC.nested_types_by_name['StaticAttributes']
MultiBotConfig = _reflection.GeneratedProtocolMessageType('MultiBotConfig', (_message.Message,), {
  'DESCRIPTOR' : _MULTIBOTCONFIG,
  '__module__' : 'test_platform.multibot.common_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.multibot.MultiBotConfig)
  })
_sym_db.RegisterMessage(MultiBotConfig)

HostInfoStore = _reflection.GeneratedProtocolMessageType('HostInfoStore', (_message.Message,), {

  'HostInfosEntry' : _reflection.GeneratedProtocolMessageType('HostInfosEntry', (_message.Message,), {
    'DESCRIPTOR' : _HOSTINFOSTORE_HOSTINFOSENTRY,
    '__module__' : 'test_platform.multibot.common_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.multibot.HostInfoStore.HostInfosEntry)
    })
  ,
  'DESCRIPTOR' : _HOSTINFOSTORE,
  '__module__' : 'test_platform.multibot.common_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.multibot.HostInfoStore)
  })
_sym_db.RegisterMessage(HostInfoStore)
_sym_db.RegisterMessage(HostInfoStore.HostInfosEntry)

FollowerSpec = _reflection.GeneratedProtocolMessageType('FollowerSpec', (_message.Message,), {

  'StaticAttributes' : _reflection.GeneratedProtocolMessageType('StaticAttributes', (_message.Message,), {
    'DESCRIPTOR' : _FOLLOWERSPEC_STATICATTRIBUTES,
    '__module__' : 'test_platform.multibot.common_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.multibot.FollowerSpec.StaticAttributes)
    })
  ,
  'DESCRIPTOR' : _FOLLOWERSPEC,
  '__module__' : 'test_platform.multibot.common_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.multibot.FollowerSpec)
  })
_sym_db.RegisterMessage(FollowerSpec)
_sym_db.RegisterMessage(FollowerSpec.StaticAttributes)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z@go.chromium.org/chromiumos/infra/proto/go/test_platform/multibot'
  _HOSTINFOSTORE_HOSTINFOSENTRY._options = None
  _HOSTINFOSTORE_HOSTINFOSENTRY._serialized_options = b'8\001'
  _MULTIBOTCONFIG._serialized_start=190
  _MULTIBOTCONFIG._serialized_end=221
  _HOSTINFOSTORE._serialized_start=224
  _HOSTINFOSTORE._serialized_end=415
  _HOSTINFOSTORE_HOSTINFOSENTRY._serialized_start=315
  _HOSTINFOSTORE_HOSTINFOSENTRY._serialized_end=415
  _FOLLOWERSPEC._serialized_start=418
  _FOLLOWERSPEC._serialized_end=774
  _FOLLOWERSPEC_STATICATTRIBUTES._serialized_start=598
  _FOLLOWERSPEC_STATICATTRIBUTES._serialized_end=774
# @@protoc_insertion_point(module_scope)
