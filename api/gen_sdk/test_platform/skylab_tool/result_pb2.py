# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_tool/result.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&test_platform/skylab_tool/result.proto\x12\x19test_platform.skylab_tool\"\xba\x04\n\x0eWaitTaskResult\x12K\n\x06result\x18\x01 \x01(\x0b\x32..test_platform.skylab_tool.WaitTaskResult.TaskR\x0btask-result\x12\x0e\n\x06stdout\x18\x02 \x01(\t\x12T\n\rchild_results\x18\x03 \x03(\x0b\x32..test_platform.skylab_tool.WaitTaskResult.TaskR\rchild-results\x12X\n\x0clog_data_url\x18\x04 \x01(\x0b\x32\x34.test_platform.skylab_tool.WaitTaskResult.LogDataURLR\x0clog-data-url\x1a\xdb\x01\n\x04Task\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x0f\n\x07\x66\x61ilure\x18\x03 \x01(\x08\x12\x0f\n\x07success\x18\x04 \x01(\x08\x12 \n\x0btask_run_id\x18\x05 \x01(\tR\x0btask-run-id\x12(\n\x0ftask_request_id\x18\x06 \x01(\tR\x0ftask-request-id\x12\"\n\x0ctask_run_url\x18\x07 \x01(\tR\x0ctask-run-url\x12$\n\rtask_logs_url\x18\x08 \x01(\tR\rtask-logs-url\x1a=\n\nLogDataURL\x12\x17\n\x0bisolate_url\x18\x01 \x01(\tB\x02\x18\x01\x12\x16\n\x06gs_url\x18\x02 \x01(\tR\x06gs-url\"a\n\x0fWaitTasksResult\x12:\n\x07results\x18\x01 \x03(\x0b\x32).test_platform.skylab_tool.WaitTaskResult\x12\x12\n\nincomplete\x18\x02 \x01(\x08\x42\x45ZCgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_toolb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_platform.skylab_tool.result_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZCgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_tool'
  _WAITTASKRESULT_LOGDATAURL.fields_by_name['isolate_url']._options = None
  _WAITTASKRESULT_LOGDATAURL.fields_by_name['isolate_url']._serialized_options = b'\030\001'
  _WAITTASKRESULT._serialized_start=70
  _WAITTASKRESULT._serialized_end=640
  _WAITTASKRESULT_TASK._serialized_start=358
  _WAITTASKRESULT_TASK._serialized_end=577
  _WAITTASKRESULT_LOGDATAURL._serialized_start=579
  _WAITTASKRESULT_LOGDATAURL._serialized_end=640
  _WAITTASKSRESULT._serialized_start=642
  _WAITTASKSRESULT._serialized_end=739
# @@protoc_insertion_point(module_scope)
