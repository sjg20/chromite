# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/payload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen_sdk.chromiumos import common_pb2 as chromiumos_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63hromite/api/payload.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x17\x63hromiumos/common.proto\"h\n\x05\x42uild\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0e\n\x06\x62ucket\x18\x03 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\t\"\x91\x01\n\x08\x44LCImage\x12\"\n\x05\x62uild\x18\x01 \x01(\x0b\x32\x13.chromite.api.Build\x12\x0e\n\x06\x64lc_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64lc_package\x18\x03 \x01(\t\x12\x11\n\tdlc_image\x18\x04 \x01(\t\x12)\n\nimage_type\x18\x05 \x01(\x0e\x32\x15.chromiumos.ImageType\"i\n\x0bSignedImage\x12\"\n\x05\x62uild\x18\x01 \x01(\x0b\x32\x13.chromite.api.Build\x12)\n\nimage_type\x18\x02 \x01(\x0e\x32\x15.chromiumos.ImageType\x12\x0b\n\x03key\x18\x03 \x01(\t\"q\n\rUnsignedImage\x12\"\n\x05\x62uild\x18\x01 \x01(\x0b\x32\x13.chromite.api.Build\x12)\n\nimage_type\x18\x02 \x01(\x0e\x32\x15.chromiumos.ImageType\x12\x11\n\tmilestone\x18\x03 \x01(\t\"\x8a\x04\n\x11GenerationRequest\x12\x15\n\x0b\x66ull_update\x18\x01 \x01(\x08H\x00\x12\x35\n\x10src_signed_image\x18\x02 \x01(\x0b\x32\x19.chromite.api.SignedImageH\x00\x12\x39\n\x12src_unsigned_image\x18\x03 \x01(\x0b\x32\x1b.chromite.api.UnsignedImageH\x00\x12/\n\rsrc_dlc_image\x18\n \x01(\x0b\x32\x16.chromite.api.DLCImageH\x00\x12\x35\n\x10tgt_signed_image\x18\x04 \x01(\x0b\x32\x19.chromite.api.SignedImageH\x01\x12\x39\n\x12tgt_unsigned_image\x18\x05 \x01(\x0b\x32\x1b.chromite.api.UnsignedImageH\x01\x12/\n\rtgt_dlc_image\x18\x0b \x01(\x0b\x32\x16.chromite.api.DLCImageH\x01\x12\x0e\n\x06\x62ucket\x18\x06 \x01(\t\x12\x0e\n\x06verify\x18\x07 \x01(\x08\x12\x0e\n\x06keyset\x18\x08 \x01(\t\x12\x0e\n\x06\x64ryrun\x18\t \x01(\x08\x12\"\n\x06\x63hroot\x18\x0c \x01(\x0b\x32\x12.chromiumos.Chroot\x12\x0e\n\x06minios\x18\r \x01(\x08\x42\x11\n\x0fsrc_image_oneofB\x11\n\x0ftgt_image_oneof\"\xef\x02\n\x12GenerationResponse\x12\x12\n\nlocal_path\x18\x02 \x01(\t\x12\x12\n\nremote_uri\x18\x03 \x01(\t\x12O\n\x13versioned_artifacts\x18\x05 \x03(\x0b\x32\x32.chromite.api.GenerationResponse.VersionedArtifact\x12\x46\n\x0e\x66\x61ilure_reason\x18\x04 \x01(\x0e\x32..chromite.api.GenerationResponse.FailureReason\x1aL\n\x11VersionedArtifact\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x12\n\nlocal_path\x18\x02 \x01(\t\x12\x12\n\nremote_uri\x18\x03 \x01(\t\";\n\rFailureReason\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x19\n\x15NOT_MINIOS_COMPATIBLE\x10\x01J\x04\x08\x01\x10\x02R\x07success2w\n\x0ePayloadService\x12T\n\x0fGeneratePayload\x12\x1f.chromite.api.GenerationRequest\x1a .chromite.api.GenerationResponse\x1a\x0f\xc2\xed\x1a\x0b\n\x07payload\x10\x01\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3')



_BUILD = DESCRIPTOR.message_types_by_name['Build']
_DLCIMAGE = DESCRIPTOR.message_types_by_name['DLCImage']
_SIGNEDIMAGE = DESCRIPTOR.message_types_by_name['SignedImage']
_UNSIGNEDIMAGE = DESCRIPTOR.message_types_by_name['UnsignedImage']
_GENERATIONREQUEST = DESCRIPTOR.message_types_by_name['GenerationRequest']
_GENERATIONRESPONSE = DESCRIPTOR.message_types_by_name['GenerationResponse']
_GENERATIONRESPONSE_VERSIONEDARTIFACT = _GENERATIONRESPONSE.nested_types_by_name['VersionedArtifact']
_GENERATIONRESPONSE_FAILUREREASON = _GENERATIONRESPONSE.enum_types_by_name['FailureReason']
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

  'VersionedArtifact' : _reflection.GeneratedProtocolMessageType('VersionedArtifact', (_message.Message,), {
    'DESCRIPTOR' : _GENERATIONRESPONSE_VERSIONEDARTIFACT,
    '__module__' : 'chromite.api.payload_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.GenerationResponse.VersionedArtifact)
    })
  ,
  'DESCRIPTOR' : _GENERATIONRESPONSE,
  '__module__' : 'chromite.api.payload_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.GenerationResponse)
  })
_sym_db.RegisterMessage(GenerationResponse)
_sym_db.RegisterMessage(GenerationResponse.VersionedArtifact)

_PAYLOADSERVICE = DESCRIPTOR.services_by_name['PayloadService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api'
  _PAYLOADSERVICE._options = None
  _PAYLOADSERVICE._serialized_options = b'\302\355\032\013\n\007payload\020\001'
  _BUILD._serialized_start=99
  _BUILD._serialized_end=203
  _DLCIMAGE._serialized_start=206
  _DLCIMAGE._serialized_end=351
  _SIGNEDIMAGE._serialized_start=353
  _SIGNEDIMAGE._serialized_end=458
  _UNSIGNEDIMAGE._serialized_start=460
  _UNSIGNEDIMAGE._serialized_end=573
  _GENERATIONREQUEST._serialized_start=576
  _GENERATIONREQUEST._serialized_end=1098
  _GENERATIONRESPONSE._serialized_start=1101
  _GENERATIONRESPONSE._serialized_end=1468
  _GENERATIONRESPONSE_VERSIONEDARTIFACT._serialized_start=1316
  _GENERATIONRESPONSE_VERSIONEDARTIFACT._serialized_end=1392
  _GENERATIONRESPONSE_FAILUREREASON._serialized_start=1394
  _GENERATIONRESPONSE_FAILUREREASON._serialized_end=1453
  _PAYLOADSERVICE._serialized_start=1470
  _PAYLOADSERVICE._serialized_end=1589
# @@protoc_insertion_point(module_scope)
