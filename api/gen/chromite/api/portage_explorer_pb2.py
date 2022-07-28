# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/portage_explorer.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen.chromiumos import common_pb2 as chromiumos_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromite/api/portage_explorer.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#chromite/api/portage_explorer.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x17\x63hromiumos/common.proto\"7\n\x11RunSpidersRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\"\x82\x0b\n\x12RunSpidersResponse\x12\x43\n\rbuild_targets\x18\x01 \x03(\x0b\x32,.chromite.api.RunSpidersResponse.BuildTarget\x12:\n\x08overlays\x18\x02 \x03(\x0b\x32(.chromite.api.RunSpidersResponse.Overlay\x1aY\n\x0b\x42uildTarget\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\nprofile_id\x18\x02 \x01(\x0b\x32(.chromite.api.RunSpidersResponse.Profile\x1a\xb4\x01\n\x07Profile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12>\n\tuse_flags\x18\x04 \x03(\x0b\x32+.chromite.api.RunSpidersResponse.ProfileUse\x12\x41\n\x0fparent_profiles\x18\x05 \x03(\x0b\x32(.chromite.api.RunSpidersResponse.Profile\x1a\xd6\x01\n\x07Overlay\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12:\n\x08profiles\x18\x03 \x03(\x0b\x32(.chromite.api.RunSpidersResponse.Profile\x12\x38\n\x07\x65\x62uilds\x18\x04 \x03(\x0b\x32\'.chromite.api.RunSpidersResponse.Ebuild\x12\x39\n\x08\x65\x63lasses\x18\x05 \x03(\x0b\x32\'.chromite.api.RunSpidersResponse.Eclass\x1a\xfa\x02\n\x06\x45\x62uild\x12\x0c\n\x04path\x18\x01 \x01(\t\x12-\n\x0cpackage_info\x18\x02 \x01(\x0b\x32\x17.chromiumos.PackageInfo\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x10\n\x08revision\x18\x04 \x01(\x05\x12\x0c\n\x04\x65\x61pi\x18\x05 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x10\n\x08homepage\x18\x07 \x01(\t\x12\x0f\n\x07license\x18\x08 \x01(\t\x12\x0c\n\x04slot\x18\t \x01(\t\x12\x0f\n\x07src_uri\x18\n \x01(\t\x12\x10\n\x08restrict\x18\x0b \x01(\t\x12\x41\n\x0c\x64\x65pendencies\x18\x0c \x03(\x0b\x32+.chromite.api.RunSpidersResponse.Dependency\x12=\n\tuse_flags\x18\r \x03(\x0b\x32*.chromite.api.RunSpidersResponse.EbuildUse\x12\x17\n\x0f\x65\x63lass_inherits\x18\x0e \x03(\t\x1a\xe2\x01\n\nDependency\x12H\n\x04type\x18\x01 \x01(\x0e\x32:.chromite.api.RunSpidersResponse.Dependency.DependencyType\x12-\n\x0cpackage_info\x18\x02 \x01(\x0b\x32\x17.chromiumos.PackageInfo\"[\n\x0e\x44\x65pendencyType\x12\x16\n\x12\x44\x45PEND_UNSPECIFIED\x10\x00\x12\n\n\x06\x44\x45PEND\x10\x01\x12\x0b\n\x07RDEPEND\x10\x02\x12\x0b\n\x07\x42\x44\x45PEND\x10\x03\x12\x0b\n\x07PDEPEND\x10\x04\x1a=\n\x06\x45\x63lass\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x0f\x65\x63lass_inherits\x18\x03 \x03(\t\x1a+\n\nProfileUse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x1a\x32\n\tEbuildUse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x61ult_enabled\x18\x02 \x01(\x08\x32\x83\x01\n\x16PortageExplorerService\x12O\n\nRunSpiders\x12\x1f.chromite.api.RunSpidersRequest\x1a .chromite.api.RunSpidersResponse\x1a\x18\xc2\xed\x1a\x14\n\x10portage_explorer\x10\x01\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3'
  ,
  dependencies=[chromite_dot_api_dot_build__api__pb2.DESCRIPTOR,chromiumos_dot_common__pb2.DESCRIPTOR,])



_RUNSPIDERSRESPONSE_DEPENDENCY_DEPENDENCYTYPE = _descriptor.EnumDescriptor(
  name='DependencyType',
  full_name='chromite.api.RunSpidersResponse.Dependency.DependencyType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEPEND_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPEND', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RDEPEND', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BDEPEND', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PDEPEND', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1325,
  serialized_end=1416,
)
_sym_db.RegisterEnumDescriptor(_RUNSPIDERSRESPONSE_DEPENDENCY_DEPENDENCYTYPE)


