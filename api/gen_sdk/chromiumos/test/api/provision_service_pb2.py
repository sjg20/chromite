# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/provision_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.build.api import firmware_config_pb2 as chromiumos_dot_build_dot_api_dot_firmware__config__pb2
from chromite.api.gen_sdk.chromiumos.longrunning import operations_pb2 as chromiumos_dot_longrunning_dot_operations__pb2
from chromite.api.gen_sdk.chromiumos import storage_path_pb2 as chromiumos_dot_storage__path__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/test/api/provision_service.proto',
  package='chromiumos.test.api',
  syntax='proto3',
  serialized_options=_b('Z-go.chromium.org/chromiumos/config/go/test/api'),
  serialized_pb=_b('\n+chromiumos/test/api/provision_service.proto\x12\x13\x63hromiumos.test.api\x1a*chromiumos/build/api/firmware_config.proto\x1a\'chromiumos/longrunning/operations.proto\x1a\x1d\x63hromiumos/storage_path.proto\"\x10\n\x0eInstallSuccess\"\xaf\x02\n\x0eInstallFailure\x12:\n\x06reason\x18\x01 \x01(\x0e\x32*.chromiumos.test.api.InstallFailure.Reason\"\xe0\x01\n\x06Reason\x12\x1a\n\x16REASON_INVALID_REQUEST\x10\x00\x12(\n$REASON_DUT_UNREACHABLE_PRE_PROVISION\x10\x01\x12#\n\x1fREASON_DOWNLOADING_IMAGE_FAILED\x10\x02\x12 \n\x1cREASON_PROVISIONING_TIMEDOUT\x10\x03\x12\x1e\n\x1aREASON_PROVISIONING_FAILED\x10\x04\x12)\n%REASON_DUT_UNREACHABLE_POST_PROVISION\x10\x05\"\xbc\x01\n\x12InstallCrosRequest\x12\x30\n\x0f\x63ros_image_path\x18\x01 \x01(\x0b\x32\x17.chromiumos.StoragePath\x12\x42\n\tdlc_specs\x18\x02 \x03(\x0b\x32/.chromiumos.test.api.InstallCrosRequest.DLCSpec\x12\x19\n\x11preserve_stateful\x18\x03 \x01(\x08\x1a\x15\n\x07\x44LCSpec\x12\n\n\x02id\x18\x01 \x01(\t\"\x90\x01\n\x13InstallCrosResponse\x12\x36\n\x07success\x18\x01 \x01(\x0b\x32#.chromiumos.test.api.InstallSuccessH\x00\x12\x36\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32#.chromiumos.test.api.InstallFailureH\x00\x42\t\n\x07outcome\"\x15\n\x13InstallCrosMetadata\"J\n\x14InstallLacrosRequest\x12\x32\n\x11lacros_image_path\x18\x01 \x01(\x0b\x32\x17.chromiumos.StoragePath\"\x92\x01\n\x15InstallLacrosResponse\x12\x36\n\x07success\x18\x01 \x01(\x0b\x32#.chromiumos.test.api.InstallSuccessH\x00\x12\x36\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32#.chromiumos.test.api.InstallFailureH\x00\x42\t\n\x07outcome\"\x17\n\x15InstallLacrosMetadata\"D\n\x11InstallAshRequest\x12/\n\x0e\x61sh_image_path\x18\x01 \x01(\x0b\x32\x17.chromiumos.StoragePath\"\x8f\x01\n\x12InstallAshResponse\x12\x36\n\x07success\x18\x01 \x01(\x0b\x32#.chromiumos.test.api.InstallSuccessH\x00\x12\x36\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32#.chromiumos.test.api.InstallFailureH\x00\x42\t\n\x07outcome\"\x14\n\x12InstallAshMetadata\"D\n\x11InstallArcRequest\x12/\n\x0e\x61sh_image_path\x18\x01 \x01(\x0b\x32\x17.chromiumos.StoragePath\"\x8f\x01\n\x12InstallArcResponse\x12\x36\n\x07success\x18\x01 \x01(\x0b\x32#.chromiumos.test.api.InstallSuccessH\x00\x12\x36\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32#.chromiumos.test.api.InstallFailureH\x00\x42\t\n\x07outcome\"\x14\n\x12InstallArcMetadata\"W\n\x16InstallFirmwareRequest\x12=\n\x0f\x66irmware_config\x18\x01 \x01(\x0b\x32$.chromiumos.build.api.FirmwareConfig\"\x94\x01\n\x17InstallFirmwareResponse\x12\x36\n\x07success\x18\x01 \x01(\x0b\x32#.chromiumos.test.api.InstallSuccessH\x00\x12\x36\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32#.chromiumos.test.api.InstallFailureH\x00\x42\t\n\x07outcome\"\x19\n\x17InstallFirmwareMetadata2\xd9\x05\n\x10ProvisionService\x12\x88\x01\n\x0bInstallCros\x12\'.chromiumos.test.api.InstallCrosRequest\x1a!.chromiumos.longrunning.Operation\"-\xd2\x41*\n\x13InstallCrosResponse\x12\x13InstallCrosMetadata\x12\x90\x01\n\rInstallLacros\x12).chromiumos.test.api.InstallLacrosRequest\x1a!.chromiumos.longrunning.Operation\"1\xd2\x41.\n\x15InstallLacrosResponse\x12\x15InstallLacrosMetadata\x12\x84\x01\n\nInstallAsh\x12&.chromiumos.test.api.InstallAshRequest\x1a!.chromiumos.longrunning.Operation\"+\xd2\x41(\n\x12InstallAshResponse\x12\x12InstallAshMetadata\x12\x84\x01\n\nInstallArc\x12&.chromiumos.test.api.InstallArcRequest\x1a!.chromiumos.longrunning.Operation\"+\xd2\x41(\n\x12InstallArcResponse\x12\x12InstallArcMetadata\x12\x98\x01\n\x0fInstallFirmware\x12+.chromiumos.test.api.InstallFirmwareRequest\x1a!.chromiumos.longrunning.Operation\"5\xd2\x41\x32\n\x17InstallFirmwareResponse\x12\x17InstallFirmwareMetadataB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3')
  ,
  dependencies=[chromiumos_dot_build_dot_api_dot_firmware__config__pb2.DESCRIPTOR,chromiumos_dot_longrunning_dot_operations__pb2.DESCRIPTOR,chromiumos_dot_storage__path__pb2.DESCRIPTOR,])



