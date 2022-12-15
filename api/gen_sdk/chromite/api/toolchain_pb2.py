# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/toolchain.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromite.api import artifacts_pb2 as chromite_dot_api_dot_artifacts__pb2
from chromite.api.gen_sdk.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen_sdk.chromite.api import sysroot_pb2 as chromite_dot_api_dot_sysroot__pb2
from chromite.api.gen_sdk.chromiumos import builder_config_pb2 as chromiumos_dot_builder__config__pb2
from chromite.api.gen_sdk.chromiumos import common_pb2 as chromiumos_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63hromite/api/toolchain.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/artifacts.proto\x1a\x1c\x63hromite/api/build_api.proto\x1a\x1a\x63hromite/api/sysroot.proto\x1a\x1f\x63hromiumos/builder_config.proto\x1a\x17\x63hromiumos/common.proto\"\x83\x01\n\x0c\x41rtifactInfo\x12H\n\rartifact_type\x18\x01 \x01(\x0e\x32\x31.chromiumos.BuilderConfig.Artifacts.ArtifactTypes\x12)\n\tartifacts\x18\x02 \x03(\x0b\x32\x16.chromite.api.Artifact\"\x83\x03\n\x1fPrepareForToolchainBuildRequest\x12I\n\x0e\x61rtifact_types\x18\x01 \x03(\x0e\x32\x31.chromiumos.BuilderConfig.Artifacts.ArtifactTypes\x12\"\n\x06\x63hroot\x18\x02 \x01(\x0b\x32\x12.chromiumos.Chroot\x12&\n\x07sysroot\x18\x03 \x01(\x0b\x32\x15.chromite.api.Sysroot\x12N\n\x0finput_artifacts\x18\x04 \x03(\x0b\x32\x35.chromiumos.BuilderConfig.Artifacts.InputArtifactInfo\x12\x42\n\x0f\x61\x64\x64itional_args\x18\x05 \x01(\x0b\x32).chromiumos.PrepareForBuildAdditionalArgs\x12\x35\n\x0cprofile_info\x18\x06 \x01(\x0b\x32\x1f.chromiumos.ArtifactProfileInfo\"q\n PrepareForToolchainBuildResponse\x12M\n\x0f\x62uild_relevance\x18\x01 \x01(\x0e\x32\x34.chromite.api.PrepareForBuildResponse.BuildRelevance\"\xbe\x02\n\x16\x42undleToolchainRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\x12&\n\x07sysroot\x18\x02 \x01(\x0b\x32\x15.chromite.api.Sysroot\x12\x12\n\noutput_dir\x18\x03 \x01(\t\x12I\n\x0e\x61rtifact_types\x18\x04 \x03(\x0e\x32\x31.chromiumos.BuilderConfig.Artifacts.ArtifactTypes\x12\x42\n\x0f\x61\x64\x64itional_args\x18\x05 \x01(\x0b\x32).chromiumos.PrepareForBuildAdditionalArgs\x12\x35\n\x0cprofile_info\x18\x06 \x01(\x0b\x32\x1f.chromiumos.ArtifactProfileInfo\"S\n\x17\x42undleToolchainResponse\x12\x32\n\x0e\x61rtifacts_info\x18\x02 \x03(\x0b\x32\x1a.chromite.api.ArtifactInfoJ\x04\x08\x01\x10\x02\"\xeb\x01\n\x16GetUpdatedFilesRequest\x12R\n\x12uploaded_artifacts\x18\x01 \x03(\x0b\x32\x36.chromite.api.GetUpdatedFilesRequest.UploadedArtifacts\x1a}\n\x11UploadedArtifacts\x12\x31\n\rartifact_info\x18\x01 \x01(\x0b\x32\x1a.chromite.api.ArtifactInfo\x12\x35\n\x0cprofile_info\x18\x02 \x01(\x0b\x32\x1f.chromiumos.ArtifactProfileInfo\"\xf4\x03\n\x17GetUpdatedFilesResponse\x12H\n\rupdated_files\x18\x01 \x03(\x0b\x32\x31.chromite.api.GetUpdatedFilesResponse.UpdatedFile\x12\x16\n\x0e\x63ommit_message\x18\x02 \x01(\t\x12I\n\rcommit_footer\x18\x03 \x03(\x0b\x32\x32.chromite.api.GetUpdatedFilesResponse.CommitFooter\x1a\x1b\n\x0bUpdatedFile\x12\x0c\n\x04path\x18\x01 \x01(\t\x1a\x41\n\x0e\x43qDependFooter\x12/\n\rgerrit_change\x18\x01 \x03(\x0b\x32\x18.chromiumos.GerritChange\x1a\x1c\n\rCqClTagFooter\x12\x0b\n\x03tag\x18\x01 \x01(\t\x1a\xad\x01\n\x0c\x43ommitFooter\x12I\n\tcq_depend\x18\x01 \x01(\x0b\x32\x34.chromite.api.GetUpdatedFilesResponse.CqDependFooterH\x00\x12H\n\tcq_cl_tag\x18\x02 \x01(\x0b\x32\x33.chromite.api.GetUpdatedFilesResponse.CqClTagFooterH\x00\x42\x08\n\x06\x66ooter\"\xb7\x02\n\rLinterFinding\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x36\n\tlocations\x18\x02 \x03(\x0b\x32#.chromite.api.LinterFindingLocation\x12\x33\n\x06linter\x18\x03 \x01(\x0e\x32#.chromite.api.LinterFinding.Linters\x12\x11\n\tlint_name\x18\x04 \x01(\t\x12\x39\n\x0fsuggested_fixes\x18\x05 \x03(\x0b\x32 .chromite.api.LinterSuggestedFix\"Z\n\x07Linters\x12\x16\n\x12LINTER_UNSPECIFIED\x10\x00\x12\x0e\n\nCLANG_TIDY\x10\x01\x12\x10\n\x0c\x43\x41RGO_CLIPPY\x10\x02\x12\x0b\n\x07GO_LINT\x10\x03\x12\x08\n\x04IWYU\x10\x04\"s\n\x15LinterFindingLocation\x12\x10\n\x08\x66ilepath\x18\x01 \x01(\t\x12\x12\n\nline_start\x18\x02 \x01(\x05\x12\x10\n\x08line_end\x18\x03 \x01(\x05\x12\x11\n\tcol_start\x18\x04 \x01(\x05\x12\x0f\n\x07\x63ol_end\x18\x05 \x01(\x05\"`\n\x12LinterSuggestedFix\x12\x35\n\x08location\x18\x01 \x01(\x0b\x32#.chromite.api.LinterFindingLocation\x12\x13\n\x0breplacement\x18\x02 \x01(\t\"\xde\x01\n\rLinterRequest\x12)\n\x08packages\x18\x01 \x03(\x0b\x32\x17.chromiumos.PackageInfo\x12&\n\x07sysroot\x18\x02 \x01(\x0b\x32\x15.chromite.api.Sysroot\x12\"\n\x06\x63hroot\x18\x03 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\x17\n\x0f\x66ilter_modified\x18\x04 \x01(\x08\x12=\n\x10\x64isabled_linters\x18\x05 \x03(\x0e\x32#.chromite.api.LinterFinding.Linters\"?\n\x0eLinterResponse\x12-\n\x08\x66indings\x18\x01 \x03(\x0b\x32\x1b.chromite.api.LinterFinding\"v\n\x14\x44\x61shboardLintRequest\x12&\n\x07sysroot\x18\x01 \x01(\x0b\x32\x15.chromite.api.Sysroot\x12\"\n\x06\x63hroot\x18\x02 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\x12\n\nstart_time\x18\x03 \x01(\x03\"(\n\x15\x44\x61shboardLintResponse\x12\x0f\n\x07gs_path\x18\x01 \x01(\t\"\"\n\x11ToolchainsRequest\x12\r\n\x05\x62oard\x18\x01 \x01(\t\"O\n\x12ToolchainsResponse\x12\x1a\n\x12\x64\x65\x66\x61ult_toolchains\x18\x01 \x03(\t\x12\x1d\n\x15nondefault_toolchains\x18\x02 \x03(\t2\xc9\x05\n\x10ToolchainService\x12p\n\x0fPrepareForBuild\x12-.chromite.api.PrepareForToolchainBuildRequest\x1a..chromite.api.PrepareForToolchainBuildResponse\x12^\n\x0f\x42undleArtifacts\x12$.chromite.api.BundleToolchainRequest\x1a%.chromite.api.BundleToolchainResponse\x12^\n\x0fGetUpdatedFiles\x12$.chromite.api.GetUpdatedFilesRequest\x1a%.chromite.api.GetUpdatedFilesResponse\x12g\n\x14\x45mergeAndUploadLints\x12\".chromite.api.DashboardLintRequest\x1a#.chromite.api.DashboardLintResponse\"\x06\xc2\xed\x1a\x02\x10\x01\x12V\n\x11\x45mergeWithLinting\x12\x1b.chromite.api.LinterRequest\x1a\x1c.chromite.api.LinterResponse\"\x06\xc2\xed\x1a\x02\x10\x01\x12S\n\x0eGetClippyLints\x12\x1b.chromite.api.LinterRequest\x1a\x1c.chromite.api.LinterResponse\"\x06\xc2\xed\x1a\x02\x10\x01\x12Z\n\x15GetToolchainsForBoard\x12\x1f.chromite.api.ToolchainsRequest\x1a .chromite.api.ToolchainsResponse\x1a\x11\xc2\xed\x1a\r\n\ttoolchain\x10\x02\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3')



