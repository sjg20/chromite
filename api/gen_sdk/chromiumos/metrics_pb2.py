# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/metrics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/metrics.proto',
  package='chromiumos',
  syntax='proto3',
  serialized_options=_b('\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumos'),
  serialized_pb=_b('\n\x18\x63hromiumos/metrics.proto\x12\nchromiumos\"i\n\x0bMetricEvent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x16timestamp_milliseconds\x18\x02 \x01(\x03\x12\x1d\n\x15\x64uration_milliseconds\x18\x03 \x01(\x04\x12\r\n\x05gauge\x18\x04 \x01(\x04\x42Y\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumosb\x06proto3')
)




_METRICEVENT = _descriptor.Descriptor(
  name='MetricEvent',
  full_name='chromiumos.MetricEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chromiumos.MetricEvent.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_milliseconds', full_name='chromiumos.MetricEvent.timestamp_milliseconds', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_milliseconds', full_name='chromiumos.MetricEvent.duration_milliseconds', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gauge', full_name='chromiumos.MetricEvent.gauge', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=40,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['MetricEvent'] = _METRICEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetricEvent = _reflection.GeneratedProtocolMessageType('MetricEvent', (_message.Message,), dict(
  DESCRIPTOR = _METRICEVENT,
  __module__ = 'chromiumos.metrics_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.MetricEvent)
  ))
_sym_db.RegisterMessage(MetricEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