_INSTALLFAILURE_REASON = _descriptor.EnumDescriptor(
  name='Reason',
  full_name='chromiumos.test.api.InstallFailure.Reason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REASON_INVALID_REQUEST', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REASON_DUT_UNREACHABLE_PRE_PROVISION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REASON_DOWNLOADING_IMAGE_FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REASON_PROVISIONING_TIMEDOUT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REASON_PROVISIONING_FAILED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REASON_DUT_UNREACHABLE_POST_PROVISION', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=282,
  serialized_end=506,
)
_sym_db.RegisterEnumDescriptor(_INSTALLFAILURE_REASON)


_INSTALLSUCCESS = _descriptor.Descriptor(
  name='InstallSuccess',
  full_name='chromiumos.test.api.InstallSuccess',
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
  serialized_start=184,
  serialized_end=200,
)


_INSTALLFAILURE = _descriptor.Descriptor(
  name='InstallFailure',
  full_name='chromiumos.test.api.InstallFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='chromiumos.test.api.InstallFailure.reason', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INSTALLFAILURE_REASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=506,
)


_INSTALLCROSREQUEST_DLCSPEC = _descriptor.Descriptor(
  name='DLCSpec',
  full_name='chromiumos.test.api.InstallCrosRequest.DLCSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chromiumos.test.api.InstallCrosRequest.DLCSpec.id', index=0,
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
  serialized_start=676,
  serialized_end=697,
)

