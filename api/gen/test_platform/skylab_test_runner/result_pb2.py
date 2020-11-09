# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_test_runner/result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.test_platform.common import task_pb2 as test__platform_dot_common_dot_task__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/skylab_test_runner/result.proto',
  package='test_platform.skylab_test_runner',
  syntax='proto3',
  serialized_options=_b('ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runner'),
  serialized_pb=_b('\n-test_platform/skylab_test_runner/result.proto\x12 test_platform.skylab_test_runner\x1a\x1ftest_platform/common/task.proto\"0\n\x0c\x41syncResults\x12\x10\n\x08logs_url\x18\x01 \x01(\t\x12\x0e\n\x06gs_url\x18\x02 \x01(\t\"\xec\t\n\x06Result\x12L\n\x0f\x61utotest_result\x18\x01 \x01(\x0b\x32\x31.test_platform.skylab_test_runner.Result.AutotestH\x00\x12?\n\x06prejob\x18\x02 \x01(\x0b\x32/.test_platform.skylab_test_runner.Result.Prejob\x12\x33\n\x08log_data\x18\x03 \x01(\x0b\x32!.test_platform.common.TaskLogData\x12J\n\x0cstate_update\x18\x04 \x01(\x0b\x32\x34.test_platform.skylab_test_runner.Result.StateUpdate\x12\x45\n\rasync_results\x18\x05 \x01(\x0b\x32..test_platform.skylab_test_runner.AsyncResults\x12W\n\x10\x61utotest_results\x18\x06 \x03(\x0b\x32=.test_platform.skylab_test_runner.Result.AutotestResultsEntry\x1a\xfe\x02\n\x08\x41utotest\x12N\n\ntest_cases\x18\x01 \x03(\x0b\x32:.test_platform.skylab_test_runner.Result.Autotest.TestCase\x12\x12\n\nincomplete\x18\x02 \x01(\x08\x12 \n\x18synchronous_log_data_url\x18\x03 \x01(\t\x1a\xeb\x01\n\x08TestCase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12S\n\x07verdict\x18\x02 \x01(\x0e\x32\x42.test_platform.skylab_test_runner.Result.Autotest.TestCase.Verdict\x12\x1e\n\x16human_readable_summary\x18\x03 \x01(\t\"\\\n\x07Verdict\x12\x15\n\x11VERDICT_UNDEFINED\x10\x00\x12\x10\n\x0cVERDICT_PASS\x10\x01\x12\x10\n\x0cVERDICT_FAIL\x10\x02\x12\x16\n\x12VERDICT_NO_VERDICT\x10\x03\x1a\x98\x02\n\x06Prejob\x12\x42\n\x04step\x18\x01 \x03(\x0b\x32\x34.test_platform.skylab_test_runner.Result.Prejob.Step\x1a\xc9\x01\n\x04Step\x12\x0c\n\x04name\x18\x01 \x01(\t\x12M\n\x07verdict\x18\x02 \x01(\x0e\x32<.test_platform.skylab_test_runner.Result.Prejob.Step.Verdict\x12\x1e\n\x16human_readable_summary\x18\x03 \x01(\t\"D\n\x07Verdict\x12\x15\n\x11VERDICT_UNDEFINED\x10\x00\x12\x10\n\x0cVERDICT_PASS\x10\x01\x12\x10\n\x0cVERDICT_FAIL\x10\x02\x1a \n\x0bStateUpdate\x12\x11\n\tdut_state\x18\x01 \x01(\t\x1ai\n\x14\x41utotestResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b\x32\x31.test_platform.skylab_test_runner.Result.Autotest:\x02\x38\x01\x42\t\n\x07harnessBLZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runnerb\x06proto3')
  ,
  dependencies=[test__platform_dot_common_dot_task__pb2.DESCRIPTOR,])



_RESULT_AUTOTEST_TESTCASE_VERDICT = _descriptor.EnumDescriptor(
  name='Verdict',
  full_name='test_platform.skylab_test_runner.Result.Autotest.TestCase.Verdict',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VERDICT_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_PASS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_FAIL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_NO_VERDICT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=900,
  serialized_end=992,
)
_sym_db.RegisterEnumDescriptor(_RESULT_AUTOTEST_TESTCASE_VERDICT)

_RESULT_PREJOB_STEP_VERDICT = _descriptor.EnumDescriptor(
  name='Verdict',
  full_name='test_platform.skylab_test_runner.Result.Prejob.Step.Verdict',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VERDICT_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_PASS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_FAIL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=900,
  serialized_end=968,
)
_sym_db.RegisterEnumDescriptor(_RESULT_PREJOB_STEP_VERDICT)


