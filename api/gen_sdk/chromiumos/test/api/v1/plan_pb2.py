# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/v1/plan.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.test.api import coverage_rule_pb2 as chromiumos_dot_test_dot_api_dot_coverage__rule__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/test/api/v1/plan.proto',
  package='chromiumos.test.api.v1',
  syntax='proto3',
  serialized_options=b'Z<go.chromium.org/chromiumos/config/go/test/api/v1;test_api_v1',
  serialized_pb=b'\n!chromiumos/test/api/v1/plan.proto\x12\x16\x63hromiumos.test.api.v1\x1a\'chromiumos/test/api/coverage_rule.proto\"\x9f\x01\n\nHWTestPlan\x12\x39\n\x02id\x18\x01 \x01(\x0b\x32-.chromiumos.test.api.v1.HWTestPlan.TestPlanId\x12\x39\n\x0e\x63overage_rules\x18\x02 \x03(\x0b\x32!.chromiumos.test.api.CoverageRule\x1a\x1b\n\nTestPlanId\x12\r\n\x05value\x18\x01 \x01(\t\"\x9f\x01\n\nVMTestPlan\x12\x39\n\x02id\x18\x01 \x01(\x0b\x32-.chromiumos.test.api.v1.VMTestPlan.TestPlanId\x12\x39\n\x0e\x63overage_rules\x18\x02 \x03(\x0b\x32!.chromiumos.test.api.CoverageRule\x1a\x1b\n\nTestPlanId\x12\r\n\x05value\x18\x01 \x01(\tB>Z<go.chromium.org/chromiumos/config/go/test/api/v1;test_api_v1b\x06proto3'
  ,
  dependencies=[chromiumos_dot_test_dot_api_dot_coverage__rule__pb2.DESCRIPTOR,])




_HWTESTPLAN_TESTPLANID = _descriptor.Descriptor(
  name='TestPlanId',
  full_name='chromiumos.test.api.v1.HWTestPlan.TestPlanId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.test.api.v1.HWTestPlan.TestPlanId.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=235,
  serialized_end=262,
)

_HWTESTPLAN = _descriptor.Descriptor(
  name='HWTestPlan',
  full_name='chromiumos.test.api.v1.HWTestPlan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chromiumos.test.api.v1.HWTestPlan.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coverage_rules', full_name='chromiumos.test.api.v1.HWTestPlan.coverage_rules', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HWTESTPLAN_TESTPLANID, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=262,
)


_VMTESTPLAN_TESTPLANID = _descriptor.Descriptor(
  name='TestPlanId',
  full_name='chromiumos.test.api.v1.VMTestPlan.TestPlanId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.test.api.v1.VMTestPlan.TestPlanId.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=235,
  serialized_end=262,
)

_VMTESTPLAN = _descriptor.Descriptor(
  name='VMTestPlan',
  full_name='chromiumos.test.api.v1.VMTestPlan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chromiumos.test.api.v1.VMTestPlan.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coverage_rules', full_name='chromiumos.test.api.v1.VMTestPlan.coverage_rules', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VMTESTPLAN_TESTPLANID, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=424,
)

_HWTESTPLAN_TESTPLANID.containing_type = _HWTESTPLAN
_HWTESTPLAN.fields_by_name['id'].message_type = _HWTESTPLAN_TESTPLANID
_HWTESTPLAN.fields_by_name['coverage_rules'].message_type = chromiumos_dot_test_dot_api_dot_coverage__rule__pb2._COVERAGERULE
_VMTESTPLAN_TESTPLANID.containing_type = _VMTESTPLAN
_VMTESTPLAN.fields_by_name['id'].message_type = _VMTESTPLAN_TESTPLANID
_VMTESTPLAN.fields_by_name['coverage_rules'].message_type = chromiumos_dot_test_dot_api_dot_coverage__rule__pb2._COVERAGERULE
DESCRIPTOR.message_types_by_name['HWTestPlan'] = _HWTESTPLAN
DESCRIPTOR.message_types_by_name['VMTestPlan'] = _VMTESTPLAN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HWTestPlan = _reflection.GeneratedProtocolMessageType('HWTestPlan', (_message.Message,), {

  'TestPlanId' : _reflection.GeneratedProtocolMessageType('TestPlanId', (_message.Message,), {
    'DESCRIPTOR' : _HWTESTPLAN_TESTPLANID,
    '__module__' : 'chromiumos.test.api.v1.plan_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.v1.HWTestPlan.TestPlanId)
    })
  ,
  'DESCRIPTOR' : _HWTESTPLAN,
  '__module__' : 'chromiumos.test.api.v1.plan_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.v1.HWTestPlan)
  })
_sym_db.RegisterMessage(HWTestPlan)
_sym_db.RegisterMessage(HWTestPlan.TestPlanId)

VMTestPlan = _reflection.GeneratedProtocolMessageType('VMTestPlan', (_message.Message,), {

  'TestPlanId' : _reflection.GeneratedProtocolMessageType('TestPlanId', (_message.Message,), {
    'DESCRIPTOR' : _VMTESTPLAN_TESTPLANID,
    '__module__' : 'chromiumos.test.api.v1.plan_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.v1.VMTestPlan.TestPlanId)
    })
  ,
  'DESCRIPTOR' : _VMTESTPLAN,
  '__module__' : 'chromiumos.test.api.v1.plan_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.v1.VMTestPlan)
  })
_sym_db.RegisterMessage(VMTestPlan)
_sym_db.RegisterMessage(VMTestPlan.TestPlanId)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
