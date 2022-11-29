# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/binhost.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen_sdk.chromite.api import sysroot_pb2 as chromite_dot_api_dot_sysroot__pb2
from chromite.api.gen_sdk.chromiumos import common_pb2 as chromiumos_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63hromite/api/binhost.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x1a\x63hromite/api/sysroot.proto\x1a\x17\x63hromiumos/common.proto\"-\n\x07\x42inhost\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x15\n\rpackage_index\x18\x02 \x01(\t\".\n\x0cPackageIndex\x12\x1e\n\x04path\x18\x01 \x01(\x0b\x32\x10.chromiumos.Path\"?\n\x0e\x41\x63lArgsRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\"k\n\x0f\x41\x63lArgsResponse\x12\x32\n\x04\x61rgs\x18\x01 \x03(\x0b\x32$.chromite.api.AclArgsResponse.AclArg\x1a$\n\x06\x41\x63lArg\x12\x0b\n\x03\x61rg\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"S\n\x11\x42inhostGetRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x0f\n\x07private\x18\x02 \x01(\x08\"=\n\x12\x42inhostGetResponse\x12\'\n\x08\x62inhosts\x18\x01 \x03(\x0b\x32\x15.chromite.api.Binhost\"\xdf\x01\n\x1cPrepareBinhostUploadsRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\"\n\x06\x63hroot\x18\x03 \x01(\x0b\x32\x12.chromiumos.Chroot\x12&\n\x07sysroot\x18\x04 \x01(\x0b\x32\x15.chromite.api.Sysroot\x12\x37\n\x13package_index_files\x18\x05 \x03(\x0b\x32\x1a.chromite.api.PackageIndex\"\x1c\n\x0cUploadTarget\x12\x0c\n\x04path\x18\x01 \x01(\t\"h\n\x1dPrepareBinhostUploadsResponse\x12\x13\n\x0buploads_dir\x18\x01 \x01(\t\x12\x32\n\x0eupload_targets\x18\x02 \x03(\x0b\x32\x1a.chromite.api.UploadTarget\"\x96\x01\n&PrepareDevInstallBinhostUploadsRequest\x12\x13\n\x0buploads_dir\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\"\n\x06\x63hroot\x18\x03 \x01(\x0b\x32\x12.chromiumos.Chroot\x12&\n\x07sysroot\x18\x04 \x01(\x0b\x32\x15.chromite.api.Sysroot\"]\n\'PrepareDevInstallBinhostUploadsResponse\x12\x32\n\x0eupload_targets\x18\x01 \x03(\x0b\x32\x1a.chromite.api.UploadTarget\"\x99\x01\n\x11SetBinhostRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x0f\n\x07private\x18\x02 \x01(\x08\x12%\n\x03key\x18\x03 \x01(\x0e\x32\x18.chromite.api.BinhostKey\x12\x0b\n\x03uri\x18\x04 \x01(\t\x12\x10\n\x08max_uris\x18\x05 \x01(\x05\")\n\x12SetBinhostResponse\x12\x13\n\x0boutput_file\x18\x01 \x01(\t\"m\n\x16RegenBuildCacheRequest\x12/\n\x0coverlay_type\x18\x01 \x01(\x0e\x32\x19.chromite.api.OverlayType\x12\"\n\x06\x63hroot\x18\x02 \x01(\x0b\x32\x12.chromiumos.Chroot\"\xc4\x01\n\x17RegenBuildCacheResponse\x12H\n\x11modified_overlays\x18\x01 \x03(\x0b\x32-.chromite.api.RegenBuildCacheResponse.Overlay\x12\x46\n\x0f\x66\x61iled_overlays\x18\x02 \x03(\x0b\x32-.chromite.api.RegenBuildCacheResponse.Overlay\x1a\x17\n\x07Overlay\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x82\x01\n\x19GetBinhostConfPathRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x0f\n\x07private\x18\x02 \x01(\x08\x12%\n\x03key\x18\x03 \x01(\x0e\x32\x18.chromite.api.BinhostKey\"/\n\x1aGetBinhostConfPathResponse\x12\x11\n\tconf_path\x18\x01 \x01(\t*o\n\nBinhostKey\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x16\n\x12POSTSUBMIT_BINHOST\x10\x01\x12!\n\x1dLATEST_RELEASE_CHROME_BINHOST\x10\x02\x12\x15\n\x11PREFLIGHT_BINHOST\x10\x03*\x87\x01\n\x0bOverlayType\x12\x1b\n\x17OVERLAYTYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10OVERLAYTYPE_BOTH\x10\x01\x12\x16\n\x12OVERLAYTYPE_PUBLIC\x10\x02\x12\x17\n\x13OVERLAYTYPE_PRIVATE\x10\x03\x12\x14\n\x10OVERLAYTYPE_NONE\x10\x04\x32\xf5\x05\n\x0e\x42inhostService\x12[\n\x03Get\x12\x1f.chromite.api.BinhostGetRequest\x1a .chromite.api.BinhostGetResponse\"\x11\xc2\xed\x1a\r\n\x0bGetBinhosts\x12X\n\x19GetPrivatePrebuiltAclArgs\x12\x1c.chromite.api.AclArgsRequest\x1a\x1d.chromite.api.AclArgsResponse\x12p\n\x15PrepareBinhostUploads\x12*.chromite.api.PrepareBinhostUploadsRequest\x1a+.chromite.api.PrepareBinhostUploadsResponse\x12\x8e\x01\n\x1fPrepareDevInstallBinhostUploads\x12\x34.chromite.api.PrepareDevInstallBinhostUploadsRequest\x1a\x35.chromite.api.PrepareDevInstallBinhostUploadsResponse\x12O\n\nSetBinhost\x12\x1f.chromite.api.SetBinhostRequest\x1a .chromite.api.SetBinhostResponse\x12^\n\x0fRegenBuildCache\x12$.chromite.api.RegenBuildCacheRequest\x1a%.chromite.api.RegenBuildCacheResponse\x12g\n\x12GetBinhostConfPath\x12\'.chromite.api.GetBinhostConfPathRequest\x1a(.chromite.api.GetBinhostConfPathResponse\x1a\x0f\xc2\xed\x1a\x0b\n\x07\x62inhost\x10\x02\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3')

_BINHOSTKEY = DESCRIPTOR.enum_types_by_name['BinhostKey']
BinhostKey = enum_type_wrapper.EnumTypeWrapper(_BINHOSTKEY)
_OVERLAYTYPE = DESCRIPTOR.enum_types_by_name['OverlayType']
OverlayType = enum_type_wrapper.EnumTypeWrapper(_OVERLAYTYPE)
UNSPECIFIED = 0
POSTSUBMIT_BINHOST = 1
LATEST_RELEASE_CHROME_BINHOST = 2
PREFLIGHT_BINHOST = 3
OVERLAYTYPE_UNSPECIFIED = 0
OVERLAYTYPE_BOTH = 1
OVERLAYTYPE_PUBLIC = 2
OVERLAYTYPE_PRIVATE = 3
OVERLAYTYPE_NONE = 4


_BINHOST = DESCRIPTOR.message_types_by_name['Binhost']
_PACKAGEINDEX = DESCRIPTOR.message_types_by_name['PackageIndex']
_ACLARGSREQUEST = DESCRIPTOR.message_types_by_name['AclArgsRequest']
_ACLARGSRESPONSE = DESCRIPTOR.message_types_by_name['AclArgsResponse']
_ACLARGSRESPONSE_ACLARG = _ACLARGSRESPONSE.nested_types_by_name['AclArg']
_BINHOSTGETREQUEST = DESCRIPTOR.message_types_by_name['BinhostGetRequest']
_BINHOSTGETRESPONSE = DESCRIPTOR.message_types_by_name['BinhostGetResponse']
_PREPAREBINHOSTUPLOADSREQUEST = DESCRIPTOR.message_types_by_name['PrepareBinhostUploadsRequest']
_UPLOADTARGET = DESCRIPTOR.message_types_by_name['UploadTarget']
_PREPAREBINHOSTUPLOADSRESPONSE = DESCRIPTOR.message_types_by_name['PrepareBinhostUploadsResponse']
_PREPAREDEVINSTALLBINHOSTUPLOADSREQUEST = DESCRIPTOR.message_types_by_name['PrepareDevInstallBinhostUploadsRequest']
_PREPAREDEVINSTALLBINHOSTUPLOADSRESPONSE = DESCRIPTOR.message_types_by_name['PrepareDevInstallBinhostUploadsResponse']
_SETBINHOSTREQUEST = DESCRIPTOR.message_types_by_name['SetBinhostRequest']
_SETBINHOSTRESPONSE = DESCRIPTOR.message_types_by_name['SetBinhostResponse']
_REGENBUILDCACHEREQUEST = DESCRIPTOR.message_types_by_name['RegenBuildCacheRequest']
_REGENBUILDCACHERESPONSE = DESCRIPTOR.message_types_by_name['RegenBuildCacheResponse']
_REGENBUILDCACHERESPONSE_OVERLAY = _REGENBUILDCACHERESPONSE.nested_types_by_name['Overlay']
_GETBINHOSTCONFPATHREQUEST = DESCRIPTOR.message_types_by_name['GetBinhostConfPathRequest']
_GETBINHOSTCONFPATHRESPONSE = DESCRIPTOR.message_types_by_name['GetBinhostConfPathResponse']
Binhost = _reflection.GeneratedProtocolMessageType('Binhost', (_message.Message,), {
  'DESCRIPTOR' : _BINHOST,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.Binhost)
  })
