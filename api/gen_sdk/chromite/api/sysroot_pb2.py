# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/sysroot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen_sdk.chromiumos import common_pb2 as chromiumos_dot_common__pb2
from chromite.api.gen_sdk.chromiumos import metrics_pb2 as chromiumos_dot_metrics__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromite/api/sysroot.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=_b('Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api'),
  serialized_pb=_b('\n\x1a\x63hromite/api/sysroot.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x17\x63hromiumos/common.proto\x1a\x18\x63hromiumos/metrics.proto\"F\n\x07Sysroot\x12\x0c\n\x04path\x18\x01 \x01(\t\x12-\n\x0c\x62uild_target\x18\x02 \x01(\x0b\x32\x17.chromiumos.BuildTarget\"\x17\n\x07Profile\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xce\x02\n\x14SysrootCreateRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x37\n\x05\x66lags\x18\x02 \x01(\x0b\x32(.chromite.api.SysrootCreateRequest.Flags\x12&\n\x07profile\x18\x03 \x01(\x0b\x32\x15.chromite.api.Profile\x12\"\n\x06\x63hroot\x18\x04 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\x35\n\x0fpackage_indexes\x18\x05 \x03(\x0b\x32\x1c.chromiumos.PackageIndexInfo\x1aK\n\x05\x46lags\x12\x16\n\x0e\x63hroot_current\x18\x01 \x01(\x08\x12\x0f\n\x07replace\x18\x02 \x01(\x08\x12\x19\n\x11toolchain_changed\x18\x03 \x01(\x08\"?\n\x15SysrootCreateResponse\x12&\n\x07sysroot\x18\x01 \x01(\x0b\x32\x15.chromite.api.Sysroot\"\xc9\x01\n\x1dSysrootGenerateArchiveRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\"\n\x06\x63hroot\x18\x02 \x01(\x0b\x32\x12.chromiumos.Chroot\x12)\n\x08packages\x18\x03 \x03(\x0b\x32\x17.chromiumos.PackageInfo\x12*\n\ntarget_dir\x18\x04 \x01(\x0b\x32\x16.chromiumos.ResultPath\"K\n\x1eSysrootGenerateArchiveResponse\x12)\n\x0fsysroot_archive\x18\x01 \x01(\x0b\x32\x10.chromiumos.Path\"\xdd\x01\n\x17InstallToolchainRequest\x12&\n\x07sysroot\x18\x01 \x01(\x0b\x32\x15.chromite.api.Sysroot\x12:\n\x05\x66lags\x18\x02 \x01(\x0b\x32+.chromite.api.InstallToolchainRequest.Flags\x12\"\n\x06\x63hroot\x18\x03 \x01(\x0b\x32\x12.chromiumos.Chroot\x1a:\n\x05\x46lags\x12\x16\n\x0e\x63ompile_source\x18\x01 \x01(\x08\x12\x19\n\x11toolchain_changed\x18\x02 \x01(\x08\"L\n\x18InstallToolchainResponse\x12\x30\n\x0f\x66\x61iled_packages\x18\x01 \x03(\x0b\x32\x17.chromiumos.PackageInfo\"\xc6\x03\n\x16InstallPackagesRequest\x12&\n\x07sysroot\x18\x01 \x01(\x0b\x32\x15.chromite.api.Sysroot\x12\x39\n\x05\x66lags\x18\x02 \x01(\x0b\x32*.chromite.api.InstallPackagesRequest.Flags\x12)\n\x08packages\x18\x03 \x03(\x0b\x32\x17.chromiumos.PackageInfo\x12\"\n\x06\x63hroot\x18\x04 \x01(\x0b\x32\x12.chromiumos.Chroot\x12&\n\tuse_flags\x18\x05 \x03(\x0b\x32\x13.chromiumos.UseFlag\x12+\n\x0bgoma_config\x18\x06 \x01(\x0b\x32\x16.chromiumos.GomaConfig\x12\x35\n\x0fpackage_indexes\x18\x07 \x03(\x0b\x32\x1c.chromiumos.PackageIndexInfo\x1an\n\x05\x46lags\x12\x16\n\x0e\x63ompile_source\x18\x01 \x01(\x08\x12\x10\n\x08use_goma\x18\x03 \x01(\x08\x12\x19\n\x11toolchain_changed\x18\x04 \x01(\x08\x12\x0e\n\x06\x64ryrun\x18\x05 \x01(\x08J\x04\x08\x02\x10\x03R\nevent_file\"\xa7\x01\n\x17InstallPackagesResponse\x12\x30\n\x0f\x66\x61iled_packages\x18\x01 \x03(\x0b\x32\x17.chromiumos.PackageInfo\x12\'\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x17.chromiumos.MetricEvent\x12\x31\n\x0egoma_artifacts\x18\x03 \x01(\x0b\x32\x19.chromiumos.GomaArtifacts\"\xb4\x01\n CreateSimpleChromeSysrootRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x11\n\tuse_flags\x18\x02 \x03(\t\x12*\n\ntarget_dir\x18\x03 \x01(\x0b\x32\x16.chromiumos.ResultPath\x12\"\n\x06\x63hroot\x18\x04 \x01(\x0b\x32\x12.chromiumos.Chroot\"N\n!CreateSimpleChromeSysrootResponse\x12)\n\x0fsysroot_archive\x18\x01 \x01(\x0b\x32\x10.chromiumos.Path2\xa3\x04\n\x0eSysrootService\x12Q\n\x06\x43reate\x12\".chromite.api.SysrootCreateRequest\x1a#.chromite.api.SysrootCreateResponse\x12l\n\x0fGenerateArchive\x12+.chromite.api.SysrootGenerateArchiveRequest\x1a,.chromite.api.SysrootGenerateArchiveResponse\x12\x61\n\x10InstallToolchain\x12%.chromite.api.InstallToolchainRequest\x1a&.chromite.api.InstallToolchainResponse\x12^\n\x0fInstallPackages\x12$.chromite.api.InstallPackagesRequest\x1a%.chromite.api.InstallPackagesResponse\x12|\n\x19\x43reateSimpleChromeSysroot\x12..chromite.api.CreateSimpleChromeSysrootRequest\x1a/.chromite.api.CreateSimpleChromeSysrootResponse\x1a\x0f\xc2\xed\x1a\x0b\n\x07sysroot\x10\x01\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3')
  ,
  dependencies=[chromite_dot_api_dot_build__api__pb2.DESCRIPTOR,chromiumos_dot_common__pb2.DESCRIPTOR,chromiumos_dot_metrics__pb2.DESCRIPTOR,])




