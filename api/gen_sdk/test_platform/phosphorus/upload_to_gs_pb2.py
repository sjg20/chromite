# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/phosphorus/upload_to_gs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.test_platform.phosphorus import common_pb2 as test__platform_dot_phosphorus_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/phosphorus/upload_to_gs.proto',
  package='test_platform.phosphorus',
  syntax='proto3',
  serialized_options=_b('ZBgo.chromium.org/chromiumos/infra/proto/go/test_platform/phosphorus'),
  serialized_pb=_b('\n+test_platform/phosphorus/upload_to_gs.proto\x12\x18test_platform.phosphorus\x1a%test_platform/phosphorus/common.proto\"~\n\x11UploadToGSRequest\x12\x34\n\x06\x63onfig\x18\x01 \x01(\x0b\x32 .test_platform.phosphorus.ConfigB\x02\x18\x01\x12\x14\n\x0cgs_directory\x18\x02 \x01(\t\x12\x17\n\x0flocal_directory\x18\x04 \x01(\tJ\x04\x08\x03\x10\x04\"$\n\x12UploadToGSResponse\x12\x0e\n\x06gs_url\x18\x01 \x01(\tBDZBgo.chromium.org/chromiumos/infra/proto/go/test_platform/phosphorusb\x06proto3')
  ,
  dependencies=[test__platform_dot_phosphorus_dot_common__pb2.DESCRIPTOR,])




_UPLOADTOGSREQUEST = _descriptor.Descriptor(
  name='UploadToGSRequest',
  full_name='test_platform.phosphorus.UploadToGSRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='test_platform.phosphorus.UploadToGSRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gs_directory', full_name='test_platform.phosphorus.UploadToGSRequest.gs_directory', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_directory', full_name='test_platform.phosphorus.UploadToGSRequest.local_directory', index=2,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=112,
  serialized_end=238,
)


_UPLOADTOGSRESPONSE = _descriptor.Descriptor(
  name='UploadToGSResponse',
  full_name='test_platform.phosphorus.UploadToGSResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gs_url', full_name='test_platform.phosphorus.UploadToGSResponse.gs_url', index=0,
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
  serialized_start=240,
  serialized_end=276,
)

_UPLOADTOGSREQUEST.fields_by_name['config'].message_type = test__platform_dot_phosphorus_dot_common__pb2._CONFIG
DESCRIPTOR.message_types_by_name['UploadToGSRequest'] = _UPLOADTOGSREQUEST
DESCRIPTOR.message_types_by_name['UploadToGSResponse'] = _UPLOADTOGSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadToGSRequest = _reflection.GeneratedProtocolMessageType('UploadToGSRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADTOGSREQUEST,
  __module__ = 'test_platform.phosphorus.upload_to_gs_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.phosphorus.UploadToGSRequest)
  ))
_sym_db.RegisterMessage(UploadToGSRequest)

UploadToGSResponse = _reflection.GeneratedProtocolMessageType('UploadToGSResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADTOGSRESPONSE,
  __module__ = 'test_platform.phosphorus.upload_to_gs_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.phosphorus.UploadToGSResponse)
  ))
_sym_db.RegisterMessage(UploadToGSResponse)


DESCRIPTOR._options = None
_UPLOADTOGSREQUEST.fields_by_name['config']._options = None
# @@protoc_insertion_point(module_scope)