_sym_db.RegisterMessage(Binhost)

PackageIndex = _reflection.GeneratedProtocolMessageType('PackageIndex', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGEINDEX,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.PackageIndex)
  })
_sym_db.RegisterMessage(PackageIndex)

AclArgsRequest = _reflection.GeneratedProtocolMessageType('AclArgsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACLARGSREQUEST,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.AclArgsRequest)
  })
_sym_db.RegisterMessage(AclArgsRequest)

AclArgsResponse = _reflection.GeneratedProtocolMessageType('AclArgsResponse', (_message.Message,), {

  'AclArg' : _reflection.GeneratedProtocolMessageType('AclArg', (_message.Message,), {
    'DESCRIPTOR' : _ACLARGSRESPONSE_ACLARG,
    '__module__' : 'chromite.api.binhost_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.AclArgsResponse.AclArg)
    })
  ,
  'DESCRIPTOR' : _ACLARGSRESPONSE,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.AclArgsResponse)
  })
_sym_db.RegisterMessage(AclArgsResponse)
_sym_db.RegisterMessage(AclArgsResponse.AclArg)

BinhostGetRequest = _reflection.GeneratedProtocolMessageType('BinhostGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _BINHOSTGETREQUEST,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BinhostGetRequest)
  })
_sym_db.RegisterMessage(BinhostGetRequest)