_SYSROOT = _descriptor.Descriptor(
  name='Sysroot',
  full_name='chromite.api.Sysroot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='chromite.api.Sysroot.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_target', full_name='chromite.api.Sysroot.build_target', index=1,
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
  serialized_start=125,
  serialized_end=195,
)


_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='chromite.api.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromite.api.Profile.name', index=0,
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
  serialized_start=197,
  serialized_end=220,
)


_SYSROOTCREATEREQUEST_FLAGS = _descriptor.Descriptor(
  name='Flags',
  full_name='chromite.api.SysrootCreateRequest.Flags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chroot_current', full_name='chromite.api.SysrootCreateRequest.Flags.chroot_current', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replace', full_name='chromite.api.SysrootCreateRequest.Flags.replace', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolchain_changed', full_name='chromite.api.SysrootCreateRequest.Flags.toolchain_changed', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=482,
  serialized_end=557,
)

_SYSROOTCREATEREQUEST = _descriptor.Descriptor(
  name='SysrootCreateRequest',
  full_name='chromite.api.SysrootCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_target', full_name='chromite.api.SysrootCreateRequest.build_target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='chromite.api.SysrootCreateRequest.flags', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile', full_name='chromite.api.SysrootCreateRequest.profile', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.SysrootCreateRequest.chroot', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_indexes', full_name='chromite.api.SysrootCreateRequest.package_indexes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SYSROOTCREATEREQUEST_FLAGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=557,
)


_SYSROOTCREATERESPONSE = _descriptor.Descriptor(
  name='SysrootCreateResponse',
  full_name='chromite.api.SysrootCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sysroot', full_name='chromite.api.SysrootCreateResponse.sysroot', index=0,
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
  serialized_start=559,
  serialized_end=622,
)


