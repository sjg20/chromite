# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/chromiumdash.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63hromiumos/chromiumdash.proto\x12\nchromiumos\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9e\x08\n\tMilestone\x12\x32\n\x0e\x66inal_beta_cut\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nfinal_beta\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0e\x66\x65\x61ture_freeze\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rearliest_beta\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14stable_refresh_first\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0blatest_beta\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x06owners\x18\x07 \x03(\x0b\x32!.chromiumos.Milestone.OwnersEntry\x12.\n\nstable_cut\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x15stable_refresh_second\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06mstone\x18\n \x01(\x05\x12\x34\n\x10late_stable_date\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bstable_date\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x05ldaps\x18\r \x03(\x0b\x32 .chromiumos.Milestone.LdapsEntry\x12\x35\n\x11\x65\x61rliest_beta_ios\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x62ranch_point\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14stable_refresh_third\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08ltc_date\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08ltr_date\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x15ltr_last_refresh_date\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a-\n\x0bOwnersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a,\n\nLdapsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"H\n\x1e\x46\x65tchMilestoneScheduleResponse\x12&\n\x07mstones\x18\x01 \x03(\x0b\x32\x15.chromiumos.MilestoneBY\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumosb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.chromiumdash_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumos'
  _MILESTONE_OWNERSENTRY._options = None
  _MILESTONE_OWNERSENTRY._serialized_options = b'8\001'
  _MILESTONE_LDAPSENTRY._options = None
  _MILESTONE_LDAPSENTRY._serialized_options = b'8\001'
  _MILESTONE._serialized_start=79
  _MILESTONE._serialized_end=1133
  _MILESTONE_OWNERSENTRY._serialized_start=1042
  _MILESTONE_OWNERSENTRY._serialized_end=1087
  _MILESTONE_LDAPSENTRY._serialized_start=1089
  _MILESTONE_LDAPSENTRY._serialized_end=1133
  _FETCHMILESTONESCHEDULERESPONSE._serialized_start=1135
  _FETCHMILESTONESCHEDULERESPONSE._serialized_end=1207
# @@protoc_insertion_point(module_scope)