_ASYNCRESULTS = _descriptor.Descriptor(
  name='AsyncResults',
  full_name='test_platform.skylab_test_runner.AsyncResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logs_url', full_name='test_platform.skylab_test_runner.AsyncResults.logs_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gs_url', full_name='test_platform.skylab_test_runner.AsyncResults.gs_url', index=1,
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
  serialized_start=116,
  serialized_end=164,
)


_RESULT_AUTOTEST_TESTCASE = _descriptor.Descriptor(
  name='TestCase',
  full_name='test_platform.skylab_test_runner.Result.Autotest.TestCase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test_platform.skylab_test_runner.Result.Autotest.TestCase.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verdict', full_name='test_platform.skylab_test_runner.Result.Autotest.TestCase.verdict', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='human_readable_summary', full_name='test_platform.skylab_test_runner.Result.Autotest.TestCase.human_readable_summary', index=2,
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
    _RESULT_AUTOTEST_TESTCASE_VERDICT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=757,
  serialized_end=992,
)

_RESULT_AUTOTEST = _descriptor.Descriptor(
  name='Autotest',
  full_name='test_platform.skylab_test_runner.Result.Autotest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_cases', full_name='test_platform.skylab_test_runner.Result.Autotest.test_cases', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incomplete', full_name='test_platform.skylab_test_runner.Result.Autotest.incomplete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='synchronous_log_data_url', full_name='test_platform.skylab_test_runner.Result.Autotest.synchronous_log_data_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESULT_AUTOTEST_TESTCASE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=992,
)

_RESULT_PREJOB_STEP = _descriptor.Descriptor(
  name='Step',
  full_name='test_platform.skylab_test_runner.Result.Prejob.Step',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test_platform.skylab_test_runner.Result.Prejob.Step.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verdict', full_name='test_platform.skylab_test_runner.Result.Prejob.Step.verdict', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='human_readable_summary', full_name='test_platform.skylab_test_runner.Result.Prejob.Step.human_readable_summary', index=2,
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
    _RESULT_PREJOB_STEP_VERDICT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1074,
  serialized_end=1275,
)

_RESULT_PREJOB = _descriptor.Descriptor(
  name='Prejob',
  full_name='test_platform.skylab_test_runner.Result.Prejob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='test_platform.skylab_test_runner.Result.Prejob.step', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESULT_PREJOB_STEP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=995,
  serialized_end=1275,
)

_RESULT_STATEUPDATE = _descriptor.Descriptor(
  name='StateUpdate',
  full_name='test_platform.skylab_test_runner.Result.StateUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dut_state', full_name='test_platform.skylab_test_runner.Result.StateUpdate.dut_state', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1277,
  serialized_end=1309,
)

_RESULT_AUTOTESTRESULTSENTRY = _descriptor.Descriptor(
  name='AutotestResultsEntry',
  full_name='test_platform.skylab_test_runner.Result.AutotestResultsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.skylab_test_runner.Result.AutotestResultsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.skylab_test_runner.Result.AutotestResultsEntry.value', index=1,
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
  serialized_start=1311,
  serialized_end=1416,
)

_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='test_platform.skylab_test_runner.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='autotest_result', full_name='test_platform.skylab_test_runner.Result.autotest_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prejob', full_name='test_platform.skylab_test_runner.Result.prejob', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_data', full_name='test_platform.skylab_test_runner.Result.log_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_update', full_name='test_platform.skylab_test_runner.Result.state_update', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='async_results', full_name='test_platform.skylab_test_runner.Result.async_results', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='autotest_results', full_name='test_platform.skylab_test_runner.Result.autotest_results', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESULT_AUTOTEST, _RESULT_PREJOB, _RESULT_STATEUPDATE, _RESULT_AUTOTESTRESULTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='harness', full_name='test_platform.skylab_test_runner.Result.harness',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=167,
  serialized_end=1427,
)

