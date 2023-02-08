# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/android_provision_cli.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromiumos.test.api import android_provision_metadata_pb2 as chromiumos_dot_test_dot_api_dot_android__provision__metadata__pb2
from chromite.api.gen.chromiumos.test.api import provision_service_pb2 as chromiumos_dot_test_dot_api_dot_provision__service__pb2
from chromite.api.gen.chromiumos.test.lab.api import dut_pb2 as chromiumos_dot_test_dot_lab_dot_api_dot_dut__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/test/api/android_provision_cli.proto',
  package='chromiumos.test.api',
  syntax='proto3',
  serialized_options=b'Z-go.chromium.org/chromiumos/config/go/test/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/chromiumos/test/api/android_provision_cli.proto\x12\x13\x63hromiumos.test.api\x1a\x34\x63hromiumos/test/api/android_provision_metadata.proto\x1a+chromiumos/test/api/provision_service.proto\x1a!chromiumos/test/lab/api/dut.proto\"\x8d\x02\n\x1b\x41ndroidProvisionCLIResponse\x12+\n\x02id\x18\x01 \x01(\x0b\x32\x1f.chromiumos.test.lab.api.Dut.Id\x12\x36\n\x07success\x18\x02 \x01(\x0b\x32#.chromiumos.test.api.InstallSuccessH\x00\x12\x36\n\x07\x66\x61ilure\x18\x03 \x01(\x0b\x32#.chromiumos.test.api.InstallFailureH\x00\x12\x46\n\x10\x61ndroid_packages\x18\x04 \x03(\x0b\x32,.chromiumos.test.api.InstalledAndroidPackageB\t\n\x07outcomeB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3'
  ,
  dependencies=[chromiumos_dot_test_dot_api_dot_android__provision__metadata__pb2.DESCRIPTOR,chromiumos_dot_test_dot_api_dot_provision__service__pb2.DESCRIPTOR,chromiumos_dot_test_dot_lab_dot_api_dot_dut__pb2.DESCRIPTOR,])




_ANDROIDPROVISIONCLIRESPONSE = _descriptor.Descriptor(
  name='AndroidProvisionCLIResponse',
  full_name='chromiumos.test.api.AndroidProvisionCLIResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chromiumos.test.api.AndroidProvisionCLIResponse.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success', full_name='chromiumos.test.api.AndroidProvisionCLIResponse.success', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failure', full_name='chromiumos.test.api.AndroidProvisionCLIResponse.failure', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='android_packages', full_name='chromiumos.test.api.AndroidProvisionCLIResponse.android_packages', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
    _descriptor.OneofDescriptor(
      name='outcome', full_name='chromiumos.test.api.AndroidProvisionCLIResponse.outcome',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=207,
  serialized_end=476,
)

_ANDROIDPROVISIONCLIRESPONSE.fields_by_name['id'].message_type = chromiumos_dot_test_dot_lab_dot_api_dot_dut__pb2._DUT_ID
_ANDROIDPROVISIONCLIRESPONSE.fields_by_name['success'].message_type = chromiumos_dot_test_dot_api_dot_provision__service__pb2._INSTALLSUCCESS
_ANDROIDPROVISIONCLIRESPONSE.fields_by_name['failure'].message_type = chromiumos_dot_test_dot_api_dot_provision__service__pb2._INSTALLFAILURE
_ANDROIDPROVISIONCLIRESPONSE.fields_by_name['android_packages'].message_type = chromiumos_dot_test_dot_api_dot_android__provision__metadata__pb2._INSTALLEDANDROIDPACKAGE
_ANDROIDPROVISIONCLIRESPONSE.oneofs_by_name['outcome'].fields.append(
  _ANDROIDPROVISIONCLIRESPONSE.fields_by_name['success'])
_ANDROIDPROVISIONCLIRESPONSE.fields_by_name['success'].containing_oneof = _ANDROIDPROVISIONCLIRESPONSE.oneofs_by_name['outcome']
_ANDROIDPROVISIONCLIRESPONSE.oneofs_by_name['outcome'].fields.append(
  _ANDROIDPROVISIONCLIRESPONSE.fields_by_name['failure'])
_ANDROIDPROVISIONCLIRESPONSE.fields_by_name['failure'].containing_oneof = _ANDROIDPROVISIONCLIRESPONSE.oneofs_by_name['outcome']
DESCRIPTOR.message_types_by_name['AndroidProvisionCLIResponse'] = _ANDROIDPROVISIONCLIRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AndroidProvisionCLIResponse = _reflection.GeneratedProtocolMessageType('AndroidProvisionCLIResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANDROIDPROVISIONCLIRESPONSE,
  '__module__' : 'chromiumos.test.api.android_provision_cli_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.AndroidProvisionCLIResponse)
  })
_sym_db.RegisterMessage(AndroidProvisionCLIResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
