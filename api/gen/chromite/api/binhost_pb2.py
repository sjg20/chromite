# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/binhost.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen.chromite.api import sysroot_pb2 as chromite_dot_api_dot_sysroot__pb2
from chromite.api.gen.chromiumos import common_pb2 as chromiumos_dot_common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromite/api/binhost.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x63hromite/api/binhost.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x1a\x63hromite/api/sysroot.proto\x1a\x17\x63hromiumos/common.proto\x1a\x1bgoogle/protobuf/empty.proto\"Z\n\x1cPrepareBinhostUploadsRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x0b\n\x03uri\x18\x02 \x01(\t\"\xa4\x01\n\x1dPrepareBinhostUploadsResponse\x12\x13\n\x0buploads_dir\x18\x01 \x01(\t\x12P\n\x0eupload_targets\x18\x02 \x03(\x0b\x32\x38.chromite.api.PrepareBinhostUploadsResponse.UploadTarget\x1a\x1c\n\x0cUploadTarget\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x87\x01\n\x11SetBinhostRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x0f\n\x07private\x18\x02 \x01(\x08\x12%\n\x03key\x18\x03 \x01(\x0e\x32\x18.chromite.api.BinhostKey\x12\x0b\n\x03uri\x18\x04 \x01(\t\")\n\x12SetBinhostResponse\x12\x13\n\x0boutput_file\x18\x01 \x01(\t\"q\n\x16RegenBuildCacheRequest\x12/\n\x0coverlay_type\x18\x01 \x01(\x0e\x32\x19.chromite.api.OverlayType\x12&\n\x07sysroot\x18\x02 \x01(\x0b\x32\x15.chromite.api.Sysroot*\x82\x01\n\nBinhostKey\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x11\n\rDUMMY_BINHOST\x10\x01\x12\x16\n\x12POSTSUBMIT_BINHOST\x10\x02\x12!\n\x1dLATEST_RELEASE_CHROME_BINHOST\x10\x03\x12\x15\n\x11PREFLIGHT_BINHOST\x10\x04*\x87\x01\n\x0bOverlayType\x12\x1b\n\x17OVERLAYTYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10OVERLAYTYPE_BOTH\x10\x01\x12\x16\n\x12OVERLAYTYPE_PUBLIC\x10\x02\x12\x17\n\x13OVERLAYTYPE_PRIVATE\x10\x03\x12\x14\n\x10OVERLAYTYPE_NONE\x10\x04\x32\xbd\x02\n\x0e\x42inhostService\x12p\n\x15PrepareBinhostUploads\x12*.chromite.api.PrepareBinhostUploadsRequest\x1a+.chromite.api.PrepareBinhostUploadsResponse\x12O\n\nSetBinhost\x12\x1f.chromite.api.SetBinhostRequest\x1a .chromite.api.SetBinhostResponse\x12W\n\x0fRegenBuildCache\x12$.chromite.api.RegenBuildCacheRequest\x1a\x16.google.protobuf.Empty\"\x06\xc2\xed\x1a\x02\x10\x01\x1a\x0f\xc2\xed\x1a\x0b\n\x07\x62inhost\x10\x02\x62\x06proto3')
  ,
  dependencies=[chromite_dot_api_dot_build__api__pb2.DESCRIPTOR,chromite_dot_api_dot_sysroot__pb2.DESCRIPTOR,chromiumos_dot_common__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_BINHOSTKEY = _descriptor.EnumDescriptor(
  name='BinhostKey',
  full_name='chromite.api.BinhostKey',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUMMY_BINHOST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTSUBMIT_BINHOST', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LATEST_RELEASE_CHROME_BINHOST', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREFLIGHT_BINHOST', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=712,
  serialized_end=842,
)
_sym_db.RegisterEnumDescriptor(_BINHOSTKEY)

BinhostKey = enum_type_wrapper.EnumTypeWrapper(_BINHOSTKEY)
_OVERLAYTYPE = _descriptor.EnumDescriptor(
  name='OverlayType',
  full_name='chromite.api.OverlayType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OVERLAYTYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAYTYPE_BOTH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAYTYPE_PUBLIC', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAYTYPE_PRIVATE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAYTYPE_NONE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=845,
  serialized_end=980,
)
_sym_db.RegisterEnumDescriptor(_OVERLAYTYPE)

OverlayType = enum_type_wrapper.EnumTypeWrapper(_OVERLAYTYPE)
UNSPECIFIED = 0
DUMMY_BINHOST = 1
POSTSUBMIT_BINHOST = 2
LATEST_RELEASE_CHROME_BINHOST = 3
PREFLIGHT_BINHOST = 4
OVERLAYTYPE_UNSPECIFIED = 0
OVERLAYTYPE_BOTH = 1
OVERLAYTYPE_PUBLIC = 2
OVERLAYTYPE_PRIVATE = 3
OVERLAYTYPE_NONE = 4



_PREPAREBINHOSTUPLOADSREQUEST = _descriptor.Descriptor(
  name='PrepareBinhostUploadsRequest',
  full_name='chromite.api.PrepareBinhostUploadsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_target', full_name='chromite.api.PrepareBinhostUploadsRequest.build_target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='chromite.api.PrepareBinhostUploadsRequest.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=156,
  serialized_end=246,
)


_PREPAREBINHOSTUPLOADSRESPONSE_UPLOADTARGET = _descriptor.Descriptor(
  name='UploadTarget',
  full_name='chromite.api.PrepareBinhostUploadsResponse.UploadTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='chromite.api.PrepareBinhostUploadsResponse.UploadTarget.path', index=0,
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
  serialized_start=385,
  serialized_end=413,
)

_PREPAREBINHOSTUPLOADSRESPONSE = _descriptor.Descriptor(
  name='PrepareBinhostUploadsResponse',
  full_name='chromite.api.PrepareBinhostUploadsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uploads_dir', full_name='chromite.api.PrepareBinhostUploadsResponse.uploads_dir', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_targets', full_name='chromite.api.PrepareBinhostUploadsResponse.upload_targets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREPAREBINHOSTUPLOADSRESPONSE_UPLOADTARGET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=413,
)


_SETBINHOSTREQUEST = _descriptor.Descriptor(
  name='SetBinhostRequest',
  full_name='chromite.api.SetBinhostRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_target', full_name='chromite.api.SetBinhostRequest.build_target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private', full_name='chromite.api.SetBinhostRequest.private', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='chromite.api.SetBinhostRequest.key', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='chromite.api.SetBinhostRequest.uri', index=3,
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
  serialized_start=416,
  serialized_end=551,
)


_SETBINHOSTRESPONSE = _descriptor.Descriptor(
  name='SetBinhostResponse',
  full_name='chromite.api.SetBinhostResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_file', full_name='chromite.api.SetBinhostResponse.output_file', index=0,
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
  serialized_start=553,
  serialized_end=594,
)


_REGENBUILDCACHEREQUEST = _descriptor.Descriptor(
  name='RegenBuildCacheRequest',
  full_name='chromite.api.RegenBuildCacheRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='overlay_type', full_name='chromite.api.RegenBuildCacheRequest.overlay_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sysroot', full_name='chromite.api.RegenBuildCacheRequest.sysroot', index=1,
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
  serialized_start=596,
  serialized_end=709,
)

_PREPAREBINHOSTUPLOADSREQUEST.fields_by_name['build_target'].message_type = chromiumos_dot_common__pb2._BUILDTARGET
_PREPAREBINHOSTUPLOADSRESPONSE_UPLOADTARGET.containing_type = _PREPAREBINHOSTUPLOADSRESPONSE
_PREPAREBINHOSTUPLOADSRESPONSE.fields_by_name['upload_targets'].message_type = _PREPAREBINHOSTUPLOADSRESPONSE_UPLOADTARGET
_SETBINHOSTREQUEST.fields_by_name['build_target'].message_type = chromiumos_dot_common__pb2._BUILDTARGET
_SETBINHOSTREQUEST.fields_by_name['key'].enum_type = _BINHOSTKEY
_REGENBUILDCACHEREQUEST.fields_by_name['overlay_type'].enum_type = _OVERLAYTYPE
_REGENBUILDCACHEREQUEST.fields_by_name['sysroot'].message_type = chromite_dot_api_dot_sysroot__pb2._SYSROOT
DESCRIPTOR.message_types_by_name['PrepareBinhostUploadsRequest'] = _PREPAREBINHOSTUPLOADSREQUEST
DESCRIPTOR.message_types_by_name['PrepareBinhostUploadsResponse'] = _PREPAREBINHOSTUPLOADSRESPONSE
DESCRIPTOR.message_types_by_name['SetBinhostRequest'] = _SETBINHOSTREQUEST
DESCRIPTOR.message_types_by_name['SetBinhostResponse'] = _SETBINHOSTRESPONSE
DESCRIPTOR.message_types_by_name['RegenBuildCacheRequest'] = _REGENBUILDCACHEREQUEST
DESCRIPTOR.enum_types_by_name['BinhostKey'] = _BINHOSTKEY
DESCRIPTOR.enum_types_by_name['OverlayType'] = _OVERLAYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrepareBinhostUploadsRequest = _reflection.GeneratedProtocolMessageType('PrepareBinhostUploadsRequest', (_message.Message,), dict(
  DESCRIPTOR = _PREPAREBINHOSTUPLOADSREQUEST,
  __module__ = 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.PrepareBinhostUploadsRequest)
  ))