_RUNSPIDERSREQUEST = _descriptor.Descriptor(
  name='RunSpidersRequest',
  full_name='chromite.api.RunSpidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.RunSpidersRequest.chroot', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=108,
  serialized_end=163,
)


_RUNSPIDERSRESPONSE_BUILDTARGET = _descriptor.Descriptor(
  name='BuildTarget',
  full_name='chromite.api.RunSpidersResponse.BuildTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromite.api.RunSpidersResponse.BuildTarget.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='profile_id', full_name='chromite.api.RunSpidersResponse.BuildTarget.profile_id', index=1,
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
  ],
  serialized_start=317,
  serialized_end=406,
)

_RUNSPIDERSRESPONSE_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='chromite.api.RunSpidersResponse.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chromite.api.RunSpidersResponse.Profile.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='chromite.api.RunSpidersResponse.Profile.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='chromite.api.RunSpidersResponse.Profile.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_flags', full_name='chromite.api.RunSpidersResponse.Profile.use_flags', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_profiles', full_name='chromite.api.RunSpidersResponse.Profile.parent_profiles', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=409,
  serialized_end=589,
)

_RUNSPIDERSRESPONSE_OVERLAY = _descriptor.Descriptor(
  name='Overlay',
  full_name='chromite.api.RunSpidersResponse.Overlay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='chromite.api.RunSpidersResponse.Overlay.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='chromite.api.RunSpidersResponse.Overlay.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='profiles', full_name='chromite.api.RunSpidersResponse.Overlay.profiles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ebuilds', full_name='chromite.api.RunSpidersResponse.Overlay.ebuilds', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eclasses', full_name='chromite.api.RunSpidersResponse.Overlay.eclasses', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=592,
  serialized_end=806,
)

_RUNSPIDERSRESPONSE_EBUILD = _descriptor.Descriptor(
  name='Ebuild',
  full_name='chromite.api.RunSpidersResponse.Ebuild',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='chromite.api.RunSpidersResponse.Ebuild.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='package_info', full_name='chromite.api.RunSpidersResponse.Ebuild.package_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='chromite.api.RunSpidersResponse.Ebuild.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision', full_name='chromite.api.RunSpidersResponse.Ebuild.revision', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eapi', full_name='chromite.api.RunSpidersResponse.Ebuild.eapi', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='chromite.api.RunSpidersResponse.Ebuild.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='homepage', full_name='chromite.api.RunSpidersResponse.Ebuild.homepage', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='license', full_name='chromite.api.RunSpidersResponse.Ebuild.license', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slot', full_name='chromite.api.RunSpidersResponse.Ebuild.slot', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='src_uri', full_name='chromite.api.RunSpidersResponse.Ebuild.src_uri', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='restrict', full_name='chromite.api.RunSpidersResponse.Ebuild.restrict', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='chromite.api.RunSpidersResponse.Ebuild.dependencies', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_flags', full_name='chromite.api.RunSpidersResponse.Ebuild.use_flags', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eclass_inherits', full_name='chromite.api.RunSpidersResponse.Ebuild.eclass_inherits', index=13,
      number=14, type=9, cpp_type=9, label=3,
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
  serialized_start=809,
  serialized_end=1187,
)

_RUNSPIDERSRESPONSE_DEPENDENCY = _descriptor.Descriptor(
  name='Dependency',
  full_name='chromite.api.RunSpidersResponse.Dependency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='chromite.api.RunSpidersResponse.Dependency.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='package_info', full_name='chromite.api.RunSpidersResponse.Dependency.package_info', index=1,
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
    _RUNSPIDERSRESPONSE_DEPENDENCY_DEPENDENCYTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1190,
  serialized_end=1416,
)

_RUNSPIDERSRESPONSE_ECLASS = _descriptor.Descriptor(
  name='Eclass',
  full_name='chromite.api.RunSpidersResponse.Eclass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='chromite.api.RunSpidersResponse.Eclass.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='chromite.api.RunSpidersResponse.Eclass.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eclass_inherits', full_name='chromite.api.RunSpidersResponse.Eclass.eclass_inherits', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=1418,
  serialized_end=1479,
)

_RUNSPIDERSRESPONSE_PROFILEUSE = _descriptor.Descriptor(
  name='ProfileUse',
  full_name='chromite.api.RunSpidersResponse.ProfileUse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromite.api.RunSpidersResponse.ProfileUse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='chromite.api.RunSpidersResponse.ProfileUse.enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1481,
  serialized_end=1524,
)