_INSTALLCROSREQUEST = _descriptor.Descriptor(
  name='InstallCrosRequest',
  full_name='chromiumos.test.api.InstallCrosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cros_image_path', full_name='chromiumos.test.api.InstallCrosRequest.cros_image_path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dlc_specs', full_name='chromiumos.test.api.InstallCrosRequest.dlc_specs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preserve_stateful', full_name='chromiumos.test.api.InstallCrosRequest.preserve_stateful', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INSTALLCROSREQUEST_DLCSPEC, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=697,
)


_INSTALLCROSRESPONSE = _descriptor.Descriptor(
  name='InstallCrosResponse',
  full_name='chromiumos.test.api.InstallCrosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='chromiumos.test.api.InstallCrosResponse.success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failure', full_name='chromiumos.test.api.InstallCrosResponse.failure', index=1,
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
    _descriptor.OneofDescriptor(
      name='outcome', full_name='chromiumos.test.api.InstallCrosResponse.outcome',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=700,
  serialized_end=844,
)


_INSTALLCROSMETADATA = _descriptor.Descriptor(
  name='InstallCrosMetadata',
  full_name='chromiumos.test.api.InstallCrosMetadata',
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
  serialized_start=846,
  serialized_end=867,
)


_INSTALLLACROSREQUEST = _descriptor.Descriptor(
  name='InstallLacrosRequest',
  full_name='chromiumos.test.api.InstallLacrosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lacros_image_path', full_name='chromiumos.test.api.InstallLacrosRequest.lacros_image_path', index=0,
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
  serialized_start=869,
  serialized_end=943,
)


_INSTALLLACROSRESPONSE = _descriptor.Descriptor(
  name='InstallLacrosResponse',
  full_name='chromiumos.test.api.InstallLacrosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='chromiumos.test.api.InstallLacrosResponse.success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failure', full_name='chromiumos.test.api.InstallLacrosResponse.failure', index=1,
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
    _descriptor.OneofDescriptor(
      name='outcome', full_name='chromiumos.test.api.InstallLacrosResponse.outcome',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=946,
  serialized_end=1092,
)


_INSTALLLACROSMETADATA = _descriptor.Descriptor(
  name='InstallLacrosMetadata',
  full_name='chromiumos.test.api.InstallLacrosMetadata',
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
  serialized_start=1094,
  serialized_end=1117,
)


_INSTALLASHREQUEST = _descriptor.Descriptor(
  name='InstallAshRequest',
  full_name='chromiumos.test.api.InstallAshRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ash_image_path', full_name='chromiumos.test.api.InstallAshRequest.ash_image_path', index=0,
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
  serialized_start=1119,
  serialized_end=1187,
)


_INSTALLASHRESPONSE = _descriptor.Descriptor(
  name='InstallAshResponse',
  full_name='chromiumos.test.api.InstallAshResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='chromiumos.test.api.InstallAshResponse.success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failure', full_name='chromiumos.test.api.InstallAshResponse.failure', index=1,
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
    _descriptor.OneofDescriptor(
      name='outcome', full_name='chromiumos.test.api.InstallAshResponse.outcome',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1190,
  serialized_end=1333,
)


_INSTALLASHMETADATA = _descriptor.Descriptor(
  name='InstallAshMetadata',
  full_name='chromiumos.test.api.InstallAshMetadata',
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
  serialized_start=1335,
  serialized_end=1355,
)


_INSTALLARCREQUEST = _descriptor.Descriptor(
  name='InstallArcRequest',
  full_name='chromiumos.test.api.InstallArcRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ash_image_path', full_name='chromiumos.test.api.InstallArcRequest.ash_image_path', index=0,
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
  serialized_start=1357,
  serialized_end=1425,
)


_INSTALLARCRESPONSE = _descriptor.Descriptor(
  name='InstallArcResponse',
  full_name='chromiumos.test.api.InstallArcResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='chromiumos.test.api.InstallArcResponse.success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failure', full_name='chromiumos.test.api.InstallArcResponse.failure', index=1,
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
    _descriptor.OneofDescriptor(
      name='outcome', full_name='chromiumos.test.api.InstallArcResponse.outcome',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1428,
  serialized_end=1571,
)


_INSTALLARCMETADATA = _descriptor.Descriptor(
  name='InstallArcMetadata',
  full_name='chromiumos.test.api.InstallArcMetadata',
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
  serialized_start=1573,
  serialized_end=1593,
)


_INSTALLFIRMWAREREQUEST = _descriptor.Descriptor(
  name='InstallFirmwareRequest',
  full_name='chromiumos.test.api.InstallFirmwareRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firmware_config', full_name='chromiumos.test.api.InstallFirmwareRequest.firmware_config', index=0,
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
  serialized_start=1595,
  serialized_end=1682,
)


_INSTALLFIRMWARERESPONSE = _descriptor.Descriptor(
  name='InstallFirmwareResponse',
  full_name='chromiumos.test.api.InstallFirmwareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='chromiumos.test.api.InstallFirmwareResponse.success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failure', full_name='chromiumos.test.api.InstallFirmwareResponse.failure', index=1,
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
    _descriptor.OneofDescriptor(
      name='outcome', full_name='chromiumos.test.api.InstallFirmwareResponse.outcome',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1685,
  serialized_end=1833,
)


_INSTALLFIRMWAREMETADATA = _descriptor.Descriptor(
  name='InstallFirmwareMetadata',
  full_name='chromiumos.test.api.InstallFirmwareMetadata',
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
  serialized_start=1835,
  serialized_end=1860,
)

_INSTALLFAILURE.fields_by_name['reason'].enum_type = _INSTALLFAILURE_REASON
_INSTALLFAILURE_REASON.containing_type = _INSTALLFAILURE
_INSTALLCROSREQUEST_DLCSPEC.containing_type = _INSTALLCROSREQUEST
_INSTALLCROSREQUEST.fields_by_name['cros_image_path'].message_type = chromiumos_dot_storage__path__pb2._STORAGEPATH
_INSTALLCROSREQUEST.fields_by_name['dlc_specs'].message_type = _INSTALLCROSREQUEST_DLCSPEC
_INSTALLCROSRESPONSE.fields_by_name['success'].message_type = _INSTALLSUCCESS
_INSTALLCROSRESPONSE.fields_by_name['failure'].message_type = _INSTALLFAILURE
_INSTALLCROSRESPONSE.oneofs_by_name['outcome'].fields.append(
  _INSTALLCROSRESPONSE.fields_by_name['success'])
_INSTALLCROSRESPONSE.fields_by_name['success'].containing_oneof = _INSTALLCROSRESPONSE.oneofs_by_name['outcome']
_INSTALLCROSRESPONSE.oneofs_by_name['outcome'].fields.append(
  _INSTALLCROSRESPONSE.fields_by_name['failure'])
_INSTALLCROSRESPONSE.fields_by_name['failure'].containing_oneof = _INSTALLCROSRESPONSE.oneofs_by_name['outcome']
_INSTALLLACROSREQUEST.fields_by_name['lacros_image_path'].message_type = chromiumos_dot_storage__path__pb2._STORAGEPATH
_INSTALLLACROSRESPONSE.fields_by_name['success'].message_type = _INSTALLSUCCESS
_INSTALLLACROSRESPONSE.fields_by_name['failure'].message_type = _INSTALLFAILURE
_INSTALLLACROSRESPONSE.oneofs_by_name['outcome'].fields.append(
  _INSTALLLACROSRESPONSE.fields_by_name['success'])
_INSTALLLACROSRESPONSE.fields_by_name['success'].containing_oneof = _INSTALLLACROSRESPONSE.oneofs_by_name['outcome']
_INSTALLLACROSRESPONSE.oneofs_by_name['outcome'].fields.append(
  _INSTALLLACROSRESPONSE.fields_by_name['failure'])
_INSTALLLACROSRESPONSE.fields_by_name['failure'].containing_oneof = _INSTALLLACROSRESPONSE.oneofs_by_name['outcome']
_INSTALLASHREQUEST.fields_by_name['ash_image_path'].message_type = chromiumos_dot_storage__path__pb2._STORAGEPATH
_INSTALLASHRESPONSE.fields_by_name['success'].message_type = _INSTALLSUCCESS
_INSTALLASHRESPONSE.fields_by_name['failure'].message_type = _INSTALLFAILURE
_INSTALLASHRESPONSE.oneofs_by_name['outcome'].fields.append(
  _INSTALLASHRESPONSE.fields_by_name['success'])
_INSTALLASHRESPONSE.fields_by_name['success'].containing_oneof = _INSTALLASHRESPONSE.oneofs_by_name['outcome']
_INSTALLASHRESPONSE.oneofs_by_name['outcome'].fields.append(
  _INSTALLASHRESPONSE.fields_by_name['failure'])
_INSTALLASHRESPONSE.fields_by_name['failure'].containing_oneof = _INSTALLASHRESPONSE.oneofs_by_name['outcome']
_INSTALLARCREQUEST.fields_by_name['ash_image_path'].message_type = chromiumos_dot_storage__path__pb2._STORAGEPATH
_INSTALLARCRESPONSE.fields_by_name['success'].message_type = _INSTALLSUCCESS
_INSTALLARCRESPONSE.fields_by_name['failure'].message_type = _INSTALLFAILURE
_INSTALLARCRESPONSE.oneofs_by_name['outcome'].fields.append(
  _INSTALLARCRESPONSE.fields_by_name['success'])
_INSTALLARCRESPONSE.fields_by_name['success'].containing_oneof = _INSTALLARCRESPONSE.oneofs_by_name['outcome']
_INSTALLARCRESPONSE.oneofs_by_name['outcome'].fields.append(
  _INSTALLARCRESPONSE.fields_by_name['failure'])
_INSTALLARCRESPONSE.fields_by_name['failure'].containing_oneof = _INSTALLARCRESPONSE.oneofs_by_name['outcome']
_INSTALLFIRMWAREREQUEST.fields_by_name['firmware_config'].message_type = chromiumos_dot_build_dot_api_dot_firmware__config__pb2._FIRMWARECONFIG
_INSTALLFIRMWARERESPONSE.fields_by_name['success'].message_type = _INSTALLSUCCESS
_INSTALLFIRMWARERESPONSE.fields_by_name['failure'].message_type = _INSTALLFAILURE
_INSTALLFIRMWARERESPONSE.oneofs_by_name['outcome'].fields.append(
  _INSTALLFIRMWARERESPONSE.fields_by_name['success'])
_INSTALLFIRMWARERESPONSE.fields_by_name['success'].containing_oneof = _INSTALLFIRMWARERESPONSE.oneofs_by_name['outcome']
_INSTALLFIRMWARERESPONSE.oneofs_by_name['outcome'].fields.append(
  _INSTALLFIRMWARERESPONSE.fields_by_name['failure'])
_INSTALLFIRMWARERESPONSE.fields_by_name['failure'].containing_oneof = _INSTALLFIRMWARERESPONSE.oneofs_by_name['outcome']
DESCRIPTOR.message_types_by_name['InstallSuccess'] = _INSTALLSUCCESS
DESCRIPTOR.message_types_by_name['InstallFailure'] = _INSTALLFAILURE
DESCRIPTOR.message_types_by_name['InstallCrosRequest'] = _INSTALLCROSREQUEST
DESCRIPTOR.message_types_by_name['InstallCrosResponse'] = _INSTALLCROSRESPONSE
DESCRIPTOR.message_types_by_name['InstallCrosMetadata'] = _INSTALLCROSMETADATA
DESCRIPTOR.message_types_by_name['InstallLacrosRequest'] = _INSTALLLACROSREQUEST
DESCRIPTOR.message_types_by_name['InstallLacrosResponse'] = _INSTALLLACROSRESPONSE
DESCRIPTOR.message_types_by_name['InstallLacrosMetadata'] = _INSTALLLACROSMETADATA
DESCRIPTOR.message_types_by_name['InstallAshRequest'] = _INSTALLASHREQUEST
DESCRIPTOR.message_types_by_name['InstallAshResponse'] = _INSTALLASHRESPONSE
DESCRIPTOR.message_types_by_name['InstallAshMetadata'] = _INSTALLASHMETADATA
DESCRIPTOR.message_types_by_name['InstallArcRequest'] = _INSTALLARCREQUEST
DESCRIPTOR.message_types_by_name['InstallArcResponse'] = _INSTALLARCRESPONSE
DESCRIPTOR.message_types_by_name['InstallArcMetadata'] = _INSTALLARCMETADATA
DESCRIPTOR.message_types_by_name['InstallFirmwareRequest'] = _INSTALLFIRMWAREREQUEST
DESCRIPTOR.message_types_by_name['InstallFirmwareResponse'] = _INSTALLFIRMWARERESPONSE
DESCRIPTOR.message_types_by_name['InstallFirmwareMetadata'] = _INSTALLFIRMWAREMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstallSuccess = _reflection.GeneratedProtocolMessageType('InstallSuccess', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLSUCCESS,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallSuccess)
  ))
_sym_db.RegisterMessage(InstallSuccess)

InstallFailure = _reflection.GeneratedProtocolMessageType('InstallFailure', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLFAILURE,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallFailure)
  ))
_sym_db.RegisterMessage(InstallFailure)

InstallCrosRequest = _reflection.GeneratedProtocolMessageType('InstallCrosRequest', (_message.Message,), dict(

  DLCSpec = _reflection.GeneratedProtocolMessageType('DLCSpec', (_message.Message,), dict(
    DESCRIPTOR = _INSTALLCROSREQUEST_DLCSPEC,
    __module__ = 'chromiumos.test.api.provision_service_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallCrosRequest.DLCSpec)
    ))
  ,
  DESCRIPTOR = _INSTALLCROSREQUEST,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallCrosRequest)
  ))
