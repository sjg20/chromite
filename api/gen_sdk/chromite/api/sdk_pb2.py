# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/sdk.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen_sdk.chromiumos import common_pb2 as chromiumos_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63hromite/api/sdk.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x17\x63hromiumos/common.proto\" \n\rChrootVersion\x12\x0f\n\x07version\x18\x01 \x01(\r\"\xdd\x01\n\rCreateRequest\x12\x30\n\x05\x66lags\x18\x01 \x01(\x0b\x32!.chromite.api.CreateRequest.Flags\x12\"\n\x06\x63hroot\x18\x02 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\x13\n\x0bsdk_version\x18\x03 \x01(\t\x12\x1b\n\x13skip_chroot_upgrade\x18\x04 \x01(\x08\x1a\x44\n\x05\x46lags\x12\x12\n\nno_replace\x18\x01 \x01(\x08\x12\x11\n\tbootstrap\x18\x02 \x01(\x08\x12\x14\n\x0cno_use_image\x18\x03 \x01(\x08\">\n\x0e\x43reateResponse\x12,\n\x07version\x18\x01 \x01(\x0b\x32\x1b.chromite.api.ChrootVersion\"3\n\rDeleteRequest\x12\"\n\x06\x63hroot\x18\x02 \x01(\x0b\x32\x12.chromiumos.Chroot\"\x10\n\x0e\x44\x65leteResponse\"4\n\x0eUnmountRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\"\x11\n\x0fUnmountResponse\"\xd3\x01\n\rUpdateRequest\x12\x30\n\x05\x66lags\x18\x01 \x01(\x0b\x32!.chromite.api.UpdateRequest.Flags\x12\x32\n\x11toolchain_targets\x18\x02 \x03(\x0b\x32\x17.chromiumos.BuildTarget\x12\"\n\x06\x63hroot\x18\x03 \x01(\x0b\x32\x12.chromiumos.Chroot\x1a\x38\n\x05\x46lags\x12\x14\n\x0c\x62uild_source\x18\x01 \x01(\x08\x12\x19\n\x11toolchain_changed\x18\x02 \x01(\x08\">\n\x0eUpdateResponse\x12,\n\x07version\x18\x01 \x01(\x0b\x32\x1b.chromite.api.ChrootVersion\"\x80\x01\n\x0cUprevRequest\x12%\n\x0bsource_root\x18\x01 \x01(\x0b\x32\x10.chromiumos.Path\x12\x1d\n\x15sdk_tarball_gs_bucket\x18\x02 \x01(\t\x12\x19\n\x11\x62inhost_gs_bucket\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"J\n\rUprevResponse\x12(\n\x0emodified_files\x18\x01 \x03(\x0b\x32\x10.chromiumos.Path\x12\x0f\n\x07version\x18\x02 \x01(\t\"\xb4\x01\n\x0c\x43leanRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\x0c\n\x04safe\x18\x02 \x01(\x08\x12\x0e\n\x06images\x18\x03 \x01(\x08\x12\x10\n\x08sysroots\x18\x04 \x01(\x08\x12\x0b\n\x03tmp\x18\x05 \x01(\x08\x12\r\n\x05\x63\x61\x63he\x18\x06 \x01(\x08\x12\x0c\n\x04logs\x18\x07 \x01(\x08\x12\x10\n\x08workdirs\x18\x08 \x01(\x08\x12\x14\n\x0cincrementals\x18\t \x01(\x08\"\x0f\n\rCleanResponse\"\x1e\n\rSnapshotToken\x12\r\n\x05value\x18\x01 \x01(\t\";\n\x15\x43reateSnapshotRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\"M\n\x16\x43reateSnapshotResponse\x12\x33\n\x0esnapshot_token\x18\x01 \x01(\x0b\x32\x1b.chromite.api.SnapshotToken\"q\n\x16RestoreSnapshotRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\x33\n\x0esnapshot_token\x18\x02 \x01(\x0b\x32\x1b.chromite.api.SnapshotToken\"\x19\n\x17RestoreSnapshotResponse\"4\n\x12UnmountPathRequest\x12\x1e\n\x04path\x18\x01 \x01(\x0b\x32\x10.chromiumos.Path\"\x15\n\x13UnmountPathResponse\"j\n\x15\x42uildPrebuiltsRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\x12-\n\x0c\x62uild_target\x18\x02 \x01(\x0b\x32\x17.chromiumos.BuildTarget\"\x18\n\x16\x42uildPrebuiltsResponse\"<\n\x16\x42uildSdkTarballRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\"E\n\x17\x42uildSdkTarballResponse\x12*\n\x10sdk_tarball_path\x18\x01 \x01(\x0b\x32\x10.chromiumos.Path\"\x8a\x01\n\x1c\x43reateManifestFromSdkRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\"\n\x08sdk_path\x18\x02 \x01(\x0b\x32\x10.chromiumos.Path\x12\"\n\x08\x64\x65st_dir\x18\x03 \x01(\x0b\x32\x10.chromiumos.Path\"H\n\x1d\x43reateManifestFromSdkResponse\x12\'\n\rmanifest_path\x18\x01 \x01(\x0b\x32\x10.chromiumos.Path\"z\n\x17\x43reateBinhostCLsRequest\x12\x17\n\x0fprepend_version\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x17\n\x0fupload_location\x18\x03 \x01(\t\x12\x1c\n\x14sdk_tarball_template\x18\x04 \x01(\t\"\'\n\x18\x43reateBinhostCLsResponse\x12\x0b\n\x03\x63ls\x18\x01 \x03(\t\"\x86\x01\n\x1dUploadPrebuiltPackagesRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\x17\n\x0fprepend_version\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x17\n\x0fupload_location\x18\x04 \x01(\t\" \n\x1eUploadPrebuiltPackagesResponse\"f\n\x18\x42uildSdkToolchainRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\x12&\n\tuse_flags\x18\x02 \x03(\x0b\x32\x13.chromiumos.UseFlag\"F\n\x19\x42uildSdkToolchainResponse\x12)\n\x0fgenerated_files\x18\x01 \x03(\x0b\x32\x10.chromiumos.Path2\xba\n\n\nSdkService\x12\x43\n\x06\x43reate\x12\x1b.chromite.api.CreateRequest\x1a\x1c.chromite.api.CreateResponse\x12\x43\n\x06\x44\x65lete\x12\x1b.chromite.api.DeleteRequest\x1a\x1c.chromite.api.DeleteResponse\x12@\n\x05\x43lean\x12\x1a.chromite.api.CleanRequest\x1a\x1b.chromite.api.CleanResponse\x12\x46\n\x07Unmount\x12\x1c.chromite.api.UnmountRequest\x1a\x1d.chromite.api.UnmountResponse\x12K\n\x06Update\x12\x1b.chromite.api.UpdateRequest\x1a\x1c.chromite.api.UpdateResponse\"\x06\xc2\xed\x1a\x02\x10\x01\x12@\n\x05Uprev\x12\x1a.chromite.api.UprevRequest\x1a\x1b.chromite.api.UprevResponse\x12[\n\x0e\x43reateSnapshot\x12#.chromite.api.CreateSnapshotRequest\x1a$.chromite.api.CreateSnapshotResponse\x12^\n\x0fRestoreSnapshot\x12$.chromite.api.RestoreSnapshotRequest\x1a%.chromite.api.RestoreSnapshotResponse\x12R\n\x0bUnmountPath\x12 .chromite.api.UnmountPathRequest\x1a!.chromite.api.UnmountPathResponse\x12[\n\x0e\x42uildPrebuilts\x12#.chromite.api.BuildPrebuiltsRequest\x1a$.chromite.api.BuildPrebuiltsResponse\x12^\n\x0f\x42uildSdkTarball\x12$.chromite.api.BuildSdkTarballRequest\x1a%.chromite.api.BuildSdkTarballResponse\x12p\n\x15\x43reateManifestFromSdk\x12*.chromite.api.CreateManifestFromSdkRequest\x1a+.chromite.api.CreateManifestFromSdkResponse\x12\x61\n\x10\x43reateBinhostCLs\x12%.chromite.api.CreateBinhostCLsRequest\x1a&.chromite.api.CreateBinhostCLsResponse\x12s\n\x16UploadPrebuiltPackages\x12+.chromite.api.UploadPrebuiltPackagesRequest\x1a,.chromite.api.UploadPrebuiltPackagesResponse\x12\x64\n\x11\x42uildSdkToolchain\x12&.chromite.api.BuildSdkToolchainRequest\x1a\'.chromite.api.BuildSdkToolchainResponse\x1a\x0b\xc2\xed\x1a\x07\n\x03sdk\x10\x02\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3')



