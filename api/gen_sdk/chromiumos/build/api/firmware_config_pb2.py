# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/build/api/firmware_config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.build.api import portage_pb2 as chromiumos_dot_build_dot_api_dot_portage__pb2
from chromite.api.gen_sdk.chromiumos import storage_path_pb2 as chromiumos_dot_storage__path__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/build/api/firmware_config.proto',
  package='chromiumos.build.api',
  syntax='proto3',
  serialized_options=b'Z.go.chromium.org/chromiumos/config/go/build/api',
  serialized_pb=b'\n*chromiumos/build/api/firmware_config.proto\x12\x14\x63hromiumos.build.api\x1a\"chromiumos/build/api/portage.proto\x1a\x1d\x63hromiumos/storage_path.proto\"=\n\x0c\x46irmwareType\"-\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04MAIN\x10\x01\x12\x06\n\x02\x45\x43\x10\x02\x12\x06\n\x02PD\x10\x03\"6\n\x07Version\x12\r\n\x05major\x18\x01 \x01(\x05\x12\r\n\x05minor\x18\x02 \x01(\x05\x12\r\n\x05patch\x18\x03 \x01(\x05\"\xeb\x01\n\x0f\x46irmwarePayload\x12\x36\n\x13\x66irmware_image_path\x18\x05 \x01(\x0b\x32\x17.chromiumos.StoragePathH\x00\x12!\n\x13\x66irmware_image_name\x18\x02 \x01(\tB\x02\x18\x01H\x00\x12\x35\n\x04type\x18\x03 \x01(\x0e\x32\'.chromiumos.build.api.FirmwareType.Type\x12.\n\x07version\x18\x04 \x01(\x0b\x32\x1d.chromiumos.build.api.VersionB\x10\n\x0e\x66irmware_imageJ\x04\x08\x01\x10\x02\"\x92\x02\n\x0e\x46irmwareConfig\x12>\n\x0fmain_ro_payload\x18\x01 \x01(\x0b\x32%.chromiumos.build.api.FirmwarePayload\x12>\n\x0fmain_rw_payload\x18\x02 \x01(\x0b\x32%.chromiumos.build.api.FirmwarePayload\x12<\n\rec_ro_payload\x18\x03 \x01(\x0b\x32%.chromiumos.build.api.FirmwarePayload\x12<\n\rpd_ro_payload\x18\x05 \x01(\x0b\x32%.chromiumos.build.api.FirmwarePayloadJ\x04\x08\x04\x10\x05\"\xa5\x02\n\x08\x46irmware\x12\x42\n\rbuild_targets\x18\x01 \x01(\x0b\x32+.chromiumos.build.api.Firmware.BuildTargets\x1a\xd4\x01\n\x0c\x42uildTargets\x12\x10\n\x08\x63oreboot\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65pthcharge\x18\x02 \x01(\t\x12\n\n\x02\x65\x63\x18\x03 \x01(\t\x12\x11\n\tec_extras\x18\x04 \x03(\t\x12\x12\n\nlibpayload\x18\x05 \x01(\t\x12G\n\x14portage_build_target\x18\x06 \x01(\x0b\x32).chromiumos.build.api.Portage.BuildTarget\x12\x11\n\tzephyr_ec\x18\x07 \x01(\t\x12\x0e\n\x06\x62mpblk\x18\x08 \x01(\t\"Y\n\x13\x46irmwareBuildConfig\x12\x42\n\rbuild_targets\x18\x01 \x01(\x0b\x32+.chromiumos.build.api.Firmware.BuildTargetsB0Z.go.chromium.org/chromiumos/config/go/build/apib\x06proto3'
  ,
  dependencies=[chromiumos_dot_build_dot_api_dot_portage__pb2.DESCRIPTOR,chromiumos_dot_storage__path__pb2.DESCRIPTOR,])



_FIRMWARETYPE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='chromiumos.build.api.FirmwareType.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAIN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EC', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PD', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=151,
  serialized_end=196,
)
_sym_db.RegisterEnumDescriptor(_FIRMWARETYPE_TYPE)


