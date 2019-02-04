# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: build_api_test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import build_api_pb2 as build__api__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='build_api_test.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x62uild_api_test.proto\x12\x0c\x63hromite.api\x1a\x0f\x62uild_api.proto\x1a\x1bgoogle/protobuf/empty.proto\" \n\x12TestRequestMessage\x12\n\n\x02id\x18\x01 \x01(\t\"#\n\x11TestResultMessage\x12\x0e\n\x06result\x18\x01 \x01(\t2\xa2\x03\n\x0eTestApiService\x12V\n\x11InputOutputMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\x12G\n\x0bInputMethod\x12 .chromite.api.TestRequestMessage\x1a\x16.google.protobuf.Empty\x12G\n\x0cOutputMethod\x12\x16.google.protobuf.Empty\x1a\x1f.chromite.api.TestResultMessage\x12<\n\nNoIoMethod\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12R\n\rRenamedMethod\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x11\xc2\xed\x1a\r\n\x0b\x43orrectName\x1a\x14\xc2\xed\x1a\x10\n\x0e\x62uild_api_test2\xd3\x01\n\x16InsideChrootApiService\x12K\n\x19InsideServiceInsideMethod\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12T\n\x1aInsideServiceOutsideMethod\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x06\xc2\xed\x1a\x02\x10\x02\x1a\x16\xc2\xed\x1a\x12\n\x0e\x62uild_api_test\x10\x01\x32\xd6\x01\n\x17OutsideChrootApiService\x12M\n\x1bOutsideServiceOutsideMethod\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12T\n\x1aOutsideServiceInsideMethod\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x06\xc2\xed\x1a\x02\x10\x01\x1a\x16\xc2\xed\x1a\x12\n\x0e\x62uild_api_test\x10\x02\x62\x06proto3')
  ,
  dependencies=[build__api__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_TESTREQUESTMESSAGE = _descriptor.Descriptor(
  name='TestRequestMessage',
  full_name='chromite.api.TestRequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chromite.api.TestRequestMessage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=84,
  serialized_end=116,
)


_TESTRESULTMESSAGE = _descriptor.Descriptor(
  name='TestResultMessage',
  full_name='chromite.api.TestResultMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='chromite.api.TestResultMessage.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=118,
  serialized_end=153,
)

DESCRIPTOR.message_types_by_name['TestRequestMessage'] = _TESTREQUESTMESSAGE
DESCRIPTOR.message_types_by_name['TestResultMessage'] = _TESTRESULTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestRequestMessage = _reflection.GeneratedProtocolMessageType('TestRequestMessage', (_message.Message,), dict(
  DESCRIPTOR = _TESTREQUESTMESSAGE,
  __module__ = 'build_api_test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.TestRequestMessage)
  ))
_sym_db.RegisterMessage(TestRequestMessage)

TestResultMessage = _reflection.GeneratedProtocolMessageType('TestResultMessage', (_message.Message,), dict(
  DESCRIPTOR = _TESTRESULTMESSAGE,
  __module__ = 'build_api_test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.TestResultMessage)
  ))
_sym_db.RegisterMessage(TestResultMessage)



_TESTAPISERVICE = _descriptor.ServiceDescriptor(
  name='TestApiService',
  full_name='chromite.api.TestApiService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\302\355\032\020\n\016build_api_test'),
  serialized_start=156,
  serialized_end=574,
  methods=[
  _descriptor.MethodDescriptor(
    name='InputOutputMethod',
    full_name='chromite.api.TestApiService.InputOutputMethod',
    index=0,
    containing_service=None,
    input_type=_TESTREQUESTMESSAGE,
    output_type=_TESTRESULTMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InputMethod',
    full_name='chromite.api.TestApiService.InputMethod',
    index=1,
    containing_service=None,
    input_type=_TESTREQUESTMESSAGE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='OutputMethod',
    full_name='chromite.api.TestApiService.OutputMethod',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_TESTRESULTMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NoIoMethod',
    full_name='chromite.api.TestApiService.NoIoMethod',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RenamedMethod',
    full_name='chromite.api.TestApiService.RenamedMethod',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\302\355\032\r\n\013CorrectName'),
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTAPISERVICE)

DESCRIPTOR.services_by_name['TestApiService'] = _TESTAPISERVICE


_INSIDECHROOTAPISERVICE = _descriptor.ServiceDescriptor(
  name='InsideChrootApiService',
  full_name='chromite.api.InsideChrootApiService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=_b('\302\355\032\022\n\016build_api_test\020\001'),
  serialized_start=577,
  serialized_end=788,
  methods=[
  _descriptor.MethodDescriptor(
    name='InsideServiceInsideMethod',
    full_name='chromite.api.InsideChrootApiService.InsideServiceInsideMethod',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InsideServiceOutsideMethod',
    full_name='chromite.api.InsideChrootApiService.InsideServiceOutsideMethod',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\302\355\032\002\020\002'),
  ),
])
_sym_db.RegisterServiceDescriptor(_INSIDECHROOTAPISERVICE)

DESCRIPTOR.services_by_name['InsideChrootApiService'] = _INSIDECHROOTAPISERVICE


_OUTSIDECHROOTAPISERVICE = _descriptor.ServiceDescriptor(
  name='OutsideChrootApiService',
  full_name='chromite.api.OutsideChrootApiService',
  file=DESCRIPTOR,
  index=2,
  serialized_options=_b('\302\355\032\022\n\016build_api_test\020\002'),
  serialized_start=791,
  serialized_end=1005,
  methods=[
  _descriptor.MethodDescriptor(
    name='OutsideServiceOutsideMethod',
    full_name='chromite.api.OutsideChrootApiService.OutsideServiceOutsideMethod',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='OutsideServiceInsideMethod',
    full_name='chromite.api.OutsideChrootApiService.OutsideServiceInsideMethod',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\302\355\032\002\020\001'),
  ),
])
_sym_db.RegisterServiceDescriptor(_OUTSIDECHROOTAPISERVICE)

DESCRIPTOR.services_by_name['OutsideChrootApiService'] = _OUTSIDECHROOTAPISERVICE

# @@protoc_insertion_point(module_scope)
