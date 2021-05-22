# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/payload.proto

from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen_sdk.chromiumos import common_pb2 as chromiumos_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromite/api/payload.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api',
  serialized_pb=b'\n\x1a\x63hromite/api/payload.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x17\x63hromiumos/common.proto\"h\n\x05\x42uild\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0e\n\x06\x62ucket\x18\x03 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\t\"\x91\x01\n\x08\x44LCImage\x12\"\n\x05\x62uild\x18\x01 \x01(\x0b\x32\x13.chromite.api.Build\x12\x0e\n\x06\x64lc_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64lc_package\x18\x03 \x01(\t\x12\x11\n\tdlc_image\x18\x04 \x01(\t\x12)\n\nimage_type\x18\x05 \x01(\x0e\x32\x15.chromiumos.ImageType\"i\n\x0bSignedImage\x12\"\n\x05\x62uild\x18\x01 \x01(\x0b\x32\x13.chromite.api.Build\x12)\n\nimage_type\x18\x02 \x01(\x0e\x32\x15.chromiumos.ImageType\x12\x0b\n\x03key\x18\x03 \x01(\t\"q\n\rUnsignedImage\x12\"\n\x05\x62uild\x18\x01 \x01(\x0b\x32\x13.chromite.api.Build\x12)\n\nimage_type\x18\x02 \x01(\x0e\x32\x15.chromiumos.ImageType\x12\x11\n\tmilestone\x18\x03 \x01(\t\"\xfa\x03\n\x11GenerationRequest\x12\x15\n\x0b\x66ull_update\x18\x01 \x01(\x08H\x00\x12\x35\n\x10src_signed_image\x18\x02 \x01(\x0b\x32\x19.chromite.api.SignedImageH\x00\x12\x39\n\x12src_unsigned_image\x18\x03 \x01(\x0b\x32\x1b.chromite.api.UnsignedImageH\x00\x12/\n\rsrc_dlc_image\x18\n \x01(\x0b\x32\x16.chromite.api.DLCImageH\x00\x12\x35\n\x10tgt_signed_image\x18\x04 \x01(\x0b\x32\x19.chromite.api.SignedImageH\x01\x12\x39\n\x12tgt_unsigned_image\x18\x05 \x01(\x0b\x32\x1b.chromite.api.UnsignedImageH\x01\x12/\n\rtgt_dlc_image\x18\x0b \x01(\x0b\x32\x16.chromite.api.DLCImageH\x01\x12\x0e\n\x06\x62ucket\x18\x06 \x01(\t\x12\x0e\n\x06verify\x18\x07 \x01(\x08\x12\x0e\n\x06keyset\x18\x08 \x01(\t\x12\x0e\n\x06\x64ryrun\x18\t \x01(\x08\x12\"\n\x06\x63hroot\x18\x0c \x01(\x0b\x32\x12.chromiumos.ChrootB\x11\n\x0fsrc_image_oneofB\x11\n\x0ftgt_image_oneof\"M\n\x12GenerationResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\nlocal_path\x18\x02 \x01(\t\x12\x12\n\nremote_uri\x18\x03 \x01(\t2w\n\x0ePayloadService\x12T\n\x0fGeneratePayload\x12\x1f.chromite.api.GenerationRequest\x1a .chromite.api.GenerationResponse\x1a\x0f\xc2\xed\x1a\x0b\n\x07payload\x10\x01\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3'
  ,
  dependencies=[chromite_dot_api_dot_build__api__pb2.DESCRIPTOR,chromiumos_dot_common__pb2.DESCRIPTOR,])




_BUILD = _descriptor.Descriptor(
  name='Build',
  full_name='chromite.api.Build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_target', full_name='chromite.api.Build.build_target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='chromite.api.Build.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='chromite.api.Build.bucket', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='chromite.api.Build.channel', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=99,
  serialized_end=203,
)


_DLCIMAGE = _descriptor.Descriptor(
  name='DLCImage',
  full_name='chromite.api.DLCImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build', full_name='chromite.api.DLCImage.build', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dlc_id', full_name='chromite.api.DLCImage.dlc_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dlc_package', full_name='chromite.api.DLCImage.dlc_package', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dlc_image', full_name='chromite.api.DLCImage.dlc_image', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_type', full_name='chromite.api.DLCImage.image_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=206,
  serialized_end=351,
)


_SIGNEDIMAGE = _descriptor.Descriptor(
  name='SignedImage',
  full_name='chromite.api.SignedImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build', full_name='chromite.api.SignedImage.build', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_type', full_name='chromite.api.SignedImage.image_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='chromite.api.SignedImage.key', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=353,
  serialized_end=458,
)


