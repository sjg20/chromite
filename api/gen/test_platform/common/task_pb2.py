# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/common/task.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/common/task.proto',
  package='test_platform.common',
  syntax='proto3',
  serialized_options=b'Z>go.chromium.org/chromiumos/infra/proto/go/test_platform/common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1ftest_platform/common/task.proto\x12\x14test_platform.common\"J\n\x0bTaskLogData\x12\x0e\n\x06gs_url\x18\x01 \x01(\t\x12\x15\n\rstainless_url\x18\x02 \x01(\t\x12\x14\n\x0ctesthaus_url\x18\x03 \x01(\tB@Z>go.chromium.org/chromiumos/infra/proto/go/test_platform/commonb\x06proto3'
)




_TASKLOGDATA = _descriptor.Descriptor(
  name='TaskLogData',
  full_name='test_platform.common.TaskLogData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gs_url', full_name='test_platform.common.TaskLogData.gs_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stainless_url', full_name='test_platform.common.TaskLogData.stainless_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='testhaus_url', full_name='test_platform.common.TaskLogData.testhaus_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=57,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['TaskLogData'] = _TASKLOGDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskLogData = _reflection.GeneratedProtocolMessageType('TaskLogData', (_message.Message,), {
  'DESCRIPTOR' : _TASKLOGDATA,
  '__module__' : 'test_platform.common.task_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.common.TaskLogData)
  })
_sym_db.RegisterMessage(TaskLogData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
