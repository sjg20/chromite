# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/results/v1/software_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from chromite.api.gen_sdk.chromiumos.config.api.test.results.v1 import package_pb2 as chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_package__pb2
from chromite.api.gen_sdk.chromiumos.config.api.test.results.v1 import software_config_id_pb2 as chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_software__config__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;chromiumos/config/api/test/results/v1/software_config.proto\x12%chromiumos.config.api.test.results.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x33\x63hromiumos/config/api/test/results/v1/package.proto\x1a>chromiumos/config/api/test/results/v1/software_config_id.proto\"\xf7\x06\n\x0eSoftwareConfig\x12\x43\n\x02id\x18\x01 \x01(\x0b\x32\x37.chromiumos.config.api.test.results.v1.SoftwareConfigId\x12/\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\x06parent\x18\x03 \x01(\x0b\x32\x37.chromiumos.config.api.test.results.v1.SoftwareConfigId\x12@\n\x08packages\x18\x04 \x03(\x0b\x32..chromiumos.config.api.test.results.v1.Package\x12\x16\n\x0ekernel_release\x18\x05 \x01(\t\x12\x16\n\x0ekernel_version\x18\x06 \x01(\t\x12P\n\x08\x63hromeos\x18\x07 \x01(\x0b\x32>.chromiumos.config.api.test.results.v1.SoftwareConfig.ChromeOS\x12\x44\n\x02os\x18\x08 \x01(\x0b\x32\x38.chromiumos.config.api.test.results.v1.SoftwareConfig.OS\x12\x14\n\x0c\x62ios_version\x18\t \x01(\t\x12\x12\n\nec_version\x18\n \x01(\t\x1a\xf3\x01\n\x08\x43hromeOS\x12\r\n\x05\x62oard\x18\x01 \x01(\t\x12\x15\n\rbranch_number\x18\x02 \x01(\r\x12\x14\n\x0c\x62uilder_path\x18\x03 \x01(\t\x12\x14\n\x0c\x62uild_number\x18\x04 \x01(\r\x12\x12\n\nbuild_type\x18\x05 \x01(\t\x12\x18\n\x10\x63hrome_milestone\x18\x06 \x01(\r\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x0e\n\x06keyset\x18\x08 \x01(\t\x12\x0c\n\x04name\x18\t \x01(\t\x12\x14\n\x0cpatch_number\x18\n \x01(\t\x12\r\n\x05track\x18\x0b \x01(\t\x12\x0f\n\x07version\x18\x0c \x01(\t\x1a|\n\x02OS\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12\x10\n\x08\x63odename\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0bpretty_name\x18\x05 \x01(\t\x12\x12\n\nversion_id\x18\x06 \x01(\t\x12\x0f\n\x07version\x18\x07 \x01(\tBBZ@go.chromium.org/chromiumos/config/go/api/test/results/v1;resultsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.config.api.test.results.v1.software_config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z@go.chromium.org/chromiumos/config/go/api/test/results/v1;results'
  _SOFTWARECONFIG._serialized_start=253
  _SOFTWARECONFIG._serialized_end=1140
  _SOFTWARECONFIG_CHROMEOS._serialized_start=771
  _SOFTWARECONFIG_CHROMEOS._serialized_end=1014
  _SOFTWARECONFIG_OS._serialized_start=1016
  _SOFTWARECONFIG_OS._serialized_end=1140
# @@protoc_insertion_point(module_scope)