_SYSROOTGENERATEARCHIVEREQUEST = _descriptor.Descriptor(
  name='SysrootGenerateArchiveRequest',
  full_name='chromite.api.SysrootGenerateArchiveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_target', full_name='chromite.api.SysrootGenerateArchiveRequest.build_target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.SysrootGenerateArchiveRequest.chroot', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packages', full_name='chromite.api.SysrootGenerateArchiveRequest.packages', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_dir', full_name='chromite.api.SysrootGenerateArchiveRequest.target_dir', index=3,
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
  ],
  serialized_start=625,
  serialized_end=826,
)


_SYSROOTGENERATEARCHIVERESPONSE = _descriptor.Descriptor(
  name='SysrootGenerateArchiveResponse',
  full_name='chromite.api.SysrootGenerateArchiveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sysroot_archive', full_name='chromite.api.SysrootGenerateArchiveResponse.sysroot_archive', index=0,
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
  serialized_start=828,
  serialized_end=903,
)


_INSTALLTOOLCHAINREQUEST_FLAGS = _descriptor.Descriptor(
  name='Flags',
  full_name='chromite.api.InstallToolchainRequest.Flags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='compile_source', full_name='chromite.api.InstallToolchainRequest.Flags.compile_source', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolchain_changed', full_name='chromite.api.InstallToolchainRequest.Flags.toolchain_changed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1069,
  serialized_end=1127,
)

_INSTALLTOOLCHAINREQUEST = _descriptor.Descriptor(
  name='InstallToolchainRequest',
  full_name='chromite.api.InstallToolchainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sysroot', full_name='chromite.api.InstallToolchainRequest.sysroot', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='chromite.api.InstallToolchainRequest.flags', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.InstallToolchainRequest.chroot', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INSTALLTOOLCHAINREQUEST_FLAGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=906,
  serialized_end=1127,
)


_INSTALLTOOLCHAINRESPONSE = _descriptor.Descriptor(
  name='InstallToolchainResponse',
  full_name='chromite.api.InstallToolchainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failed_packages', full_name='chromite.api.InstallToolchainResponse.failed_packages', index=0,
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
  serialized_start=1129,
  serialized_end=1205,
)


_INSTALLPACKAGESREQUEST_FLAGS = _descriptor.Descriptor(
  name='Flags',
  full_name='chromite.api.InstallPackagesRequest.Flags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='compile_source', full_name='chromite.api.InstallPackagesRequest.Flags.compile_source', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_goma', full_name='chromite.api.InstallPackagesRequest.Flags.use_goma', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolchain_changed', full_name='chromite.api.InstallPackagesRequest.Flags.toolchain_changed', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dryrun', full_name='chromite.api.InstallPackagesRequest.Flags.dryrun', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1552,
  serialized_end=1662,
)

_INSTALLPACKAGESREQUEST = _descriptor.Descriptor(
  name='InstallPackagesRequest',
  full_name='chromite.api.InstallPackagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sysroot', full_name='chromite.api.InstallPackagesRequest.sysroot', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='chromite.api.InstallPackagesRequest.flags', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packages', full_name='chromite.api.InstallPackagesRequest.packages', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.InstallPackagesRequest.chroot', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_flags', full_name='chromite.api.InstallPackagesRequest.use_flags', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goma_config', full_name='chromite.api.InstallPackagesRequest.goma_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_indexes', full_name='chromite.api.InstallPackagesRequest.package_indexes', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INSTALLPACKAGESREQUEST_FLAGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1208,
  serialized_end=1662,
)


_INSTALLPACKAGESRESPONSE = _descriptor.Descriptor(
  name='InstallPackagesResponse',
  full_name='chromite.api.InstallPackagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failed_packages', full_name='chromite.api.InstallPackagesResponse.failed_packages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='chromite.api.InstallPackagesResponse.events', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goma_artifacts', full_name='chromite.api.InstallPackagesResponse.goma_artifacts', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1665,
  serialized_end=1832,
)


_CREATESIMPLECHROMESYSROOTREQUEST = _descriptor.Descriptor(
  name='CreateSimpleChromeSysrootRequest',
  full_name='chromite.api.CreateSimpleChromeSysrootRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_target', full_name='chromite.api.CreateSimpleChromeSysrootRequest.build_target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_flags', full_name='chromite.api.CreateSimpleChromeSysrootRequest.use_flags', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_dir', full_name='chromite.api.CreateSimpleChromeSysrootRequest.target_dir', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.CreateSimpleChromeSysrootRequest.chroot', index=3,
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
  ],
  serialized_start=1835,
  serialized_end=2015,
)