_RESULT_AUTOTEST_TESTCASE.fields_by_name['verdict'].enum_type = _RESULT_AUTOTEST_TESTCASE_VERDICT
_RESULT_AUTOTEST_TESTCASE.containing_type = _RESULT_AUTOTEST
_RESULT_AUTOTEST_TESTCASE_VERDICT.containing_type = _RESULT_AUTOTEST_TESTCASE
_RESULT_AUTOTEST.fields_by_name['test_cases'].message_type = _RESULT_AUTOTEST_TESTCASE
_RESULT_AUTOTEST.containing_type = _RESULT
_RESULT_PREJOB_STEP.fields_by_name['verdict'].enum_type = _RESULT_PREJOB_STEP_VERDICT
_RESULT_PREJOB_STEP.containing_type = _RESULT_PREJOB
_RESULT_PREJOB_STEP_VERDICT.containing_type = _RESULT_PREJOB_STEP
_RESULT_PREJOB.fields_by_name['step'].message_type = _RESULT_PREJOB_STEP
_RESULT_PREJOB.containing_type = _RESULT
_RESULT_STATEUPDATE.containing_type = _RESULT
_RESULT_AUTOTESTRESULTSENTRY.fields_by_name['value'].message_type = _RESULT_AUTOTEST
_RESULT_AUTOTESTRESULTSENTRY.containing_type = _RESULT
_RESULT.fields_by_name['autotest_result'].message_type = _RESULT_AUTOTEST
_RESULT.fields_by_name['prejob'].message_type = _RESULT_PREJOB
_RESULT.fields_by_name['log_data'].message_type = test__platform_dot_common_dot_task__pb2._TASKLOGDATA
_RESULT.fields_by_name['state_update'].message_type = _RESULT_STATEUPDATE
_RESULT.fields_by_name['async_results'].message_type = _ASYNCRESULTS
_RESULT.fields_by_name['autotest_results'].message_type = _RESULT_AUTOTESTRESULTSENTRY
_RESULT.oneofs_by_name['harness'].fields.append(
  _RESULT.fields_by_name['autotest_result'])
_RESULT.fields_by_name['autotest_result'].containing_oneof = _RESULT.oneofs_by_name['harness']
DESCRIPTOR.message_types_by_name['AsyncResults'] = _ASYNCRESULTS
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AsyncResults = _reflection.GeneratedProtocolMessageType('AsyncResults', (_message.Message,), dict(
  DESCRIPTOR = _ASYNCRESULTS,
  __module__ = 'test_platform.skylab_test_runner.result_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.AsyncResults)
  ))
_sym_db.RegisterMessage(AsyncResults)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(

  Autotest = _reflection.GeneratedProtocolMessageType('Autotest', (_message.Message,), dict(

    TestCase = _reflection.GeneratedProtocolMessageType('TestCase', (_message.Message,), dict(
      DESCRIPTOR = _RESULT_AUTOTEST_TESTCASE,
      __module__ = 'test_platform.skylab_test_runner.result_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Result.Autotest.TestCase)
      ))
    ,
    DESCRIPTOR = _RESULT_AUTOTEST,
    __module__ = 'test_platform.skylab_test_runner.result_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Result.Autotest)
    ))
  ,

  Prejob = _reflection.GeneratedProtocolMessageType('Prejob', (_message.Message,), dict(

    Step = _reflection.GeneratedProtocolMessageType('Step', (_message.Message,), dict(
      DESCRIPTOR = _RESULT_PREJOB_STEP,
      __module__ = 'test_platform.skylab_test_runner.result_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Result.Prejob.Step)
      ))
    ,
    DESCRIPTOR = _RESULT_PREJOB,
    __module__ = 'test_platform.skylab_test_runner.result_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Result.Prejob)
    ))
  ,

  StateUpdate = _reflection.GeneratedProtocolMessageType('StateUpdate', (_message.Message,), dict(
    DESCRIPTOR = _RESULT_STATEUPDATE,
    __module__ = 'test_platform.skylab_test_runner.result_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Result.StateUpdate)
    ))
  ,

  AutotestResultsEntry = _reflection.GeneratedProtocolMessageType('AutotestResultsEntry', (_message.Message,), dict(
    DESCRIPTOR = _RESULT_AUTOTESTRESULTSENTRY,
    __module__ = 'test_platform.skylab_test_runner.result_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Result.AutotestResultsEntry)
    ))
  ,
  DESCRIPTOR = _RESULT,
  __module__ = 'test_platform.skylab_test_runner.result_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.skylab_test_runner.Result)
  ))
_sym_db.RegisterMessage(Result)
_sym_db.RegisterMessage(Result.Autotest)
_sym_db.RegisterMessage(Result.Autotest.TestCase)
_sym_db.RegisterMessage(Result.Prejob)
_sym_db.RegisterMessage(Result.Prejob.Step)
_sym_db.RegisterMessage(Result.StateUpdate)
_sym_db.RegisterMessage(Result.AutotestResultsEntry)


DESCRIPTOR._options = None
_RESULT_AUTOTESTRESULTSENTRY._options = None
# @@protoc_insertion_point(module_scope)