_sym_db.RegisterMessage(InstallCrosRequest)
_sym_db.RegisterMessage(InstallCrosRequest.DLCSpec)

InstallCrosResponse = _reflection.GeneratedProtocolMessageType('InstallCrosResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLCROSRESPONSE,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallCrosResponse)
  ))
_sym_db.RegisterMessage(InstallCrosResponse)

InstallCrosMetadata = _reflection.GeneratedProtocolMessageType('InstallCrosMetadata', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLCROSMETADATA,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallCrosMetadata)
  ))
_sym_db.RegisterMessage(InstallCrosMetadata)

InstallLacrosRequest = _reflection.GeneratedProtocolMessageType('InstallLacrosRequest', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLLACROSREQUEST,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallLacrosRequest)
  ))
_sym_db.RegisterMessage(InstallLacrosRequest)

InstallLacrosResponse = _reflection.GeneratedProtocolMessageType('InstallLacrosResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLLACROSRESPONSE,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallLacrosResponse)
  ))
_sym_db.RegisterMessage(InstallLacrosResponse)

InstallLacrosMetadata = _reflection.GeneratedProtocolMessageType('InstallLacrosMetadata', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLLACROSMETADATA,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallLacrosMetadata)
  ))
_sym_db.RegisterMessage(InstallLacrosMetadata)