BinhostGetResponse = _reflection.GeneratedProtocolMessageType('BinhostGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _BINHOSTGETRESPONSE,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BinhostGetResponse)
  })
_sym_db.RegisterMessage(BinhostGetResponse)

PrepareBinhostUploadsRequest = _reflection.GeneratedProtocolMessageType('PrepareBinhostUploadsRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREBINHOSTUPLOADSREQUEST,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.PrepareBinhostUploadsRequest)
  })
_sym_db.RegisterMessage(PrepareBinhostUploadsRequest)

UploadTarget = _reflection.GeneratedProtocolMessageType('UploadTarget', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADTARGET,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.UploadTarget)
  })
_sym_db.RegisterMessage(UploadTarget)

PrepareBinhostUploadsResponse = _reflection.GeneratedProtocolMessageType('PrepareBinhostUploadsResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREBINHOSTUPLOADSRESPONSE,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.PrepareBinhostUploadsResponse)
  })
_sym_db.RegisterMessage(PrepareBinhostUploadsResponse)

PrepareDevInstallBinhostUploadsRequest = _reflection.GeneratedProtocolMessageType('PrepareDevInstallBinhostUploadsRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREDEVINSTALLBINHOSTUPLOADSREQUEST,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.PrepareDevInstallBinhostUploadsRequest)
  })
_sym_db.RegisterMessage(PrepareDevInstallBinhostUploadsRequest)

PrepareDevInstallBinhostUploadsResponse = _reflection.GeneratedProtocolMessageType('PrepareDevInstallBinhostUploadsResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREDEVINSTALLBINHOSTUPLOADSRESPONSE,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.PrepareDevInstallBinhostUploadsResponse)
  })
_sym_db.RegisterMessage(PrepareDevInstallBinhostUploadsResponse)

SetBinhostRequest = _reflection.GeneratedProtocolMessageType('SetBinhostRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETBINHOSTREQUEST,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SetBinhostRequest)
  })
_sym_db.RegisterMessage(SetBinhostRequest)

SetBinhostResponse = _reflection.GeneratedProtocolMessageType('SetBinhostResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETBINHOSTRESPONSE,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.SetBinhostResponse)
  })
_sym_db.RegisterMessage(SetBinhostResponse)

RegenBuildCacheRequest = _reflection.GeneratedProtocolMessageType('RegenBuildCacheRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGENBUILDCACHEREQUEST,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.RegenBuildCacheRequest)
  })
_sym_db.RegisterMessage(RegenBuildCacheRequest)

