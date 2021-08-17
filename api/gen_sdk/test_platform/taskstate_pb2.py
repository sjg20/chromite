# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/taskstate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/taskstate.proto',
  package='test_platform',
  syntax='proto3',
  serialized_options=_b('Z7go.chromium.org/chromiumos/infra/proto/go/test_platform'),
  serialized_pb=_b('\n\x1dtest_platform/taskstate.proto\x12\rtest_platform\"\xc0\x04\n\tTaskState\x12\x36\n\nlife_cycle\x18\x01 \x01(\x0e\x32\".test_platform.TaskState.LifeCycle\x12\x31\n\x07verdict\x18\x02 \x01(\x0e\x32 .test_platform.TaskState.Verdict\"\x87\x01\n\rLifeCycleMask\x12\x1f\n\x1bLIFE_CYCLE_MASK_UNSPECIFIED\x10\x00\x12\x1b\n\x17LIFE_CYCLE_MASK_STARTED\x10\x10\x12\x1d\n\x19LIFE_CYCLE_MASK_COMPLETED\x10 \x12\x19\n\x15LIFE_CYCLE_MASK_FINAL\x10@\"\xbc\x01\n\tLifeCycle\x12\x1a\n\x16LIFE_CYCLE_UNSPECIFIED\x10\x00\x12\x16\n\x12LIFE_CYCLE_PENDING\x10\x01\x12\x16\n\x12LIFE_CYCLE_RUNNING\x10\x10\x12\x18\n\x14LIFE_CYCLE_COMPLETED\x10p\x12\x18\n\x14LIFE_CYCLE_CANCELLED\x10\x41\x12\x17\n\x13LIFE_CYCLE_REJECTED\x10\x42\x12\x16\n\x12LIFE_CYCLE_ABORTED\x10P\"\x7f\n\x07Verdict\x12\x17\n\x13VERDICT_UNSPECIFIED\x10\x00\x12\x12\n\x0eVERDICT_PASSED\x10\x01\x12\x12\n\x0eVERDICT_FAILED\x10\x02\x12\x16\n\x12VERDICT_NO_VERDICT\x10\x03\x12\x1b\n\x17VERDICT_PASSED_ON_RETRY\x10\x04\x42\x39Z7go.chromium.org/chromiumos/infra/proto/go/test_platformb\x06proto3')
)



_TASKSTATE_LIFECYCLEMASK = _descriptor.EnumDescriptor(
  name='LifeCycleMask',
  full_name='test_platform.TaskState.LifeCycleMask',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_MASK_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_MASK_STARTED', index=1, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_MASK_COMPLETED', index=2, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_MASK_FINAL', index=3, number=64,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=170,
  serialized_end=305,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATE_LIFECYCLEMASK)

_TASKSTATE_LIFECYCLE = _descriptor.EnumDescriptor(
  name='LifeCycle',
  full_name='test_platform.TaskState.LifeCycle',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_RUNNING', index=2, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_COMPLETED', index=3, number=112,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_CANCELLED', index=4, number=65,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_REJECTED', index=5, number=66,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFE_CYCLE_ABORTED', index=6, number=80,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=308,
  serialized_end=496,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATE_LIFECYCLE)

_TASKSTATE_VERDICT = _descriptor.EnumDescriptor(
  name='Verdict',
  full_name='test_platform.TaskState.Verdict',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VERDICT_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_PASSED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_NO_VERDICT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_PASSED_ON_RETRY', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=498,
  serialized_end=625,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATE_VERDICT)


_TASKSTATE = _descriptor.Descriptor(
  name='TaskState',
  full_name='test_platform.TaskState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='life_cycle', full_name='test_platform.TaskState.life_cycle', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verdict', full_name='test_platform.TaskState.verdict', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TASKSTATE_LIFECYCLEMASK,
    _TASKSTATE_LIFECYCLE,
    _TASKSTATE_VERDICT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=625,
)

_TASKSTATE.fields_by_name['life_cycle'].enum_type = _TASKSTATE_LIFECYCLE
_TASKSTATE.fields_by_name['verdict'].enum_type = _TASKSTATE_VERDICT
_TASKSTATE_LIFECYCLEMASK.containing_type = _TASKSTATE
_TASKSTATE_LIFECYCLE.containing_type = _TASKSTATE
_TASKSTATE_VERDICT.containing_type = _TASKSTATE
DESCRIPTOR.message_types_by_name['TaskState'] = _TASKSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskState = _reflection.GeneratedProtocolMessageType('TaskState', (_message.Message,), dict(
  DESCRIPTOR = _TASKSTATE,
  __module__ = 'test_platform.taskstate_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.TaskState)
  ))
_sym_db.RegisterMessage(TaskState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