_CREATESIMPLECHROMESYSROOTRESPONSE = _descriptor.Descriptor(
  name='CreateSimpleChromeSysrootResponse',
  full_name='chromite.api.CreateSimpleChromeSysrootResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sysroot_archive', full_name='chromite.api.CreateSimpleChromeSysrootResponse.sysroot_archive', index=0,
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
  serialized_start=2017,
  serialized_end=2095,
)

_SYSROOT.fields_by_name['build_target'].message_type = chromiumos_dot_common__pb2._BUILDTARGET
_SYSROOTCREATEREQUEST_FLAGS.containing_type = _SYSROOTCREATEREQUEST
_SYSROOTCREATEREQUEST.fields_by_name['build_target'].message_type = chromiumos_dot_common__pb2._BUILDTARGET
_SYSROOTCREATEREQUEST.fields_by_name['flags'].message_type = _SYSROOTCREATEREQUEST_FLAGS
_SYSROOTCREATEREQUEST.fields_by_name['profile'].message_type = _PROFILE
_SYSROOTCREATEREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_SYSROOTCREATEREQUEST.fields_by_name['package_indexes'].message_type = chromiumos_dot_common__pb2._PACKAGEINDEXINFO
_SYSROOTCREATERESPONSE.fields_by_name['sysroot'].message_type = _SYSROOT
_SYSROOTGENERATEARCHIVEREQUEST.fields_by_name['build_target'].message_type = chromiumos_dot_common__pb2._BUILDTARGET
_SYSROOTGENERATEARCHIVEREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_SYSROOTGENERATEARCHIVEREQUEST.fields_by_name['packages'].message_type = chromiumos_dot_common__pb2._PACKAGEINFO
_SYSROOTGENERATEARCHIVEREQUEST.fields_by_name['target_dir'].message_type = chromiumos_dot_common__pb2._RESULTPATH
_SYSROOTGENERATEARCHIVERESPONSE.fields_by_name['sysroot_archive'].message_type = chromiumos_dot_common__pb2._PATH
_INSTALLTOOLCHAINREQUEST_FLAGS.containing_type = _INSTALLTOOLCHAINREQUEST
_INSTALLTOOLCHAINREQUEST.fields_by_name['sysroot'].message_type = _SYSROOT
_INSTALLTOOLCHAINREQUEST.fields_by_name['flags'].message_type = _INSTALLTOOLCHAINREQUEST_FLAGS
_INSTALLTOOLCHAINREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_INSTALLTOOLCHAINRESPONSE.fields_by_name['failed_packages'].message_type = chromiumos_dot_common__pb2._PACKAGEINFO
_INSTALLPACKAGESREQUEST_FLAGS.containing_type = _INSTALLPACKAGESREQUEST
_INSTALLPACKAGESREQUEST.fields_by_name['sysroot'].message_type = _SYSROOT
_INSTALLPACKAGESREQUEST.fields_by_name['flags'].message_type = _INSTALLPACKAGESREQUEST_FLAGS
_INSTALLPACKAGESREQUEST.fields_by_name['packages'].message_type = chromiumos_dot_common__pb2._PACKAGEINFO
_INSTALLPACKAGESREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_INSTALLPACKAGESREQUEST.fields_by_name['use_flags'].message_type = chromiumos_dot_common__pb2._USEFLAG
_INSTALLPACKAGESREQUEST.fields_by_name['goma_config'].message_type = chromiumos_dot_common__pb2._GOMACONFIG
_INSTALLPACKAGESREQUEST.fields_by_name['package_indexes'].message_type = chromiumos_dot_common__pb2._PACKAGEINDEXINFO
_INSTALLPACKAGESRESPONSE.fields_by_name['failed_packages'].message_type = chromiumos_dot_common__pb2._PACKAGEINFO
_INSTALLPACKAGESRESPONSE.fields_by_name['events'].message_type = chromiumos_dot_metrics__pb2._METRICEVENT
_INSTALLPACKAGESRESPONSE.fields_by_name['goma_artifacts'].message_type = chromiumos_dot_common__pb2._GOMAARTIFACTS
_CREATESIMPLECHROMESYSROOTREQUEST.fields_by_name['build_target'].message_type = chromiumos_dot_common__pb2._BUILDTARGET
_CREATESIMPLECHROMESYSROOTREQUEST.fields_by_name['target_dir'].message_type = chromiumos_dot_common__pb2._RESULTPATH
_CREATESIMPLECHROMESYSROOTREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_CREATESIMPLECHROMESYSROOTRESPONSE.fields_by_name['sysroot_archive'].message_type = chromiumos_dot_common__pb2._PATH
DESCRIPTOR.message_types_by_name['Sysroot'] = _SYSROOT
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['SysrootCreateRequest'] = _SYSROOTCREATEREQUEST
DESCRIPTOR.message_types_by_name['SysrootCreateResponse'] = _SYSROOTCREATERESPONSE
DESCRIPTOR.message_types_by_name['SysrootGenerateArchiveRequest'] = _SYSROOTGENERATEARCHIVEREQUEST
DESCRIPTOR.message_types_by_name['SysrootGenerateArchiveResponse'] = _SYSROOTGENERATEARCHIVERESPONSE
DESCRIPTOR.message_types_by_name['InstallToolchainRequest'] = _INSTALLTOOLCHAINREQUEST
DESCRIPTOR.message_types_by_name['InstallToolchainResponse'] = _INSTALLTOOLCHAINRESPONSE
DESCRIPTOR.message_types_by_name['InstallPackagesRequest'] = _INSTALLPACKAGESREQUEST
DESCRIPTOR.message_types_by_name['InstallPackagesResponse'] = _INSTALLPACKAGESRESPONSE
DESCRIPTOR.message_types_by_name['CreateSimpleChromeSysrootRequest'] = _CREATESIMPLECHROMESYSROOTREQUEST
DESCRIPTOR.message_types_by_name['CreateSimpleChromeSysrootResponse'] = _CREATESIMPLECHROMESYSROOTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sysroot = _reflection.GeneratedProtocolMessageType('Sysroot', (_message.Message,), dict(
  DESCRIPTOR = _SYSROOT,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.Sysroot)
  ))
