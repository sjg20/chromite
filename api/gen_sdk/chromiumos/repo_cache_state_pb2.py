# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/repo_cache_state.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!chromiumos/repo_cache_state.proto\x12\nchromiumos\"\xbc\x01\n\tRepoState\x12*\n\x05state\x18\x01 \x01(\x0e\x32\x1b.chromiumos.RepoState.State\x12\x17\n\x0fmanifest_branch\x18\x02 \x01(\t\x12\x14\n\x0cmanifest_url\x18\x03 \x01(\t\"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bSTATE_CLEAN\x10\x01\x12\x0f\n\x0bSTATE_DIRTY\x10\x02\x12\x12\n\x0eSTATE_RECOVERY\x10\x03\x42Y\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumosb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.repo_cache_state_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.chrome.crosinfra.protoZ4go.chromium.org/chromiumos/infra/proto/go/chromiumos'
  _REPOSTATE._serialized_start=50
  _REPOSTATE._serialized_end=238
  _REPOSTATE_STATE._serialized_start=154
  _REPOSTATE_STATE._serialized_end=238
# @@protoc_insertion_point(module_scope)
