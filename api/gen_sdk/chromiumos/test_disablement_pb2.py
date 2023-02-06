# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test_disablement.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/test_disablement.proto',
  package='chromiumos',
  syntax='proto3',
  serialized_options=b'\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumos',
  serialized_pb=b'\n!chromiumos/test_disablement.proto\x12\nchromiumos\"\xdb\x03\n\x0fTestDisablement\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x41\n\x0c\x64ut_criteria\x18\x02 \x03(\x0b\x32+.chromiumos.TestDisablement.FilterCriterion\x12\x42\n\rtest_criteria\x18\x03 \x03(\x0b\x32+.chromiumos.TestDisablement.FilterCriterion\x12\x45\n\x10\x63ontext_criteria\x18\x04 \x03(\x0b\x32+.chromiumos.TestDisablement.FilterCriterion\x12:\n\x08\x62\x65havior\x18\x05 \x01(\x0e\x32(.chromiumos.TestDisablement.TestBehavior\x12\x0f\n\x07\x62ug_ids\x18\x06 \x03(\t\x1a?\n\x0f\x46ilterCriterion\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\x12\x0f\n\x07negated\x18\x03 \x01(\x08\"^\n\x0cTestBehavior\x12\x0c\n\x08\x43RITICAL\x10\x00\x12\x11\n\rINFORMATIONAL\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x12\x0c\n\x08WONT_FIX\x10\x03\x12\x12\n\x0eSKIP_TEMPORARY\x10\x04\"G\n\x12TestDisablementCfg\x12\x31\n\x0c\x64isablements\x18\x01 \x03(\x0b\x32\x1b.chromiumos.TestDisablementBY\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumosb\x06proto3'
)



_TESTDISABLEMENT_TESTBEHAVIOR = _descriptor.EnumDescriptor(
  name='TestBehavior',
  full_name='chromiumos.TestDisablement.TestBehavior',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CRITICAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFORMATIONAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WONT_FIX', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKIP_TEMPORARY', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=431,
  serialized_end=525,
)
_sym_db.RegisterEnumDescriptor(_TESTDISABLEMENT_TESTBEHAVIOR)


_TESTDISABLEMENT_FILTERCRITERION = _descriptor.Descriptor(
  name='FilterCriterion',
  full_name='chromiumos.TestDisablement.FilterCriterion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='chromiumos.TestDisablement.FilterCriterion.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='chromiumos.TestDisablement.FilterCriterion.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='negated', full_name='chromiumos.TestDisablement.FilterCriterion.negated', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=366,
  serialized_end=429,
)

_TESTDISABLEMENT = _descriptor.Descriptor(
  name='TestDisablement',
  full_name='chromiumos.TestDisablement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromiumos.TestDisablement.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dut_criteria', full_name='chromiumos.TestDisablement.dut_criteria', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_criteria', full_name='chromiumos.TestDisablement.test_criteria', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context_criteria', full_name='chromiumos.TestDisablement.context_criteria', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='behavior', full_name='chromiumos.TestDisablement.behavior', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bug_ids', full_name='chromiumos.TestDisablement.bug_ids', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TESTDISABLEMENT_FILTERCRITERION, ],
  enum_types=[
    _TESTDISABLEMENT_TESTBEHAVIOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=525,
)


_TESTDISABLEMENTCFG = _descriptor.Descriptor(
  name='TestDisablementCfg',
  full_name='chromiumos.TestDisablementCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disablements', full_name='chromiumos.TestDisablementCfg.disablements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=527,
  serialized_end=598,
)

_TESTDISABLEMENT_FILTERCRITERION.containing_type = _TESTDISABLEMENT
_TESTDISABLEMENT.fields_by_name['dut_criteria'].message_type = _TESTDISABLEMENT_FILTERCRITERION
_TESTDISABLEMENT.fields_by_name['test_criteria'].message_type = _TESTDISABLEMENT_FILTERCRITERION
_TESTDISABLEMENT.fields_by_name['context_criteria'].message_type = _TESTDISABLEMENT_FILTERCRITERION
_TESTDISABLEMENT.fields_by_name['behavior'].enum_type = _TESTDISABLEMENT_TESTBEHAVIOR
_TESTDISABLEMENT_TESTBEHAVIOR.containing_type = _TESTDISABLEMENT
_TESTDISABLEMENTCFG.fields_by_name['disablements'].message_type = _TESTDISABLEMENT
DESCRIPTOR.message_types_by_name['TestDisablement'] = _TESTDISABLEMENT
DESCRIPTOR.message_types_by_name['TestDisablementCfg'] = _TESTDISABLEMENTCFG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestDisablement = _reflection.GeneratedProtocolMessageType('TestDisablement', (_message.Message,), {

  'FilterCriterion' : _reflection.GeneratedProtocolMessageType('FilterCriterion', (_message.Message,), {
    'DESCRIPTOR' : _TESTDISABLEMENT_FILTERCRITERION,
    '__module__' : 'chromiumos.test_disablement_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.TestDisablement.FilterCriterion)
    })
  ,
  'DESCRIPTOR' : _TESTDISABLEMENT,
  '__module__' : 'chromiumos.test_disablement_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.TestDisablement)
  })
_sym_db.RegisterMessage(TestDisablement)
_sym_db.RegisterMessage(TestDisablement.FilterCriterion)

TestDisablementCfg = _reflection.GeneratedProtocolMessageType('TestDisablementCfg', (_message.Message,), {
  'DESCRIPTOR' : _TESTDISABLEMENTCFG,
  '__module__' : 'chromiumos.test_disablement_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.TestDisablementCfg)
  })
_sym_db.RegisterMessage(TestDisablementCfg)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
