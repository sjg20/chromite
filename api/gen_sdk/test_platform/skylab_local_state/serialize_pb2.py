# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_local_state/serialize.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0test_platform/skylab_local_state/serialize.proto\x12 test_platform.skylab_local_state\"9\n\x10SerializeRequest\x12\x10\n\x08\x64ut_name\x18\x01 \x01(\t\x12\x13\n\x0bresults_dir\x18\x02 \x01(\tBLZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_local_stateb\x06proto3')



_SERIALIZEREQUEST = DESCRIPTOR.message_types_by_name['SerializeRequest']
SerializeRequest = _reflection.GeneratedProtocolMessageType('SerializeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERIALIZEREQUEST,
  '__module__' : 'test_platform.skylab_local_state.serialize_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_local_state.SerializeRequest)
  })
_sym_db.RegisterMessage(SerializeRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_local_state'
  _SERIALIZEREQUEST._serialized_start=86
  _SERIALIZEREQUEST._serialized_end=143
# @@protoc_insertion_point(module_scope)
