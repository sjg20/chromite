# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/artifact/test_result.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos import storage_path_pb2 as chromiumos_dot_storage__path__pb2
from chromite.api.gen_sdk.chromiumos.test.api import provision_state_pb2 as chromiumos_dot_test_dot_api_dot_provision__state__pb2
from chromite.api.gen_sdk.chromiumos.test.api import test_case_metadata_pb2 as chromiumos_dot_test_dot_api_dot_test__case__metadata__pb2
from chromite.api.gen_sdk.chromiumos.test.api import test_case_result_pb2 as chromiumos_dot_test_dot_api_dot_test__case__result__pb2
from chromite.api.gen_sdk.chromiumos.test.api.v1 import plan_pb2 as chromiumos_dot_test_dot_api_dot_v1_dot_plan__pb2
from chromite.api.gen_sdk.chromiumos.test.lab.api import dut_pb2 as chromiumos_dot_test_dot_lab_dot_api_dot_dut__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*chromiumos/test/artifact/test_result.proto\x12\x18\x63hromiumos.test.artifact\x1a\x1d\x63hromiumos/storage_path.proto\x1a)chromiumos/test/api/provision_state.proto\x1a,chromiumos/test/api/test_case_metadata.proto\x1a*chromiumos/test/api/test_case_result.proto\x1a!chromiumos/test/api/v1/plan.proto\x1a!chromiumos/test/lab/api/dut.proto\"\x96\x01\n\nTestResult\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x41\n\x0ftest_invocation\x18\x02 \x01(\x0b\x32(.chromiumos.test.artifact.TestInvocation\x12\x34\n\ttest_runs\x18\x03 \x03(\x0b\x32!.chromiumos.test.artifact.TestRun\"\xe1\x01\n\x0eTestInvocation\x12:\n\x0c\x64ut_topology\x18\x01 \x01(\x0b\x32$.chromiumos.test.lab.api.DutTopology\x12G\n\x16primary_execution_info\x18\x02 \x01(\x0b\x32\'.chromiumos.test.artifact.ExecutionInfo\x12J\n\x19secondary_executions_info\x18\x03 \x03(\x0b\x32\'.chromiumos.test.artifact.ExecutionInfo\"\xd7\x03\n\x07TestRun\x12>\n\x0etest_case_info\x18\x01 \x01(\x0b\x32&.chromiumos.test.artifact.TestCaseInfo\x12*\n\tlogs_info\x18\x02 \x03(\x0b\x32\x17.chromiumos.StoragePath\x12>\n\x0c\x64ut_topology\x18\x03 \x01(\x0b\x32$.chromiumos.test.lab.api.DutTopologyB\x02\x18\x01\x12K\n\x16primary_execution_info\x18\x04 \x01(\x0b\x32\'.chromiumos.test.artifact.ExecutionInfoB\x02\x18\x01\x12N\n\x19secondary_executions_info\x18\x05 \x03(\x0b\x32\'.chromiumos.test.artifact.ExecutionInfoB\x02\x18\x01\x12>\n\x0e\x63ustom_results\x18\x06 \x03(\x0b\x32&.chromiumos.test.artifact.CustomResult\x12\x43\n\x0ctest_plan_id\x18\x07 \x01(\x0b\x32-.chromiumos.test.api.v1.HWTestPlan.TestPlanId\"\xb5\x01\n\x0cTestCaseInfo\x12\x41\n\x12test_case_metadata\x18\x01 \x01(\x0b\x32%.chromiumos.test.api.TestCaseMetadata\x12=\n\x10test_case_result\x18\x02 \x01(\x0b\x32#.chromiumos.test.api.TestCaseResult\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\r\n\x05suite\x18\x04 \x01(\t\"\xad\x01\n\tBuildInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tmilestone\x18\x02 \x01(\x04\x12\x19\n\x11\x63hrome_os_version\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x18\n\x10snapshot_version\x18\x05 \x01(\t\x12\x14\n\x0c\x62uild_target\x18\x06 \x01(\t\x12\x15\n\rboard_variant\x18\x07 \x01(\t\x12\r\n\x05\x62oard\x18\x08 \x01(\t\"\xda\x01\n\x07\x44utInfo\x12)\n\x03\x64ut\x18\x01 \x01(\x0b\x32\x1c.chromiumos.test.lab.api.Dut\x12<\n\x0fprovision_state\x18\x02 \x01(\x0b\x32#.chromiumos.test.api.ProvisionState\x12\x39\n\x04tags\x18\x03 \x03(\x0b\x32+.chromiumos.test.artifact.DutInfo.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"}\n\rExecutionInfo\x12\x37\n\nbuild_info\x18\x01 \x01(\x0b\x32#.chromiumos.test.artifact.BuildInfo\x12\x33\n\x08\x64ut_info\x18\x02 \x01(\x0b\x32!.chromiumos.test.artifact.DutInfo\"\x8f\x01\n\x0c\x43ustomResult\x12\x35\n\x14result_artifact_path\x18\x01 \x01(\x0b\x32\x17.chromiumos.StoragePath\x12\x39\n\x03\x63ts\x18\x02 \x01(\x0b\x32*.chromiumos.test.artifact.CustomResult.CtsH\x00\x1a\x05\n\x03\x43tsB\x06\n\x04typeB4Z2go.chromium.org/chromiumos/config/go/test/artifactb\x06proto3')



_TESTRESULT = DESCRIPTOR.message_types_by_name['TestResult']
_TESTINVOCATION = DESCRIPTOR.message_types_by_name['TestInvocation']
_TESTRUN = DESCRIPTOR.message_types_by_name['TestRun']
_TESTCASEINFO = DESCRIPTOR.message_types_by_name['TestCaseInfo']
_BUILDINFO = DESCRIPTOR.message_types_by_name['BuildInfo']
_DUTINFO = DESCRIPTOR.message_types_by_name['DutInfo']
_DUTINFO_TAGSENTRY = _DUTINFO.nested_types_by_name['TagsEntry']
_EXECUTIONINFO = DESCRIPTOR.message_types_by_name['ExecutionInfo']
_CUSTOMRESULT = DESCRIPTOR.message_types_by_name['CustomResult']
_CUSTOMRESULT_CTS = _CUSTOMRESULT.nested_types_by_name['Cts']
TestResult = _reflection.GeneratedProtocolMessageType('TestResult', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESULT,
  '__module__' : 'chromiumos.test.artifact.test_result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.TestResult)
  })
