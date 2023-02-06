# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/android_provision_metadata.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/test/api/android_provision_metadata.proto',
  package='chromiumos.test.api',
  syntax='proto3',
  serialized_options=b'Z-go.chromium.org/chromiumos/config/go/test/api',
  serialized_pb=b'\n4chromiumos/test/api/android_provision_metadata.proto\x12\x13\x63hromiumos.test.api\"\xe8\x05\n\nApkDetails\x12\x42\n\x0c\x61rchitecture\x18\x01 \x01(\x0e\x32,.chromiumos.test.api.ApkDetails.Architecture\x12=\n\nbuild_type\x18\x02 \x01(\x0e\x32).chromiumos.test.api.ApkDetails.BuildType\x12\x43\n\rbuild_purpose\x18\x03 \x01(\x0e\x32,.chromiumos.test.api.ApkDetails.BuildPurpose\x12\x38\n\x07\x64\x65nsity\x18\x04 \x01(\x0e\x32\'.chromiumos.test.api.ApkDetails.Density\"W\n\x0c\x41rchitecture\x12\x1c\n\x18\x41RCHITECTURE_UNSPECIFIED\x10\x00\x12\t\n\x05\x41RMV7\x10\x01\x12\t\n\x05\x41RM64\x10\x02\x12\x07\n\x03X86\x10\x03\x12\n\n\x06X86_64\x10\x04\"\xc1\x01\n\tBuildType\x12\x1a\n\x16\x42UILD_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rPHONE_PRE_LMP\x10\x01\x12\r\n\tPHONE_LMP\x10\x02\x12\r\n\tPHONE_MNC\x10\x03\x12\x0c\n\x08PHONE_PI\x10\x04\x12\r\n\tPHONE_RVC\x10\x05\x12\x0c\n\x08PHONE_SC\x10\x06\x12\x0e\n\nPHONE_NEXT\x10\x07\x12\x0c\n\x08PHONE_GO\x10\x08\x12\x0e\n\nPHONE_GO_R\x10\t\x12\x0e\n\nPHONE_GO_S\x10\n\"`\n\x0c\x42uildPurpose\x12\x1d\n\x19\x42UILD_PURPOSE_UNSPECIFIED\x10\x00\x12\x07\n\x03RAW\x10\x01\x12\x0b\n\x07RELEASE\x10\x02\x12\t\n\x05\x44\x45\x42UG\x10\x03\x12\x10\n\x0c\x44\x45\x42UG_SHRUNK\x10\x04\"Y\n\x07\x44\x65nsity\x12\x17\n\x13\x44\x45NSITY_UNSPECIFIED\x10\x00\x12\x08\n\x04MDPI\x10\x01\x12\x08\n\x04HDPI\x10\x02\x12\t\n\x05XHDPI\x10\x03\x12\n\n\x06XXHDPI\x10\x04\x12\n\n\x06\x41LLDPI\x10\x05\"\xea\x01\n\x0b\x43IPDPackage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x03ref\x18\x02 \x01(\tH\x00\x12\r\n\x03tag\x18\x03 \x01(\tH\x00\x12\x15\n\x0binstance_id\x18\x04 \x01(\tH\x00\x12\x13\n\x0bservice_url\x18\x05 \x01(\t\x12<\n\x0f\x61ndroid_package\x18\x06 \x01(\x0e\x32#.chromiumos.test.api.AndroidPackage\x12\x34\n\x0b\x61pk_details\x18\x07 \x01(\x0b\x32\x1f.chromiumos.test.api.ApkDetailsB\x0f\n\rversion_oneof\"Z\n\x1f\x41ndroidProvisionRequestMetadata\x12\x37\n\rcipd_packages\x18\x01 \x03(\x0b\x32 .chromiumos.test.api.CIPDPackage\"=\n\x17InstalledAndroidPackage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cversion_code\x18\x02 \x01(\t\"t\n AndroidProvisionResponseMetadata\x12P\n\x1ainstalled_android_packages\x18\x01 \x03(\x0b\x32,.chromiumos.test.api.InstalledAndroidPackage*?\n\x0e\x41ndroidPackage\x12\x1f\n\x1b\x41NDROID_PACKAGE_UNSPECIFIED\x10\x00\x12\x0c\n\x08GMS_CORE\x10\x01\x42/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3'
)

_ANDROIDPACKAGE = _descriptor.EnumDescriptor(
  name='AndroidPackage',
  full_name='chromiumos.test.api.AndroidPackage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANDROID_PACKAGE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GMS_CORE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1334,
  serialized_end=1397,
)
_sym_db.RegisterEnumDescriptor(_ANDROIDPACKAGE)