_FIRMWARETYPE = _descriptor.Descriptor(
  name='FirmwareType',
  full_name='chromiumos.build.api.FirmwareType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FIRMWARETYPE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=196,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='chromiumos.build.api.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='chromiumos.build.api.Version.major', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor', full_name='chromiumos.build.api.Version.minor', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patch', full_name='chromiumos.build.api.Version.patch', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=198,
  serialized_end=252,
)


_FIRMWAREPAYLOAD = _descriptor.Descriptor(
  name='FirmwarePayload',
  full_name='chromiumos.build.api.FirmwarePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firmware_image_path', full_name='chromiumos.build.api.FirmwarePayload.firmware_image_path', index=0,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firmware_image_name', full_name='chromiumos.build.api.FirmwarePayload.firmware_image_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='chromiumos.build.api.FirmwarePayload.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='chromiumos.build.api.FirmwarePayload.version', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
      name='firmware_image', full_name='chromiumos.build.api.FirmwarePayload.firmware_image',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=255,
  serialized_end=490,
)


_FIRMWARECONFIG = _descriptor.Descriptor(
  name='FirmwareConfig',
  full_name='chromiumos.build.api.FirmwareConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='main_ro_payload', full_name='chromiumos.build.api.FirmwareConfig.main_ro_payload', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='main_rw_payload', full_name='chromiumos.build.api.FirmwareConfig.main_rw_payload', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ec_ro_payload', full_name='chromiumos.build.api.FirmwareConfig.ec_ro_payload', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pd_ro_payload', full_name='chromiumos.build.api.FirmwareConfig.pd_ro_payload', index=3,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=493,
  serialized_end=767,
)


_FIRMWARE_BUILDTARGETS = _descriptor.Descriptor(
  name='BuildTargets',
  full_name='chromiumos.build.api.Firmware.BuildTargets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coreboot', full_name='chromiumos.build.api.Firmware.BuildTargets.coreboot', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depthcharge', full_name='chromiumos.build.api.Firmware.BuildTargets.depthcharge', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ec', full_name='chromiumos.build.api.Firmware.BuildTargets.ec', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ec_extras', full_name='chromiumos.build.api.Firmware.BuildTargets.ec_extras', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='libpayload', full_name='chromiumos.build.api.Firmware.BuildTargets.libpayload', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portage_build_target', full_name='chromiumos.build.api.Firmware.BuildTargets.portage_build_target', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zephyr_ec', full_name='chromiumos.build.api.Firmware.BuildTargets.zephyr_ec', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bmpblk', full_name='chromiumos.build.api.Firmware.BuildTargets.bmpblk', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=851,
  serialized_end=1063,
)

_FIRMWARE = _descriptor.Descriptor(
  name='Firmware',
  full_name='chromiumos.build.api.Firmware',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_targets', full_name='chromiumos.build.api.Firmware.build_targets', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FIRMWARE_BUILDTARGETS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=770,
  serialized_end=1063,
)


_FIRMWAREBUILDCONFIG = _descriptor.Descriptor(
  name='FirmwareBuildConfig',
  full_name='chromiumos.build.api.FirmwareBuildConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_targets', full_name='chromiumos.build.api.FirmwareBuildConfig.build_targets', index=0,
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
  serialized_start=1065,
  serialized_end=1154,
)

_FIRMWARETYPE_TYPE.containing_type = _FIRMWARETYPE
_FIRMWAREPAYLOAD.fields_by_name['firmware_image_path'].message_type = chromiumos_dot_storage__path__pb2._STORAGEPATH
_FIRMWAREPAYLOAD.fields_by_name['type'].enum_type = _FIRMWARETYPE_TYPE
_FIRMWAREPAYLOAD.fields_by_name['version'].message_type = _VERSION
_FIRMWAREPAYLOAD.oneofs_by_name['firmware_image'].fields.append(
  _FIRMWAREPAYLOAD.fields_by_name['firmware_image_path'])
_FIRMWAREPAYLOAD.fields_by_name['firmware_image_path'].containing_oneof = _FIRMWAREPAYLOAD.oneofs_by_name['firmware_image']
_FIRMWAREPAYLOAD.oneofs_by_name['firmware_image'].fields.append(
  _FIRMWAREPAYLOAD.fields_by_name['firmware_image_name'])