_sym_db.RegisterMessage(PrepareBinhostUploadsRequest)

PrepareBinhostUploadsResponse = _reflection.GeneratedProtocolMessageType('PrepareBinhostUploadsResponse', (_message.Message,), dict(

  UploadTarget = _reflection.GeneratedProtocolMessageType('UploadTarget', (_message.Message,), dict(
    DESCRIPTOR = _PREPAREBINHOSTUPLOADSRESPONSE_UPLOADTARGET,
    __module__ = 'chromite.api.binhost_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.PrepareBinhostUploadsResponse.UploadTarget)
    ))
  ,
  DESCRIPTOR = _PREPAREBINHOSTUPLOADSRESPONSE,
  __module__ = 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.PrepareBinhostUploadsResponse)
  ))
_sym_db.RegisterMessage(PrepareBinhostUploadsResponse)
_sym_db.RegisterMessage(PrepareBinhostUploadsResponse.UploadTarget)

SetBinhostRequest = _reflection.GeneratedProtocolMessageType('SetBinhostRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETBINHOSTREQUEST,
  __module__ = 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SetBinhostRequest)
  ))
_sym_db.RegisterMessage(SetBinhostRequest)

SetBinhostResponse = _reflection.GeneratedProtocolMessageType('SetBinhostResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETBINHOSTRESPONSE,
  __module__ = 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SetBinhostResponse)
  ))
