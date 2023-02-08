# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/request.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromite.api import test_metadata_pb2 as chromite_dot_api_dot_test__metadata__pb2
from chromite.api.gen_sdk.chromiumos import common_pb2 as chromiumos_dot_common__pb2
from chromite.api.gen_sdk.chromiumos.test.api import test_suite_pb2 as chromiumos_dot_test_dot_api_dot_test__suite__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from chromite.api.gen_sdk.test_platform.execution import param_pb2 as test__platform_dot_execution_dot_param__pb2
from chromite.api.gen_sdk.test_platform.skylab_test_runner import cft_steps_config_pb2 as test__platform_dot_skylab__test__runner_dot_cft__steps__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1btest_platform/request.proto\x12\rtest_platform\x1a chromite/api/test_metadata.proto\x1a\x17\x63hromiumos/common.proto\x1a$chromiumos/test/api/test_suite.proto\x1a\x1egoogle/protobuf/duration.proto\x1a#test_platform/execution/param.proto\x1a\x37test_platform/skylab_test_runner/cft_steps_config.proto\"\xa3\x1d\n\x07Request\x12-\n\x06params\x18\x01 \x01(\x0b\x32\x1d.test_platform.Request.Params\x12\x32\n\ttest_plan\x18\x05 \x01(\x0b\x32\x1f.test_platform.Request.TestPlan\x1a\xfa\x15\n\x06Params\x12M\n\x13hardware_attributes\x18\x01 \x01(\x0b\x32\x30.test_platform.Request.Params.HardwareAttributes\x12M\n\x13software_attributes\x18\x02 \x01(\x0b\x32\x30.test_platform.Request.Params.SoftwareAttributes\x12M\n\x13\x66reeform_attributes\x18\t \x01(\x0b\x32\x30.test_platform.Request.Params.FreeformAttributes\x12O\n\x15software_dependencies\x18\x03 \x03(\x0b\x32\x30.test_platform.Request.Params.SoftwareDependency\x12H\n\x11secondary_devices\x18\x0e \x03(\x0b\x32-.test_platform.Request.Params.SecondaryDevice\x12<\n\nscheduling\x18\x04 \x01(\x0b\x32(.test_platform.Request.Params.Scheduling\x12\x32\n\x05retry\x18\x05 \x01(\x0b\x32#.test_platform.Request.Params.Retry\x12\x38\n\x08metadata\x18\x06 \x01(\x0b\x32&.test_platform.Request.Params.Metadata\x12\x30\n\x04time\x18\x07 \x01(\x0b\x32\".test_platform.Request.Params.Time\x12>\n\x0b\x64\x65\x63orations\x18\x08 \x01(\x0b\x32).test_platform.Request.Params.Decorations\x12<\n\nmigrations\x18\x0c \x01(\x0b\x32(.test_platform.Request.Params.Migrations\x12\x37\n\x0f\x65xecution_param\x18\r \x01(\x0b\x32\x1e.test_platform.execution.Param\x12T\n\x17test_execution_behavior\x18\x0f \x01(\x0e\x32\x33.test_platform.Request.Params.TestExecutionBehavior\x12\x13\n\x0brun_via_cft\x18\x10 \x01(\x08\x12\x1d\n\x15schedule_via_scheduke\x18\x11 \x01(\x08\x12\x14\n\x0crun_via_trv2\x18\x12 \x01(\x08\x12K\n\x11trv2_steps_config\x18\x13 \x01(\x0b\x32\x30.test_platform.skylab_test_runner.CftStepsConfig\x1a\x42\n\x12HardwareAttributes\x12\r\n\x05model\x18\x01 \x01(\t\x12\x1d\n\x15require_stable_device\x18\x02 \x01(\x08\x1a\x43\n\x12SoftwareAttributes\x12-\n\x0c\x62uild_target\x18\x02 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x1a\x31\n\x12\x46reeformAttributes\x12\x1b\n\x13swarming_dimensions\x18\x01 \x03(\t\x1a\xaf\x01\n\x12SoftwareDependency\x12\x18\n\x0e\x63hromeos_build\x18\x03 \x01(\tH\x00\x12#\n\x19\x63hromeos_build_gcs_bucket\x18\x07 \x01(\tH\x00\x12\x1b\n\x11ro_firmware_build\x18\x04 \x01(\tH\x00\x12\x1b\n\x11rw_firmware_build\x18\x05 \x01(\tH\x00\x12\x19\n\x0flacros_gcs_path\x18\x06 \x01(\tH\x00\x42\x05\n\x03\x64\x65p\x1a\x80\x02\n\x0fSecondaryDevice\x12M\n\x13software_attributes\x18\x01 \x01(\x0b\x32\x30.test_platform.Request.Params.SoftwareAttributes\x12M\n\x13hardware_attributes\x18\x02 \x01(\x0b\x32\x30.test_platform.Request.Params.HardwareAttributes\x12O\n\x15software_dependencies\x18\x03 \x03(\x0b\x32\x30.test_platform.Request.Params.SoftwareDependency\x1a\x9e\x03\n\nScheduling\x12L\n\x0cmanaged_pool\x18\x01 \x01(\x0e\x32\x34.test_platform.Request.Params.Scheduling.ManagedPoolH\x00\x12\x18\n\x0eunmanaged_pool\x18\x02 \x01(\tH\x00\x12\x10\n\x08priority\x18\x04 \x01(\x03\x12\x12\n\nqs_account\x18\x05 \x01(\t\"\xf9\x01\n\x0bManagedPool\x12\x1c\n\x18MANAGED_POOL_UNSPECIFIED\x10\x00\x12\x13\n\x0fMANAGED_POOL_CQ\x10\x01\x12\x14\n\x10MANAGED_POOL_BVT\x10\x02\x12\x17\n\x13MANAGED_POOL_SUITES\x10\x03\x12\x14\n\x10MANAGED_POOL_CTS\x10\x04\x12\x1d\n\x19MANAGED_POOL_CTS_PERBUILD\x10\x05\x12\x1b\n\x17MANAGED_POOL_CONTINUOUS\x10\x06\x12\x1e\n\x1aMANAGED_POOL_ARC_PRESUBMIT\x10\x07\x12\x16\n\x12MANAGED_POOL_QUOTA\x10\x08\x42\x06\n\x04pool\x1a#\n\x05Retry\x12\r\n\x05\x61llow\x18\x01 \x01(\x08\x12\x0b\n\x03max\x18\x02 \x01(\x05\x1ah\n\x08Metadata\x12\x19\n\x11test_metadata_url\x18\x01 \x01(\t\x12!\n\x19\x64\x65\x62ug_symbols_archive_url\x18\x02 \x01(\t\x12\x1e\n\x16\x63ontainer_metadata_url\x18\x03 \x01(\t\x1a;\n\x04Time\x12\x33\n\x10maximum_duration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x1a\xaa\x02\n\x0b\x44\x65\x63orations\x12X\n\x10\x61utotest_keyvals\x18\x01 \x03(\x0b\x32>.test_platform.Request.Params.Decorations.AutotestKeyvalsEntry\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12J\n\ttest_args\x18\x03 \x03(\x0b\x32\x37.test_platform.Request.Params.Decorations.TestArgsEntry\x1a\x36\n\x14\x41utotestKeyvalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rTestArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x65\n\nMigrationsJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04R\x0fuse_test_runnerR\x1a\x65nable_synchronous_offloadR\x18notificationless_offload\"Q\n\x15TestExecutionBehavior\x12\x18\n\x14\x42\x45HAVIOR_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43RITICAL\x10\x01\x12\x10\n\x0cNON_CRITICAL\x10\x02J\x04\x08\x0b\x10\x0cJ\x04\x08\n\x10\x0bR\rnotificationsR\x06legacy\x1a\x14\n\x03Tag\x12\r\n\x05value\x18\x01 \x01(\t\x1a(\n\x05Suite\x12\x0c\n\x04name\x18\x01 \x01(\tJ\x04\x08\x02\x10\x03R\x0brun_via_cft\x1a\x8e\x01\n\x04Test\x12\x38\n\x08\x61utotest\x18\x01 \x01(\x0b\x32$.test_platform.Request.Test.AutotestH\x00\x1a\x41\n\x08\x41utotest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\ttest_args\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\tB\t\n\x07harness\x1a\xe4\x02\n\x0b\x45numeration\x12S\n\x14\x61utotest_invocations\x18\x02 \x03(\x0b\x32\x35.test_platform.Request.Enumeration.AutotestInvocation\x1a\xff\x01\n\x12\x41utotestInvocation\x12(\n\x04test\x18\x01 \x01(\x0b\x32\x1a.chromite.api.AutotestTest\x12\x11\n\ttest_args\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12`\n\x0eresult_keyvals\x18\x04 \x03(\x0b\x32H.test_platform.Request.Enumeration.AutotestInvocation.ResultKeyvalsEntry\x1a\x34\n\x12ResultKeyvalsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xf3\x01\n\x08TestPlan\x12+\n\x05suite\x18\x01 \x03(\x0b\x32\x1c.test_platform.Request.Suite\x12)\n\x04test\x18\x02 \x03(\x0b\x32\x1b.test_platform.Request.Test\x12\x37\n\x0b\x65numeration\x18\x03 \x01(\x0b\x32\".test_platform.Request.Enumeration\x12H\n\x0ctag_criteria\x18\x04 \x01(\x0b\x32\x32.chromiumos.test.api.TestSuite.TestCaseTagCriteria\x12\x0c\n\x04seed\x18\x05 \x01(\x03J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08\x42\x39Z7go.chromium.org/chromiumos/infra/proto/go/test_platformb\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_REQUEST_PARAMS = _REQUEST.nested_types_by_name['Params']
_REQUEST_PARAMS_HARDWAREATTRIBUTES = _REQUEST_PARAMS.nested_types_by_name['HardwareAttributes']
_REQUEST_PARAMS_SOFTWAREATTRIBUTES = _REQUEST_PARAMS.nested_types_by_name['SoftwareAttributes']
_REQUEST_PARAMS_FREEFORMATTRIBUTES = _REQUEST_PARAMS.nested_types_by_name['FreeformAttributes']
_REQUEST_PARAMS_SOFTWAREDEPENDENCY = _REQUEST_PARAMS.nested_types_by_name['SoftwareDependency']
_REQUEST_PARAMS_SECONDARYDEVICE = _REQUEST_PARAMS.nested_types_by_name['SecondaryDevice']
_REQUEST_PARAMS_SCHEDULING = _REQUEST_PARAMS.nested_types_by_name['Scheduling']
_REQUEST_PARAMS_RETRY = _REQUEST_PARAMS.nested_types_by_name['Retry']
_REQUEST_PARAMS_METADATA = _REQUEST_PARAMS.nested_types_by_name['Metadata']
_REQUEST_PARAMS_TIME = _REQUEST_PARAMS.nested_types_by_name['Time']
_REQUEST_PARAMS_DECORATIONS = _REQUEST_PARAMS.nested_types_by_name['Decorations']
_REQUEST_PARAMS_DECORATIONS_AUTOTESTKEYVALSENTRY = _REQUEST_PARAMS_DECORATIONS.nested_types_by_name['AutotestKeyvalsEntry']
_REQUEST_PARAMS_DECORATIONS_TESTARGSENTRY = _REQUEST_PARAMS_DECORATIONS.nested_types_by_name['TestArgsEntry']
_REQUEST_PARAMS_MIGRATIONS = _REQUEST_PARAMS.nested_types_by_name['Migrations']
_REQUEST_TAG = _REQUEST.nested_types_by_name['Tag']
_REQUEST_SUITE = _REQUEST.nested_types_by_name['Suite']
_REQUEST_TEST = _REQUEST.nested_types_by_name['Test']
_REQUEST_TEST_AUTOTEST = _REQUEST_TEST.nested_types_by_name['Autotest']
_REQUEST_ENUMERATION = _REQUEST.nested_types_by_name['Enumeration']
_REQUEST_ENUMERATION_AUTOTESTINVOCATION = _REQUEST_ENUMERATION.nested_types_by_name['AutotestInvocation']
_REQUEST_ENUMERATION_AUTOTESTINVOCATION_RESULTKEYVALSENTRY = _REQUEST_ENUMERATION_AUTOTESTINVOCATION.nested_types_by_name['ResultKeyvalsEntry']
_REQUEST_TESTPLAN = _REQUEST.nested_types_by_name['TestPlan']
_REQUEST_PARAMS_SCHEDULING_MANAGEDPOOL = _REQUEST_PARAMS_SCHEDULING.enum_types_by_name['ManagedPool']
_REQUEST_PARAMS_TESTEXECUTIONBEHAVIOR = _REQUEST_PARAMS.enum_types_by_name['TestExecutionBehavior']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {

  'Params' : _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {

    'HardwareAttributes' : _reflection.GeneratedProtocolMessageType('HardwareAttributes', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PARAMS_HARDWAREATTRIBUTES,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.HardwareAttributes)
      })
    ,

    'SoftwareAttributes' : _reflection.GeneratedProtocolMessageType('SoftwareAttributes', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PARAMS_SOFTWAREATTRIBUTES,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.SoftwareAttributes)
      })
    ,

    'FreeformAttributes' : _reflection.GeneratedProtocolMessageType('FreeformAttributes', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PARAMS_FREEFORMATTRIBUTES,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.FreeformAttributes)
      })
    ,

    'SoftwareDependency' : _reflection.GeneratedProtocolMessageType('SoftwareDependency', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PARAMS_SOFTWAREDEPENDENCY,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.SoftwareDependency)
      })
    ,

    'SecondaryDevice' : _reflection.GeneratedProtocolMessageType('SecondaryDevice', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PARAMS_SECONDARYDEVICE,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.SecondaryDevice)
      })
    ,

    'Scheduling' : _reflection.GeneratedProtocolMessageType('Scheduling', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PARAMS_SCHEDULING,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.Scheduling)
      })
    ,

    'Retry' : _reflection.GeneratedProtocolMessageType('Retry', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PARAMS_RETRY,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.Retry)
      })
    ,

    'Metadata' : _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PARAMS_METADATA,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.Metadata)
      })
    ,

    'Time' : _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PARAMS_TIME,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.Time)
      })
    ,

    'Decorations' : _reflection.GeneratedProtocolMessageType('Decorations', (_message.Message,), {

      'AutotestKeyvalsEntry' : _reflection.GeneratedProtocolMessageType('AutotestKeyvalsEntry', (_message.Message,), {
        'DESCRIPTOR' : _REQUEST_PARAMS_DECORATIONS_AUTOTESTKEYVALSENTRY,
        '__module__' : 'test_platform.request_pb2'
        # @@protoc_insertion_point(class_scope:test_platform.Request.Params.Decorations.AutotestKeyvalsEntry)
        })
      ,

      'TestArgsEntry' : _reflection.GeneratedProtocolMessageType('TestArgsEntry', (_message.Message,), {
        'DESCRIPTOR' : _REQUEST_PARAMS_DECORATIONS_TESTARGSENTRY,
        '__module__' : 'test_platform.request_pb2'
        # @@protoc_insertion_point(class_scope:test_platform.Request.Params.Decorations.TestArgsEntry)
        })
      ,
      'DESCRIPTOR' : _REQUEST_PARAMS_DECORATIONS,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.Decorations)
      })
    ,

    'Migrations' : _reflection.GeneratedProtocolMessageType('Migrations', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_PARAMS_MIGRATIONS,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Params.Migrations)
      })
    ,
    'DESCRIPTOR' : _REQUEST_PARAMS,
    '__module__' : 'test_platform.request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.Request.Params)
    })
  ,

  'Tag' : _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_TAG,
    '__module__' : 'test_platform.request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.Request.Tag)
    })
  ,

  'Suite' : _reflection.GeneratedProtocolMessageType('Suite', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_SUITE,
    '__module__' : 'test_platform.request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.Request.Suite)
    })
  ,

  'Test' : _reflection.GeneratedProtocolMessageType('Test', (_message.Message,), {

    'Autotest' : _reflection.GeneratedProtocolMessageType('Autotest', (_message.Message,), {
      'DESCRIPTOR' : _REQUEST_TEST_AUTOTEST,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Test.Autotest)
      })
    ,
    'DESCRIPTOR' : _REQUEST_TEST,
    '__module__' : 'test_platform.request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.Request.Test)
    })
  ,

  'Enumeration' : _reflection.GeneratedProtocolMessageType('Enumeration', (_message.Message,), {

    'AutotestInvocation' : _reflection.GeneratedProtocolMessageType('AutotestInvocation', (_message.Message,), {

      'ResultKeyvalsEntry' : _reflection.GeneratedProtocolMessageType('ResultKeyvalsEntry', (_message.Message,), {
        'DESCRIPTOR' : _REQUEST_ENUMERATION_AUTOTESTINVOCATION_RESULTKEYVALSENTRY,
        '__module__' : 'test_platform.request_pb2'
        # @@protoc_insertion_point(class_scope:test_platform.Request.Enumeration.AutotestInvocation.ResultKeyvalsEntry)
        })
      ,
      'DESCRIPTOR' : _REQUEST_ENUMERATION_AUTOTESTINVOCATION,
      '__module__' : 'test_platform.request_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.Request.Enumeration.AutotestInvocation)
      })
    ,
    'DESCRIPTOR' : _REQUEST_ENUMERATION,
    '__module__' : 'test_platform.request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.Request.Enumeration)
    })
  ,

  'TestPlan' : _reflection.GeneratedProtocolMessageType('TestPlan', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_TESTPLAN,
    '__module__' : 'test_platform.request_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.Request.TestPlan)
    })
  ,
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'test_platform.request_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.Request)
  })
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.Params)
_sym_db.RegisterMessage(Request.Params.HardwareAttributes)
_sym_db.RegisterMessage(Request.Params.SoftwareAttributes)
_sym_db.RegisterMessage(Request.Params.FreeformAttributes)
_sym_db.RegisterMessage(Request.Params.SoftwareDependency)
_sym_db.RegisterMessage(Request.Params.SecondaryDevice)
_sym_db.RegisterMessage(Request.Params.Scheduling)
_sym_db.RegisterMessage(Request.Params.Retry)
_sym_db.RegisterMessage(Request.Params.Metadata)
_sym_db.RegisterMessage(Request.Params.Time)
_sym_db.RegisterMessage(Request.Params.Decorations)
_sym_db.RegisterMessage(Request.Params.Decorations.AutotestKeyvalsEntry)
_sym_db.RegisterMessage(Request.Params.Decorations.TestArgsEntry)
_sym_db.RegisterMessage(Request.Params.Migrations)
_sym_db.RegisterMessage(Request.Tag)
_sym_db.RegisterMessage(Request.Suite)
_sym_db.RegisterMessage(Request.Test)
_sym_db.RegisterMessage(Request.Test.Autotest)
_sym_db.RegisterMessage(Request.Enumeration)
_sym_db.RegisterMessage(Request.Enumeration.AutotestInvocation)
_sym_db.RegisterMessage(Request.Enumeration.AutotestInvocation.ResultKeyvalsEntry)
_sym_db.RegisterMessage(Request.TestPlan)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7go.chromium.org/chromiumos/infra/proto/go/test_platform'
  _REQUEST_PARAMS_DECORATIONS_AUTOTESTKEYVALSENTRY._options = None
  _REQUEST_PARAMS_DECORATIONS_AUTOTESTKEYVALSENTRY._serialized_options = b'8\001'
  _REQUEST_PARAMS_DECORATIONS_TESTARGSENTRY._options = None
  _REQUEST_PARAMS_DECORATIONS_TESTARGSENTRY._serialized_options = b'8\001'
  _REQUEST_ENUMERATION_AUTOTESTINVOCATION_RESULTKEYVALSENTRY._options = None
  _REQUEST_ENUMERATION_AUTOTESTINVOCATION_RESULTKEYVALSENTRY._serialized_options = b'8\001'
  _REQUEST._serialized_start=270
  _REQUEST._serialized_end=4017
  _REQUEST_PARAMS._serialized_start=381
  _REQUEST_PARAMS._serialized_end=3191
  _REQUEST_PARAMS_HARDWAREATTRIBUTES._serialized_start=1425
  _REQUEST_PARAMS_HARDWAREATTRIBUTES._serialized_end=1491
  _REQUEST_PARAMS_SOFTWAREATTRIBUTES._serialized_start=1493
  _REQUEST_PARAMS_SOFTWAREATTRIBUTES._serialized_end=1560
  _REQUEST_PARAMS_FREEFORMATTRIBUTES._serialized_start=1562
  _REQUEST_PARAMS_FREEFORMATTRIBUTES._serialized_end=1611
  _REQUEST_PARAMS_SOFTWAREDEPENDENCY._serialized_start=1614
  _REQUEST_PARAMS_SOFTWAREDEPENDENCY._serialized_end=1789
  _REQUEST_PARAMS_SECONDARYDEVICE._serialized_start=1792
  _REQUEST_PARAMS_SECONDARYDEVICE._serialized_end=2048
  _REQUEST_PARAMS_SCHEDULING._serialized_start=2051
  _REQUEST_PARAMS_SCHEDULING._serialized_end=2465
  _REQUEST_PARAMS_SCHEDULING_MANAGEDPOOL._serialized_start=2208
  _REQUEST_PARAMS_SCHEDULING_MANAGEDPOOL._serialized_end=2457
  _REQUEST_PARAMS_RETRY._serialized_start=2467
  _REQUEST_PARAMS_RETRY._serialized_end=2502
  _REQUEST_PARAMS_METADATA._serialized_start=2504
  _REQUEST_PARAMS_METADATA._serialized_end=2608
  _REQUEST_PARAMS_TIME._serialized_start=2610
  _REQUEST_PARAMS_TIME._serialized_end=2669
  _REQUEST_PARAMS_DECORATIONS._serialized_start=2672
  _REQUEST_PARAMS_DECORATIONS._serialized_end=2970
  _REQUEST_PARAMS_DECORATIONS_AUTOTESTKEYVALSENTRY._serialized_start=2867
  _REQUEST_PARAMS_DECORATIONS_AUTOTESTKEYVALSENTRY._serialized_end=2921
  _REQUEST_PARAMS_DECORATIONS_TESTARGSENTRY._serialized_start=2923
  _REQUEST_PARAMS_DECORATIONS_TESTARGSENTRY._serialized_end=2970
  _REQUEST_PARAMS_MIGRATIONS._serialized_start=2972
  _REQUEST_PARAMS_MIGRATIONS._serialized_end=3073
  _REQUEST_PARAMS_TESTEXECUTIONBEHAVIOR._serialized_start=3075
  _REQUEST_PARAMS_TESTEXECUTIONBEHAVIOR._serialized_end=3156
  _REQUEST_TAG._serialized_start=3193
  _REQUEST_TAG._serialized_end=3213
  _REQUEST_SUITE._serialized_start=3215
  _REQUEST_SUITE._serialized_end=3255
  _REQUEST_TEST._serialized_start=3258
  _REQUEST_TEST._serialized_end=3400
  _REQUEST_TEST_AUTOTEST._serialized_start=3324
  _REQUEST_TEST_AUTOTEST._serialized_end=3389
  _REQUEST_ENUMERATION._serialized_start=3403
  _REQUEST_ENUMERATION._serialized_end=3759
  _REQUEST_ENUMERATION_AUTOTESTINVOCATION._serialized_start=3504
  _REQUEST_ENUMERATION_AUTOTESTINVOCATION._serialized_end=3759
  _REQUEST_ENUMERATION_AUTOTESTINVOCATION_RESULTKEYVALSENTRY._serialized_start=3707
  _REQUEST_ENUMERATION_AUTOTESTINVOCATION_RESULTKEYVALSENTRY._serialized_end=3759
  _REQUEST_TESTPLAN._serialized_start=3762
  _REQUEST_TESTPLAN._serialized_end=4005
# @@protoc_insertion_point(module_scope)