_sym_db.RegisterMessage(TestResult)

TestInvocation = _reflection.GeneratedProtocolMessageType('TestInvocation', (_message.Message,), {
  'DESCRIPTOR' : _TESTINVOCATION,
  '__module__' : 'chromiumos.test.artifact.test_result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.TestInvocation)
  })
_sym_db.RegisterMessage(TestInvocation)

TestRun = _reflection.GeneratedProtocolMessageType('TestRun', (_message.Message,), {
  'DESCRIPTOR' : _TESTRUN,
  '__module__' : 'chromiumos.test.artifact.test_result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.TestRun)
  })
_sym_db.RegisterMessage(TestRun)

TestCaseInfo = _reflection.GeneratedProtocolMessageType('TestCaseInfo', (_message.Message,), {
  'DESCRIPTOR' : _TESTCASEINFO,
  '__module__' : 'chromiumos.test.artifact.test_result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.TestCaseInfo)
  })
_sym_db.RegisterMessage(TestCaseInfo)

BuildInfo = _reflection.GeneratedProtocolMessageType('BuildInfo', (_message.Message,), {
  'DESCRIPTOR' : _BUILDINFO,
  '__module__' : 'chromiumos.test.artifact.test_result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.BuildInfo)
  })
_sym_db.RegisterMessage(BuildInfo)

DutInfo = _reflection.GeneratedProtocolMessageType('DutInfo', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DUTINFO_TAGSENTRY,
    '__module__' : 'chromiumos.test.artifact.test_result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.DutInfo.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _DUTINFO,
  '__module__' : 'chromiumos.test.artifact.test_result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.DutInfo)
  })
_sym_db.RegisterMessage(DutInfo)
_sym_db.RegisterMessage(DutInfo.TagsEntry)

ExecutionInfo = _reflection.GeneratedProtocolMessageType('ExecutionInfo', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONINFO,
  '__module__' : 'chromiumos.test.artifact.test_result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.ExecutionInfo)
  })
_sym_db.RegisterMessage(ExecutionInfo)

CustomResult = _reflection.GeneratedProtocolMessageType('CustomResult', (_message.Message,), {

  'Cts' : _reflection.GeneratedProtocolMessageType('Cts', (_message.Message,), {
    'DESCRIPTOR' : _CUSTOMRESULT_CTS,
    '__module__' : 'chromiumos.test.artifact.test_result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.CustomResult.Cts)
    })
  ,
  'DESCRIPTOR' : _CUSTOMRESULT,
  '__module__' : 'chromiumos.test.artifact.test_result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.CustomResult)
  })
_sym_db.RegisterMessage(CustomResult)
_sym_db.RegisterMessage(CustomResult.Cts)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2go.chromium.org/chromiumos/config/go/test/artifact'
  _TESTRUN.fields_by_name['dut_topology']._options = None
  _TESTRUN.fields_by_name['dut_topology']._serialized_options = b'\030\001'
  _TESTRUN.fields_by_name['primary_execution_info']._options = None
  _TESTRUN.fields_by_name['primary_execution_info']._serialized_options = b'\030\001'
  _TESTRUN.fields_by_name['secondary_executions_info']._options = None
  _TESTRUN.fields_by_name['secondary_executions_info']._serialized_options = b'\030\001'
  _DUTINFO_TAGSENTRY._options = None
  _DUTINFO_TAGSENTRY._serialized_options = b'8\001'
  _TESTRESULT._serialized_start=307
  _TESTRESULT._serialized_end=457
  _TESTINVOCATION._serialized_start=460
  _TESTINVOCATION._serialized_end=685
  _TESTRUN._serialized_start=688
  _TESTRUN._serialized_end=1159
  _TESTCASEINFO._serialized_start=1162
  _TESTCASEINFO._serialized_end=1343
  _BUILDINFO._serialized_start=1346
  _BUILDINFO._serialized_end=1519
  _DUTINFO._serialized_start=1522
  _DUTINFO._serialized_end=1740
  _DUTINFO_TAGSENTRY._serialized_start=1697
  _DUTINFO_TAGSENTRY._serialized_end=1740
  _EXECUTIONINFO._serialized_start=1742
  _EXECUTIONINFO._serialized_end=1867
  _CUSTOMRESULT._serialized_start=1870
  _CUSTOMRESULT._serialized_end=2013
  _CUSTOMRESULT_CTS._serialized_start=2000
  _CUSTOMRESULT_CTS._serialized_end=2005
# @@protoc_insertion_point(module_scope)
