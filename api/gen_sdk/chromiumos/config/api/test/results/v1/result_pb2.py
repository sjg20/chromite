# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/results/v1/result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from chromite.api.gen_sdk.chromiumos.config.api.test.results.v1 import machine_id_pb2 as chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_machine__id__pb2
from chromite.api.gen_sdk.chromiumos.config.api.test.results.v1 import result_id_pb2 as chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_result__id__pb2
from chromite.api.gen_sdk.chromiumos.config.api.test.results.v1 import software_config_id_pb2 as chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_software__config__id__pb2
from chromite.api.gen_sdk.chromiumos.config.api.test.results.v1 import software_overrides_config_pb2 as chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_software__overrides__config__pb2
from chromite.api.gen_sdk.chromiumos.config.api.test.results.graphics.v1 import trace_id_pb2 as chromiumos_dot_config_dot_api_dot_test_dot_results_dot_graphics_dot_v1_dot_trace__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/config/api/test/results/v1/result.proto',
  package='chromiumos.config.api.test.results.v1',
  syntax='proto3',
  serialized_options=_b('Z@go.chromium.org/chromiumos/config/go/api/test/results/v1;results'),
  serialized_pb=_b('\n2chromiumos/config/api/test/results/v1/result.proto\x12%chromiumos.config.api.test.results.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x36\x63hromiumos/config/api/test/results/v1/machine_id.proto\x1a\x35\x63hromiumos/config/api/test/results/v1/result_id.proto\x1a>chromiumos/config/api/test/results/v1/software_config_id.proto\x1a\x45\x63hromiumos/config/api/test/results/v1/software_overrides_config.proto\x1a=chromiumos/config/api/test/results/graphics/v1/trace_id.proto\"\x93\t\n\x06Result\x12;\n\x02id\x18\x01 \x01(\x0b\x32/.chromiumos.config.api.test.results.v1.ResultId\x12.\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\x07machine\x18\x04 \x01(\x0b\x32\x30.chromiumos.config.api.test.results.v1.MachineId\x12P\n\x0fsoftware_config\x18\x05 \x01(\x0b\x32\x37.chromiumos.config.api.test.results.v1.SoftwareConfigId\x12\x61\n\x15\x65xecution_environment\x18\x06 \x01(\x0e\x32\x42.chromiumos.config.api.test.results.v1.Result.ExecutionEnvironment\x12\x19\n\x11invocation_source\x18\x07 \x01(\t\x12\x0f\n\x07test_id\x18\x11 \x01(\t\x12\x11\n\ttest_name\x18\x08 \x01(\t\x12\x13\n\x0btest_job_id\x18\t \x01(\t\x12\x14\n\x0c\x63ommand_line\x18\n \x01(\t\x12\x11\n\tbenchmark\x18\x0b \x01(\t\x12\x46\n\x05trace\x18\x0c \x01(\x0b\x32\x37.chromiumos.config.api.test.results.graphics.v1.TraceId\x12\x45\n\x07metrics\x18\r \x03(\x0b\x32\x34.chromiumos.config.api.test.results.v1.Result.Metric\x12\x1b\n\x13primary_metric_name\x18\x0e \x01(\t\x12\x43\n\x06labels\x18\x0f \x03(\x0b\x32\x33.chromiumos.config.api.test.results.v1.Result.Label\x12Q\n\toverrides\x18\x12 \x01(\x0b\x32>.chromiumos.config.api.test.results.v1.SoftwareOverridesConfig\x1az\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x04\x12\r\n\x05value\x18\x03 \x01(\x01\x12\r\n\x05units\x18\x04 \x01(\t\x12\x18\n\x10larger_is_better\x18\x05 \x01(\x08\x12\x1b\n\x13\x65xternally_gathered\x18\x06 \x01(\x08\x1a\x36\n\x05Label\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x10\n\x08grouping\x18\x03 \x01(\t\"\x80\x01\n\x14\x45xecutionEnvironment\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04HOST\x10\x01\x12\x0b\n\x07TERMINA\x10\x02\x12\x0c\n\x08\x43ROSTINI\x10\x03\x12\t\n\x05STEAM\x10\x04\x12\x07\n\x03\x41RC\x10\x05\x12\t\n\x05\x41RCVM\x10\x06\x12\x0b\n\x07\x43ROUTON\x10\x07\x12\n\n\x06\x43ROSVM\x10\x08\"J\n\nResultList\x12<\n\x05value\x18\x01 \x03(\x0b\x32-.chromiumos.config.api.test.results.v1.ResultBBZ@go.chromium.org/chromiumos/config/go/api/test/results/v1;resultsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_machine__id__pb2.DESCRIPTOR,chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_result__id__pb2.DESCRIPTOR,chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_software__config__id__pb2.DESCRIPTOR,chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_software__overrides__config__pb2.DESCRIPTOR,chromiumos_dot_config_dot_api_dot_test_dot_results_dot_graphics_dot_v1_dot_trace__id__pb2.DESCRIPTOR,])



_RESULT_EXECUTIONENVIRONMENT = _descriptor.EnumDescriptor(
  name='ExecutionEnvironment',
  full_name='chromiumos.config.api.test.results.v1.Result.ExecutionEnvironment',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TERMINA', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CROSTINI', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STEAM', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARC', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARCVM', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CROUTON', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CROSVM', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1479,
  serialized_end=1607,
)
_sym_db.RegisterEnumDescriptor(_RESULT_EXECUTIONENVIRONMENT)


_RESULT_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='chromiumos.config.api.test.results.v1.Result.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromiumos.config.api.test.results.v1.Result.Metric.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='chromiumos.config.api.test.results.v1.Result.Metric.index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.config.api.test.results.v1.Result.Metric.value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='chromiumos.config.api.test.results.v1.Result.Metric.units', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='larger_is_better', full_name='chromiumos.config.api.test.results.v1.Result.Metric.larger_is_better', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='externally_gathered', full_name='chromiumos.config.api.test.results.v1.Result.Metric.externally_gathered', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1298,
  serialized_end=1420,
)

