# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/cros_test_finder_cli.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.test.api import test_suite_pb2 as chromiumos_dot_test_dot_api_dot_test__suite__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.chromiumos/test/api/cros_test_finder_cli.proto\x12\x13\x63hromiumos.test.api\x1a$chromiumos/test/api/test_suite.proto\"L\n\x15\x43rosTestFinderRequest\x12\x33\n\x0btest_suites\x18\x01 \x03(\x0b\x32\x1e.chromiumos.test.api.TestSuite\"M\n\x16\x43rosTestFinderResponse\x12\x33\n\x0btest_suites\x18\x01 \x03(\x0b\x32\x1e.chromiumos.test.api.TestSuiteB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3')



_CROSTESTFINDERREQUEST = DESCRIPTOR.message_types_by_name['CrosTestFinderRequest']
_CROSTESTFINDERRESPONSE = DESCRIPTOR.message_types_by_name['CrosTestFinderResponse']
CrosTestFinderRequest = _reflection.GeneratedProtocolMessageType('CrosTestFinderRequest', (_message.Message,), {
  'DESCRIPTOR' : _CROSTESTFINDERREQUEST,
  '__module__' : 'chromiumos.test.api.cros_test_finder_cli_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.CrosTestFinderRequest)
  })
_sym_db.RegisterMessage(CrosTestFinderRequest)

CrosTestFinderResponse = _reflection.GeneratedProtocolMessageType('CrosTestFinderResponse', (_message.Message,), {
  'DESCRIPTOR' : _CROSTESTFINDERRESPONSE,
  '__module__' : 'chromiumos.test.api.cros_test_finder_cli_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.CrosTestFinderResponse)
  })
_sym_db.RegisterMessage(CrosTestFinderResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-go.chromium.org/chromiumos/config/go/test/api'
  _CROSTESTFINDERREQUEST._serialized_start=109
  _CROSTESTFINDERREQUEST._serialized_end=185
  _CROSTESTFINDERRESPONSE._serialized_start=187
  _CROSTESTFINDERRESPONSE._serialized_end=264
# @@protoc_insertion_point(module_scope)