_sym_db.RegisterMessage(Sysroot)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), dict(
  DESCRIPTOR = _PROFILE,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.Profile)
  ))
_sym_db.RegisterMessage(Profile)

SysrootCreateRequest = _reflection.GeneratedProtocolMessageType('SysrootCreateRequest', (_message.Message,), dict(

  Flags = _reflection.GeneratedProtocolMessageType('Flags', (_message.Message,), dict(
    DESCRIPTOR = _SYSROOTCREATEREQUEST_FLAGS,
    __module__ = 'chromite.api.sysroot_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.SysrootCreateRequest.Flags)
    ))
  ,
  DESCRIPTOR = _SYSROOTCREATEREQUEST,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SysrootCreateRequest)
  ))
_sym_db.RegisterMessage(SysrootCreateRequest)
_sym_db.RegisterMessage(SysrootCreateRequest.Flags)

SysrootCreateResponse = _reflection.GeneratedProtocolMessageType('SysrootCreateResponse', (_message.Message,), dict(
  DESCRIPTOR = _SYSROOTCREATERESPONSE,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SysrootCreateResponse)
  ))
_sym_db.RegisterMessage(SysrootCreateResponse)

SysrootGenerateArchiveRequest = _reflection.GeneratedProtocolMessageType('SysrootGenerateArchiveRequest', (_message.Message,), dict(
  DESCRIPTOR = _SYSROOTGENERATEARCHIVEREQUEST,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SysrootGenerateArchiveRequest)
  ))
_sym_db.RegisterMessage(SysrootGenerateArchiveRequest)

SysrootGenerateArchiveResponse = _reflection.GeneratedProtocolMessageType('SysrootGenerateArchiveResponse', (_message.Message,), dict(
  DESCRIPTOR = _SYSROOTGENERATEARCHIVERESPONSE,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SysrootGenerateArchiveResponse)
  ))
_sym_db.RegisterMessage(SysrootGenerateArchiveResponse)

