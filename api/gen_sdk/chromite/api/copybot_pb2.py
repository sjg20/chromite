# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/copybot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63hromite/api/copybot.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\"\x87\x07\n\x11RunCopybotRequest\x12\x36\n\x08upstream\x18\x01 \x01(\x0b\x32$.chromite.api.RunCopybotRequest.Repo\x12\x38\n\ndownstream\x18\x02 \x01(\x0b\x32$.chromite.api.RunCopybotRequest.Repo\x12\r\n\x05topic\x18\x03 \x01(\t\x12;\n\x06labels\x18\x04 \x03(\x0b\x32+.chromite.api.RunCopybotRequest.GerritLabel\x12=\n\treviewers\x18\x05 \x03(\x0b\x32*.chromite.api.RunCopybotRequest.GerritUser\x12\x37\n\x03\x63\x63s\x18\x06 \x03(\x0b\x32*.chromite.api.RunCopybotRequest.GerritUser\x12\x17\n\x0fprepend_subject\x18\x07 \x01(\t\x12V\n\x17merge_conflict_behavior\x18\x08 \x01(\x0e\x32\x35.chromite.api.RunCopybotRequest.MergeConflictBehavior\x12\x46\n\x15\x65xclude_file_patterns\x18\t \x03(\x0b\x32\'.chromite.api.RunCopybotRequest.Pattern\x12H\n\x12keep_pseudoheaders\x18\n \x03(\x0b\x32,.chromite.api.RunCopybotRequest.Pseudoheader\x12\x19\n\x11\x61\x64\x64_signed_off_by\x18\x0b \x01(\x08\x1a#\n\x04Repo\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0e\n\x06\x62ranch\x18\x02 \x01(\t\x1a\x1a\n\nGerritUser\x12\x0c\n\x04user\x18\x01 \x01(\t\x1a\x1c\n\x0bGerritLabel\x12\r\n\x05label\x18\x01 \x01(\t\x1a\x1a\n\x07Pattern\x12\x0f\n\x07pattern\x18\x01 \x01(\t\x1a\x1c\n\x0cPseudoheader\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x84\x01\n\x15MergeConflictBehavior\x12\'\n#MERGE_CONFLICT_BEHAVIOR_UNSPECIFIED\x10\x00\x12 \n\x1cMERGE_CONFLICT_BEHAVIOR_SKIP\x10\x01\x12 \n\x1cMERGE_CONFLICT_BEHAVIOR_FAIL\x10\x02\"\xfc\x02\n\x12RunCopybotResponse\x12\x46\n\x0e\x66\x61ilure_reason\x18\x01 \x01(\x0e\x32..chromite.api.RunCopybotResponse.FailureReason\x12M\n\x0fmerge_conflicts\x18\x02 \x03(\x0b\x32\x34.chromite.api.RunCopybotResponse.MergeConflictCommit\x1a#\n\x13MergeConflictCommit\x12\x0c\n\x04hash\x18\x01 \x01(\t\"\xa9\x01\n\rFailureReason\x12\x13\n\x0f\x46\x41ILURE_UNKNOWN\x10\x00\x12 \n\x1c\x46\x41ILURE_UPSTREAM_FETCH_ERROR\x10\x01\x12\"\n\x1e\x46\x41ILURE_DOWNSTREAM_FETCH_ERROR\x10\x02\x12!\n\x1d\x46\x41ILURE_DOWNSTREAM_PUSH_ERROR\x10\x03\x12\x1a\n\x16\x46\x41ILURE_MERGE_CONFLITS\x10\x04\x32p\n\x0e\x43opybotService\x12O\n\nRunCopybot\x12\x1f.chromite.api.RunCopybotRequest\x1a .chromite.api.RunCopybotResponse\x1a\r\xc2\xed\x1a\t\n\x07\x63opybotB8Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3')



