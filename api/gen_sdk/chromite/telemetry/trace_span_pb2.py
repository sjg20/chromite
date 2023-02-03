# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/telemetry/trace_span.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#chromite/telemetry/trace_span.proto\x12\x12\x63hromite.telemetry\x1a\x1cgoogle/protobuf/struct.proto\"\xa2\x11\n\tTraceSpan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.chromite.telemetry.TraceSpan.Context\x12\x16\n\x0eparent_span_id\x18\x03 \x01(\t\x12\x39\n\tspan_kind\x18\x04 \x01(\x0e\x32&.chromite.telemetry.TraceSpan.SpanKind\x12\x19\n\x11start_time_millis\x18\x05 \x01(\x03\x12\x17\n\x0f\x65nd_time_millis\x18\x06 \x01(\x03\x12+\n\nattributes\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x33\n\x06\x65vents\x18\x08 \x03(\x0b\x32#.chromite.telemetry.TraceSpan.Event\x12\x31\n\x05links\x18\t \x03(\x0b\x32\".chromite.telemetry.TraceSpan.Link\x12\x34\n\x06status\x18\n \x01(\x0b\x32$.chromite.telemetry.TraceSpan.Status\x12\x38\n\x08resource\x18\x0b \x01(\x0b\x32&.chromite.telemetry.TraceSpan.Resource\x12Q\n\x15instrumentation_scope\x18\x0c \x01(\x0b\x32\x32.chromite.telemetry.TraceSpan.InstrumentationScope\x12\x41\n\rtelemetry_sdk\x18\r \x01(\x0b\x32*.chromite.telemetry.TraceSpan.TelemetrySdk\x1a?\n\x0cTelemetrySdk\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07version\x18\x02 \x02(\t\x12\x10\n\x08language\x18\x03 \x02(\t\x1a\x65\n\x06System\x12\x0f\n\x07os_name\x18\x01 \x02(\t\x12\x12\n\nos_version\x18\x02 \x01(\t\x12\x0f\n\x07os_type\x18\x03 \x01(\t\x12\x0b\n\x03\x63pu\x18\x04 \x01(\t\x12\x18\n\x10\x63pu_architecture\x18\x05 \x02(\t\x1a\xd0\x02\n\x07Process\x12\x0b\n\x03pid\x18\x01 \x01(\t\x12\x17\n\x0f\x65xecutable_name\x18\x02 \x01(\t\x12\x17\n\x0f\x65xecutable_path\x18\x03 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x04 \x01(\t\x12\x14\n\x0c\x63ommand_args\x18\x05 \x03(\t\x12\x15\n\rowner_is_root\x18\x06 \x01(\x08\x12\x14\n\x0cruntime_name\x18\x07 \x01(\t\x12\x17\n\x0fruntime_version\x18\x08 \x01(\t\x12\x1b\n\x13runtime_description\x18\t \x01(\t\x12\x13\n\x0b\x61pi_version\x18\n \x01(\t\x12;\n\x03\x65nv\x18\x0b \x03(\x0b\x32..chromite.telemetry.TraceSpan.Process.EnvEntry\x1a*\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xa5\x01\n\x08Resource\x12\x36\n\x07process\x18\x01 \x01(\x0b\x32%.chromite.telemetry.TraceSpan.Process\x12\x34\n\x06system\x18\x02 \x01(\x0b\x32$.chromite.telemetry.TraceSpan.System\x12+\n\nattributes\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x1a\x35\n\x14InstrumentationScope\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x1a]\n\x05\x45vent\x12\x19\n\x11\x65vent_time_millis\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\nattributes\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x1a\x62\n\nStackFrame\x12\x15\n\rfunction_name\x18\x01 \x02(\t\x12\x11\n\tfile_name\x18\x02 \x02(\t\x12\x13\n\x0bline_number\x18\x03 \x01(\x03\x12\x15\n\rcolumn_number\x18\x04 \x01(\x03\x1a\x83\x01\n\nStackTrace\x12>\n\x0cstack_frames\x18\x01 \x03(\x0b\x32(.chromite.telemetry.TraceSpan.StackFrame\x12\x1c\n\x14\x64ropped_frames_count\x18\x02 \x01(\x03\x12\x17\n\x0fstacktrace_hash\x18\x03 \x01(\t\x1a\xee\x01\n\x06Status\x12\x44\n\x0bstatus_code\x18\x01 \x01(\x0e\x32/.chromite.telemetry.TraceSpan.Status.StatusCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x12=\n\x0bstack_trace\x18\x03 \x01(\x0b\x32(.chromite.telemetry.TraceSpan.StackTrace\"N\n\nStatusCode\x12\x15\n\x11STATUS_CODE_UNSET\x10\x00\x12\x12\n\x0eSTATUS_CODE_OK\x10\x01\x12\x15\n\x11STATUS_CODE_ERROR\x10\x02\x1a\x41\n\x07\x43ontext\x12\x10\n\x08trace_id\x18\x01 \x01(\t\x12\x0f\n\x07span_id\x18\x02 \x01(\t\x12\x13\n\x0btrace_state\x18\x03 \x01(\t\x1ak\n\x04Link\x12\x36\n\x07\x63ontext\x18\x01 \x01(\x0b\x32%.chromite.telemetry.TraceSpan.Context\x12+\n\nattributes\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"i\n\x08SpanKind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\x16\n\x12SPAN_KIND_INTERNAL\x10\x01\x12\x14\n\x10SPAN_KIND_SERVER\x10\x02\x12\x14\n\x10SPAN_KIND_CLIENT\x10\x03\x42>Z<go.chromium.org/chromiumos/infra/proto/go/chromite/telemetry')



