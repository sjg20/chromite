# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_local_state/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-test_platform/skylab_local_state/common.proto\x12 test_platform.skylab_local_state\"\x9a\x01\n\x06\x43onfig\x12\x15\n\radmin_service\x18\x01 \x01(\t\x12\x14\n\x0c\x61utotest_dir\x18\x02 \x01(\t\x12\x1e\n\x16\x63ros_inventory_service\x18\x03 \x01(\t\x12\x18\n\x10\x63ros_ufs_service\x18\x04 \x01(\t\x12\x12\n\nbot_prefix\x18\x05 \x01(\t\x12\x15\n\rufs_namespace\x18\x06 \x01(\tBLZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_local_stateb\x06proto3')



_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'test_platform.skylab_local_state.common_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_local_state.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_local_state'
  _CONFIG._serialized_start=84
  _CONFIG._serialized_end=238
# @@protoc_insertion_point(module_scope)
