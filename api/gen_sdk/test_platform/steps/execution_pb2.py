# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/steps/execution.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.test_platform.common import task_pb2 as test__platform_dot_common_dot_task__pb2
from chromite.api.gen_sdk.test_platform.config import config_pb2 as test__platform_dot_config_dot_config__pb2
from chromite.api.gen_sdk.test_platform import request_pb2 as test__platform_dot_request__pb2
from chromite.api.gen_sdk.test_platform.steps import enumeration_pb2 as test__platform_dot_steps_dot_enumeration__pb2
from chromite.api.gen_sdk.test_platform.steps.execute import build_pb2 as test__platform_dot_steps_dot_execute_dot_build__pb2
from chromite.api.gen_sdk.test_platform import taskstate_pb2 as test__platform_dot_taskstate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/steps/execution.proto',
  package='test_platform.steps',
  syntax='proto3',
  serialized_options=_b('Z=go.chromium.org/chromiumos/infra/proto/go/test_platform/steps'),
  serialized_pb=_b('\n#test_platform/steps/execution.proto\x12\x13test_platform.steps\x1a\x1ftest_platform/common/task.proto\x1a!test_platform/config/config.proto\x1a\x1btest_platform/request.proto\x1a%test_platform/steps/enumeration.proto\x1a\'test_platform/steps/execute/build.proto\x1a\x1dtest_platform/taskstate.proto\"\xaa\x02\n\x0f\x45xecuteRequests\x12\x35\n\x08requests\x18\x01 \x03(\x0b\x32#.test_platform.steps.ExecuteRequest\x12Q\n\x0ftagged_requests\x18\x02 \x03(\x0b\x32\x38.test_platform.steps.ExecuteRequests.TaggedRequestsEntry\x12\x31\n\x05\x62uild\x18\x03 \x01(\x0b\x32\".test_platform.steps.execute.Build\x1aZ\n\x13TaggedRequestsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.test_platform.steps.ExecuteRequest:\x02\x38\x01\"\xff\x01\n\x10\x45xecuteResponses\x12\x37\n\tresponses\x18\x01 \x03(\x0b\x32$.test_platform.steps.ExecuteResponse\x12T\n\x10tagged_responses\x18\x02 \x03(\x0b\x32:.test_platform.steps.ExecuteResponses.TaggedResponsesEntry\x1a\\\n\x14TaggedResponsesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.test_platform.steps.ExecuteResponse:\x02\x38\x01\"\xb4\x01\n\x0e\x45xecuteRequest\x12\x35\n\x0erequest_params\x18\x01 \x01(\x0b\x32\x1d.test_platform.Request.Params\x12=\n\x0b\x65numeration\x18\x02 \x01(\x0b\x32(.test_platform.steps.EnumerationResponse\x12,\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x1c.test_platform.config.Config\"\xec\x08\n\x0f\x45xecuteResponse\x12I\n\x0ctask_results\x18\x01 \x03(\x0b\x32/.test_platform.steps.ExecuteResponse.TaskResultB\x02\x18\x01\x12U\n\x14\x63onsolidated_results\x18\x03 \x03(\x0b\x32\x37.test_platform.steps.ExecuteResponse.ConsolidatedResult\x12\'\n\x05state\x18\x02 \x01(\x0b\x32\x18.test_platform.TaskState\x1a\xb4\x06\n\nTaskResult\x12\x10\n\x08task_url\x18\x02 \x01(\t\x12\'\n\x05state\x18\x03 \x01(\x0b\x32\x18.test_platform.TaskState\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07log_url\x18\x05 \x01(\t\x12\x0f\n\x07\x61ttempt\x18\x06 \x01(\x05\x12R\n\ntest_cases\x18\x07 \x03(\x0b\x32>.test_platform.steps.ExecuteResponse.TaskResult.TestCaseResult\x12T\n\x0cprejob_steps\x18\x08 \x03(\x0b\x32>.test_platform.steps.ExecuteResponse.TaskResult.TestCaseResult\x12\x33\n\x08log_data\x18\t \x01(\x0b\x32!.test_platform.common.TaskLogData\x12q\n\x18rejected_task_dimensions\x18\x0b \x03(\x0b\x32K.test_platform.steps.ExecuteResponse.TaskResult.RejectedTaskDimensionsEntryB\x02\x18\x01\x12\x62\n\x13rejected_dimensions\x18\x0c \x03(\x0b\x32\x45.test_platform.steps.ExecuteResponse.TaskResult.RejectedTaskDimension\x1aq\n\x0eTestCaseResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x07verdict\x18\x02 \x01(\x0e\x32 .test_platform.TaskState.Verdict\x12\x1e\n\x16human_readable_summary\x18\x03 \x01(\t\x1a=\n\x1bRejectedTaskDimensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x33\n\x15RejectedTaskDimension\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tJ\x04\x08\n\x10\x0bR\x18synchronous_log_data_url\x1aW\n\x12\x43onsolidatedResult\x12\x41\n\x08\x61ttempts\x18\x01 \x03(\x0b\x32/.test_platform.steps.ExecuteResponse.TaskResultB?Z=go.chromium.org/chromiumos/infra/proto/go/test_platform/stepsb\x06proto3')
  ,
  dependencies=[test__platform_dot_common_dot_task__pb2.DESCRIPTOR,test__platform_dot_config_dot_config__pb2.DESCRIPTOR,test__platform_dot_request__pb2.DESCRIPTOR,test__platform_dot_steps_dot_enumeration__pb2.DESCRIPTOR,test__platform_dot_steps_dot_execute_dot_build__pb2.DESCRIPTOR,test__platform_dot_taskstate__pb2.DESCRIPTOR,])