_TRACESPAN = DESCRIPTOR.message_types_by_name['TraceSpan']
_TRACESPAN_TELEMETRYSDK = _TRACESPAN.nested_types_by_name['TelemetrySdk']
_TRACESPAN_SYSTEM = _TRACESPAN.nested_types_by_name['System']
_TRACESPAN_PROCESS = _TRACESPAN.nested_types_by_name['Process']
_TRACESPAN_PROCESS_ENVENTRY = _TRACESPAN_PROCESS.nested_types_by_name['EnvEntry']
_TRACESPAN_RESOURCE = _TRACESPAN.nested_types_by_name['Resource']
_TRACESPAN_INSTRUMENTATIONSCOPE = _TRACESPAN.nested_types_by_name['InstrumentationScope']
_TRACESPAN_EVENT = _TRACESPAN.nested_types_by_name['Event']
_TRACESPAN_STACKFRAME = _TRACESPAN.nested_types_by_name['StackFrame']
_TRACESPAN_STACKTRACE = _TRACESPAN.nested_types_by_name['StackTrace']
_TRACESPAN_STATUS = _TRACESPAN.nested_types_by_name['Status']
_TRACESPAN_CONTEXT = _TRACESPAN.nested_types_by_name['Context']
_TRACESPAN_LINK = _TRACESPAN.nested_types_by_name['Link']
_TRACESPAN_STATUS_STATUSCODE = _TRACESPAN_STATUS.enum_types_by_name['StatusCode']
_TRACESPAN_SPANKIND = _TRACESPAN.enum_types_by_name['SpanKind']
TraceSpan = _reflection.GeneratedProtocolMessageType('TraceSpan', (_message.Message,), {

  'TelemetrySdk' : _reflection.GeneratedProtocolMessageType('TelemetrySdk', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_TELEMETRYSDK,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.TelemetrySdk)
    })
  ,

  'System' : _reflection.GeneratedProtocolMessageType('System', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_SYSTEM,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.System)
    })
  ,

  'Process' : _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), {

    'EnvEntry' : _reflection.GeneratedProtocolMessageType('EnvEntry', (_message.Message,), {
      'DESCRIPTOR' : _TRACESPAN_PROCESS_ENVENTRY,
      '__module__' : 'chromite.telemetry.trace_span_pb2'
      # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.Process.EnvEntry)
      })
    ,
    'DESCRIPTOR' : _TRACESPAN_PROCESS,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.Process)
    })
  ,

  'Resource' : _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_RESOURCE,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.Resource)
    })
  ,

  'InstrumentationScope' : _reflection.GeneratedProtocolMessageType('InstrumentationScope', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_INSTRUMENTATIONSCOPE,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.InstrumentationScope)
    })
  ,

  'Event' : _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_EVENT,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.Event)
    })
  ,

  'StackFrame' : _reflection.GeneratedProtocolMessageType('StackFrame', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_STACKFRAME,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.StackFrame)
    })
  ,

  'StackTrace' : _reflection.GeneratedProtocolMessageType('StackTrace', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_STACKTRACE,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.StackTrace)
    })
  ,

  'Status' : _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_STATUS,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.Status)
    })
  ,

  'Context' : _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_CONTEXT,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.Context)
    })
  ,

  'Link' : _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_LINK,
    '__module__' : 'chromite.telemetry.trace_span_pb2'
    # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan.Link)
    })
  ,
  'DESCRIPTOR' : _TRACESPAN,
  '__module__' : 'chromite.telemetry.trace_span_pb2'
  # @@protoc_insertion_point(class_scope:chromite.telemetry.TraceSpan)
  })
