# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analysis_service/analysis_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromite.api import artifacts_pb2 as chromite_dot_api_dot_artifacts__pb2
from chromite.api.gen_sdk.chromite.api import binhost_pb2 as chromite_dot_api_dot_binhost__pb2
from chromite.api.gen_sdk.chromite.api import depgraph_pb2 as chromite_dot_api_dot_depgraph__pb2
from chromite.api.gen_sdk.chromite.api import firmware_pb2 as chromite_dot_api_dot_firmware__pb2
from chromite.api.gen_sdk.chromite.api import image_pb2 as chromite_dot_api_dot_image__pb2
from chromite.api.gen_sdk.chromite.api import packages_pb2 as chromite_dot_api_dot_packages__pb2
from chromite.api.gen_sdk.chromite.api import sdk_pb2 as chromite_dot_api_dot_sdk__pb2
from chromite.api.gen_sdk.chromite.api import sysroot_pb2 as chromite_dot_api_dot_sysroot__pb2
from chromite.api.gen_sdk.chromite.api import test_pb2 as chromite_dot_api_dot_test__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'analysis_service/analysis_service.proto\x12\x10\x61nalysis_service\x1a\x1c\x63hromite/api/artifacts.proto\x1a\x1a\x63hromite/api/binhost.proto\x1a\x1b\x63hromite/api/depgraph.proto\x1a\x1b\x63hromite/api/firmware.proto\x1a\x18\x63hromite/api/image.proto\x1a\x1b\x63hromite/api/packages.proto\x1a\x16\x63hromite/api/sdk.proto\x1a\x1a\x63hromite/api/sysroot.proto\x1a\x17\x63hromite/api/test.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"i\n\x13StepExecutionResult\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x13\n\x0bhad_timeout\x18\x02 \x01(\x08\x12\x15\n\rhad_exception\x18\x03 \x01(\x08\x12\x15\n\rwas_cancelled\x18\x04 \x01(\x08\"\xd4\x1d\n\x14\x41nalysisServiceEvent\x12\x10\n\x08\x62uild_id\x18* \x01(\x03\x12\x11\n\tstep_name\x18+ \x01(\t\x12\x30\n\x0crequest_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rresponse_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06stdout\x18\x32 \x01(\t\x12\x0e\n\x06stderr\x18\x33 \x01(\t\x12\x44\n\x15step_execution_result\x18\x34 \x01(\x0b\x32%.analysis_service.StepExecutionResult\x12H\n\x18install_packages_request\x18\x01 \x01(\x0b\x32$.chromite.api.InstallPackagesRequestH\x00\x12\x35\n\x0e\x62undle_request\x18\x05 \x01(\x0b\x32\x1b.chromite.api.BundleRequestH\x00\x12\x45\n\x17\x62undle_vm_files_request\x18\x07 \x01(\x0b\x32\".chromite.api.BundleVmFilesRequestH\x00\x12>\n\x13\x62inhost_get_request\x18\x08 \x01(\x0b\x32\x1f.chromite.api.BinhostGetRequestH\x00\x12\x38\n\x10\x61\x63l_args_request\x18\n \x01(\x0b\x32\x1c.chromite.api.AclArgsRequestH\x00\x12U\n\x1fprepare_binhost_uploads_request\x18\x0c \x01(\x0b\x32*.chromite.api.PrepareBinhostUploadsRequestH\x00\x12>\n\x13set_binhost_request\x18\x0e \x01(\x0b\x32\x1f.chromite.api.SetBinhostRequestH\x00\x12I\n\x19regen_build_cache_request\x18\x10 \x01(\x0b\x32$.chromite.api.RegenBuildCacheRequestH\x00\x12Z\n\"get_build_dependency_graph_request\x18\x12 \x01(\x0b\x32,.chromite.api.GetBuildDependencyGraphRequestH\x00\x12@\n\x14\x63reate_image_request\x18\x14 \x01(\x0b\x32 .chromite.api.CreateImageRequestH\x00\x12<\n\x12test_image_request\x18\x16 \x01(\x0b\x32\x1e.chromite.api.TestImageRequestH\x00\x12\x35\n\x0e\x63reate_request\x18\x18 \x01(\x0b\x32\x1b.chromite.api.CreateRequestH\x00\x12\x35\n\x0eupdate_request\x18\x1a \x01(\x0b\x32\x1b.chromite.api.UpdateRequestH\x00\x12\x44\n\x16sysroot_create_request\x18\x1c \x01(\x0b\x32\".chromite.api.SysrootCreateRequestH\x00\x12J\n\x19install_toolchain_request\x18\x1e \x01(\x0b\x32%.chromite.api.InstallToolchainRequestH\x00\x12R\n\x1e\x62uild_target_unit_test_request\x18  \x01(\x0b\x32(.chromite.api.BuildTargetUnitTestRequestH\x00\x12K\n\x1a\x63hromite_unit_test_request\x18\" \x01(\x0b\x32%.chromite.api.ChromiteUnitTestRequestH\x00\x12\x45\n\x17\x64\x65\x62ug_info_test_request\x18$ \x01(\x0b\x32\".chromite.api.DebugInfoTestRequestH\x00\x12\x36\n\x0fvm_test_request\x18& \x01(\x0b\x32\x1b.chromite.api.VmTestRequestH\x00\x12\x44\n\x16uprev_packages_request\x18, \x01(\x0b\x32\".chromite.api.UprevPackagesRequestH\x00\x12G\n\x18get_best_visible_request\x18. \x01(\x0b\x32#.chromite.api.GetBestVisibleRequestH\x00\x12K\n\x1aget_chrome_version_request\x18\x30 \x01(\x0b\x32%.chromite.api.GetChromeVersionRequestH\x00\x12O\n\x1cget_builder_metadata_request\x18\x35 \x01(\x0b\x32\'.chromite.api.GetBuilderMetadataRequestH\x00\x12K\n\x1a\x62uild_all_firmware_request\x18\x37 \x01(\x0b\x32%.chromite.api.BuildAllFirmwareRequestH\x00\x12I\n\x19test_all_firmware_request\x18\x39 \x01(\x0b\x32$.chromite.api.TestAllFirmwareRequestH\x00\x12J\n\x19install_packages_response\x18\x02 \x01(\x0b\x32%.chromite.api.InstallPackagesResponseH\x01\x12\x37\n\x0f\x62undle_response\x18\x06 \x01(\x0b\x32\x1c.chromite.api.BundleResponseH\x01\x12@\n\x14\x62inhost_get_response\x18\t \x01(\x0b\x32 .chromite.api.BinhostGetResponseH\x01\x12:\n\x11\x61\x63l_args_response\x18\x0b \x01(\x0b\x32\x1d.chromite.api.AclArgsResponseH\x01\x12W\n prepare_binhost_uploads_response\x18\r \x01(\x0b\x32+.chromite.api.PrepareBinhostUploadsResponseH\x01\x12@\n\x14set_binhost_response\x18\x0f \x01(\x0b\x32 .chromite.api.SetBinhostResponseH\x01\x12K\n\x1aregen_build_cache_response\x18\x11 \x01(\x0b\x32%.chromite.api.RegenBuildCacheResponseH\x01\x12\\\n#get_build_dependency_graph_response\x18\x13 \x01(\x0b\x32-.chromite.api.GetBuildDependencyGraphResponseH\x01\x12>\n\x13\x63reate_image_result\x18\x15 \x01(\x0b\x32\x1f.chromite.api.CreateImageResultH\x01\x12:\n\x11test_image_result\x18\x17 \x01(\x0b\x32\x1d.chromite.api.TestImageResultH\x01\x12\x37\n\x0f\x63reate_response\x18\x19 \x01(\x0b\x32\x1c.chromite.api.CreateResponseH\x01\x12\x37\n\x0fupdate_response\x18\x1b \x01(\x0b\x32\x1c.chromite.api.UpdateResponseH\x01\x12\x46\n\x17sysroot_create_response\x18\x1d \x01(\x0b\x32#.chromite.api.SysrootCreateResponseH\x01\x12L\n\x1ainstall_toolchain_response\x18\x1f \x01(\x0b\x32&.chromite.api.InstallToolchainResponseH\x01\x12T\n\x1f\x62uild_target_unit_test_response\x18! \x01(\x0b\x32).chromite.api.BuildTargetUnitTestResponseH\x01\x12M\n\x1b\x63hromite_unit_test_response\x18# \x01(\x0b\x32&.chromite.api.ChromiteUnitTestResponseH\x01\x12G\n\x18\x64\x65\x62ug_info_test_response\x18% \x01(\x0b\x32#.chromite.api.DebugInfoTestResponseH\x01\x12\x38\n\x10vm_test_response\x18\' \x01(\x0b\x32\x1c.chromite.api.VmTestResponseH\x01\x12\x46\n\x17uprev_packages_response\x18- \x01(\x0b\x32#.chromite.api.UprevPackagesResponseH\x01\x12I\n\x19get_best_visible_response\x18/ \x01(\x0b\x32$.chromite.api.GetBestVisibleResponseH\x01\x12M\n\x1bget_chrome_version_response\x18\x31 \x01(\x0b\x32&.chromite.api.GetChromeVersionResponseH\x01\x12Q\n\x1dget_builder_metadata_response\x18\x36 \x01(\x0b\x32(.chromite.api.GetBuilderMetadataResponseH\x01\x12M\n\x1b\x62uild_all_firmware_response\x18\x38 \x01(\x0b\x32&.chromite.api.BuildAllFirmwareResponseH\x01\x12K\n\x1atest_all_firmware_response\x18: \x01(\x0b\x32%.chromite.api.TestAllFirmwareResponseH\x01\x42\t\n\x07requestB\n\n\x08responseJ\x04\x08(\x10)J\x04\x08)\x10*B9Z7go.chromium.org/chromiumos/infra/proto/analysis_serviceb\x06proto3')