_FIRMWAREPAYLOAD.fields_by_name['firmware_image_name'].containing_oneof = _FIRMWAREPAYLOAD.oneofs_by_name['firmware_image']
_FIRMWARECONFIG.fields_by_name['main_ro_payload'].message_type = _FIRMWAREPAYLOAD
_FIRMWARECONFIG.fields_by_name['main_rw_payload'].message_type = _FIRMWAREPAYLOAD
_FIRMWARECONFIG.fields_by_name['ec_ro_payload'].message_type = _FIRMWAREPAYLOAD
_FIRMWARECONFIG.fields_by_name['pd_ro_payload'].message_type = _FIRMWAREPAYLOAD
_FIRMWARE_BUILDTARGETS.fields_by_name['portage_build_target'].message_type = chromiumos_dot_build_dot_api_dot_portage__pb2._PORTAGE_BUILDTARGET
_FIRMWARE_BUILDTARGETS.containing_type = _FIRMWARE
_FIRMWARE.fields_by_name['build_targets'].message_type = _FIRMWARE_BUILDTARGETS
_FIRMWAREBUILDCONFIG.fields_by_name['build_targets'].message_type = _FIRMWARE_BUILDTARGETS
DESCRIPTOR.message_types_by_name['FirmwareType'] = _FIRMWARETYPE
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['FirmwarePayload'] = _FIRMWAREPAYLOAD
DESCRIPTOR.message_types_by_name['FirmwareConfig'] = _FIRMWARECONFIG
DESCRIPTOR.message_types_by_name['Firmware'] = _FIRMWARE
DESCRIPTOR.message_types_by_name['FirmwareBuildConfig'] = _FIRMWAREBUILDCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FirmwareType = _reflection.GeneratedProtocolMessageType('FirmwareType', (_message.Message,), {
  'DESCRIPTOR' : _FIRMWARETYPE,
  '__module__' : 'chromiumos.build.api.firmware_config_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.build.api.FirmwareType)
  })
_sym_db.RegisterMessage(FirmwareType)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'chromiumos.build.api.firmware_config_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.build.api.Version)
  })
_sym_db.RegisterMessage(Version)

FirmwarePayload = _reflection.GeneratedProtocolMessageType('FirmwarePayload', (_message.Message,), {
  'DESCRIPTOR' : _FIRMWAREPAYLOAD,
  '__module__' : 'chromiumos.build.api.firmware_config_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.build.api.FirmwarePayload)
  })
_sym_db.RegisterMessage(FirmwarePayload)

FirmwareConfig = _reflection.GeneratedProtocolMessageType('FirmwareConfig', (_message.Message,), {
  'DESCRIPTOR' : _FIRMWARECONFIG,
  '__module__' : 'chromiumos.build.api.firmware_config_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.build.api.FirmwareConfig)
  })
_sym_db.RegisterMessage(FirmwareConfig)

Firmware = _reflection.GeneratedProtocolMessageType('Firmware', (_message.Message,), {

  'BuildTargets' : _reflection.GeneratedProtocolMessageType('BuildTargets', (_message.Message,), {
    'DESCRIPTOR' : _FIRMWARE_BUILDTARGETS,
    '__module__' : 'chromiumos.build.api.firmware_config_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.build.api.Firmware.BuildTargets)
    })
  ,
  'DESCRIPTOR' : _FIRMWARE,
  '__module__' : 'chromiumos.build.api.firmware_config_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.build.api.Firmware)
  })
_sym_db.RegisterMessage(Firmware)
_sym_db.RegisterMessage(Firmware.BuildTargets)

FirmwareBuildConfig = _reflection.GeneratedProtocolMessageType('FirmwareBuildConfig', (_message.Message,), {
  'DESCRIPTOR' : _FIRMWAREBUILDCONFIG,
  '__module__' : 'chromiumos.build.api.firmware_config_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.build.api.FirmwareBuildConfig)
  })
_sym_db.RegisterMessage(FirmwareBuildConfig)


DESCRIPTOR._options = None
_FIRMWAREPAYLOAD.fields_by_name['firmware_image_name']._options = None
# @@protoc_insertion_point(module_scope)