_sym_db.RegisterMessage(TraceSpan)
_sym_db.RegisterMessage(TraceSpan.TelemetrySdk)
_sym_db.RegisterMessage(TraceSpan.System)
_sym_db.RegisterMessage(TraceSpan.Process)
_sym_db.RegisterMessage(TraceSpan.Process.EnvEntry)
_sym_db.RegisterMessage(TraceSpan.Resource)
_sym_db.RegisterMessage(TraceSpan.InstrumentationScope)
_sym_db.RegisterMessage(TraceSpan.Event)
_sym_db.RegisterMessage(TraceSpan.StackFrame)
_sym_db.RegisterMessage(TraceSpan.StackTrace)
_sym_db.RegisterMessage(TraceSpan.Status)
_sym_db.RegisterMessage(TraceSpan.Context)
_sym_db.RegisterMessage(TraceSpan.Link)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z<go.chromium.org/chromiumos/infra/proto/go/chromite/telemetry'
  _TRACESPAN_PROCESS_ENVENTRY._options = None
  _TRACESPAN_PROCESS_ENVENTRY._serialized_options = b'8\001'
  _TRACESPAN._serialized_start=90
  _TRACESPAN._serialized_end=2300
  _TRACESPAN_TELEMETRYSDK._serialized_start=719
  _TRACESPAN_TELEMETRYSDK._serialized_end=782
  _TRACESPAN_SYSTEM._serialized_start=784
  _TRACESPAN_SYSTEM._serialized_end=885
  _TRACESPAN_PROCESS._serialized_start=888
  _TRACESPAN_PROCESS._serialized_end=1224
  _TRACESPAN_PROCESS_ENVENTRY._serialized_start=1182
  _TRACESPAN_PROCESS_ENVENTRY._serialized_end=1224
  _TRACESPAN_RESOURCE._serialized_start=1227
  _TRACESPAN_RESOURCE._serialized_end=1392
  _TRACESPAN_INSTRUMENTATIONSCOPE._serialized_start=1394
  _TRACESPAN_INSTRUMENTATIONSCOPE._serialized_end=1447
  _TRACESPAN_EVENT._serialized_start=1449
  _TRACESPAN_EVENT._serialized_end=1542
  _TRACESPAN_STACKFRAME._serialized_start=1544
  _TRACESPAN_STACKFRAME._serialized_end=1642
  _TRACESPAN_STACKTRACE._serialized_start=1645
  _TRACESPAN_STACKTRACE._serialized_end=1776
  _TRACESPAN_STATUS._serialized_start=1779
  _TRACESPAN_STATUS._serialized_end=2017
  _TRACESPAN_STATUS_STATUSCODE._serialized_start=1939
  _TRACESPAN_STATUS_STATUSCODE._serialized_end=2017
  _TRACESPAN_CONTEXT._serialized_start=2019
  _TRACESPAN_CONTEXT._serialized_end=2084
  _TRACESPAN_LINK._serialized_start=2086
  _TRACESPAN_LINK._serialized_end=2193
  _TRACESPAN_SPANKIND._serialized_start=2195
  _TRACESPAN_SPANKIND._serialized_end=2300
# @@protoc_insertion_point(module_scope)