AndroidPackage = enum_type_wrapper.EnumTypeWrapper(_ANDROIDPACKAGE)
ANDROID_PACKAGE_UNSPECIFIED = 0
GMS_CORE = 1


_APKDETAILS_ARCHITECTURE = _descriptor.EnumDescriptor(
  name='Architecture',
  full_name='chromiumos.test.api.ApkDetails.Architecture',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ARCHITECTURE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARMV7', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARM64', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='X86', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='X86_64', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=350,
  serialized_end=437,
)
_sym_db.RegisterEnumDescriptor(_APKDETAILS_ARCHITECTURE)

_APKDETAILS_BUILDTYPE = _descriptor.EnumDescriptor(
  name='BuildType',
  full_name='chromiumos.test.api.ApkDetails.BuildType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUILD_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_PRE_LMP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_LMP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_MNC', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_PI', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_RVC', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_SC', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NEXT', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_GO', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_GO_R', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_GO_S', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=440,
  serialized_end=633,
)
_sym_db.RegisterEnumDescriptor(_APKDETAILS_BUILDTYPE)

_APKDETAILS_BUILDPURPOSE = _descriptor.EnumDescriptor(
  name='BuildPurpose',
  full_name='chromiumos.test.api.ApkDetails.BuildPurpose',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUILD_PURPOSE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELEASE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBUG', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBUG_SHRUNK', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=635,
  serialized_end=731,
)
_sym_db.RegisterEnumDescriptor(_APKDETAILS_BUILDPURPOSE)

_APKDETAILS_DENSITY = _descriptor.EnumDescriptor(
  name='Density',
  full_name='chromiumos.test.api.ApkDetails.Density',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DENSITY_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MDPI', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDPI', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XHDPI', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XXHDPI', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLDPI', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=733,
  serialized_end=822,
)
_sym_db.RegisterEnumDescriptor(_APKDETAILS_DENSITY)


_APKDETAILS = _descriptor.Descriptor(
  name='ApkDetails',
  full_name='chromiumos.test.api.ApkDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='architecture', full_name='chromiumos.test.api.ApkDetails.architecture', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_type', full_name='chromiumos.test.api.ApkDetails.build_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_purpose', full_name='chromiumos.test.api.ApkDetails.build_purpose', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='density', full_name='chromiumos.test.api.ApkDetails.density', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _APKDETAILS_ARCHITECTURE,
    _APKDETAILS_BUILDTYPE,
    _APKDETAILS_BUILDPURPOSE,
    _APKDETAILS_DENSITY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=822,
)


_CIPDPACKAGE = _descriptor.Descriptor(
  name='CIPDPackage',
  full_name='chromiumos.test.api.CIPDPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromiumos.test.api.CIPDPackage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref', full_name='chromiumos.test.api.CIPDPackage.ref', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='chromiumos.test.api.CIPDPackage.tag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='chromiumos.test.api.CIPDPackage.instance_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_url', full_name='chromiumos.test.api.CIPDPackage.service_url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='android_package', full_name='chromiumos.test.api.CIPDPackage.android_package', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apk_details', full_name='chromiumos.test.api.CIPDPackage.apk_details', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
      name='version_oneof', full_name='chromiumos.test.api.CIPDPackage.version_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=825,
  serialized_end=1059,
)


_ANDROIDPROVISIONREQUESTMETADATA = _descriptor.Descriptor(
  name='AndroidProvisionRequestMetadata',
  full_name='chromiumos.test.api.AndroidProvisionRequestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cipd_packages', full_name='chromiumos.test.api.AndroidProvisionRequestMetadata.cipd_packages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1061,
  serialized_end=1151,
)


_INSTALLEDANDROIDPACKAGE = _descriptor.Descriptor(
  name='InstalledAndroidPackage',
  full_name='chromiumos.test.api.InstalledAndroidPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromiumos.test.api.InstalledAndroidPackage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_code', full_name='chromiumos.test.api.InstalledAndroidPackage.version_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1153,
  serialized_end=1214,
)


_ANDROIDPROVISIONRESPONSEMETADATA = _descriptor.Descriptor(
  name='AndroidProvisionResponseMetadata',
  full_name='chromiumos.test.api.AndroidProvisionResponseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='installed_android_packages', full_name='chromiumos.test.api.AndroidProvisionResponseMetadata.installed_android_packages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1216,
  serialized_end=1332,
)

