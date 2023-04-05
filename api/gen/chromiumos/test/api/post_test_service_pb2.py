# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/post_test_service.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/test/api/post_test_service.proto',
  package='chromiumos.test.api',
  syntax='proto3',
  serialized_options=b'Z-go.chromium.org/chromiumos/config/go/test/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+chromiumos/test/api/post_test_service.proto\x12\x13\x63hromiumos.test.api\"\xb8\x01\n\x12RunActivityRequest\x12\x44\n\x13get_fw_info_request\x18\x01 \x01(\x0b\x32%.chromiumos.test.api.GetFWInfoRequestH\x00\x12Q\n\x1aget_files_from_dut_request\x18\x02 \x01(\x0b\x32+.chromiumos.test.api.GetFilesFromDUTRequestH\x00\x42\t\n\x07request\"\x12\n\x10GetFWInfoRequest\"\'\n\x16GetFilesFromDUTRequest\x12\r\n\x05\x66iles\x18\x01 \x03(\t\"\xbe\x01\n\x13RunActivityResponse\x12\x46\n\x14get_fw_info_response\x18\x01 \x01(\x0b\x32&.chromiumos.test.api.GetFWInfoResponseH\x00\x12S\n\x1bget_files_from_dut_response\x18\x02 \x01(\x0b\x32,.chromiumos.test.api.GetFilesFromDUTResponseH\x00\x42\n\n\x08response\"M\n\x11GetFWInfoResponse\x12\x0f\n\x07ro_fwid\x18\x01 \x01(\t\x12\x0f\n\x07rw_fwid\x18\x02 \x01(\t\x12\x16\n\x0ekernel_version\x18\x03 \x01(\t\"I\n\x17GetFilesFromDUTResponse\x12.\n\x08\x66ile_map\x18\x01 \x03(\x0b\x32\x1c.chromiumos.test.api.FileMap\"3\n\x07\x46ileMap\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x15\n\rfile_location\x18\x02 \x01(\t2s\n\x0fPostTestService\x12`\n\x0bRunActivity\x12\'.chromiumos.test.api.RunActivityRequest\x1a(.chromiumos.test.api.RunActivityResponseB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3'
)




_RUNACTIVITYREQUEST = _descriptor.Descriptor(
  name='RunActivityRequest',
  full_name='chromiumos.test.api.RunActivityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='get_fw_info_request', full_name='chromiumos.test.api.RunActivityRequest.get_fw_info_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_files_from_dut_request', full_name='chromiumos.test.api.RunActivityRequest.get_files_from_dut_request', index=1,
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
    _descriptor.OneofDescriptor(
      name='request', full_name='chromiumos.test.api.RunActivityRequest.request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=69,
  serialized_end=253,
)


_GETFWINFOREQUEST = _descriptor.Descriptor(
  name='GetFWInfoRequest',
  full_name='chromiumos.test.api.GetFWInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=255,
  serialized_end=273,
)


_GETFILESFROMDUTREQUEST = _descriptor.Descriptor(
  name='GetFilesFromDUTRequest',
  full_name='chromiumos.test.api.GetFilesFromDUTRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='chromiumos.test.api.GetFilesFromDUTRequest.files', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=275,
  serialized_end=314,
)


_RUNACTIVITYRESPONSE = _descriptor.Descriptor(
  name='RunActivityResponse',
  full_name='chromiumos.test.api.RunActivityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='get_fw_info_response', full_name='chromiumos.test.api.RunActivityResponse.get_fw_info_response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_files_from_dut_response', full_name='chromiumos.test.api.RunActivityResponse.get_files_from_dut_response', index=1,
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
    _descriptor.OneofDescriptor(
      name='response', full_name='chromiumos.test.api.RunActivityResponse.response',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=317,
  serialized_end=507,
)


_GETFWINFORESPONSE = _descriptor.Descriptor(
  name='GetFWInfoResponse',
  full_name='chromiumos.test.api.GetFWInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ro_fwid', full_name='chromiumos.test.api.GetFWInfoResponse.ro_fwid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rw_fwid', full_name='chromiumos.test.api.GetFWInfoResponse.rw_fwid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kernel_version', full_name='chromiumos.test.api.GetFWInfoResponse.kernel_version', index=2,
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
  serialized_start=509,
  serialized_end=586,
)


_GETFILESFROMDUTRESPONSE = _descriptor.Descriptor(
  name='GetFilesFromDUTResponse',
  full_name='chromiumos.test.api.GetFilesFromDUTResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_map', full_name='chromiumos.test.api.GetFilesFromDUTResponse.file_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=588,
  serialized_end=661,
)


_FILEMAP = _descriptor.Descriptor(
  name='FileMap',
  full_name='chromiumos.test.api.FileMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='chromiumos.test.api.FileMap.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_location', full_name='chromiumos.test.api.FileMap.file_location', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=663,
  serialized_end=714,
)

_RUNACTIVITYREQUEST.fields_by_name['get_fw_info_request'].message_type = _GETFWINFOREQUEST
_RUNACTIVITYREQUEST.fields_by_name['get_files_from_dut_request'].message_type = _GETFILESFROMDUTREQUEST
_RUNACTIVITYREQUEST.oneofs_by_name['request'].fields.append(
  _RUNACTIVITYREQUEST.fields_by_name['get_fw_info_request'])
_RUNACTIVITYREQUEST.fields_by_name['get_fw_info_request'].containing_oneof = _RUNACTIVITYREQUEST.oneofs_by_name['request']
_RUNACTIVITYREQUEST.oneofs_by_name['request'].fields.append(
  _RUNACTIVITYREQUEST.fields_by_name['get_files_from_dut_request'])
_RUNACTIVITYREQUEST.fields_by_name['get_files_from_dut_request'].containing_oneof = _RUNACTIVITYREQUEST.oneofs_by_name['request']
_RUNACTIVITYRESPONSE.fields_by_name['get_fw_info_response'].message_type = _GETFWINFORESPONSE
_RUNACTIVITYRESPONSE.fields_by_name['get_files_from_dut_response'].message_type = _GETFILESFROMDUTRESPONSE
_RUNACTIVITYRESPONSE.oneofs_by_name['response'].fields.append(
  _RUNACTIVITYRESPONSE.fields_by_name['get_fw_info_response'])
_RUNACTIVITYRESPONSE.fields_by_name['get_fw_info_response'].containing_oneof = _RUNACTIVITYRESPONSE.oneofs_by_name['response']
_RUNACTIVITYRESPONSE.oneofs_by_name['response'].fields.append(
  _RUNACTIVITYRESPONSE.fields_by_name['get_files_from_dut_response'])
_RUNACTIVITYRESPONSE.fields_by_name['get_files_from_dut_response'].containing_oneof = _RUNACTIVITYRESPONSE.oneofs_by_name['response']
_GETFILESFROMDUTRESPONSE.fields_by_name['file_map'].message_type = _FILEMAP
DESCRIPTOR.message_types_by_name['RunActivityRequest'] = _RUNACTIVITYREQUEST
DESCRIPTOR.message_types_by_name['GetFWInfoRequest'] = _GETFWINFOREQUEST
DESCRIPTOR.message_types_by_name['GetFilesFromDUTRequest'] = _GETFILESFROMDUTREQUEST
DESCRIPTOR.message_types_by_name['RunActivityResponse'] = _RUNACTIVITYRESPONSE
DESCRIPTOR.message_types_by_name['GetFWInfoResponse'] = _GETFWINFORESPONSE
DESCRIPTOR.message_types_by_name['GetFilesFromDUTResponse'] = _GETFILESFROMDUTRESPONSE
DESCRIPTOR.message_types_by_name['FileMap'] = _FILEMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunActivityRequest = _reflection.GeneratedProtocolMessageType('RunActivityRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNACTIVITYREQUEST,
  '__module__' : 'chromiumos.test.api.post_test_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.RunActivityRequest)
  })
_sym_db.RegisterMessage(RunActivityRequest)

GetFWInfoRequest = _reflection.GeneratedProtocolMessageType('GetFWInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFWINFOREQUEST,
  '__module__' : 'chromiumos.test.api.post_test_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.GetFWInfoRequest)
  })