_ARTIFACTINFO = DESCRIPTOR.message_types_by_name['ArtifactInfo']
_PREPAREFORTOOLCHAINBUILDREQUEST = DESCRIPTOR.message_types_by_name['PrepareForToolchainBuildRequest']
_PREPAREFORTOOLCHAINBUILDRESPONSE = DESCRIPTOR.message_types_by_name['PrepareForToolchainBuildResponse']
_BUNDLETOOLCHAINREQUEST = DESCRIPTOR.message_types_by_name['BundleToolchainRequest']
_BUNDLETOOLCHAINRESPONSE = DESCRIPTOR.message_types_by_name['BundleToolchainResponse']
_GETUPDATEDFILESREQUEST = DESCRIPTOR.message_types_by_name['GetUpdatedFilesRequest']
_GETUPDATEDFILESREQUEST_UPLOADEDARTIFACTS = _GETUPDATEDFILESREQUEST.nested_types_by_name['UploadedArtifacts']
_GETUPDATEDFILESRESPONSE = DESCRIPTOR.message_types_by_name['GetUpdatedFilesResponse']
_GETUPDATEDFILESRESPONSE_UPDATEDFILE = _GETUPDATEDFILESRESPONSE.nested_types_by_name['UpdatedFile']
_GETUPDATEDFILESRESPONSE_CQDEPENDFOOTER = _GETUPDATEDFILESRESPONSE.nested_types_by_name['CqDependFooter']
_GETUPDATEDFILESRESPONSE_CQCLTAGFOOTER = _GETUPDATEDFILESRESPONSE.nested_types_by_name['CqClTagFooter']
_GETUPDATEDFILESRESPONSE_COMMITFOOTER = _GETUPDATEDFILESRESPONSE.nested_types_by_name['CommitFooter']
_LINTERFINDING = DESCRIPTOR.message_types_by_name['LinterFinding']
_LINTERFINDINGLOCATION = DESCRIPTOR.message_types_by_name['LinterFindingLocation']
_LINTERSUGGESTEDFIX = DESCRIPTOR.message_types_by_name['LinterSuggestedFix']
_LINTERREQUEST = DESCRIPTOR.message_types_by_name['LinterRequest']
_LINTERRESPONSE = DESCRIPTOR.message_types_by_name['LinterResponse']
_DASHBOARDLINTREQUEST = DESCRIPTOR.message_types_by_name['DashboardLintRequest']
_DASHBOARDLINTRESPONSE = DESCRIPTOR.message_types_by_name['DashboardLintResponse']
_TOOLCHAINSREQUEST = DESCRIPTOR.message_types_by_name['ToolchainsRequest']
_TOOLCHAINSRESPONSE = DESCRIPTOR.message_types_by_name['ToolchainsResponse']
_LINTERFINDING_LINTERS = _LINTERFINDING.enum_types_by_name['Linters']
ArtifactInfo = _reflection.GeneratedProtocolMessageType('ArtifactInfo', (_message.Message,), {
  'DESCRIPTOR' : _ARTIFACTINFO,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.ArtifactInfo)
  })