_RUNSPIDERSRESPONSE_EBUILDUSE = _descriptor.Descriptor(
  name='EbuildUse',
  full_name='chromite.api.RunSpidersResponse.EbuildUse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromite.api.RunSpidersResponse.EbuildUse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_enabled', full_name='chromite.api.RunSpidersResponse.EbuildUse.default_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1526,
  serialized_end=1576,
)

_RUNSPIDERSRESPONSE = _descriptor.Descriptor(
  name='RunSpidersResponse',
  full_name='chromite.api.RunSpidersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_targets', full_name='chromite.api.RunSpidersResponse.build_targets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='overlays', full_name='chromite.api.RunSpidersResponse.overlays', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RUNSPIDERSRESPONSE_BUILDTARGET, _RUNSPIDERSRESPONSE_PROFILE, _RUNSPIDERSRESPONSE_OVERLAY, _RUNSPIDERSRESPONSE_EBUILD, _RUNSPIDERSRESPONSE_DEPENDENCY, _RUNSPIDERSRESPONSE_ECLASS, _RUNSPIDERSRESPONSE_PROFILEUSE, _RUNSPIDERSRESPONSE_EBUILDUSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=1576,
)

_RUNSPIDERSREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_RUNSPIDERSRESPONSE_BUILDTARGET.fields_by_name['profile_id'].message_type = _RUNSPIDERSRESPONSE_PROFILE
_RUNSPIDERSRESPONSE_BUILDTARGET.containing_type = _RUNSPIDERSRESPONSE
_RUNSPIDERSRESPONSE_PROFILE.fields_by_name['use_flags'].message_type = _RUNSPIDERSRESPONSE_PROFILEUSE
_RUNSPIDERSRESPONSE_PROFILE.fields_by_name['parent_profiles'].message_type = _RUNSPIDERSRESPONSE_PROFILE
_RUNSPIDERSRESPONSE_PROFILE.containing_type = _RUNSPIDERSRESPONSE
_RUNSPIDERSRESPONSE_OVERLAY.fields_by_name['profiles'].message_type = _RUNSPIDERSRESPONSE_PROFILE
_RUNSPIDERSRESPONSE_OVERLAY.fields_by_name['ebuilds'].message_type = _RUNSPIDERSRESPONSE_EBUILD
_RUNSPIDERSRESPONSE_OVERLAY.fields_by_name['eclasses'].message_type = _RUNSPIDERSRESPONSE_ECLASS
_RUNSPIDERSRESPONSE_OVERLAY.containing_type = _RUNSPIDERSRESPONSE
_RUNSPIDERSRESPONSE_EBUILD.fields_by_name['package_info'].message_type = chromiumos_dot_common__pb2._PACKAGEINFO
_RUNSPIDERSRESPONSE_EBUILD.fields_by_name['dependencies'].message_type = _RUNSPIDERSRESPONSE_DEPENDENCY
_RUNSPIDERSRESPONSE_EBUILD.fields_by_name['use_flags'].message_type = _RUNSPIDERSRESPONSE_EBUILDUSE
_RUNSPIDERSRESPONSE_EBUILD.containing_type = _RUNSPIDERSRESPONSE
_RUNSPIDERSRESPONSE_DEPENDENCY.fields_by_name['type'].enum_type = _RUNSPIDERSRESPONSE_DEPENDENCY_DEPENDENCYTYPE
_RUNSPIDERSRESPONSE_DEPENDENCY.fields_by_name['package_info'].message_type = chromiumos_dot_common__pb2._PACKAGEINFO
_RUNSPIDERSRESPONSE_DEPENDENCY.containing_type = _RUNSPIDERSRESPONSE
_RUNSPIDERSRESPONSE_DEPENDENCY_DEPENDENCYTYPE.containing_type = _RUNSPIDERSRESPONSE_DEPENDENCY
_RUNSPIDERSRESPONSE_ECLASS.containing_type = _RUNSPIDERSRESPONSE
_RUNSPIDERSRESPONSE_PROFILEUSE.containing_type = _RUNSPIDERSRESPONSE
_RUNSPIDERSRESPONSE_EBUILDUSE.containing_type = _RUNSPIDERSRESPONSE
_RUNSPIDERSRESPONSE.fields_by_name['build_targets'].message_type = _RUNSPIDERSRESPONSE_BUILDTARGET
_RUNSPIDERSRESPONSE.fields_by_name['overlays'].message_type = _RUNSPIDERSRESPONSE_OVERLAY
DESCRIPTOR.message_types_by_name['RunSpidersRequest'] = _RUNSPIDERSREQUEST
DESCRIPTOR.message_types_by_name['RunSpidersResponse'] = _RUNSPIDERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunSpidersRequest = _reflection.GeneratedProtocolMessageType('RunSpidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNSPIDERSREQUEST,
  '__module__' : 'chromite.api.portage_explorer_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.RunSpidersRequest)
  })