_CHROOTVERSION = DESCRIPTOR.message_types_by_name['ChrootVersion']
_CREATEREQUEST = DESCRIPTOR.message_types_by_name['CreateRequest']
_CREATEREQUEST_FLAGS = _CREATEREQUEST.nested_types_by_name['Flags']
_CREATERESPONSE = DESCRIPTOR.message_types_by_name['CreateResponse']
_DELETEREQUEST = DESCRIPTOR.message_types_by_name['DeleteRequest']
_DELETERESPONSE = DESCRIPTOR.message_types_by_name['DeleteResponse']
_UNMOUNTREQUEST = DESCRIPTOR.message_types_by_name['UnmountRequest']
_UNMOUNTRESPONSE = DESCRIPTOR.message_types_by_name['UnmountResponse']
_UPDATEREQUEST = DESCRIPTOR.message_types_by_name['UpdateRequest']
_UPDATEREQUEST_FLAGS = _UPDATEREQUEST.nested_types_by_name['Flags']
_UPDATERESPONSE = DESCRIPTOR.message_types_by_name['UpdateResponse']
_UPREVREQUEST = DESCRIPTOR.message_types_by_name['UprevRequest']
_UPREVRESPONSE = DESCRIPTOR.message_types_by_name['UprevResponse']
_CLEANREQUEST = DESCRIPTOR.message_types_by_name['CleanRequest']
_CLEANRESPONSE = DESCRIPTOR.message_types_by_name['CleanResponse']
_SNAPSHOTTOKEN = DESCRIPTOR.message_types_by_name['SnapshotToken']
_CREATESNAPSHOTREQUEST = DESCRIPTOR.message_types_by_name['CreateSnapshotRequest']
_CREATESNAPSHOTRESPONSE = DESCRIPTOR.message_types_by_name['CreateSnapshotResponse']
_RESTORESNAPSHOTREQUEST = DESCRIPTOR.message_types_by_name['RestoreSnapshotRequest']
_RESTORESNAPSHOTRESPONSE = DESCRIPTOR.message_types_by_name['RestoreSnapshotResponse']
_UNMOUNTPATHREQUEST = DESCRIPTOR.message_types_by_name['UnmountPathRequest']
_UNMOUNTPATHRESPONSE = DESCRIPTOR.message_types_by_name['UnmountPathResponse']
_BUILDPREBUILTSREQUEST = DESCRIPTOR.message_types_by_name['BuildPrebuiltsRequest']
_BUILDPREBUILTSRESPONSE = DESCRIPTOR.message_types_by_name['BuildPrebuiltsResponse']
_BUILDSDKTARBALLREQUEST = DESCRIPTOR.message_types_by_name['BuildSdkTarballRequest']
_BUILDSDKTARBALLRESPONSE = DESCRIPTOR.message_types_by_name['BuildSdkTarballResponse']
_CREATEMANIFESTFROMSDKREQUEST = DESCRIPTOR.message_types_by_name['CreateManifestFromSdkRequest']
_CREATEMANIFESTFROMSDKRESPONSE = DESCRIPTOR.message_types_by_name['CreateManifestFromSdkResponse']
_CREATEBINHOSTCLSREQUEST = DESCRIPTOR.message_types_by_name['CreateBinhostCLsRequest']
_CREATEBINHOSTCLSRESPONSE = DESCRIPTOR.message_types_by_name['CreateBinhostCLsResponse']
_UPLOADPREBUILTPACKAGESREQUEST = DESCRIPTOR.message_types_by_name['UploadPrebuiltPackagesRequest']
_UPLOADPREBUILTPACKAGESRESPONSE = DESCRIPTOR.message_types_by_name['UploadPrebuiltPackagesResponse']
_BUILDSDKTOOLCHAINREQUEST = DESCRIPTOR.message_types_by_name['BuildSdkToolchainRequest']
_BUILDSDKTOOLCHAINRESPONSE = DESCRIPTOR.message_types_by_name['BuildSdkToolchainResponse']
ChrootVersion = _reflection.GeneratedProtocolMessageType('ChrootVersion', (_message.Message,), {
  'DESCRIPTOR' : _CHROOTVERSION,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.ChrootVersion)
  })
