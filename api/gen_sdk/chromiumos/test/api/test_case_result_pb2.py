# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/test_case_result.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from chromite.api.gen_sdk.chromiumos import storage_path_pb2 as chromiumos_dot_storage__path__pb2
from chromite.api.gen_sdk.chromiumos.test.api import test_case_pb2 as chromiumos_dot_test_dot_api_dot_test__case__pb2
from chromite.api.gen_sdk.chromiumos.test.api import test_harness_pb2 as chromiumos_dot_test_dot_api_dot_test__harness__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*chromiumos/test/api/test_case_result.proto\x12\x13\x63hromiumos.test.api\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1d\x63hromiumos/storage_path.proto\x1a#chromiumos/test/api/test_case.proto\x1a&chromiumos/test/api/test_harness.proto\"\xd0\x05\n\x0eTestCaseResult\x12\x36\n\x0ctest_case_id\x18\x01 \x01(\x0b\x32 .chromiumos.test.api.TestCase.Id\x12\x30\n\x0fresult_dir_path\x18\x02 \x01(\x0b\x32\x17.chromiumos.StoragePath\x12\x38\n\x04pass\x18\x03 \x01(\x0b\x32(.chromiumos.test.api.TestCaseResult.PassH\x00\x12\x38\n\x04\x66\x61il\x18\x04 \x01(\x0b\x32(.chromiumos.test.api.TestCaseResult.FailH\x00\x12:\n\x05\x63rash\x18\x05 \x01(\x0b\x32).chromiumos.test.api.TestCaseResult.CrashH\x00\x12:\n\x05\x61\x62ort\x18\x06 \x01(\x0b\x32).chromiumos.test.api.TestCaseResult.AbortH\x00\x12\x38\n\x04skip\x18\x07 \x01(\x0b\x32(.chromiumos.test.api.TestCaseResult.SkipH\x00\x12=\n\x07not_run\x18\x08 \x01(\x0b\x32*.chromiumos.test.api.TestCaseResult.NotRunH\x00\x12\x0e\n\x06reason\x18\t \x01(\t\x12\x36\n\x0ctest_harness\x18\n \x01(\x0b\x32 .chromiumos.test.api.TestHarness\x12.\n\nstart_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x64uration\x18\x0c \x01(\x0b\x32\x19.google.protobuf.Duration\x1a\x0b\n\tArtifacts\x1a\x06\n\x04Pass\x1a\x06\n\x04\x46\x61il\x1a\x07\n\x05\x43rash\x1a\x07\n\x05\x41\x62ort\x1a\x06\n\x04Skip\x1a\x08\n\x06NotRunB\t\n\x07verdictB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3')



_TESTCASERESULT = DESCRIPTOR.message_types_by_name['TestCaseResult']
_TESTCASERESULT_ARTIFACTS = _TESTCASERESULT.nested_types_by_name['Artifacts']
_TESTCASERESULT_PASS = _TESTCASERESULT.nested_types_by_name['Pass']
_TESTCASERESULT_FAIL = _TESTCASERESULT.nested_types_by_name['Fail']
_TESTCASERESULT_CRASH = _TESTCASERESULT.nested_types_by_name['Crash']
_TESTCASERESULT_ABORT = _TESTCASERESULT.nested_types_by_name['Abort']
_TESTCASERESULT_SKIP = _TESTCASERESULT.nested_types_by_name['Skip']
_TESTCASERESULT_NOTRUN = _TESTCASERESULT.nested_types_by_name['NotRun']
TestCaseResult = _reflection.GeneratedProtocolMessageType('TestCaseResult', (_message.Message,), {

  'Artifacts' : _reflection.GeneratedProtocolMessageType('Artifacts', (_message.Message,), {
    'DESCRIPTOR' : _TESTCASERESULT_ARTIFACTS,
    '__module__' : 'chromiumos.test.api.test_case_result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.TestCaseResult.Artifacts)
    })
  ,

  'Pass' : _reflection.GeneratedProtocolMessageType('Pass', (_message.Message,), {
    'DESCRIPTOR' : _TESTCASERESULT_PASS,
    '__module__' : 'chromiumos.test.api.test_case_result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.TestCaseResult.Pass)
    })
  ,

  'Fail' : _reflection.GeneratedProtocolMessageType('Fail', (_message.Message,), {
    'DESCRIPTOR' : _TESTCASERESULT_FAIL,
    '__module__' : 'chromiumos.test.api.test_case_result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.TestCaseResult.Fail)
    })
  ,

  'Crash' : _reflection.GeneratedProtocolMessageType('Crash', (_message.Message,), {
    'DESCRIPTOR' : _TESTCASERESULT_CRASH,
    '__module__' : 'chromiumos.test.api.test_case_result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.TestCaseResult.Crash)
    })
  ,

  'Abort' : _reflection.GeneratedProtocolMessageType('Abort', (_message.Message,), {
    'DESCRIPTOR' : _TESTCASERESULT_ABORT,
    '__module__' : 'chromiumos.test.api.test_case_result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.TestCaseResult.Abort)
    })
  ,

  'Skip' : _reflection.GeneratedProtocolMessageType('Skip', (_message.Message,), {
    'DESCRIPTOR' : _TESTCASERESULT_SKIP,
    '__module__' : 'chromiumos.test.api.test_case_result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.TestCaseResult.Skip)
    })
  ,

  'NotRun' : _reflection.GeneratedProtocolMessageType('NotRun', (_message.Message,), {
    'DESCRIPTOR' : _TESTCASERESULT_NOTRUN,
    '__module__' : 'chromiumos.test.api.test_case_result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.api.TestCaseResult.NotRun)
    })
  ,
  'DESCRIPTOR' : _TESTCASERESULT,
  '__module__' : 'chromiumos.test.api.test_case_result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.TestCaseResult)
  })
_sym_db.RegisterMessage(TestCaseResult)
_sym_db.RegisterMessage(TestCaseResult.Artifacts)
_sym_db.RegisterMessage(TestCaseResult.Pass)
_sym_db.RegisterMessage(TestCaseResult.Fail)
_sym_db.RegisterMessage(TestCaseResult.Crash)
_sym_db.RegisterMessage(TestCaseResult.Abort)
_sym_db.RegisterMessage(TestCaseResult.Skip)
_sym_db.RegisterMessage(TestCaseResult.NotRun)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-go.chromium.org/chromiumos/config/go/test/api'
  _TESTCASERESULT._serialized_start=241
  _TESTCASERESULT._serialized_end=961
  _TESTCASERESULT_ARTIFACTS._serialized_start=887
  _TESTCASERESULT_ARTIFACTS._serialized_end=898
  _TESTCASERESULT_PASS._serialized_start=900
  _TESTCASERESULT_PASS._serialized_end=906
  _TESTCASERESULT_FAIL._serialized_start=908
  _TESTCASERESULT_FAIL._serialized_end=914
  _TESTCASERESULT_CRASH._serialized_start=916
  _TESTCASERESULT_CRASH._serialized_end=923
  _TESTCASERESULT_ABORT._serialized_start=925
  _TESTCASERESULT_ABORT._serialized_end=932
  _TESTCASERESULT_SKIP._serialized_start=934
  _TESTCASERESULT_SKIP._serialized_end=940
  _TESTCASERESULT_NOTRUN._serialized_start=942
  _TESTCASERESULT_NOTRUN._serialized_end=950
# @@protoc_insertion_point(module_scope)