_sym_db.RegisterMessage(ArtifactInfo)

PrepareForToolchainBuildRequest = _reflection.GeneratedProtocolMessageType('PrepareForToolchainBuildRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREFORTOOLCHAINBUILDREQUEST,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.PrepareForToolchainBuildRequest)
  })
_sym_db.RegisterMessage(PrepareForToolchainBuildRequest)

PrepareForToolchainBuildResponse = _reflection.GeneratedProtocolMessageType('PrepareForToolchainBuildResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREFORTOOLCHAINBUILDRESPONSE,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.PrepareForToolchainBuildResponse)
  })
_sym_db.RegisterMessage(PrepareForToolchainBuildResponse)

BundleToolchainRequest = _reflection.GeneratedProtocolMessageType('BundleToolchainRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUNDLETOOLCHAINREQUEST,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BundleToolchainRequest)
  })
_sym_db.RegisterMessage(BundleToolchainRequest)

BundleToolchainResponse = _reflection.GeneratedProtocolMessageType('BundleToolchainResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUNDLETOOLCHAINRESPONSE,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BundleToolchainResponse)
  })
_sym_db.RegisterMessage(BundleToolchainResponse)

GetUpdatedFilesRequest = _reflection.GeneratedProtocolMessageType('GetUpdatedFilesRequest', (_message.Message,), {

  'UploadedArtifacts' : _reflection.GeneratedProtocolMessageType('UploadedArtifacts', (_message.Message,), {
    'DESCRIPTOR' : _GETUPDATEDFILESREQUEST_UPLOADEDARTIFACTS,
    '__module__' : 'chromite.api.toolchain_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.GetUpdatedFilesRequest.UploadedArtifacts)
    })
  ,
  'DESCRIPTOR' : _GETUPDATEDFILESREQUEST,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.GetUpdatedFilesRequest)
  })