_sym_db.RegisterMessage(RunSpidersRequest)

RunSpidersResponse = _reflection.GeneratedProtocolMessageType('RunSpidersResponse', (_message.Message,), {

  'BuildTarget' : _reflection.GeneratedProtocolMessageType('BuildTarget', (_message.Message,), {
    'DESCRIPTOR' : _RUNSPIDERSRESPONSE_BUILDTARGET,
    '__module__' : 'chromite.api.portage_explorer_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunSpidersResponse.BuildTarget)
    })
  ,

  'Profile' : _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), {
    'DESCRIPTOR' : _RUNSPIDERSRESPONSE_PROFILE,
    '__module__' : 'chromite.api.portage_explorer_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunSpidersResponse.Profile)
    })
  ,

  'Overlay' : _reflection.GeneratedProtocolMessageType('Overlay', (_message.Message,), {
    'DESCRIPTOR' : _RUNSPIDERSRESPONSE_OVERLAY,
    '__module__' : 'chromite.api.portage_explorer_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunSpidersResponse.Overlay)
    })
  ,

  'Ebuild' : _reflection.GeneratedProtocolMessageType('Ebuild', (_message.Message,), {
    'DESCRIPTOR' : _RUNSPIDERSRESPONSE_EBUILD,
    '__module__' : 'chromite.api.portage_explorer_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunSpidersResponse.Ebuild)
    })
  ,

  'Dependency' : _reflection.GeneratedProtocolMessageType('Dependency', (_message.Message,), {
    'DESCRIPTOR' : _RUNSPIDERSRESPONSE_DEPENDENCY,
    '__module__' : 'chromite.api.portage_explorer_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunSpidersResponse.Dependency)
    })
  ,

  'Eclass' : _reflection.GeneratedProtocolMessageType('Eclass', (_message.Message,), {
    'DESCRIPTOR' : _RUNSPIDERSRESPONSE_ECLASS,
    '__module__' : 'chromite.api.portage_explorer_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunSpidersResponse.Eclass)
    })
  ,

  'ProfileUse' : _reflection.GeneratedProtocolMessageType('ProfileUse', (_message.Message,), {
    'DESCRIPTOR' : _RUNSPIDERSRESPONSE_PROFILEUSE,
    '__module__' : 'chromite.api.portage_explorer_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunSpidersResponse.ProfileUse)
    })
  ,

  'EbuildUse' : _reflection.GeneratedProtocolMessageType('EbuildUse', (_message.Message,), {
    'DESCRIPTOR' : _RUNSPIDERSRESPONSE_EBUILDUSE,
    '__module__' : 'chromite.api.portage_explorer_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunSpidersResponse.EbuildUse)
    })
  ,
  'DESCRIPTOR' : _RUNSPIDERSRESPONSE,
  '__module__' : 'chromite.api.portage_explorer_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.RunSpidersResponse)
  })
_sym_db.RegisterMessage(RunSpidersResponse)
_sym_db.RegisterMessage(RunSpidersResponse.BuildTarget)
_sym_db.RegisterMessage(RunSpidersResponse.Profile)
_sym_db.RegisterMessage(RunSpidersResponse.Overlay)
_sym_db.RegisterMessage(RunSpidersResponse.Ebuild)
_sym_db.RegisterMessage(RunSpidersResponse.Dependency)
_sym_db.RegisterMessage(RunSpidersResponse.Eclass)
_sym_db.RegisterMessage(RunSpidersResponse.ProfileUse)
_sym_db.RegisterMessage(RunSpidersResponse.EbuildUse)


DESCRIPTOR._options = None

_PORTAGEEXPLORERSERVICE = _descriptor.ServiceDescriptor(
  name='PortageExplorerService',
  full_name='chromite.api.PortageExplorerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\302\355\032\024\n\020portage_explorer\020\001',
  create_key=_descriptor._internal_create_key,
  serialized_start=1579,
  serialized_end=1710,
  methods=[
  _descriptor.MethodDescriptor(
    name='RunSpiders',
    full_name='chromite.api.PortageExplorerService.RunSpiders',
    index=0,
    containing_service=None,
    input_type=_RUNSPIDERSREQUEST,
    output_type=_RUNSPIDERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PORTAGEEXPLORERSERVICE)

DESCRIPTOR.services_by_name['PortageExplorerService'] = _PORTAGEEXPLORERSERVICE

# @@protoc_insertion_point(module_scope)