_sym_db.RegisterMessage(GetFWInfoRequest)

GetFilesFromDUTRequest = _reflection.GeneratedProtocolMessageType('GetFilesFromDUTRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFILESFROMDUTREQUEST,
  '__module__' : 'chromiumos.test.api.post_test_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.GetFilesFromDUTRequest)
  })
_sym_db.RegisterMessage(GetFilesFromDUTRequest)

RunActivityResponse = _reflection.GeneratedProtocolMessageType('RunActivityResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNACTIVITYRESPONSE,
  '__module__' : 'chromiumos.test.api.post_test_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.RunActivityResponse)
  })
_sym_db.RegisterMessage(RunActivityResponse)

GetFWInfoResponse = _reflection.GeneratedProtocolMessageType('GetFWInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFWINFORESPONSE,
  '__module__' : 'chromiumos.test.api.post_test_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.GetFWInfoResponse)
  })
_sym_db.RegisterMessage(GetFWInfoResponse)

GetFilesFromDUTResponse = _reflection.GeneratedProtocolMessageType('GetFilesFromDUTResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFILESFROMDUTRESPONSE,
  '__module__' : 'chromiumos.test.api.post_test_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.GetFilesFromDUTResponse)
  })
_sym_db.RegisterMessage(GetFilesFromDUTResponse)

FileMap = _reflection.GeneratedProtocolMessageType('FileMap', (_message.Message,), {
  'DESCRIPTOR' : _FILEMAP,
  '__module__' : 'chromiumos.test.api.post_test_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.FileMap)
  })
_sym_db.RegisterMessage(FileMap)


DESCRIPTOR._options = None

_POSTTESTSERVICE = _descriptor.ServiceDescriptor(
  name='PostTestService',
  full_name='chromiumos.test.api.PostTestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=716,
  serialized_end=831,
  methods=[
  _descriptor.MethodDescriptor(
    name='RunActivity',
    full_name='chromiumos.test.api.PostTestService.RunActivity',
    index=0,
    containing_service=None,
    input_type=_RUNACTIVITYREQUEST,
    output_type=_RUNACTIVITYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_POSTTESTSERVICE)

DESCRIPTOR.services_by_name['PostTestService'] = _POSTTESTSERVICE

# @@protoc_insertion_point(module_scope)