_RESULT_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='chromiumos.config.api.test.results.v1.Result.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromiumos.config.api.test.results.v1.Result.Label.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.config.api.test.results.v1.Result.Label.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grouping', full_name='chromiumos.config.api.test.results.v1.Result.Label.grouping', index=2,
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
  serialized_start=1422,
  serialized_end=1476,
)

_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='chromiumos.config.api.test.results.v1.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chromiumos.config.api.test.results.v1.Result.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='chromiumos.config.api.test.results.v1.Result.start_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='chromiumos.config.api.test.results.v1.Result.end_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='machine', full_name='chromiumos.config.api.test.results.v1.Result.machine', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='software_config', full_name='chromiumos.config.api.test.results.v1.Result.software_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execution_environment', full_name='chromiumos.config.api.test.results.v1.Result.execution_environment', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invocation_source', full_name='chromiumos.config.api.test.results.v1.Result.invocation_source', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_id', full_name='chromiumos.config.api.test.results.v1.Result.test_id', index=7,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_name', full_name='chromiumos.config.api.test.results.v1.Result.test_name', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_job_id', full_name='chromiumos.config.api.test.results.v1.Result.test_job_id', index=9,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command_line', full_name='chromiumos.config.api.test.results.v1.Result.command_line', index=10,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='benchmark', full_name='chromiumos.config.api.test.results.v1.Result.benchmark', index=11,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace', full_name='chromiumos.config.api.test.results.v1.Result.trace', index=12,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='chromiumos.config.api.test.results.v1.Result.metrics', index=13,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary_metric_name', full_name='chromiumos.config.api.test.results.v1.Result.primary_metric_name', index=14,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='chromiumos.config.api.test.results.v1.Result.labels', index=15,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overrides', full_name='chromiumos.config.api.test.results.v1.Result.overrides', index=16,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESULT_METRIC, _RESULT_LABEL, ],
  enum_types=[
    _RESULT_EXECUTIONENVIRONMENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=1607,
)


_RESULTLIST = _descriptor.Descriptor(
  name='ResultList',
  full_name='chromiumos.config.api.test.results.v1.ResultList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='chromiumos.config.api.test.results.v1.ResultList.value', index=0,
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
  serialized_start=1609,
  serialized_end=1683,
)

_RESULT_METRIC.containing_type = _RESULT
_RESULT_LABEL.containing_type = _RESULT
_RESULT.fields_by_name['id'].message_type = chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_result__id__pb2._RESULTID
_RESULT.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RESULT.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RESULT.fields_by_name['machine'].message_type = chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_machine__id__pb2._MACHINEID
_RESULT.fields_by_name['software_config'].message_type = chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_software__config__id__pb2._SOFTWARECONFIGID
_RESULT.fields_by_name['execution_environment'].enum_type = _RESULT_EXECUTIONENVIRONMENT
_RESULT.fields_by_name['trace'].message_type = chromiumos_dot_config_dot_api_dot_test_dot_results_dot_graphics_dot_v1_dot_trace__id__pb2._TRACEID
_RESULT.fields_by_name['metrics'].message_type = _RESULT_METRIC
_RESULT.fields_by_name['labels'].message_type = _RESULT_LABEL
_RESULT.fields_by_name['overrides'].message_type = chromiumos_dot_config_dot_api_dot_test_dot_results_dot_v1_dot_software__overrides__config__pb2._SOFTWAREOVERRIDESCONFIG
_RESULT_EXECUTIONENVIRONMENT.containing_type = _RESULT
_RESULTLIST.fields_by_name['value'].message_type = _RESULT
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['ResultList'] = _RESULTLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(

  Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), dict(
    DESCRIPTOR = _RESULT_METRIC,
    __module__ = 'chromiumos.config.api.test.results.v1.result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.results.v1.Result.Metric)
    ))
  ,

  Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), dict(
    DESCRIPTOR = _RESULT_LABEL,
    __module__ = 'chromiumos.config.api.test.results.v1.result_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.results.v1.Result.Label)
    ))
  ,
  DESCRIPTOR = _RESULT,
  __module__ = 'chromiumos.config.api.test.results.v1.result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.results.v1.Result)
  ))
_sym_db.RegisterMessage(Result)
_sym_db.RegisterMessage(Result.Metric)
_sym_db.RegisterMessage(Result.Label)

ResultList = _reflection.GeneratedProtocolMessageType('ResultList', (_message.Message,), dict(
  DESCRIPTOR = _RESULTLIST,
  __module__ = 'chromiumos.config.api.test.results.v1.result_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.results.v1.ResultList)
  ))
_sym_db.RegisterMessage(ResultList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)