_sym_db.RegisterMessage(GetUpdatedFilesRequest)
_sym_db.RegisterMessage(GetUpdatedFilesRequest.UploadedArtifacts)

GetUpdatedFilesResponse = _reflection.GeneratedProtocolMessageType('GetUpdatedFilesResponse', (_message.Message,), {

  'UpdatedFile' : _reflection.GeneratedProtocolMessageType('UpdatedFile', (_message.Message,), {
    'DESCRIPTOR' : _GETUPDATEDFILESRESPONSE_UPDATEDFILE,
    '__module__' : 'chromite.api.toolchain_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.GetUpdatedFilesResponse.UpdatedFile)
    })
  ,

  'CqDependFooter' : _reflection.GeneratedProtocolMessageType('CqDependFooter', (_message.Message,), {
    'DESCRIPTOR' : _GETUPDATEDFILESRESPONSE_CQDEPENDFOOTER,
    '__module__' : 'chromite.api.toolchain_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.GetUpdatedFilesResponse.CqDependFooter)
    })
  ,

  'CqClTagFooter' : _reflection.GeneratedProtocolMessageType('CqClTagFooter', (_message.Message,), {
    'DESCRIPTOR' : _GETUPDATEDFILESRESPONSE_CQCLTAGFOOTER,
    '__module__' : 'chromite.api.toolchain_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.GetUpdatedFilesResponse.CqClTagFooter)
    })
  ,

  'CommitFooter' : _reflection.GeneratedProtocolMessageType('CommitFooter', (_message.Message,), {
    'DESCRIPTOR' : _GETUPDATEDFILESRESPONSE_COMMITFOOTER,
    '__module__' : 'chromite.api.toolchain_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.GetUpdatedFilesResponse.CommitFooter)
    })
  ,
  'DESCRIPTOR' : _GETUPDATEDFILESRESPONSE,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.GetUpdatedFilesResponse)
  })