_sym_db.RegisterMessage(ChrootVersion)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {

  'Flags' : _reflection.GeneratedProtocolMessageType('Flags', (_message.Message,), {
    'DESCRIPTOR' : _CREATEREQUEST_FLAGS,
    '__module__' : 'chromite.api.sdk_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.CreateRequest.Flags)
    })
  ,
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)
_sym_db.RegisterMessage(CreateRequest.Flags)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATERESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CreateResponse)
  })
_sym_db.RegisterMessage(CreateResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

UnmountRequest = _reflection.GeneratedProtocolMessageType('UnmountRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNMOUNTREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UnmountRequest)
  })
_sym_db.RegisterMessage(UnmountRequest)

UnmountResponse = _reflection.GeneratedProtocolMessageType('UnmountResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNMOUNTRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UnmountResponse)
  })
_sym_db.RegisterMessage(UnmountResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {

  'Flags' : _reflection.GeneratedProtocolMessageType('Flags', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEREQUEST_FLAGS,
    '__module__' : 'chromite.api.sdk_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.UpdateRequest.Flags)
    })
  ,
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)
_sym_db.RegisterMessage(UpdateRequest.Flags)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UpdateResponse)
  })
_sym_db.RegisterMessage(UpdateResponse)

UprevRequest = _reflection.GeneratedProtocolMessageType('UprevRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPREVREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UprevRequest)
  })
