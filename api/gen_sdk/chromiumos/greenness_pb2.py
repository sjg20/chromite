# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/greenness.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63hromiumos/greenness.proto\x12\nchromiumos\"\xc5\x02\n\x12\x41ggregateGreenness\x12\x18\n\x10\x61ggregate_metric\x18\x01 \x01(\x03\x12\x42\n\x10target_greenness\x18\x02 \x03(\x0b\x32(.chromiumos.AggregateGreenness.Greenness\x12\x1e\n\x16\x61ggregate_build_metric\x18\x03 \x01(\x03\x1a\xb0\x01\n\tGreenness\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x0e\n\x06metric\x18\x02 \x01(\x03\x12\x41\n\x07\x63ontext\x18\x03 \x01(\x0e\x32\x30.chromiumos.AggregateGreenness.Greenness.Context\x12\x14\n\x0c\x62uild_metric\x18\x04 \x01(\x03\"*\n\x07\x43ontext\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0e\n\nIRRELEVANT\x10\x01\x42Y\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumosb\x06proto3')



_AGGREGATEGREENNESS = DESCRIPTOR.message_types_by_name['AggregateGreenness']
_AGGREGATEGREENNESS_GREENNESS = _AGGREGATEGREENNESS.nested_types_by_name['Greenness']
_AGGREGATEGREENNESS_GREENNESS_CONTEXT = _AGGREGATEGREENNESS_GREENNESS.enum_types_by_name['Context']
AggregateGreenness = _reflection.GeneratedProtocolMessageType('AggregateGreenness', (_message.Message,), {

  'Greenness' : _reflection.GeneratedProtocolMessageType('Greenness', (_message.Message,), {
    'DESCRIPTOR' : _AGGREGATEGREENNESS_GREENNESS,
    '__module__' : 'chromiumos.greenness_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.AggregateGreenness.Greenness)
    })
  ,
  'DESCRIPTOR' : _AGGREGATEGREENNESS,
  '__module__' : 'chromiumos.greenness_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.AggregateGreenness)
  })
_sym_db.RegisterMessage(AggregateGreenness)
_sym_db.RegisterMessage(AggregateGreenness.Greenness)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumos'
  _AGGREGATEGREENNESS._serialized_start=43
  _AGGREGATEGREENNESS._serialized_end=368
  _AGGREGATEGREENNESS_GREENNESS._serialized_start=192
  _AGGREGATEGREENNESS_GREENNESS._serialized_end=368
  _AGGREGATEGREENNESS_GREENNESS_CONTEXT._serialized_start=326
  _AGGREGATEGREENNESS_GREENNESS_CONTEXT._serialized_end=368
# @@protoc_insertion_point(module_scope)