_EXECUTEREQUESTS_TAGGEDREQUESTSENTRY = _descriptor.Descriptor(
  name='TaggedRequestsEntry',
  full_name='test_platform.steps.ExecuteRequests.TaggedRequestsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.steps.ExecuteRequests.TaggedRequestsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.steps.ExecuteRequests.TaggedRequestsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=567,
)

_EXECUTEREQUESTS = _descriptor.Descriptor(
  name='ExecuteRequests',
  full_name='test_platform.steps.ExecuteRequests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requests', full_name='test_platform.steps.ExecuteRequests.requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagged_requests', full_name='test_platform.steps.ExecuteRequests.tagged_requests', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build', full_name='test_platform.steps.ExecuteRequests.build', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXECUTEREQUESTS_TAGGEDREQUESTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=567,
)


_EXECUTERESPONSES_TAGGEDRESPONSESENTRY = _descriptor.Descriptor(
  name='TaggedResponsesEntry',
  full_name='test_platform.steps.ExecuteResponses.TaggedResponsesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.steps.ExecuteResponses.TaggedResponsesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.steps.ExecuteResponses.TaggedResponsesEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=733,
  serialized_end=825,
)

_EXECUTERESPONSES = _descriptor.Descriptor(
  name='ExecuteResponses',
  full_name='test_platform.steps.ExecuteResponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='test_platform.steps.ExecuteResponses.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagged_responses', full_name='test_platform.steps.ExecuteResponses.tagged_responses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXECUTERESPONSES_TAGGEDRESPONSESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=570,
  serialized_end=825,
)


_EXECUTEREQUEST = _descriptor.Descriptor(
  name='ExecuteRequest',
  full_name='test_platform.steps.ExecuteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_params', full_name='test_platform.steps.ExecuteRequest.request_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enumeration', full_name='test_platform.steps.ExecuteRequest.enumeration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='test_platform.steps.ExecuteRequest.config', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=828,
  serialized_end=1008,
)


_EXECUTERESPONSE_TASKRESULT_TESTCASERESULT = _descriptor.Descriptor(
  name='TestCaseResult',
  full_name='test_platform.steps.ExecuteResponse.TaskResult.TestCaseResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test_platform.steps.ExecuteResponse.TaskResult.TestCaseResult.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verdict', full_name='test_platform.steps.ExecuteResponse.TaskResult.TestCaseResult.verdict', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='human_readable_summary', full_name='test_platform.steps.ExecuteResponse.TaskResult.TestCaseResult.human_readable_summary', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1793,
  serialized_end=1906,
)

_EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSIONSENTRY = _descriptor.Descriptor(
  name='RejectedTaskDimensionsEntry',
  full_name='test_platform.steps.ExecuteResponse.TaskResult.RejectedTaskDimensionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.steps.ExecuteResponse.TaskResult.RejectedTaskDimensionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.steps.ExecuteResponse.TaskResult.RejectedTaskDimensionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1908,
  serialized_end=1969,
)

_EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSION = _descriptor.Descriptor(
  name='RejectedTaskDimension',
  full_name='test_platform.steps.ExecuteResponse.TaskResult.RejectedTaskDimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.steps.ExecuteResponse.TaskResult.RejectedTaskDimension.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.steps.ExecuteResponse.TaskResult.RejectedTaskDimension.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1971,
  serialized_end=2022,
)

_EXECUTERESPONSE_TASKRESULT = _descriptor.Descriptor(
  name='TaskResult',
  full_name='test_platform.steps.ExecuteResponse.TaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_url', full_name='test_platform.steps.ExecuteResponse.TaskResult.task_url', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='test_platform.steps.ExecuteResponse.TaskResult.state', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='test_platform.steps.ExecuteResponse.TaskResult.name', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_url', full_name='test_platform.steps.ExecuteResponse.TaskResult.log_url', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attempt', full_name='test_platform.steps.ExecuteResponse.TaskResult.attempt', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_cases', full_name='test_platform.steps.ExecuteResponse.TaskResult.test_cases', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prejob_steps', full_name='test_platform.steps.ExecuteResponse.TaskResult.prejob_steps', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_data', full_name='test_platform.steps.ExecuteResponse.TaskResult.log_data', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rejected_task_dimensions', full_name='test_platform.steps.ExecuteResponse.TaskResult.rejected_task_dimensions', index=8,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rejected_dimensions', full_name='test_platform.steps.ExecuteResponse.TaskResult.rejected_dimensions', index=9,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXECUTERESPONSE_TASKRESULT_TESTCASERESULT, _EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSIONSENTRY, _EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1234,
  serialized_end=2054,
)

_EXECUTERESPONSE_CONSOLIDATEDRESULT = _descriptor.Descriptor(
  name='ConsolidatedResult',
  full_name='test_platform.steps.ExecuteResponse.ConsolidatedResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attempts', full_name='test_platform.steps.ExecuteResponse.ConsolidatedResult.attempts', index=0,
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
  serialized_start=2056,
  serialized_end=2143,
)

_EXECUTERESPONSE = _descriptor.Descriptor(
  name='ExecuteResponse',
  full_name='test_platform.steps.ExecuteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_results', full_name='test_platform.steps.ExecuteResponse.task_results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consolidated_results', full_name='test_platform.steps.ExecuteResponse.consolidated_results', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='test_platform.steps.ExecuteResponse.state', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXECUTERESPONSE_TASKRESULT, _EXECUTERESPONSE_CONSOLIDATEDRESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1011,
  serialized_end=2143,
)