InstallToolchainRequest = _reflection.GeneratedProtocolMessageType('InstallToolchainRequest', (_message.Message,), dict(

  Flags = _reflection.GeneratedProtocolMessageType('Flags', (_message.Message,), dict(
    DESCRIPTOR = _INSTALLTOOLCHAINREQUEST_FLAGS,
    __module__ = 'chromite.api.sysroot_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.InstallToolchainRequest.Flags)
    ))
  ,
  DESCRIPTOR = _INSTALLTOOLCHAINREQUEST,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.InstallToolchainRequest)
  ))
_sym_db.RegisterMessage(InstallToolchainRequest)
_sym_db.RegisterMessage(InstallToolchainRequest.Flags)

InstallToolchainResponse = _reflection.GeneratedProtocolMessageType('InstallToolchainResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLTOOLCHAINRESPONSE,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.InstallToolchainResponse)
  ))
_sym_db.RegisterMessage(InstallToolchainResponse)

InstallPackagesRequest = _reflection.GeneratedProtocolMessageType('InstallPackagesRequest', (_message.Message,), dict(

  Flags = _reflection.GeneratedProtocolMessageType('Flags', (_message.Message,), dict(
    DESCRIPTOR = _INSTALLPACKAGESREQUEST_FLAGS,
    __module__ = 'chromite.api.sysroot_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.InstallPackagesRequest.Flags)
    ))
  ,
  DESCRIPTOR = _INSTALLPACKAGESREQUEST,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.InstallPackagesRequest)
  ))
_sym_db.RegisterMessage(InstallPackagesRequest)
_sym_db.RegisterMessage(InstallPackagesRequest.Flags)

InstallPackagesResponse = _reflection.GeneratedProtocolMessageType('InstallPackagesResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLPACKAGESRESPONSE,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.InstallPackagesResponse)
  ))
_sym_db.RegisterMessage(InstallPackagesResponse)

CreateSimpleChromeSysrootRequest = _reflection.GeneratedProtocolMessageType('CreateSimpleChromeSysrootRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESIMPLECHROMESYSROOTREQUEST,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CreateSimpleChromeSysrootRequest)
  ))
_sym_db.RegisterMessage(CreateSimpleChromeSysrootRequest)

CreateSimpleChromeSysrootResponse = _reflection.GeneratedProtocolMessageType('CreateSimpleChromeSysrootResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATESIMPLECHROMESYSROOTRESPONSE,
  __module__ = 'chromite.api.sysroot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CreateSimpleChromeSysrootResponse)
  ))
_sym_db.RegisterMessage(CreateSimpleChromeSysrootResponse)


DESCRIPTOR._options = None

_SYSROOTSERVICE = _descriptor.ServiceDescriptor(
  name='SysrootService',
  full_name='chromite.api.SysrootService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\302\355\032\013\n\007sysroot\020\001'),
  serialized_start=2098,
  serialized_end=2645,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='chromite.api.SysrootService.Create',
    index=0,
    containing_service=None,
    input_type=_SYSROOTCREATEREQUEST,
    output_type=_SYSROOTCREATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateArchive',
    full_name='chromite.api.SysrootService.GenerateArchive',
    index=1,
    containing_service=None,
    input_type=_SYSROOTGENERATEARCHIVEREQUEST,
    output_type=_SYSROOTGENERATEARCHIVERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InstallToolchain',
    full_name='chromite.api.SysrootService.InstallToolchain',
    index=2,
    containing_service=None,
    input_type=_INSTALLTOOLCHAINREQUEST,
    output_type=_INSTALLTOOLCHAINRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InstallPackages',
    full_name='chromite.api.SysrootService.InstallPackages',
    index=3,
    containing_service=None,
    input_type=_INSTALLPACKAGESREQUEST,
    output_type=_INSTALLPACKAGESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateSimpleChromeSysroot',
    full_name='chromite.api.SysrootService.CreateSimpleChromeSysroot',
    index=4,
    containing_service=None,
    input_type=_CREATESIMPLECHROMESYSROOTREQUEST,
    output_type=_CREATESIMPLECHROMESYSROOTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SYSROOTSERVICE)

DESCRIPTOR.services_by_name['SysrootService'] = _SYSROOTSERVICE

# @@protoc_insertion_point(module_scope)
