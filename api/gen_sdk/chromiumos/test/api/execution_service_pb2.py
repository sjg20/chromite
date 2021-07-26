# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/execution_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.longrunning import operations_pb2 as chromiumos_dot_longrunning_dot_operations__pb2
from chromite.api.gen_sdk.chromiumos.test.api import test_case_result_pb2 as chromiumos_dot_test_dot_api_dot_test__case__result__pb2
from chromite.api.gen_sdk.chromiumos.test.api import test_suite_pb2 as chromiumos_dot_test_dot_api_dot_test__suite__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/test/api/execution_service.proto',
  package='chromiumos.test.api',
  syntax='proto3',
  serialized_options=b'Z-go.chromium.org/chromiumos/config/go/test/api',
  serialized_pb=b'\n+chromiumos/test/api/execution_service.proto\x12\x13\x63hromiumos.test.api\x1a\'chromiumos/longrunning/operations.proto\x1a*chromiumos/test/api/test_case_result.proto\x1a$chromiumos/test/api/test_suite.proto\"t\n\x0fRunTestsRequest\x12\x33\n\x0btest_suites\x18\x01 \x03(\x0b\x32\x1e.chromiumos.test.api.TestSuite\x12,\n\x03\x64ut\x18\x02 \x01(\x0b\x32\x1f.chromiumos.test.api.DeviceInfo\"^\n\nDeviceInfo\x12\x14\n\x0cprimary_host\x18\x01 \x01(\t\x12:\n\ncompanions\x18\x02 \x03(\x0b\x32&.chromiumos.test.api.CompanionHostInfo\"!\n\x11\x43ompanionHostInfo\x12\x0c\n\x04host\x18\x01 \x01(\t\"R\n\x10RunTestsResponse\x12>\n\x11test_case_results\x18\x01 \x03(\x0b\x32#.chromiumos.test.api.TestCaseResult\"\x12\n\x10RunTestsMetadata2\x90\x01\n\x10\x45xecutionService\x12|\n\x08RunTests\x12$.chromiumos.test.api.RunTestsRequest\x1a!.chromiumos.longrunning.Operation\"\'\xd2\x41$\n\x10RunTestsResponse\x12\x10RunTestsMetadataB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3'
  ,
  dependencies=[chromiumos_dot_longrunning_dot_operations__pb2.DESCRIPTOR,chromiumos_dot_test_dot_api_dot_test__case__result__pb2.DESCRIPTOR,chromiumos_dot_test_dot_api_dot_test__suite__pb2.DESCRIPTOR,])




_RUNTESTSREQUEST = _descriptor.Descriptor(
  name='RunTestsRequest',
  full_name='chromiumos.test.api.RunTestsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_suites', full_name='chromiumos.test.api.RunTestsRequest.test_suites', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dut', full_name='chromiumos.test.api.RunTestsRequest.dut', index=1,
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
  serialized_start=191,
  serialized_end=307,
)


_DEVICEINFO = _descriptor.Descriptor(
  name='DeviceInfo',
  full_name='chromiumos.test.api.DeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='primary_host', full_name='chromiumos.test.api.DeviceInfo.primary_host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='companions', full_name='chromiumos.test.api.DeviceInfo.companions', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=309,
  serialized_end=403,
)


_COMPANIONHOSTINFO = _descriptor.Descriptor(
  name='CompanionHostInfo',
  full_name='chromiumos.test.api.CompanionHostInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='chromiumos.test.api.CompanionHostInfo.host', index=0,
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
  serialized_start=405,
  serialized_end=438,
)


_RUNTESTSRESPONSE = _descriptor.Descriptor(
  name='RunTestsResponse',
  full_name='chromiumos.test.api.RunTestsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_case_results', full_name='chromiumos.test.api.RunTestsResponse.test_case_results', index=0,
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
  serialized_start=440,
  serialized_end=522,
)


_RUNTESTSMETADATA = _descriptor.Descriptor(
  name='RunTestsMetadata',
  full_name='chromiumos.test.api.RunTestsMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=524,
  serialized_end=542,
)

_RUNTESTSREQUEST.fields_by_name['test_suites'].message_type = chromiumos_dot_test_dot_api_dot_test__suite__pb2._TESTSUITE
_RUNTESTSREQUEST.fields_by_name['dut'].message_type = _DEVICEINFO
_DEVICEINFO.fields_by_name['companions'].message_type = _COMPANIONHOSTINFO
_RUNTESTSRESPONSE.fields_by_name['test_case_results'].message_type = chromiumos_dot_test_dot_api_dot_test__case__result__pb2._TESTCASERESULT
DESCRIPTOR.message_types_by_name['RunTestsRequest'] = _RUNTESTSREQUEST
DESCRIPTOR.message_types_by_name['DeviceInfo'] = _DEVICEINFO
DESCRIPTOR.message_types_by_name['CompanionHostInfo'] = _COMPANIONHOSTINFO
DESCRIPTOR.message_types_by_name['RunTestsResponse'] = _RUNTESTSRESPONSE
DESCRIPTOR.message_types_by_name['RunTestsMetadata'] = _RUNTESTSMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunTestsRequest = _reflection.GeneratedProtocolMessageType('RunTestsRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNTESTSREQUEST,
  '__module__' : 'chromiumos.test.api.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.RunTestsRequest)
  })
_sym_db.RegisterMessage(RunTestsRequest)

DeviceInfo = _reflection.GeneratedProtocolMessageType('DeviceInfo', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEINFO,
  '__module__' : 'chromiumos.test.api.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.DeviceInfo)
  })
_sym_db.RegisterMessage(DeviceInfo)

CompanionHostInfo = _reflection.GeneratedProtocolMessageType('CompanionHostInfo', (_message.Message,), {
  'DESCRIPTOR' : _COMPANIONHOSTINFO,
  '__module__' : 'chromiumos.test.api.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.CompanionHostInfo)
  })
_sym_db.RegisterMessage(CompanionHostInfo)

RunTestsResponse = _reflection.GeneratedProtocolMessageType('RunTestsResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNTESTSRESPONSE,
  '__module__' : 'chromiumos.test.api.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.RunTestsResponse)
  })
_sym_db.RegisterMessage(RunTestsResponse)

RunTestsMetadata = _reflection.GeneratedProtocolMessageType('RunTestsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _RUNTESTSMETADATA,
  '__module__' : 'chromiumos.test.api.execution_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.RunTestsMetadata)
  })
_sym_db.RegisterMessage(RunTestsMetadata)


DESCRIPTOR._options = None

_EXECUTIONSERVICE = _descriptor.ServiceDescriptor(
  name='ExecutionService',
  full_name='chromiumos.test.api.ExecutionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=545,
  serialized_end=689,
  methods=[
  _descriptor.MethodDescriptor(
    name='RunTests',
    full_name='chromiumos.test.api.ExecutionService.RunTests',
    index=0,
    containing_service=None,
    input_type=_RUNTESTSREQUEST,
    output_type=chromiumos_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\322A$\n\020RunTestsResponse\022\020RunTestsMetadata',
  ),
])
_sym_db.RegisterServiceDescriptor(_EXECUTIONSERVICE)

DESCRIPTOR.services_by_name['ExecutionService'] = _EXECUTIONSERVICE

# @@protoc_insertion_point(module_scope)
