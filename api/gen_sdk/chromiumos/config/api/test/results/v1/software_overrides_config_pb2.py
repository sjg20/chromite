# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/results/v1/software_overrides_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.config.api.test.results.v1 import package_pb2 as chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_package__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/test/results/v1/software_overrides_config.proto',
  package='chromiumos.config.api.test.results.v1',
  syntax='proto3',
  serialized_options=_b('Z@go.chromium.org/chromiumos/config/go/api/test/results/v1;results'),
  serialized_pb=_b('\nEchromiumos/config/api/test/results/v1/software_overrides_config.proto\x12%chromiumos.config.api.test.results.v1\x1a\x33\x63hromiumos/config/api/test/results/v1/package.proto\"[\n\x17SoftwareOverridesConfig\x12@\n\x08packages\x18\x01 \x03(\x0b\x32..chromiumos.config.api.test.results.v1.PackageBBZ@go.chromium.org/chromiumos/config/go/api/test/results/v1;resultsb\x06proto3')
  ,
  dependencies=[chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_package__pb2.DESCRIPTOR,])




_SOFTWAREOVERRIDESCONFIG = _descriptor.Descriptor(
  name='SoftwareOverridesConfig',
  full_name='chromiumos.config.api.test.results.v1.SoftwareOverridesConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packages', full_name='chromiumos.config.api.test.results.v1.SoftwareOverridesConfig.packages', index=0,
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
  serialized_start=165,
  serialized_end=256,
)

_SOFTWAREOVERRIDESCONFIG.fields_by_name['packages'].message_type = chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_package__pb2._PACKAGE
DESCRIPTOR.message_types_by_name['SoftwareOverridesConfig'] = _SOFTWAREOVERRIDESCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SoftwareOverridesConfig = _reflection.GeneratedProtocolMessageType('SoftwareOverridesConfig', (_message.Message,), dict(
  DESCRIPTOR = _SOFTWAREOVERRIDESCONFIG,
  __module__ = 'chromiumos.config.api.test.results.v1.software_overrides_config_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.results.v1.SoftwareOverridesConfig)
  ))
_sym_db.RegisterMessage(SoftwareOverridesConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