_sym_db.RegisterMessage(SetBinhostResponse)

RegenBuildCacheRequest = _reflection.GeneratedProtocolMessageType('RegenBuildCacheRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGENBUILDCACHEREQUEST,
  __module__ = 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.RegenBuildCacheRequest)
  ))
_sym_db.RegisterMessage(RegenBuildCacheRequest)



_BINHOSTSERVICE = _descriptor.ServiceDescriptor(
  name='BinhostService',
  full_name='chromite.api.BinhostService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\302\355\032\013\n\007binhost\020\002'),
  serialized_start=983,
  serialized_end=1300,
  methods=[
  _descriptor.MethodDescriptor(
    name='PrepareBinhostUploads',
    full_name='chromite.api.BinhostService.PrepareBinhostUploads',
    index=0,
    containing_service=None,
    input_type=_PREPAREBINHOSTUPLOADSREQUEST,
    output_type=_PREPAREBINHOSTUPLOADSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetBinhost',
    full_name='chromite.api.BinhostService.SetBinhost',
    index=1,
    containing_service=None,
    input_type=_SETBINHOSTREQUEST,
    output_type=_SETBINHOSTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RegenBuildCache',
    full_name='chromite.api.BinhostService.RegenBuildCache',
    index=2,
    containing_service=None,
    input_type=_REGENBUILDCACHEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\302\355\032\002\020\001'),
  ),
])
_sym_db.RegisterServiceDescriptor(_BINHOSTSERVICE)

DESCRIPTOR.services_by_name['BinhostService'] = _BINHOSTSERVICE

# @@protoc_insertion_point(module_scope)