_RUNCOPYBOTREQUEST = DESCRIPTOR.message_types_by_name['RunCopybotRequest']
_RUNCOPYBOTREQUEST_REPO = _RUNCOPYBOTREQUEST.nested_types_by_name['Repo']
_RUNCOPYBOTREQUEST_GERRITUSER = _RUNCOPYBOTREQUEST.nested_types_by_name['GerritUser']
_RUNCOPYBOTREQUEST_GERRITLABEL = _RUNCOPYBOTREQUEST.nested_types_by_name['GerritLabel']
_RUNCOPYBOTREQUEST_PATTERN = _RUNCOPYBOTREQUEST.nested_types_by_name['Pattern']
_RUNCOPYBOTREQUEST_PSEUDOHEADER = _RUNCOPYBOTREQUEST.nested_types_by_name['Pseudoheader']
_RUNCOPYBOTRESPONSE = DESCRIPTOR.message_types_by_name['RunCopybotResponse']
_RUNCOPYBOTRESPONSE_MERGECONFLICTCOMMIT = _RUNCOPYBOTRESPONSE.nested_types_by_name['MergeConflictCommit']
_RUNCOPYBOTREQUEST_MERGECONFLICTBEHAVIOR = _RUNCOPYBOTREQUEST.enum_types_by_name['MergeConflictBehavior']
_RUNCOPYBOTRESPONSE_FAILUREREASON = _RUNCOPYBOTRESPONSE.enum_types_by_name['FailureReason']
RunCopybotRequest = _reflection.GeneratedProtocolMessageType('RunCopybotRequest', (_message.Message,), {

  'Repo' : _reflection.GeneratedProtocolMessageType('Repo', (_message.Message,), {
    'DESCRIPTOR' : _RUNCOPYBOTREQUEST_REPO,
    '__module__' : 'chromite.api.copybot_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunCopybotRequest.Repo)
    })
  ,

  'GerritUser' : _reflection.GeneratedProtocolMessageType('GerritUser', (_message.Message,), {
    'DESCRIPTOR' : _RUNCOPYBOTREQUEST_GERRITUSER,
    '__module__' : 'chromite.api.copybot_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunCopybotRequest.GerritUser)
    })
  ,

  'GerritLabel' : _reflection.GeneratedProtocolMessageType('GerritLabel', (_message.Message,), {
    'DESCRIPTOR' : _RUNCOPYBOTREQUEST_GERRITLABEL,
    '__module__' : 'chromite.api.copybot_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunCopybotRequest.GerritLabel)
    })
  ,

  'Pattern' : _reflection.GeneratedProtocolMessageType('Pattern', (_message.Message,), {
    'DESCRIPTOR' : _RUNCOPYBOTREQUEST_PATTERN,
    '__module__' : 'chromite.api.copybot_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunCopybotRequest.Pattern)
    })
  ,

  'Pseudoheader' : _reflection.GeneratedProtocolMessageType('Pseudoheader', (_message.Message,), {
    'DESCRIPTOR' : _RUNCOPYBOTREQUEST_PSEUDOHEADER,
    '__module__' : 'chromite.api.copybot_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunCopybotRequest.Pseudoheader)
    })
  ,
  'DESCRIPTOR' : _RUNCOPYBOTREQUEST,
  '__module__' : 'chromite.api.copybot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.RunCopybotRequest)
  })
_sym_db.RegisterMessage(RunCopybotRequest)
_sym_db.RegisterMessage(RunCopybotRequest.Repo)
_sym_db.RegisterMessage(RunCopybotRequest.GerritUser)
_sym_db.RegisterMessage(RunCopybotRequest.GerritLabel)
_sym_db.RegisterMessage(RunCopybotRequest.Pattern)
_sym_db.RegisterMessage(RunCopybotRequest.Pseudoheader)

RunCopybotResponse = _reflection.GeneratedProtocolMessageType('RunCopybotResponse', (_message.Message,), {

  'MergeConflictCommit' : _reflection.GeneratedProtocolMessageType('MergeConflictCommit', (_message.Message,), {
    'DESCRIPTOR' : _RUNCOPYBOTRESPONSE_MERGECONFLICTCOMMIT,
    '__module__' : 'chromite.api.copybot_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RunCopybotResponse.MergeConflictCommit)
    })
  ,
  'DESCRIPTOR' : _RUNCOPYBOTRESPONSE,
  '__module__' : 'chromite.api.copybot_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.RunCopybotResponse)
  })
_sym_db.RegisterMessage(RunCopybotResponse)
_sym_db.RegisterMessage(RunCopybotResponse.MergeConflictCommit)

_COPYBOTSERVICE = DESCRIPTOR.services_by_name['CopybotService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api'
  _COPYBOTSERVICE._options = None
  _COPYBOTSERVICE._serialized_options = b'\302\355\032\t\n\007copybot'
  _RUNCOPYBOTREQUEST._serialized_start=75
  _RUNCOPYBOTREQUEST._serialized_end=978
  _RUNCOPYBOTREQUEST_REPO._serialized_start=692
  _RUNCOPYBOTREQUEST_REPO._serialized_end=727
  _RUNCOPYBOTREQUEST_GERRITUSER._serialized_start=729
  _RUNCOPYBOTREQUEST_GERRITUSER._serialized_end=755
  _RUNCOPYBOTREQUEST_GERRITLABEL._serialized_start=757
  _RUNCOPYBOTREQUEST_GERRITLABEL._serialized_end=785
  _RUNCOPYBOTREQUEST_PATTERN._serialized_start=787
  _RUNCOPYBOTREQUEST_PATTERN._serialized_end=813
  _RUNCOPYBOTREQUEST_PSEUDOHEADER._serialized_start=815
  _RUNCOPYBOTREQUEST_PSEUDOHEADER._serialized_end=843
  _RUNCOPYBOTREQUEST_MERGECONFLICTBEHAVIOR._serialized_start=846
  _RUNCOPYBOTREQUEST_MERGECONFLICTBEHAVIOR._serialized_end=978
  _RUNCOPYBOTRESPONSE._serialized_start=981
  _RUNCOPYBOTRESPONSE._serialized_end=1361
  _RUNCOPYBOTRESPONSE_MERGECONFLICTCOMMIT._serialized_start=1154
  _RUNCOPYBOTRESPONSE_MERGECONFLICTCOMMIT._serialized_end=1189
  _RUNCOPYBOTRESPONSE_FAILUREREASON._serialized_start=1192
  _RUNCOPYBOTRESPONSE_FAILUREREASON._serialized_end=1361
  _COPYBOTSERVICE._serialized_start=1363
  _COPYBOTSERVICE._serialized_end=1475
# @@protoc_insertion_point(module_scope)