_STEPEXECUTIONRESULT = DESCRIPTOR.message_types_by_name['StepExecutionResult']
_ANALYSISSERVICEEVENT = DESCRIPTOR.message_types_by_name['AnalysisServiceEvent']
StepExecutionResult = _reflection.GeneratedProtocolMessageType('StepExecutionResult', (_message.Message,), {
  'DESCRIPTOR' : _STEPEXECUTIONRESULT,
  '__module__' : 'analysis_service.analysis_service_pb2'
  # @@protoc_insertion_point(class_scope:analysis_service.StepExecutionResult)
  })
_sym_db.RegisterMessage(StepExecutionResult)

AnalysisServiceEvent = _reflection.GeneratedProtocolMessageType('AnalysisServiceEvent', (_message.Message,), {
  'DESCRIPTOR' : _ANALYSISSERVICEEVENT,
  '__module__' : 'analysis_service.analysis_service_pb2'
  # @@protoc_insertion_point(class_scope:analysis_service.AnalysisServiceEvent)
  })
_sym_db.RegisterMessage(AnalysisServiceEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7go.chromium.org/chromiumos/infra/proto/analysis_service'
  _STEPEXECUTIONRESULT._serialized_start=342
  _STEPEXECUTIONRESULT._serialized_end=447
  _ANALYSISSERVICEEVENT._serialized_start=450
  _ANALYSISSERVICEEVENT._serialized_end=4246
# @@protoc_insertion_point(module_scope)