_sym_db.RegisterMessage(UprevRequest)

UprevResponse = _reflection.GeneratedProtocolMessageType('UprevResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPREVRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UprevResponse)
  })
_sym_db.RegisterMessage(UprevResponse)

CleanRequest = _reflection.GeneratedProtocolMessageType('CleanRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLEANREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CleanRequest)
  })
_sym_db.RegisterMessage(CleanRequest)

CleanResponse = _reflection.GeneratedProtocolMessageType('CleanResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLEANRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CleanResponse)
  })
_sym_db.RegisterMessage(CleanResponse)

SnapshotToken = _reflection.GeneratedProtocolMessageType('SnapshotToken', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTTOKEN,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SnapshotToken)
  })
_sym_db.RegisterMessage(SnapshotToken)

CreateSnapshotRequest = _reflection.GeneratedProtocolMessageType('CreateSnapshotRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESNAPSHOTREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CreateSnapshotRequest)
  })
_sym_db.RegisterMessage(CreateSnapshotRequest)

CreateSnapshotResponse = _reflection.GeneratedProtocolMessageType('CreateSnapshotResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESNAPSHOTRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CreateSnapshotResponse)
  })
_sym_db.RegisterMessage(CreateSnapshotResponse)

RestoreSnapshotRequest = _reflection.GeneratedProtocolMessageType('RestoreSnapshotRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESTORESNAPSHOTREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.RestoreSnapshotRequest)
  })
_sym_db.RegisterMessage(RestoreSnapshotRequest)

RestoreSnapshotResponse = _reflection.GeneratedProtocolMessageType('RestoreSnapshotResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESTORESNAPSHOTRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.RestoreSnapshotResponse)
  })
_sym_db.RegisterMessage(RestoreSnapshotResponse)

UnmountPathRequest = _reflection.GeneratedProtocolMessageType('UnmountPathRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNMOUNTPATHREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UnmountPathRequest)
  })
_sym_db.RegisterMessage(UnmountPathRequest)

UnmountPathResponse = _reflection.GeneratedProtocolMessageType('UnmountPathResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNMOUNTPATHRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UnmountPathResponse)
  })
_sym_db.RegisterMessage(UnmountPathResponse)

