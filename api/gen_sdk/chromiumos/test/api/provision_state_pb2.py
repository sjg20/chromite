# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/provision_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.build.api import dlc_pb2 as chromiumos_dot_build_dot_api_dot_dlc__pb2
from chromite.api.gen_sdk.chromiumos.build.api import firmware_config_pb2 as chromiumos_dot_build_dot_api_dot_firmware__config__pb2
from chromite.api.gen_sdk.chromiumos.build.api import portage_pb2 as chromiumos_dot_build_dot_api_dot_portage__pb2
from chromite.api.gen_sdk.chromiumos import storage_path_pb2 as chromiumos_dot_storage__path__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/test/api/provision_state.proto',
  package='chromiumos.test.api',
  syntax='proto3',
  serialized_options=_b('Z-go.chromium.org/chromiumos/config/go/test/api'),
  serialized_pb=_b('\n)chromiumos/test/api/provision_state.proto\x12\x13\x63hromiumos.test.api\x1a\x1e\x63hromiumos/build/api/dlc.proto\x1a*chromiumos/build/api/firmware_config.proto\x1a\"chromiumos/build/api/portage.proto\x1a\x1d\x63hromiumos/storage_path.proto\"\x91\x04\n\x0eProvisionState\x12\x32\n\x02id\x18\x01 \x01(\x0b\x32&.chromiumos.test.api.ProvisionState.Id\x12\x36\n\x08\x66irmware\x18\x02 \x01(\x0b\x32$.chromiumos.build.api.FirmwareConfig\x12\x45\n\x0csystem_image\x18\x03 \x01(\x0b\x32/.chromiumos.test.api.ProvisionState.SystemImage\x12=\n\x08packages\x18\x04 \x03(\x0b\x32+.chromiumos.test.api.ProvisionState.Package\x1a\x13\n\x02Id\x12\r\n\x05value\x18\x01 \x01(\t\x1a~\n\x0bSystemImage\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x32\n\x11system_image_path\x18\x02 \x01(\x0b\x32\x17.chromiumos.StoragePath\x12*\n\x04\x64lcs\x18\x03 \x03(\x0b\x32\x1c.chromiumos.build.api.Dlc.Id\x1ax\n\x07Package\x12>\n\x0fportage_package\x18\x01 \x01(\x0b\x32%.chromiumos.build.api.Portage.Package\x12-\n\x0cpackage_path\x18\x02 \x01(\x0b\x32\x17.chromiumos.StoragePathB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3')
  ,
  dependencies=[chromiumos_dot_build_dot_api_dot_dlc__pb2.DESCRIPTOR,chromiumos_dot_build_dot_api_dot_firmware__config__pb2.DESCRIPTOR,chromiumos_dot_build_dot_api_dot_portage__pb2.DESCRIPTOR,chromiumos_dot_storage__path__pb2.DESCRIPTOR,])




_PROVISIONSTATE_ID = _descriptor.Descriptor(
  name='Id',
  full_name='chromiumos.test.api.ProvisionState.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.test.api.ProvisionState.Id.value', index=0,
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
  serialized_start=470,
  serialized_end=489,
)

_PROVISIONSTATE_SYSTEMIMAGE = _descriptor.Descriptor(
  name='SystemImage',
  full_name='chromiumos.test.api.ProvisionState.SystemImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='chromiumos.test.api.ProvisionState.SystemImage.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_image_path', full_name='chromiumos.test.api.ProvisionState.SystemImage.system_image_path', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dlcs', full_name='chromiumos.test.api.ProvisionState.SystemImage.dlcs', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=491,
  serialized_end=617,
)

_PROVISIONSTATE_PACKAGE = _descriptor.Descriptor(
  name='Package',
  full_name='chromiumos.test.api.ProvisionState.Package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='portage_package', full_name='chromiumos.test.api.ProvisionState.Package.portage_package', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_path', full_name='chromiumos.test.api.ProvisionState.Package.package_path', index=1,
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
  serialized_start=619,
  serialized_end=739,
)

_PROVISIONSTATE = _descriptor.Descriptor(
  name='ProvisionState',
  full_name='chromiumos.test.api.ProvisionState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chromiumos.test.api.ProvisionState.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firmware', full_name='chromiumos.test.api.ProvisionState.firmware', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_image', full_name='chromiumos.test.api.ProvisionState.system_image', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packages', full_name='chromiumos.test.api.ProvisionState.packages', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PROVISIONSTATE_ID, _PROVISIONSTATE_SYSTEMIMAGE, _PROVISIONSTATE_PACKAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=739,
)

_PROVISIONSTATE_ID.containing_type = _PROVISIONSTATE
_PROVISIONSTATE_SYSTEMIMAGE.fields_by_name['system_image_path'].message_type = chromiumos_dot_storage__path__pb2._STORAGEPATH
_PROVISIONSTATE_SYSTEMIMAGE.fields_by_name['dlcs'].message_type = chromiumos_dot_build_dot_api_dot_dlc__pb2._DLC_ID
_PROVISIONSTATE_SYSTEMIMAGE.containing_type = _PROVISIONSTATE
_PROVISIONSTATE_PACKAGE.fields_by_name['portage_package'].message_type = chromiumos_dot_build_dot_api_dot_portage__pb2._PORTAGE_PACKAGE
_PROVISIONSTATE_PACKAGE.fields_by_name['package_path'].message_type = chromiumos_dot_storage__path__pb2._STORAGEPATH
_PROVISIONSTATE_PACKAGE.containing_type = _PROVISIONSTATE
_PROVISIONSTATE.fields_by_name['id'].message_type = _PROVISIONSTATE_ID
_PROVISIONSTATE.fields_by_name['firmware'].message_type = chromiumos_dot_build_dot_api_dot_firmware__config__pb2._FIRMWARECONFIG
_PROVISIONSTATE.fields_by_name['system_image'].message_type = _PROVISIONSTATE_SYSTEMIMAGE
_PROVISIONSTATE.fields_by_name['packages'].message_type = _PROVISIONSTATE_PACKAGE
DESCRIPTOR.message_types_by_name['ProvisionState'] = _PROVISIONSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProvisionState = _reflection.GeneratedProtocolMessageType('ProvisionState', (_message.Message,), dict(

  Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), dict(
    DESCRIPTOR = _PROVISIONSTATE_ID,
    __module__ = 'chromiumos.test.api.provision_state_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.ProvisionState.Id)
    ))
  ,

  SystemImage = _reflection.GeneratedProtocolMessageType('SystemImage', (_message.Message,), dict(
    DESCRIPTOR = _PROVISIONSTATE_SYSTEMIMAGE,
    __module__ = 'chromiumos.test.api.provision_state_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.ProvisionState.SystemImage)
    ))
  ,

  Package = _reflection.GeneratedProtocolMessageType('Package', (_message.Message,), dict(
    DESCRIPTOR = _PROVISIONSTATE_PACKAGE,
    __module__ = 'chromiumos.test.api.provision_state_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.ProvisionState.Package)
    ))
  ,
  DESCRIPTOR = _PROVISIONSTATE,
  __module__ = 'chromiumos.test.api.provision_state_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.ProvisionState)
  ))
_sym_db.RegisterMessage(ProvisionState)
_sym_db.RegisterMessage(ProvisionState.Id)
_sym_db.RegisterMessage(ProvisionState.SystemImage)
_sym_db.RegisterMessage(ProvisionState.Package)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