_sym_db.RegisterMessage(GetUpdatedFilesResponse)
_sym_db.RegisterMessage(GetUpdatedFilesResponse.UpdatedFile)
_sym_db.RegisterMessage(GetUpdatedFilesResponse.CqDependFooter)
_sym_db.RegisterMessage(GetUpdatedFilesResponse.CqClTagFooter)
_sym_db.RegisterMessage(GetUpdatedFilesResponse.CommitFooter)

LinterFinding = _reflection.GeneratedProtocolMessageType('LinterFinding', (_message.Message,), {
  'DESCRIPTOR' : _LINTERFINDING,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.LinterFinding)
  })
_sym_db.RegisterMessage(LinterFinding)

LinterFindingLocation = _reflection.GeneratedProtocolMessageType('LinterFindingLocation', (_message.Message,), {
  'DESCRIPTOR' : _LINTERFINDINGLOCATION,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.LinterFindingLocation)
  })
_sym_db.RegisterMessage(LinterFindingLocation)

LinterSuggestedFix = _reflection.GeneratedProtocolMessageType('LinterSuggestedFix', (_message.Message,), {
  'DESCRIPTOR' : _LINTERSUGGESTEDFIX,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.LinterSuggestedFix)
  })
_sym_db.RegisterMessage(LinterSuggestedFix)

LinterRequest = _reflection.GeneratedProtocolMessageType('LinterRequest', (_message.Message,), {
  'DESCRIPTOR' : _LINTERREQUEST,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.LinterRequest)
  })
_sym_db.RegisterMessage(LinterRequest)

LinterResponse = _reflection.GeneratedProtocolMessageType('LinterResponse', (_message.Message,), {
  'DESCRIPTOR' : _LINTERRESPONSE,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.LinterResponse)
  })
_sym_db.RegisterMessage(LinterResponse)

DashboardLintRequest = _reflection.GeneratedProtocolMessageType('DashboardLintRequest', (_message.Message,), {
  'DESCRIPTOR' : _DASHBOARDLINTREQUEST,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.DashboardLintRequest)
  })
_sym_db.RegisterMessage(DashboardLintRequest)

DashboardLintResponse = _reflection.GeneratedProtocolMessageType('DashboardLintResponse', (_message.Message,), {
  'DESCRIPTOR' : _DASHBOARDLINTRESPONSE,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.DashboardLintResponse)
  })
_sym_db.RegisterMessage(DashboardLintResponse)

ToolchainsRequest = _reflection.GeneratedProtocolMessageType('ToolchainsRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOOLCHAINSREQUEST,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.ToolchainsRequest)
  })
_sym_db.RegisterMessage(ToolchainsRequest)

ToolchainsResponse = _reflection.GeneratedProtocolMessageType('ToolchainsResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOOLCHAINSRESPONSE,
  '__module__' : 'chromite.api.toolchain_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.ToolchainsResponse)
  })
_sym_db.RegisterMessage(ToolchainsResponse)

