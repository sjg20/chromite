# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/pre_test_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.test.api import cros_test_finder_cli_pb2 as chromiumos_dot_test_dot_api_dot_cros__test__finder__cli__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*chromiumos/test/api/pre_test_service.proto\x12\x13\x63hromiumos.test.api\x1a.chromiumos/test/api/cros_test_finder_cli.proto\"\xbe\x02\n\x12\x46ilterFlakyRequest\x12?\n\x10pass_rate_policy\x18\x01 \x01(\x0b\x32#.chromiumos.test.api.PassRatePolicyH\x00\x12M\n\x17stability_sensor_policy\x18\x02 \x01(\x0b\x32*.chromiumos.test.api.StabilitySensorPolicyH\x00\x12\x11\n\tmilestone\x18\x04 \x01(\t\x12\x46\n\x11test_finder_input\x18\x03 \x01(\x0b\x32+.chromiumos.test.api.CrosTestFinderResponse\x12\x0f\n\x05\x62oard\x18\x05 \x01(\tH\x01\x12\x17\n\x0f\x64\x65\x66\x61ult_enabled\x18\x06 \x01(\x08\x42\x08\n\x06policyB\t\n\x07variant\"k\n\x13\x46ilterFlakyResponse\x12=\n\x08response\x18\x01 \x01(\x0b\x32+.chromiumos.test.api.CrosTestFinderResponse\x12\x15\n\rremoved_tests\x18\x02 \x03(\t\"\x17\n\x15StabilitySensorPolicy\"\xa9\x01\n\x0ePassRatePolicy\x12\x11\n\tpass_rate\x18\x01 \x01(\x05\x12\x10\n\x08min_runs\x18\x02 \x01(\x05\x12\x19\n\x11num_of_milestones\x18\x04 \x01(\x05\x12\x1b\n\x13\x66orce_enabled_tests\x18\x05 \x03(\t\x12\x1c\n\x14\x66orce_disabled_tests\x18\x06 \x03(\t\x12\x1c\n\x14\x66orce_enabled_boards\x18\x07 \x03(\t2w\n\x0ePreTestService\x12\x65\n\x10\x46ilterFlakyTests\x12\'.chromiumos.test.api.FilterFlakyRequest\x1a(.chromiumos.test.api.FilterFlakyResponseB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.test.api.pre_test_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-go.chromium.org/chromiumos/config/go/test/api'
  _FILTERFLAKYREQUEST._serialized_start=116
  _FILTERFLAKYREQUEST._serialized_end=434
  _FILTERFLAKYRESPONSE._serialized_start=436
  _FILTERFLAKYRESPONSE._serialized_end=543
  _STABILITYSENSORPOLICY._serialized_start=545
  _STABILITYSENSORPOLICY._serialized_end=568
  _PASSRATEPOLICY._serialized_start=571
  _PASSRATEPOLICY._serialized_end=740
  _PRETESTSERVICE._serialized_start=742
  _PRETESTSERVICE._serialized_end=861
# @@protoc_insertion_point(module_scope)
