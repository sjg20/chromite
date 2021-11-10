# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/metadata.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen_sdk.chromiumos import common_pb2 as chromiumos_dot_common__pb2
from chromite.api.gen_sdk.chromiumos.build.api import system_image_pb2 as chromiumos_dot_build_dot_api_dot_system__image__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromite/api/metadata.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api',
  serialized_pb=b'\n\x1b\x63hromite/api/metadata.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x17\x63hromiumos/common.proto\x1a\'chromiumos/build/api/system_image.proto\"@\n\x1aSystemImageMetadataRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\"V\n\x1bSystemImageMetadataResponse\x12\x37\n\x0csystem_image\x18\x01 \x01(\x0b\x32!.chromiumos.build.api.SystemImage2\x91\x01\n\x0fMetadataService\x12j\n\x13SystemImageMetadata\x12(.chromite.api.SystemImageMetadataRequest\x1a).chromite.api.SystemImageMetadataResponse\x1a\x12\xc2\xed\x1a\x0e\n\x08metadata\x10\x01\x18\x02\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3'
  ,
  dependencies=[chromite_dot_api_dot_build__api__pb2.DESCRIPTOR,chromiumos_dot_common__pb2.DESCRIPTOR,chromiumos_dot_build_dot_api_dot_system__image__pb2.DESCRIPTOR,])




_SYSTEMIMAGEMETADATAREQUEST = _descriptor.Descriptor(
  name='SystemImageMetadataRequest',
  full_name='chromite.api.SystemImageMetadataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.SystemImageMetadataRequest.chroot', index=0,
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
  serialized_start=141,
  serialized_end=205,
)


_SYSTEMIMAGEMETADATARESPONSE = _descriptor.Descriptor(
  name='SystemImageMetadataResponse',
  full_name='chromite.api.SystemImageMetadataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='system_image', full_name='chromite.api.SystemImageMetadataResponse.system_image', index=0,
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
  serialized_start=207,
  serialized_end=293,
)

_SYSTEMIMAGEMETADATAREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_SYSTEMIMAGEMETADATARESPONSE.fields_by_name['system_image'].message_type = chromiumos_dot_build_dot_api_dot_system__image__pb2._SYSTEMIMAGE
DESCRIPTOR.message_types_by_name['SystemImageMetadataRequest'] = _SYSTEMIMAGEMETADATAREQUEST
DESCRIPTOR.message_types_by_name['SystemImageMetadataResponse'] = _SYSTEMIMAGEMETADATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SystemImageMetadataRequest = _reflection.GeneratedProtocolMessageType('SystemImageMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMIMAGEMETADATAREQUEST,
  '__module__' : 'chromite.api.metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SystemImageMetadataRequest)
  })
_sym_db.RegisterMessage(SystemImageMetadataRequest)

SystemImageMetadataResponse = _reflection.GeneratedProtocolMessageType('SystemImageMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMIMAGEMETADATARESPONSE,
  '__module__' : 'chromite.api.metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SystemImageMetadataResponse)
  })
_sym_db.RegisterMessage(SystemImageMetadataResponse)


DESCRIPTOR._options = None

_METADATASERVICE = _descriptor.ServiceDescriptor(
  name='MetadataService',
  full_name='chromite.api.MetadataService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\302\355\032\016\n\010metadata\020\001\030\002',
  serialized_start=296,
  serialized_end=441,
  methods=[
  _descriptor.MethodDescriptor(
    name='SystemImageMetadata',
    full_name='chromite.api.MetadataService.SystemImageMetadata',
    index=0,
    containing_service=None,
    input_type=_SYSTEMIMAGEMETADATAREQUEST,
    output_type=_SYSTEMIMAGEMETADATARESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_METADATASERVICE)

DESCRIPTOR.services_by_name['MetadataService'] = _METADATASERVICE

# @@protoc_insertion_point(module_scope)