_UNSIGNEDIMAGE = _descriptor.Descriptor(
  name='UnsignedImage',
  full_name='chromite.api.UnsignedImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build', full_name='chromite.api.UnsignedImage.build', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_type', full_name='chromite.api.UnsignedImage.image_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='milestone', full_name='chromite.api.UnsignedImage.milestone', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=460,
  serialized_end=573,
)


_GENERATIONREQUEST = _descriptor.Descriptor(
  name='GenerationRequest',
  full_name='chromite.api.GenerationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='full_update', full_name='chromite.api.GenerationRequest.full_update', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_signed_image', full_name='chromite.api.GenerationRequest.src_signed_image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_unsigned_image', full_name='chromite.api.GenerationRequest.src_unsigned_image', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_dlc_image', full_name='chromite.api.GenerationRequest.src_dlc_image', index=3,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tgt_signed_image', full_name='chromite.api.GenerationRequest.tgt_signed_image', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tgt_unsigned_image', full_name='chromite.api.GenerationRequest.tgt_unsigned_image', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tgt_dlc_image', full_name='chromite.api.GenerationRequest.tgt_dlc_image', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='chromite.api.GenerationRequest.bucket', index=7,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verify', full_name='chromite.api.GenerationRequest.verify', index=8,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyset', full_name='chromite.api.GenerationRequest.keyset', index=9,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dryrun', full_name='chromite.api.GenerationRequest.dryrun', index=10,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.GenerationRequest.chroot', index=11,
      number=12, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='src_image_oneof', full_name='chromite.api.GenerationRequest.src_image_oneof',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='tgt_image_oneof', full_name='chromite.api.GenerationRequest.tgt_image_oneof',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=576,
  serialized_end=1082,
)


_GENERATIONRESPONSE = _descriptor.Descriptor(
  name='GenerationResponse',
  full_name='chromite.api.GenerationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='chromite.api.GenerationResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_path', full_name='chromite.api.GenerationResponse.local_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_uri', full_name='chromite.api.GenerationResponse.remote_uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1084,
  serialized_end=1161,
)

_BUILD.fields_by_name['build_target'].message_type = chromiumos_dot_common__pb2._BUILDTARGET
_DLCIMAGE.fields_by_name['build'].message_type = _BUILD
_DLCIMAGE.fields_by_name['image_type'].enum_type = chromiumos_dot_common__pb2._IMAGETYPE
_SIGNEDIMAGE.fields_by_name['build'].message_type = _BUILD
_SIGNEDIMAGE.fields_by_name['image_type'].enum_type = chromiumos_dot_common__pb2._IMAGETYPE
_UNSIGNEDIMAGE.fields_by_name['build'].message_type = _BUILD
_UNSIGNEDIMAGE.fields_by_name['image_type'].enum_type = chromiumos_dot_common__pb2._IMAGETYPE
_GENERATIONREQUEST.fields_by_name['src_signed_image'].message_type = _SIGNEDIMAGE
_GENERATIONREQUEST.fields_by_name['src_unsigned_image'].message_type = _UNSIGNEDIMAGE
_GENERATIONREQUEST.fields_by_name['src_dlc_image'].message_type = _DLCIMAGE
_GENERATIONREQUEST.fields_by_name['tgt_signed_image'].message_type = _SIGNEDIMAGE
_GENERATIONREQUEST.fields_by_name['tgt_unsigned_image'].message_type = _UNSIGNEDIMAGE
_GENERATIONREQUEST.fields_by_name['tgt_dlc_image'].message_type = _DLCIMAGE
_GENERATIONREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_GENERATIONREQUEST.oneofs_by_name['src_image_oneof'].fields.append(
  _GENERATIONREQUEST.fields_by_name['full_update'])
_GENERATIONREQUEST.fields_by_name['full_update'].containing_oneof = _GENERATIONREQUEST.oneofs_by_name['src_image_oneof']
_GENERATIONREQUEST.oneofs_by_name['src_image_oneof'].fields.append(
  _GENERATIONREQUEST.fields_by_name['src_signed_image'])
_GENERATIONREQUEST.fields_by_name['src_signed_image'].containing_oneof = _GENERATIONREQUEST.oneofs_by_name['src_image_oneof']
_GENERATIONREQUEST.oneofs_by_name['src_image_oneof'].fields.append(
  _GENERATIONREQUEST.fields_by_name['src_unsigned_image'])
