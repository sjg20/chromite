# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/build_api_test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen.chromiumos import common_pb2 as chromiumos_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromite/api/build_api_test.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=_b('Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api'),
  serialized_pb=_b('\n!chromite/api/build_api_test.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x17\x63hromiumos/common.proto\"\xfc\x01\n\x12TestRequestMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x06\x63hroot\x18\x02 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\x1e\n\x04path\x18\x03 \x01(\x0b\x32\x10.chromiumos.Path\x12&\n\x0c\x61nother_path\x18\x04 \x01(\x0b\x32\x10.chromiumos.Path\x12@\n\x0bnested_path\x18\x05 \x01(\x0b\x32+.chromite.api.TestRequestMessage.NestedPath\x1a,\n\nNestedPath\x12\x1e\n\x04path\x18\x01 \x01(\x0b\x32\x10.chromiumos.Path\"#\n\x11TestResultMessage\x12\x0e\n\x06result\x18\x01 \x01(\t2\xe5\x01\n\x0eTestApiService\x12V\n\x11InputOutputMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\x12\x65\n\rRenamedMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\"\x11\xc2\xed\x1a\r\n\x0b\x43orrectName\x1a\x14\xc2\xed\x1a\x10\n\x0e\x62uild_api_test2\xf9\x01\n\x16InsideChrootApiService\x12^\n\x19InsideServiceInsideMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\x12g\n\x1aInsideServiceOutsideMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\"\x06\xc2\xed\x1a\x02\x10\x02\x1a\x16\xc2\xed\x1a\x12\n\x0e\x62uild_api_test\x10\x01\x32\xfc\x01\n\x17OutsideChrootApiService\x12`\n\x1bOutsideServiceOutsideMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\x12g\n\x1aOutsideServiceInsideMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\"\x06\xc2\xed\x1a\x02\x10\x01\x1a\x16\xc2\xed\x1a\x12\n\x0e\x62uild_api_test\x10\x02\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3')
  ,
  dependencies=[chromite_dot_api_dot_build__api__pb2.DESCRIPTOR,chromiumos_dot_common__pb2.DESCRIPTOR,])




_TESTREQUESTMESSAGE_NESTEDPATH = _descriptor.Descriptor(
  name='NestedPath',
  full_name='chromite.api.TestRequestMessage.NestedPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='chromite.api.TestRequestMessage.NestedPath.path', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=315,
  serialized_end=359,
)

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
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.TestRequestMessage.chroot', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='chromite.api.TestRequestMessage.path', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='another_path', full_name='chromite.api.TestRequestMessage.another_path', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nested_path', full_name='chromite.api.TestRequestMessage.nested_path', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TESTREQUESTMESSAGE_NESTEDPATH, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=359,
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
  serialized_start=361,
  serialized_end=396,
)

_TESTREQUESTMESSAGE_NESTEDPATH.fields_by_name['path'].message_type = chromiumos_dot_common__pb2._PATH
_TESTREQUESTMESSAGE_NESTEDPATH.containing_type = _TESTREQUESTMESSAGE
_TESTREQUESTMESSAGE.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_TESTREQUESTMESSAGE.fields_by_name['path'].message_type = chromiumos_dot_common__pb2._PATH
_TESTREQUESTMESSAGE.fields_by_name['another_path'].message_type = chromiumos_dot_common__pb2._PATH
_TESTREQUESTMESSAGE.fields_by_name['nested_path'].message_type = _TESTREQUESTMESSAGE_NESTEDPATH
DESCRIPTOR.message_types_by_name['TestRequestMessage'] = _TESTREQUESTMESSAGE
DESCRIPTOR.message_types_by_name['TestResultMessage'] = _TESTRESULTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestRequestMessage = _reflection.GeneratedProtocolMessageType('TestRequestMessage', (_message.Message,), dict(

  NestedPath = _reflection.GeneratedProtocolMessageType('NestedPath', (_message.Message,), dict(
    DESCRIPTOR = _TESTREQUESTMESSAGE_NESTEDPATH,
    __module__ = 'chromite.api.build_api_test_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.TestRequestMessage.NestedPath)
    ))
  ,
  DESCRIPTOR = _TESTREQUESTMESSAGE,
  __module__ = 'chromite.api.build_api_test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.TestRequestMessage)
  ))
_sym_db.RegisterMessage(TestRequestMessage)
_sym_db.RegisterMessage(TestRequestMessage.NestedPath)

TestResultMessage = _reflection.GeneratedProtocolMessageType('TestResultMessage', (_message.Message,), dict(
  DESCRIPTOR = _TESTRESULTMESSAGE,
  __module__ = 'chromite.api.build_api_test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.TestResultMessage)
  ))
_sym_db.RegisterMessage(TestResultMessage)


DESCRIPTOR._options = None

_TESTAPISERVICE = _descriptor.ServiceDescriptor(
  name='TestApiService',
  full_name='chromite.api.TestApiService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\302\355\032\020\n\016build_api_test'),
  serialized_start=399,
  serialized_end=628,
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
    name='RenamedMethod',
    full_name='chromite.api.TestApiService.RenamedMethod',
    index=1,
    containing_service=None,
    input_type=_TESTREQUESTMESSAGE,
    output_type=_TESTRESULTMESSAGE,
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
  serialized_start=631,
  serialized_end=880,
  methods=[
  _descriptor.MethodDescriptor(
    name='InsideServiceInsideMethod',
    full_name='chromite.api.InsideChrootApiService.InsideServiceInsideMethod',
    index=0,
    containing_service=None,
    input_type=_TESTREQUESTMESSAGE,
    output_type=_TESTRESULTMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InsideServiceOutsideMethod',
    full_name='chromite.api.InsideChrootApiService.InsideServiceOutsideMethod',
    index=1,
    containing_service=None,
    input_type=_TESTREQUESTMESSAGE,
    output_type=_TESTRESULTMESSAGE,
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
  serialized_start=883,
  serialized_end=1135,
  methods=[
  _descriptor.MethodDescriptor(
    name='OutsideServiceOutsideMethod',
    full_name='chromite.api.OutsideChrootApiService.OutsideServiceOutsideMethod',
    index=0,
    containing_service=None,
    input_type=_TESTREQUESTMESSAGE,
    output_type=_TESTRESULTMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='OutsideServiceInsideMethod',
    full_name='chromite.api.OutsideChrootApiService.OutsideServiceInsideMethod',
    index=1,
    containing_service=None,
    input_type=_TESTREQUESTMESSAGE,
    output_type=_TESTRESULTMESSAGE,
    serialized_options=_b('\302\355\032\002\020\001'),
  ),
])
_sym_db.RegisterServiceDescriptor(_OUTSIDECHROOTAPISERVICE)

DESCRIPTOR.services_by_name['OutsideChrootApiService'] = _OUTSIDECHROOTAPISERVICE

# @@protoc_insertion_point(module_scope)