InstallAshRequest = _reflection.GeneratedProtocolMessageType('InstallAshRequest', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLASHREQUEST,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallAshRequest)
  ))
_sym_db.RegisterMessage(InstallAshRequest)

InstallAshResponse = _reflection.GeneratedProtocolMessageType('InstallAshResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLASHRESPONSE,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallAshResponse)
  ))
_sym_db.RegisterMessage(InstallAshResponse)

InstallAshMetadata = _reflection.GeneratedProtocolMessageType('InstallAshMetadata', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLASHMETADATA,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallAshMetadata)
  ))
_sym_db.RegisterMessage(InstallAshMetadata)

InstallArcRequest = _reflection.GeneratedProtocolMessageType('InstallArcRequest', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLARCREQUEST,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallArcRequest)
  ))
_sym_db.RegisterMessage(InstallArcRequest)

InstallArcResponse = _reflection.GeneratedProtocolMessageType('InstallArcResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLARCRESPONSE,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallArcResponse)
  ))
_sym_db.RegisterMessage(InstallArcResponse)

InstallArcMetadata = _reflection.GeneratedProtocolMessageType('InstallArcMetadata', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLARCMETADATA,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallArcMetadata)
  ))
_sym_db.RegisterMessage(InstallArcMetadata)

InstallFirmwareRequest = _reflection.GeneratedProtocolMessageType('InstallFirmwareRequest', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLFIRMWAREREQUEST,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallFirmwareRequest)
  ))