_APKDETAILS.fields_by_name['architecture'].enum_type = _APKDETAILS_ARCHITECTURE
_APKDETAILS.fields_by_name['build_type'].enum_type = _APKDETAILS_BUILDTYPE
_APKDETAILS.fields_by_name['build_purpose'].enum_type = _APKDETAILS_BUILDPURPOSE
_APKDETAILS.fields_by_name['density'].enum_type = _APKDETAILS_DENSITY
_APKDETAILS_ARCHITECTURE.containing_type = _APKDETAILS
_APKDETAILS_BUILDTYPE.containing_type = _APKDETAILS
_APKDETAILS_BUILDPURPOSE.containing_type = _APKDETAILS
_APKDETAILS_DENSITY.containing_type = _APKDETAILS
_CIPDPACKAGE.fields_by_name['android_package'].enum_type = _ANDROIDPACKAGE
_CIPDPACKAGE.fields_by_name['apk_details'].message_type = _APKDETAILS
_CIPDPACKAGE.oneofs_by_name['version_oneof'].fields.append(
  _CIPDPACKAGE.fields_by_name['ref'])
_CIPDPACKAGE.fields_by_name['ref'].containing_oneof = _CIPDPACKAGE.oneofs_by_name['version_oneof']
_CIPDPACKAGE.oneofs_by_name['version_oneof'].fields.append(
  _CIPDPACKAGE.fields_by_name['tag'])
_CIPDPACKAGE.fields_by_name['tag'].containing_oneof = _CIPDPACKAGE.oneofs_by_name['version_oneof']
_CIPDPACKAGE.oneofs_by_name['version_oneof'].fields.append(
  _CIPDPACKAGE.fields_by_name['instance_id'])
_CIPDPACKAGE.fields_by_name['instance_id'].containing_oneof = _CIPDPACKAGE.oneofs_by_name['version_oneof']
_ANDROIDPROVISIONREQUESTMETADATA.fields_by_name['cipd_packages'].message_type = _CIPDPACKAGE
_ANDROIDPROVISIONRESPONSEMETADATA.fields_by_name['installed_android_packages'].message_type = _INSTALLEDANDROIDPACKAGE
DESCRIPTOR.message_types_by_name['ApkDetails'] = _APKDETAILS
DESCRIPTOR.message_types_by_name['CIPDPackage'] = _CIPDPACKAGE
DESCRIPTOR.message_types_by_name['AndroidProvisionRequestMetadata'] = _ANDROIDPROVISIONREQUESTMETADATA
DESCRIPTOR.message_types_by_name['InstalledAndroidPackage'] = _INSTALLEDANDROIDPACKAGE
DESCRIPTOR.message_types_by_name['AndroidProvisionResponseMetadata'] = _ANDROIDPROVISIONRESPONSEMETADATA
DESCRIPTOR.enum_types_by_name['AndroidPackage'] = _ANDROIDPACKAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApkDetails = _reflection.GeneratedProtocolMessageType('ApkDetails', (_message.Message,), {
  'DESCRIPTOR' : _APKDETAILS,
  '__module__' : 'chromiumos.test.api.android_provision_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.ApkDetails)
  })
_sym_db.RegisterMessage(ApkDetails)

CIPDPackage = _reflection.GeneratedProtocolMessageType('CIPDPackage', (_message.Message,), {
  'DESCRIPTOR' : _CIPDPACKAGE,
  '__module__' : 'chromiumos.test.api.android_provision_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.CIPDPackage)
  })
_sym_db.RegisterMessage(CIPDPackage)

AndroidProvisionRequestMetadata = _reflection.GeneratedProtocolMessageType('AndroidProvisionRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ANDROIDPROVISIONREQUESTMETADATA,
  '__module__' : 'chromiumos.test.api.android_provision_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.AndroidProvisionRequestMetadata)
  })
_sym_db.RegisterMessage(AndroidProvisionRequestMetadata)

InstalledAndroidPackage = _reflection.GeneratedProtocolMessageType('InstalledAndroidPackage', (_message.Message,), {
  'DESCRIPTOR' : _INSTALLEDANDROIDPACKAGE,
  '__module__' : 'chromiumos.test.api.android_provision_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.InstalledAndroidPackage)
  })
_sym_db.RegisterMessage(InstalledAndroidPackage)

AndroidProvisionResponseMetadata = _reflection.GeneratedProtocolMessageType('AndroidProvisionResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ANDROIDPROVISIONRESPONSEMETADATA,
  '__module__' : 'chromiumos.test.api.android_provision_metadata_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.AndroidProvisionResponseMetadata)
  })
_sym_db.RegisterMessage(AndroidProvisionResponseMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