_TOOLCHAINSERVICE = DESCRIPTOR.services_by_name['ToolchainService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api'
  _TOOLCHAINSERVICE._options = None
  _TOOLCHAINSERVICE._serialized_options = b'\302\355\032\r\n\ttoolchain\020\002'
  _TOOLCHAINSERVICE.methods_by_name['EmergeAndUploadLints']._options = None
  _TOOLCHAINSERVICE.methods_by_name['EmergeAndUploadLints']._serialized_options = b'\302\355\032\002\020\001'
  _TOOLCHAINSERVICE.methods_by_name['EmergeWithLinting']._options = None
  _TOOLCHAINSERVICE.methods_by_name['EmergeWithLinting']._serialized_options = b'\302\355\032\002\020\001'
  _TOOLCHAINSERVICE.methods_by_name['GetClippyLints']._options = None
  _TOOLCHAINSERVICE.methods_by_name['GetClippyLints']._serialized_options = b'\302\355\032\002\020\001'
  _ARTIFACTINFO._serialized_start=193
  _ARTIFACTINFO._serialized_end=324
  _PREPAREFORTOOLCHAINBUILDREQUEST._serialized_start=327
  _PREPAREFORTOOLCHAINBUILDREQUEST._serialized_end=714
  _PREPAREFORTOOLCHAINBUILDRESPONSE._serialized_start=716
  _PREPAREFORTOOLCHAINBUILDRESPONSE._serialized_end=829
  _BUNDLETOOLCHAINREQUEST._serialized_start=832
  _BUNDLETOOLCHAINREQUEST._serialized_end=1150
  _BUNDLETOOLCHAINRESPONSE._serialized_start=1152
  _BUNDLETOOLCHAINRESPONSE._serialized_end=1235
  _GETUPDATEDFILESREQUEST._serialized_start=1238
  _GETUPDATEDFILESREQUEST._serialized_end=1473
  _GETUPDATEDFILESREQUEST_UPLOADEDARTIFACTS._serialized_start=1348
  _GETUPDATEDFILESREQUEST_UPLOADEDARTIFACTS._serialized_end=1473
  _GETUPDATEDFILESRESPONSE._serialized_start=1476
  _GETUPDATEDFILESRESPONSE._serialized_end=1976
  _GETUPDATEDFILESRESPONSE_UPDATEDFILE._serialized_start=1676
  _GETUPDATEDFILESRESPONSE_UPDATEDFILE._serialized_end=1703
  _GETUPDATEDFILESRESPONSE_CQDEPENDFOOTER._serialized_start=1705
  _GETUPDATEDFILESRESPONSE_CQDEPENDFOOTER._serialized_end=1770
  _GETUPDATEDFILESRESPONSE_CQCLTAGFOOTER._serialized_start=1772
  _GETUPDATEDFILESRESPONSE_CQCLTAGFOOTER._serialized_end=1800
  _GETUPDATEDFILESRESPONSE_COMMITFOOTER._serialized_start=1803
  _GETUPDATEDFILESRESPONSE_COMMITFOOTER._serialized_end=1976
  _LINTERFINDING._serialized_start=1979
  _LINTERFINDING._serialized_end=2290
  _LINTERFINDING_LINTERS._serialized_start=2200
  _LINTERFINDING_LINTERS._serialized_end=2290
  _LINTERFINDINGLOCATION._serialized_start=2292
  _LINTERFINDINGLOCATION._serialized_end=2407
  _LINTERSUGGESTEDFIX._serialized_start=2409
  _LINTERSUGGESTEDFIX._serialized_end=2505
  _LINTERREQUEST._serialized_start=2508
  _LINTERREQUEST._serialized_end=2730
  _LINTERRESPONSE._serialized_start=2732
  _LINTERRESPONSE._serialized_end=2795
  _DASHBOARDLINTREQUEST._serialized_start=2797
  _DASHBOARDLINTREQUEST._serialized_end=2915
  _DASHBOARDLINTRESPONSE._serialized_start=2917
  _DASHBOARDLINTRESPONSE._serialized_end=2957
  _TOOLCHAINSREQUEST._serialized_start=2959
  _TOOLCHAINSREQUEST._serialized_end=2993
  _TOOLCHAINSRESPONSE._serialized_start=2995
  _TOOLCHAINSRESPONSE._serialized_end=3074
  _TOOLCHAINSERVICE._serialized_start=3077
  _TOOLCHAINSERVICE._serialized_end=3790
# @@protoc_insertion_point(module_scope)