RegenBuildCacheResponse = _reflection.GeneratedProtocolMessageType('RegenBuildCacheResponse', (_message.Message,), {

  'Overlay' : _reflection.GeneratedProtocolMessageType('Overlay', (_message.Message,), {
    'DESCRIPTOR' : _REGENBUILDCACHERESPONSE_OVERLAY,
    '__module__' : 'chromite.api.binhost_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.RegenBuildCacheResponse.Overlay)
    })
  ,
  'DESCRIPTOR' : _REGENBUILDCACHERESPONSE,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.RegenBuildCacheResponse)
  })
_sym_db.RegisterMessage(RegenBuildCacheResponse)
_sym_db.RegisterMessage(RegenBuildCacheResponse.Overlay)

GetBinhostConfPathRequest = _reflection.GeneratedProtocolMessageType('GetBinhostConfPathRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBINHOSTCONFPATHREQUEST,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.GetBinhostConfPathRequest)
  })
_sym_db.RegisterMessage(GetBinhostConfPathRequest)

GetBinhostConfPathResponse = _reflection.GeneratedProtocolMessageType('GetBinhostConfPathResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBINHOSTCONFPATHRESPONSE,
  '__module__' : 'chromite.api.binhost_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.GetBinhostConfPathResponse)
  })
_sym_db.RegisterMessage(GetBinhostConfPathResponse)

_BINHOSTSERVICE = DESCRIPTOR.services_by_name['BinhostService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api'
  _BINHOSTSERVICE._options = None
  _BINHOSTSERVICE._serialized_options = b'\302\355\032\013\n\007binhost\020\002'
  _BINHOSTSERVICE.methods_by_name['Get']._options = None
  _BINHOSTSERVICE.methods_by_name['Get']._serialized_options = b'\302\355\032\r\n\013GetBinhosts'
  _BINHOSTKEY._serialized_start=1845
  _BINHOSTKEY._serialized_end=1956
  _OVERLAYTYPE._serialized_start=1959
  _OVERLAYTYPE._serialized_end=2094
  _BINHOST._serialized_start=127
  _BINHOST._serialized_end=172
  _PACKAGEINDEX._serialized_start=174
  _PACKAGEINDEX._serialized_end=220
  _ACLARGSREQUEST._serialized_start=222
  _ACLARGSREQUEST._serialized_end=285
  _ACLARGSRESPONSE._serialized_start=287
  _ACLARGSRESPONSE._serialized_end=394
  _ACLARGSRESPONSE_ACLARG._serialized_start=358
  _ACLARGSRESPONSE_ACLARG._serialized_end=394
  _BINHOSTGETREQUEST._serialized_start=396
  _BINHOSTGETREQUEST._serialized_end=479
  _BINHOSTGETRESPONSE._serialized_start=481
  _BINHOSTGETRESPONSE._serialized_end=542
  _PREPAREBINHOSTUPLOADSREQUEST._serialized_start=545
  _PREPAREBINHOSTUPLOADSREQUEST._serialized_end=768
  _UPLOADTARGET._serialized_start=770
  _UPLOADTARGET._serialized_end=798
  _PREPAREBINHOSTUPLOADSRESPONSE._serialized_start=800
  _PREPAREBINHOSTUPLOADSRESPONSE._serialized_end=904
  _PREPAREDEVINSTALLBINHOSTUPLOADSREQUEST._serialized_start=907
  _PREPAREDEVINSTALLBINHOSTUPLOADSREQUEST._serialized_end=1057
  _PREPAREDEVINSTALLBINHOSTUPLOADSRESPONSE._serialized_start=1059
  _PREPAREDEVINSTALLBINHOSTUPLOADSRESPONSE._serialized_end=1152
  _SETBINHOSTREQUEST._serialized_start=1155
  _SETBINHOSTREQUEST._serialized_end=1308
  _SETBINHOSTRESPONSE._serialized_start=1310
  _SETBINHOSTRESPONSE._serialized_end=1351
  _REGENBUILDCACHEREQUEST._serialized_start=1353
  _REGENBUILDCACHEREQUEST._serialized_end=1462
  _REGENBUILDCACHERESPONSE._serialized_start=1465
  _REGENBUILDCACHERESPONSE._serialized_end=1661
  _REGENBUILDCACHERESPONSE_OVERLAY._serialized_start=1638
  _REGENBUILDCACHERESPONSE_OVERLAY._serialized_end=1661
  _GETBINHOSTCONFPATHREQUEST._serialized_start=1664
  _GETBINHOSTCONFPATHREQUEST._serialized_end=1794
  _GETBINHOSTCONFPATHRESPONSE._serialized_start=1796
  _GETBINHOSTCONFPATHRESPONSE._serialized_end=1843
  _BINHOSTSERVICE._serialized_start=2097
  _BINHOSTSERVICE._serialized_end=2854
# @@protoc_insertion_point(module_scope)