_EXECUTEREQUESTS_TAGGEDREQUESTSENTRY.fields_by_name['value'].message_type = _EXECUTEREQUEST
_EXECUTEREQUESTS_TAGGEDREQUESTSENTRY.containing_type = _EXECUTEREQUESTS
_EXECUTEREQUESTS.fields_by_name['requests'].message_type = _EXECUTEREQUEST
_EXECUTEREQUESTS.fields_by_name['tagged_requests'].message_type = _EXECUTEREQUESTS_TAGGEDREQUESTSENTRY
_EXECUTEREQUESTS.fields_by_name['build'].message_type = test__platform_dot_steps_dot_execute_dot_build__pb2._BUILD
_EXECUTERESPONSES_TAGGEDRESPONSESENTRY.fields_by_name['value'].message_type = _EXECUTERESPONSE
_EXECUTERESPONSES_TAGGEDRESPONSESENTRY.containing_type = _EXECUTERESPONSES
_EXECUTERESPONSES.fields_by_name['responses'].message_type = _EXECUTERESPONSE
_EXECUTERESPONSES.fields_by_name['tagged_responses'].message_type = _EXECUTERESPONSES_TAGGEDRESPONSESENTRY
_EXECUTEREQUEST.fields_by_name['request_params'].message_type = test__platform_dot_request__pb2._REQUEST_PARAMS
_EXECUTEREQUEST.fields_by_name['enumeration'].message_type = test__platform_dot_steps_dot_enumeration__pb2._ENUMERATIONRESPONSE
_EXECUTEREQUEST.fields_by_name['config'].message_type = test__platform_dot_config_dot_config__pb2._CONFIG
_EXECUTERESPONSE_TASKRESULT_TESTCASERESULT.fields_by_name['verdict'].enum_type = test__platform_dot_taskstate__pb2._TASKSTATE_VERDICT
_EXECUTERESPONSE_TASKRESULT_TESTCASERESULT.containing_type = _EXECUTERESPONSE_TASKRESULT
_EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSIONSENTRY.containing_type = _EXECUTERESPONSE_TASKRESULT
_EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSION.containing_type = _EXECUTERESPONSE_TASKRESULT
_EXECUTERESPONSE_TASKRESULT.fields_by_name['state'].message_type = test__platform_dot_taskstate__pb2._TASKSTATE
_EXECUTERESPONSE_TASKRESULT.fields_by_name['test_cases'].message_type = _EXECUTERESPONSE_TASKRESULT_TESTCASERESULT
_EXECUTERESPONSE_TASKRESULT.fields_by_name['prejob_steps'].message_type = _EXECUTERESPONSE_TASKRESULT_TESTCASERESULT
_EXECUTERESPONSE_TASKRESULT.fields_by_name['log_data'].message_type = test__platform_dot_common_dot_task__pb2._TASKLOGDATA
_EXECUTERESPONSE_TASKRESULT.fields_by_name['rejected_task_dimensions'].message_type = _EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSIONSENTRY
_EXECUTERESPONSE_TASKRESULT.fields_by_name['rejected_dimensions'].message_type = _EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSION
_EXECUTERESPONSE_TASKRESULT.containing_type = _EXECUTERESPONSE
_EXECUTERESPONSE_CONSOLIDATEDRESULT.fields_by_name['attempts'].message_type = _EXECUTERESPONSE_TASKRESULT
_EXECUTERESPONSE_CONSOLIDATEDRESULT.containing_type = _EXECUTERESPONSE
_EXECUTERESPONSE.fields_by_name['task_results'].message_type = _EXECUTERESPONSE_TASKRESULT
_EXECUTERESPONSE.fields_by_name['consolidated_results'].message_type = _EXECUTERESPONSE_CONSOLIDATEDRESULT
_EXECUTERESPONSE.fields_by_name['state'].message_type = test__platform_dot_taskstate__pb2._TASKSTATE
DESCRIPTOR.message_types_by_name['ExecuteRequests'] = _EXECUTEREQUESTS
DESCRIPTOR.message_types_by_name['ExecuteResponses'] = _EXECUTERESPONSES
DESCRIPTOR.message_types_by_name['ExecuteRequest'] = _EXECUTEREQUEST
DESCRIPTOR.message_types_by_name['ExecuteResponse'] = _EXECUTERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecuteRequests = _reflection.GeneratedProtocolMessageType('ExecuteRequests', (_message.Message,), dict(

  TaggedRequestsEntry = _reflection.GeneratedProtocolMessageType('TaggedRequestsEntry', (_message.Message,), dict(
    DESCRIPTOR = _EXECUTEREQUESTS_TAGGEDREQUESTSENTRY,
    __module__ = 'test_platform.steps.execution_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteRequests.TaggedRequestsEntry)
    ))
  ,
  DESCRIPTOR = _EXECUTEREQUESTS,
  __module__ = 'test_platform.steps.execution_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteRequests)
  ))
_sym_db.RegisterMessage(ExecuteRequests)
_sym_db.RegisterMessage(ExecuteRequests.TaggedRequestsEntry)