BuildPrebuiltsRequest = _reflection.GeneratedProtocolMessageType('BuildPrebuiltsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUILDPREBUILTSREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BuildPrebuiltsRequest)
  })
_sym_db.RegisterMessage(BuildPrebuiltsRequest)

BuildPrebuiltsResponse = _reflection.GeneratedProtocolMessageType('BuildPrebuiltsResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUILDPREBUILTSRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BuildPrebuiltsResponse)
  })
_sym_db.RegisterMessage(BuildPrebuiltsResponse)

BuildSdkTarballRequest = _reflection.GeneratedProtocolMessageType('BuildSdkTarballRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUILDSDKTARBALLREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BuildSdkTarballRequest)
  })
_sym_db.RegisterMessage(BuildSdkTarballRequest)

BuildSdkTarballResponse = _reflection.GeneratedProtocolMessageType('BuildSdkTarballResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUILDSDKTARBALLRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BuildSdkTarballResponse)
  })
_sym_db.RegisterMessage(BuildSdkTarballResponse)

CreateManifestFromSdkRequest = _reflection.GeneratedProtocolMessageType('CreateManifestFromSdkRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMANIFESTFROMSDKREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CreateManifestFromSdkRequest)
  })
_sym_db.RegisterMessage(CreateManifestFromSdkRequest)

CreateManifestFromSdkResponse = _reflection.GeneratedProtocolMessageType('CreateManifestFromSdkResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMANIFESTFROMSDKRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CreateManifestFromSdkResponse)
  })
_sym_db.RegisterMessage(CreateManifestFromSdkResponse)

CreateBinhostCLsRequest = _reflection.GeneratedProtocolMessageType('CreateBinhostCLsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBINHOSTCLSREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CreateBinhostCLsRequest)
  })
_sym_db.RegisterMessage(CreateBinhostCLsRequest)

CreateBinhostCLsResponse = _reflection.GeneratedProtocolMessageType('CreateBinhostCLsResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBINHOSTCLSRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.CreateBinhostCLsResponse)
  })
_sym_db.RegisterMessage(CreateBinhostCLsResponse)

UploadPrebuiltPackagesRequest = _reflection.GeneratedProtocolMessageType('UploadPrebuiltPackagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADPREBUILTPACKAGESREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UploadPrebuiltPackagesRequest)
  })
_sym_db.RegisterMessage(UploadPrebuiltPackagesRequest)

UploadPrebuiltPackagesResponse = _reflection.GeneratedProtocolMessageType('UploadPrebuiltPackagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADPREBUILTPACKAGESRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UploadPrebuiltPackagesResponse)
  })
_sym_db.RegisterMessage(UploadPrebuiltPackagesResponse)

BuildSdkToolchainRequest = _reflection.GeneratedProtocolMessageType('BuildSdkToolchainRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUILDSDKTOOLCHAINREQUEST,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BuildSdkToolchainRequest)
  })
_sym_db.RegisterMessage(BuildSdkToolchainRequest)

BuildSdkToolchainResponse = _reflection.GeneratedProtocolMessageType('BuildSdkToolchainResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUILDSDKTOOLCHAINRESPONSE,
  '__module__' : 'chromite.api.sdk_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BuildSdkToolchainResponse)
  })
_sym_db.RegisterMessage(BuildSdkToolchainResponse)