_GENERATIONREQUEST.fields_by_name['src_unsigned_image'].containing_oneof = _GENERATIONREQUEST.oneofs_by_name['src_image_oneof']
_GENERATIONREQUEST.oneofs_by_name['src_image_oneof'].fields.append(
  _GENERATIONREQUEST.fields_by_name['src_dlc_image'])
_GENERATIONREQUEST.fields_by_name['src_dlc_image'].containing_oneof = _GENERATIONREQUEST.oneofs_by_name['src_image_oneof']
_GENERATIONREQUEST.oneofs_by_name['tgt_image_oneof'].fields.append(
  _GENERATIONREQUEST.fields_by_name['tgt_signed_image'])
_GENERATIONREQUEST.fields_by_name['tgt_signed_image'].containing_oneof = _GENERATIONREQUEST.oneofs_by_name['tgt_image_oneof']
_GENERATIONREQUEST.oneofs_by_name['tgt_image_oneof'].fields.append(
  _GENERATIONREQUEST.fields_by_name['tgt_unsigned_image'])
_GENERATIONREQUEST.fields_by_name['tgt_unsigned_image'].containing_oneof = _GENERATIONREQUEST.oneofs_by_name['tgt_image_oneof']
_GENERATIONREQUEST.oneofs_by_name['tgt_image_oneof'].fields.append(
  _GENERATIONREQUEST.fields_by_name['tgt_dlc_image'])
_GENERATIONREQUEST.fields_by_name['tgt_dlc_image'].containing_oneof = _GENERATIONREQUEST.oneofs_by_name['tgt_image_oneof']
DESCRIPTOR.message_types_by_name['Build'] = _BUILD
DESCRIPTOR.message_types_by_name['DLCImage'] = _DLCIMAGE
DESCRIPTOR.message_types_by_name['SignedImage'] = _SIGNEDIMAGE
DESCRIPTOR.message_types_by_name['UnsignedImage'] = _UNSIGNEDIMAGE
DESCRIPTOR.message_types_by_name['GenerationRequest'] = _GENERATIONREQUEST
DESCRIPTOR.message_types_by_name['GenerationResponse'] = _GENERATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Build = _reflection.GeneratedProtocolMessageType('Build', (_message.Message,), {
  'DESCRIPTOR' : _BUILD,
  '__module__' : 'chromite.api.payload_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.Build)
  })
_sym_db.RegisterMessage(Build)

DLCImage = _reflection.GeneratedProtocolMessageType('DLCImage', (_message.Message,), {
  'DESCRIPTOR' : _DLCIMAGE,
  '__module__' : 'chromite.api.payload_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.DLCImage)
  })
_sym_db.RegisterMessage(DLCImage)

SignedImage = _reflection.GeneratedProtocolMessageType('SignedImage', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDIMAGE,
  '__module__' : 'chromite.api.payload_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SignedImage)
  })
_sym_db.RegisterMessage(SignedImage)

UnsignedImage = _reflection.GeneratedProtocolMessageType('UnsignedImage', (_message.Message,), {
  'DESCRIPTOR' : _UNSIGNEDIMAGE,
  '__module__' : 'chromite.api.payload_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UnsignedImage)
  })
_sym_db.RegisterMessage(UnsignedImage)

GenerationRequest = _reflection.GeneratedProtocolMessageType('GenerationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATIONREQUEST,
  '__module__' : 'chromite.api.payload_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.GenerationRequest)
  })
_sym_db.RegisterMessage(GenerationRequest)

GenerationResponse = _reflection.GeneratedProtocolMessageType('GenerationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATIONRESPONSE,
  '__module__' : 'chromite.api.payload_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.GenerationResponse)
  })
_sym_db.RegisterMessage(GenerationResponse)


DESCRIPTOR._options = None

_PAYLOADSERVICE = _descriptor.ServiceDescriptor(
  name='PayloadService',
  full_name='chromite.api.PayloadService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\302\355\032\013\n\007payload\020\001',
  serialized_start=1163,
  serialized_end=1282,
  methods=[
  _descriptor.MethodDescriptor(
    name='GeneratePayload',
    full_name='chromite.api.PayloadService.GeneratePayload',
    index=0,
    containing_service=None,
    input_type=_GENERATIONREQUEST,
    output_type=_GENERATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAYLOADSERVICE)

DESCRIPTOR.services_by_name['PayloadService'] = _PAYLOADSERVICE

# @@protoc_insertion_point(module_scope)
