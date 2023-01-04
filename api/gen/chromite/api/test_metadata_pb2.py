# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/test_metadata.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen.chromite.api import sysroot_pb2 as chromite_dot_api_dot_sysroot__pb2
from chromite.api.gen.chromiumos import common_pb2 as chromiumos_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromite/api/test_metadata.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n chromite/api/test_metadata.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x1a\x63hromite/api/sysroot.proto\x1a\x17\x63hromiumos/common.proto\"a\n\x13TestMetadataRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\x12&\n\x07sysroot\x18\x02 \x01(\x0b\x32\x15.chromite.api.Sysroot\"L\n\x14TestMetadataResponse\x12\x34\n\x08\x61utotest\x18\x01 \x01(\x0b\x32\".chromite.api.AutotestTestMetadata\"n\n\x14\x41utotestTestMetadata\x12+\n\x06suites\x18\x01 \x03(\x0b\x32\x1b.chromite.api.AutotestSuite\x12)\n\x05tests\x18\x02 \x03(\x0b\x32\x1a.chromite.api.AutotestTest\"\xd8\x01\n\rAutotestSuite\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x12\x63hild_dependencies\x18\x02 \x03(\x0b\x32$.chromite.api.AutotestTaskDependency\x12\x1e\n\x16\x63hild_task_timeout_sec\x18\x03 \x01(\x05\x12\x38\n\x05tests\x18\x04 \x03(\x0b\x32).chromite.api.AutotestSuite.TestReference\x1a\x1d\n\rTestReference\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x97\x03\n\x0c\x41utotestTest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\x0c\x64\x65pendencies\x18\x02 \x03(\x0b\x32$.chromite.api.AutotestTaskDependency\x12\x15\n\rallow_retries\x18\x03 \x01(\x08\x12\x13\n\x0bmax_retries\x18\x04 \x01(\x05\x12\x1b\n\x13needs_multiple_duts\x18\x05 \x01(\x08\x12\x11\n\tdut_count\x18\x06 \x01(\x05\x12N\n\x15\x65xecution_environment\x18\x07 \x01(\x0e\x32/.chromite.api.AutotestTest.ExecutionEnvironment\x12\r\n\x05names\x18\x08 \x03(\t\"\x81\x01\n\x14\x45xecutionEnvironment\x12%\n!EXECUTION_ENVIRONMENT_UNSPECIFIED\x10\x00\x12 \n\x1c\x45XECUTION_ENVIRONMENT_CLIENT\x10\x01\x12 \n\x1c\x45XECUTION_ENVIRONMENT_SERVER\x10\x02\"\'\n\x16\x41utotestTaskDependency\x12\r\n\x05label\x18\x01 \x01(\t2z\n\x13TestMetadataService\x12L\n\x03Get\x12!.chromite.api.TestMetadataRequest\x1a\".chromite.api.TestMetadataResponse\x1a\x15\xc2\xed\x1a\x11\n\rtest_metadata\x10\x01\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3'
  ,
  dependencies=[chromite_dot_api_dot_build__api__pb2.DESCRIPTOR,chromite_dot_api_dot_sysroot__pb2.DESCRIPTOR,chromiumos_dot_common__pb2.DESCRIPTOR,])



_AUTOTESTTEST_EXECUTIONENVIRONMENT = _descriptor.EnumDescriptor(
  name='ExecutionEnvironment',
  full_name='chromite.api.AutotestTest.ExecutionEnvironment',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXECUTION_ENVIRONMENT_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXECUTION_ENVIRONMENT_CLIENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXECUTION_ENVIRONMENT_SERVER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=920,
  serialized_end=1049,
)
_sym_db.RegisterEnumDescriptor(_AUTOTESTTEST_EXECUTIONENVIRONMENT)


_TESTMETADATAREQUEST = _descriptor.Descriptor(
  name='TestMetadataRequest',
  full_name='chromite.api.TestMetadataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.TestMetadataRequest.chroot', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sysroot', full_name='chromite.api.TestMetadataRequest.sysroot', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=133,
  serialized_end=230,
)


_TESTMETADATARESPONSE = _descriptor.Descriptor(
  name='TestMetadataResponse',
  full_name='chromite.api.TestMetadataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='autotest', full_name='chromite.api.TestMetadataResponse.autotest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=232,
  serialized_end=308,
)


_AUTOTESTTESTMETADATA = _descriptor.Descriptor(
  name='AutotestTestMetadata',
  full_name='chromite.api.AutotestTestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='suites', full_name='chromite.api.AutotestTestMetadata.suites', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tests', full_name='chromite.api.AutotestTestMetadata.tests', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=310,
  serialized_end=420,
)


_AUTOTESTSUITE_TESTREFERENCE = _descriptor.Descriptor(
  name='TestReference',
  full_name='chromite.api.AutotestSuite.TestReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromite.api.AutotestSuite.TestReference.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=610,
  serialized_end=639,
)

_AUTOTESTSUITE = _descriptor.Descriptor(
  name='AutotestSuite',
  full_name='chromite.api.AutotestSuite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromite.api.AutotestSuite.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='child_dependencies', full_name='chromite.api.AutotestSuite.child_dependencies', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='child_task_timeout_sec', full_name='chromite.api.AutotestSuite.child_task_timeout_sec', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tests', full_name='chromite.api.AutotestSuite.tests', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_AUTOTESTSUITE_TESTREFERENCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=639,
)