ExecuteResponses = _reflection.GeneratedProtocolMessageType('ExecuteResponses', (_message.Message,), dict(

  TaggedResponsesEntry = _reflection.GeneratedProtocolMessageType('TaggedResponsesEntry', (_message.Message,), dict(
    DESCRIPTOR = _EXECUTERESPONSES_TAGGEDRESPONSESENTRY,
    __module__ = 'test_platform.steps.execution_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteResponses.TaggedResponsesEntry)
    ))
  ,
  DESCRIPTOR = _EXECUTERESPONSES,
  __module__ = 'test_platform.steps.execution_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteResponses)
  ))
_sym_db.RegisterMessage(ExecuteResponses)
_sym_db.RegisterMessage(ExecuteResponses.TaggedResponsesEntry)

ExecuteRequest = _reflection.GeneratedProtocolMessageType('ExecuteRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTEREQUEST,
  __module__ = 'test_platform.steps.execution_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteRequest)
  ))
_sym_db.RegisterMessage(ExecuteRequest)

ExecuteResponse = _reflection.GeneratedProtocolMessageType('ExecuteResponse', (_message.Message,), dict(

  TaskResult = _reflection.GeneratedProtocolMessageType('TaskResult', (_message.Message,), dict(

    TestCaseResult = _reflection.GeneratedProtocolMessageType('TestCaseResult', (_message.Message,), dict(
      DESCRIPTOR = _EXECUTERESPONSE_TASKRESULT_TESTCASERESULT,
      __module__ = 'test_platform.steps.execution_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteResponse.TaskResult.TestCaseResult)
      ))
    ,

    RejectedTaskDimensionsEntry = _reflection.GeneratedProtocolMessageType('RejectedTaskDimensionsEntry', (_message.Message,), dict(
      DESCRIPTOR = _EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSIONSENTRY,
      __module__ = 'test_platform.steps.execution_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteResponse.TaskResult.RejectedTaskDimensionsEntry)
      ))
    ,

    RejectedTaskDimension = _reflection.GeneratedProtocolMessageType('RejectedTaskDimension', (_message.Message,), dict(
      DESCRIPTOR = _EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSION,
      __module__ = 'test_platform.steps.execution_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteResponse.TaskResult.RejectedTaskDimension)
      ))
    ,
    DESCRIPTOR = _EXECUTERESPONSE_TASKRESULT,
    __module__ = 'test_platform.steps.execution_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteResponse.TaskResult)
    ))
  ,

  ConsolidatedResult = _reflection.GeneratedProtocolMessageType('ConsolidatedResult', (_message.Message,), dict(
    DESCRIPTOR = _EXECUTERESPONSE_CONSOLIDATEDRESULT,
    __module__ = 'test_platform.steps.execution_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteResponse.ConsolidatedResult)
    ))
  ,
  DESCRIPTOR = _EXECUTERESPONSE,
  __module__ = 'test_platform.steps.execution_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.steps.ExecuteResponse)
  ))
_sym_db.RegisterMessage(ExecuteResponse)
_sym_db.RegisterMessage(ExecuteResponse.TaskResult)
_sym_db.RegisterMessage(ExecuteResponse.TaskResult.TestCaseResult)
_sym_db.RegisterMessage(ExecuteResponse.TaskResult.RejectedTaskDimensionsEntry)
_sym_db.RegisterMessage(ExecuteResponse.TaskResult.RejectedTaskDimension)
_sym_db.RegisterMessage(ExecuteResponse.ConsolidatedResult)


DESCRIPTOR._options = None
_EXECUTEREQUESTS_TAGGEDREQUESTSENTRY._options = None
_EXECUTERESPONSES_TAGGEDRESPONSESENTRY._options = None
_EXECUTERESPONSE_TASKRESULT_REJECTEDTASKDIMENSIONSENTRY._options = None
_EXECUTERESPONSE_TASKRESULT.fields_by_name['rejected_task_dimensions']._options = None
_EXECUTERESPONSE.fields_by_name['task_results']._options = None
# @@protoc_insertion_point(module_scope)