_sym_db.RegisterMessage(InstallFirmwareRequest)

InstallFirmwareResponse = _reflection.GeneratedProtocolMessageType('InstallFirmwareResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLFIRMWARERESPONSE,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallFirmwareResponse)
  ))
_sym_db.RegisterMessage(InstallFirmwareResponse)

InstallFirmwareMetadata = _reflection.GeneratedProtocolMessageType('InstallFirmwareMetadata', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLFIRMWAREMETADATA,
  __module__ = 'chromiumos.test.api.provision_service_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstallFirmwareMetadata)
  ))
_sym_db.RegisterMessage(InstallFirmwareMetadata)


DESCRIPTOR._options = None

_PROVISIONSERVICE = _descriptor.ServiceDescriptor(
  name='ProvisionService',
  full_name='chromiumos.test.api.ProvisionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1863,
  serialized_end=2592,
  methods=[
  _descriptor.MethodDescriptor(
    name='InstallCros',
    full_name='chromiumos.test.api.ProvisionService.InstallCros',
    index=0,
    containing_service=None,
    input_type=_INSTALLCROSREQUEST,
    output_type=chromiumos_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=_b('\322A*\n\023InstallCrosResponse\022\023InstallCrosMetadata'),
  ),
  _descriptor.MethodDescriptor(
    name='InstallLacros',
    full_name='chromiumos.test.api.ProvisionService.InstallLacros',
    index=1,
    containing_service=None,
    input_type=_INSTALLLACROSREQUEST,
    output_type=chromiumos_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=_b('\322A.\n\025InstallLacrosResponse\022\025InstallLacrosMetadata'),
  ),
  _descriptor.MethodDescriptor(
    name='InstallAsh',
    full_name='chromiumos.test.api.ProvisionService.InstallAsh',
    index=2,
    containing_service=None,
    input_type=_INSTALLASHREQUEST,
    output_type=chromiumos_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=_b('\322A(\n\022InstallAshResponse\022\022InstallAshMetadata'),
  ),
  _descriptor.MethodDescriptor(
    name='InstallArc',
    full_name='chromiumos.test.api.ProvisionService.InstallArc',
    index=3,
    containing_service=None,
    input_type=_INSTALLARCREQUEST,
    output_type=chromiumos_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=_b('\322A(\n\022InstallArcResponse\022\022InstallArcMetadata'),
  ),
  _descriptor.MethodDescriptor(
    name='InstallFirmware',
    full_name='chromiumos.test.api.ProvisionService.InstallFirmware',
    index=4,
    containing_service=None,
    input_type=_INSTALLFIRMWAREREQUEST,
    output_type=chromiumos_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=_b('\322A2\n\027InstallFirmwareResponse\022\027InstallFirmwareMetadata'),
  ),
])
_sym_db.RegisterServiceDescriptor(_PROVISIONSERVICE)

DESCRIPTOR.services_by_name['ProvisionService'] = _PROVISIONSERVICE

# @@protoc_insertion_point(module_scope)