_AUTOTESTTEST = _descriptor.Descriptor(
  name='AutotestTest',
  full_name='chromite.api.AutotestTest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromite.api.AutotestTest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='chromite.api.AutotestTest.dependencies', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_retries', full_name='chromite.api.AutotestTest.allow_retries', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_retries', full_name='chromite.api.AutotestTest.max_retries', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='needs_multiple_duts', full_name='chromite.api.AutotestTest.needs_multiple_duts', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dut_count', full_name='chromite.api.AutotestTest.dut_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='execution_environment', full_name='chromite.api.AutotestTest.execution_environment', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='names', full_name='chromite.api.AutotestTest.names', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUTOTESTTEST_EXECUTIONENVIRONMENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=642,
  serialized_end=1049,
)


_AUTOTESTTASKDEPENDENCY = _descriptor.Descriptor(
  name='AutotestTaskDependency',
  full_name='chromite.api.AutotestTaskDependency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='chromite.api.AutotestTaskDependency.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1051,
  serialized_end=1090,
)

_TESTMETADATAREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_TESTMETADATAREQUEST.fields_by_name['sysroot'].message_type = chromite_dot_api_dot_sysroot__pb2._SYSROOT
_TESTMETADATARESPONSE.fields_by_name['autotest'].message_type = _AUTOTESTTESTMETADATA
_AUTOTESTTESTMETADATA.fields_by_name['suites'].message_type = _AUTOTESTSUITE
_AUTOTESTTESTMETADATA.fields_by_name['tests'].message_type = _AUTOTESTTEST
_AUTOTESTSUITE_TESTREFERENCE.containing_type = _AUTOTESTSUITE
_AUTOTESTSUITE.fields_by_name['child_dependencies'].message_type = _AUTOTESTTASKDEPENDENCY
_AUTOTESTSUITE.fields_by_name['tests'].message_type = _AUTOTESTSUITE_TESTREFERENCE
_AUTOTESTTEST.fields_by_name['dependencies'].message_type = _AUTOTESTTASKDEPENDENCY
_AUTOTESTTEST.fields_by_name['execution_environment'].enum_type = _AUTOTESTTEST_EXECUTIONENVIRONMENT
_AUTOTESTTEST_EXECUTIONENVIRONMENT.containing_type = _AUTOTESTTEST
DESCRIPTOR.message_types_by_name['TestMetadataRequest'] = _TESTMETADATAREQUEST
DESCRIPTOR.message_types_by_name['TestMetadataResponse'] = _TESTMETADATARESPONSE
DESCRIPTOR.message_types_by_name['AutotestTestMetadata'] = _AUTOTESTTESTMETADATA
DESCRIPTOR.message_types_by_name['AutotestSuite'] = _AUTOTESTSUITE
DESCRIPTOR.message_types_by_name['AutotestTest'] = _AUTOTESTTEST
DESCRIPTOR.message_types_by_name['AutotestTaskDependency'] = _AUTOTESTTASKDEPENDENCY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestMetadataRequest = _reflection.GeneratedProtocolMessageType('TestMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTMETADATAREQUEST,
  '__module__' : 'chromite.api.test_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.TestMetadataRequest)
  })
_sym_db.RegisterMessage(TestMetadataRequest)

TestMetadataResponse = _reflection.GeneratedProtocolMessageType('TestMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTMETADATARESPONSE,
  '__module__' : 'chromite.api.test_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.TestMetadataResponse)
  })
_sym_db.RegisterMessage(TestMetadataResponse)

AutotestTestMetadata = _reflection.GeneratedProtocolMessageType('AutotestTestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _AUTOTESTTESTMETADATA,
  '__module__' : 'chromite.api.test_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.AutotestTestMetadata)
  })
_sym_db.RegisterMessage(AutotestTestMetadata)

AutotestSuite = _reflection.GeneratedProtocolMessageType('AutotestSuite', (_message.Message,), {

  'TestReference' : _reflection.GeneratedProtocolMessageType('TestReference', (_message.Message,), {
    'DESCRIPTOR' : _AUTOTESTSUITE_TESTREFERENCE,
    '__module__' : 'chromite.api.test_metadata_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.AutotestSuite.TestReference)
    })
  ,
  'DESCRIPTOR' : _AUTOTESTSUITE,
  '__module__' : 'chromite.api.test_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.AutotestSuite)
  })
_sym_db.RegisterMessage(AutotestSuite)
_sym_db.RegisterMessage(AutotestSuite.TestReference)

AutotestTest = _reflection.GeneratedProtocolMessageType('AutotestTest', (_message.Message,), {
  'DESCRIPTOR' : _AUTOTESTTEST,
  '__module__' : 'chromite.api.test_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.AutotestTest)
  })
_sym_db.RegisterMessage(AutotestTest)

AutotestTaskDependency = _reflection.GeneratedProtocolMessageType('AutotestTaskDependency', (_message.Message,), {
  'DESCRIPTOR' : _AUTOTESTTASKDEPENDENCY,
  '__module__' : 'chromite.api.test_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.AutotestTaskDependency)
  })
_sym_db.RegisterMessage(AutotestTaskDependency)


DESCRIPTOR._options = None

_TESTMETADATASERVICE = _descriptor.ServiceDescriptor(
  name='TestMetadataService',
  full_name='chromite.api.TestMetadataService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\302\355\032\021\n\rtest_metadata\020\001',
  create_key=_descriptor._internal_create_key,
  serialized_start=1092,
  serialized_end=1214,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='chromite.api.TestMetadataService.Get',
    index=0,
    containing_service=None,
    input_type=_TESTMETADATAREQUEST,
    output_type=_TESTMETADATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTMETADATASERVICE)

DESCRIPTOR.services_by_name['TestMetadataService'] = _TESTMETADATASERVICE

# @@protoc_insertion_point(module_scope)