_SDKSERVICE = DESCRIPTOR.services_by_name['SdkService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api'
  _SDKSERVICE._options = None
  _SDKSERVICE._serialized_options = b'\302\355\032\007\n\003sdk\020\002'
  _SDKSERVICE.methods_by_name['Update']._options = None
  _SDKSERVICE.methods_by_name['Update']._serialized_options = b'\302\355\032\002\020\001'
  _CHROOTVERSION._serialized_start=95
  _CHROOTVERSION._serialized_end=127
  _CREATEREQUEST._serialized_start=130
  _CREATEREQUEST._serialized_end=351
  _CREATEREQUEST_FLAGS._serialized_start=283
  _CREATEREQUEST_FLAGS._serialized_end=351
  _CREATERESPONSE._serialized_start=353
  _CREATERESPONSE._serialized_end=415
  _DELETEREQUEST._serialized_start=417
  _DELETEREQUEST._serialized_end=468
  _DELETERESPONSE._serialized_start=470
  _DELETERESPONSE._serialized_end=486
  _UNMOUNTREQUEST._serialized_start=488
  _UNMOUNTREQUEST._serialized_end=540
  _UNMOUNTRESPONSE._serialized_start=542
  _UNMOUNTRESPONSE._serialized_end=559
  _UPDATEREQUEST._serialized_start=562
  _UPDATEREQUEST._serialized_end=773
  _UPDATEREQUEST_FLAGS._serialized_start=717
  _UPDATEREQUEST_FLAGS._serialized_end=773
  _UPDATERESPONSE._serialized_start=775
  _UPDATERESPONSE._serialized_end=837
  _UPREVREQUEST._serialized_start=840
  _UPREVREQUEST._serialized_end=968
  _UPREVRESPONSE._serialized_start=970
  _UPREVRESPONSE._serialized_end=1044
  _CLEANREQUEST._serialized_start=1047
  _CLEANREQUEST._serialized_end=1227
  _CLEANRESPONSE._serialized_start=1229
  _CLEANRESPONSE._serialized_end=1244
  _SNAPSHOTTOKEN._serialized_start=1246
  _SNAPSHOTTOKEN._serialized_end=1276
  _CREATESNAPSHOTREQUEST._serialized_start=1278
  _CREATESNAPSHOTREQUEST._serialized_end=1337
  _CREATESNAPSHOTRESPONSE._serialized_start=1339
  _CREATESNAPSHOTRESPONSE._serialized_end=1416
  _RESTORESNAPSHOTREQUEST._serialized_start=1418
  _RESTORESNAPSHOTREQUEST._serialized_end=1531
  _RESTORESNAPSHOTRESPONSE._serialized_start=1533
  _RESTORESNAPSHOTRESPONSE._serialized_end=1558
  _UNMOUNTPATHREQUEST._serialized_start=1560
  _UNMOUNTPATHREQUEST._serialized_end=1612
  _UNMOUNTPATHRESPONSE._serialized_start=1614
  _UNMOUNTPATHRESPONSE._serialized_end=1635
  _BUILDPREBUILTSREQUEST._serialized_start=1637
  _BUILDPREBUILTSREQUEST._serialized_end=1743
  _BUILDPREBUILTSRESPONSE._serialized_start=1745
  _BUILDPREBUILTSRESPONSE._serialized_end=1769
  _BUILDSDKTARBALLREQUEST._serialized_start=1771
  _BUILDSDKTARBALLREQUEST._serialized_end=1831
  _BUILDSDKTARBALLRESPONSE._serialized_start=1833
  _BUILDSDKTARBALLRESPONSE._serialized_end=1902
  _CREATEMANIFESTFROMSDKREQUEST._serialized_start=1905
  _CREATEMANIFESTFROMSDKREQUEST._serialized_end=2043
  _CREATEMANIFESTFROMSDKRESPONSE._serialized_start=2045
  _CREATEMANIFESTFROMSDKRESPONSE._serialized_end=2117
  _CREATEBINHOSTCLSREQUEST._serialized_start=2119
  _CREATEBINHOSTCLSREQUEST._serialized_end=2241
  _CREATEBINHOSTCLSRESPONSE._serialized_start=2243
  _CREATEBINHOSTCLSRESPONSE._serialized_end=2282
  _UPLOADPREBUILTPACKAGESREQUEST._serialized_start=2285
  _UPLOADPREBUILTPACKAGESREQUEST._serialized_end=2419
  _UPLOADPREBUILTPACKAGESRESPONSE._serialized_start=2421
  _UPLOADPREBUILTPACKAGESRESPONSE._serialized_end=2453
  _BUILDSDKTOOLCHAINREQUEST._serialized_start=2455
  _BUILDSDKTOOLCHAINREQUEST._serialized_end=2557
  _BUILDSDKTOOLCHAINRESPONSE._serialized_start=2559
  _BUILDSDKTOOLCHAINRESPONSE._serialized_end=2629
  _SDKSERVICE._serialized_start=2632
  _SDKSERVICE._serialized_end=3970
# @@protoc_insertion_point(module_scope)
