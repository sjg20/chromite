# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/test/tls/commontls.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chromite.api.gen_sdk.chromiumos.config.api.test.tls.dependencies.longrunning import operations_pb2 as chromiumos_dot_config_dot_api_dot_test_dot_tls_dot_dependencies_dot_longrunning_dot_operations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.chromiumos/config/api/test/tls/commontls.proto\x12\x1e\x63hromiumos.config.api.test.tls\x1a\x1bgoogle/protobuf/empty.proto\x1aHchromiumos/config/api/test/tls/dependencies/longrunning/operations.proto\"\xc3\x01\n\x15\x45xecDutCommandRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\r\n\x05stdin\x18\x04 \x01(\x0c\x12\x36\n\x06stdout\x18\x05 \x01(\x0e\x32&.chromiumos.config.api.test.tls.Output\x12\x36\n\x06stderr\x18\x06 \x01(\x0e\x32&.chromiumos.config.api.test.tls.Output\"\xe2\x01\n\x16\x45xecDutCommandResponse\x12R\n\texit_info\x18\x01 \x01(\x0b\x32?.chromiumos.config.api.test.tls.ExecDutCommandResponse.ExitInfo\x12\x0e\n\x06stdout\x18\x02 \x01(\x0c\x12\x0e\n\x06stderr\x18\x03 \x01(\x0c\x1aT\n\x08\x45xitInfo\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08signaled\x18\x02 \x01(\x08\x12\x0f\n\x07started\x18\x03 \x01(\x08\x12\x15\n\rerror_message\x18\x04 \x01(\t\"\xca\x03\n\x13ProvisionDutRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12T\n\x05image\x18\x02 \x01(\x0b\x32\x41.chromiumos.config.api.test.tls.ProvisionDutRequest.ChromeOSImageB\x02\x18\x01\x12N\n\tdlc_specs\x18\x03 \x03(\x0b\x32;.chromiumos.config.api.test.tls.ProvisionDutRequest.DLCSpec\x12\x19\n\x11preserve_stateful\x18\x04 \x01(\x08\x12\x43\n\x0ctarget_build\x18\x05 \x01(\x0b\x32-.chromiumos.config.api.test.tls.ChromeOsImage\x12\x1a\n\x12\x66orce_provision_os\x18\x06 \x01(\x08\x12\x16\n\x0eprevent_reboot\x18\x07 \x01(\x08\x12\x17\n\x0fupdate_firmware\x18\x08 \x01(\x08\x1a;\n\rChromeOSImage\x12\x18\n\x0egs_path_prefix\x18\x01 \x01(\tH\x00:\x02\x18\x01\x42\x0c\n\npath_oneof\x1a\x15\n\x07\x44LCSpec\x12\n\n\x02id\x18\x01 \x01(\t\"\x80\x03\n\x14ProvisionDutResponse\"\xe7\x02\n\x06Reason\x12\x1a\n\x16REASON_INVALID_REQUEST\x10\x00\x12(\n$REASON_DUT_UNREACHABLE_PRE_PROVISION\x10\x01\x12#\n\x1fREASON_DOWNLOADING_IMAGE_FAILED\x10\x02\x12 \n\x1cREASON_PROVISIONING_TIMEDOUT\x10\x03\x12\x1e\n\x1aREASON_PROVISIONING_FAILED\x10\x04\x12)\n%REASON_DUT_UNREACHABLE_POST_PROVISION\x10\x05\x12!\n\x1dREASON_UPDATE_FIRMWARE_FAILED\x10\x06\x12\x31\n-REASON_FIRMWARE_MISMATCH_POST_FIRMWARE_UPDATE\x10\x07\x12/\n+REASON_DUT_UNREACHABLE_POST_FIRMWARE_UPDATE\x10\x08\"\x16\n\x14ProvisionDutMetadata\"\x87\x02\n\x16ProvisionLacrosRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12Q\n\x05image\x18\x02 \x01(\x0b\x32\x42.chromiumos.config.api.test.tls.ProvisionLacrosRequest.LacrosImage\x12\x18\n\x10override_version\x18\x03 \x01(\t\x12\x1d\n\x15override_install_path\x18\x04 \x01(\t\x1aS\n\x0bLacrosImage\x12\x18\n\x0egs_path_prefix\x18\x01 \x01(\tH\x00\x12\x1c\n\x12\x64\x65vice_file_prefix\x18\x02 \x01(\tH\x00\x42\x0c\n\npath_oneof\"\xd1\x01\n\x17ProvisionLacrosResponse\"\xb5\x01\n\x06Reason\x12\x1a\n\x16REASON_INVALID_REQUEST\x10\x00\x12(\n$REASON_DUT_UNREACHABLE_PRE_PROVISION\x10\x01\x12#\n\x1fREASON_DOWNLOADING_IMAGE_FAILED\x10\x02\x12 \n\x1cREASON_PROVISIONING_TIMEDOUT\x10\x03\x12\x1e\n\x1aREASON_PROVISIONING_FAILED\x10\x04\"\x19\n\x17ProvisionLacrosMetadata\"\xa7\x01\n\x13ProvisionAshRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12M\n\x06\x62undle\x18\x02 \x01(\x0b\x32=.chromiumos.config.api.test.tls.ProvisionAshRequest.AshBundle\x1a\x33\n\tAshBundle\x12\x18\n\x0egs_bundle_path\x18\x01 \x01(\tH\x00\x42\x0c\n\npath_oneof\"\xcf\x01\n\x14ProvisionAshResponse\"\xb6\x01\n\x06Reason\x12\x1a\n\x16REASON_INVALID_REQUEST\x10\x00\x12(\n$REASON_DUT_UNREACHABLE_PRE_PROVISION\x10\x01\x12$\n REASON_DOWNLOADING_BUNDLE_FAILED\x10\x02\x12 \n\x1cREASON_PROVISIONING_TIMEDOUT\x10\x03\x12\x1e\n\x1aREASON_PROVISIONING_FAILED\x10\x04\"\x16\n\x14ProvisionAshMetadata\"6\n\x13\x46\x65tchCrashesRequest\x12\x0b\n\x03\x64ut\x18\x01 \x01(\t\x12\x12\n\nfetch_core\x18\x02 \x01(\x08\"\xb7\x01\n\x14\x46\x65tchCrashesResponse\x12\x10\n\x08\x63rash_id\x18\x01 \x01(\x03\x12:\n\x05\x63rash\x18\x02 \x01(\x0b\x32).chromiumos.config.api.test.tls.CrashInfoH\x00\x12\x39\n\x04\x62lob\x18\x03 \x01(\x0b\x32).chromiumos.config.api.test.tls.CrashBlobH\x00\x12\x0e\n\x04\x63ore\x18\x04 \x01(\x0cH\x00\x42\x06\n\x04\x64\x61ta\"\xbe\x01\n\tCrashInfo\x12\x11\n\texec_name\x18\x01 \x01(\t\x12\x0c\n\x04prod\x18\x02 \x01(\t\x12\x0b\n\x03ver\x18\x03 \x01(\t\x12\x0b\n\x03sig\x18\x04 \x01(\t\x12$\n\x1cin_progress_integration_test\x18\x05 \x01(\t\x12\x11\n\tcollector\x18\x06 \x01(\t\x12=\n\x06\x66ields\x18\x07 \x03(\x0b\x32-.chromiumos.config.api.test.tls.CrashMetadata\"*\n\rCrashMetadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"8\n\tCrashBlob\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x62lob\x18\x02 \x01(\x0c\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\"7\n\rChromeOsImage\x12\x18\n\x0egs_path_prefix\x18\x01 \x01(\tH\x00\x42\x0c\n\npath_oneof\"\xaa\x03\n\tFakeOmaha\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x64ut\x18\x02 \x01(\t\x12\x43\n\x0ctarget_build\x18\x03 \x01(\x0b\x32-.chromiumos.config.api.test.tls.ChromeOsImage\x12\x43\n\x08payloads\x18\x04 \x03(\x0b\x32\x31.chromiumos.config.api.test.tls.FakeOmaha.Payload\x12\x19\n\x11\x65xposed_via_proxy\x18\x05 \x01(\x08\x12\x17\n\x0f\x63ritical_update\x18\x06 \x01(\x08\x12 \n\x18return_noupdate_starting\x18\x07 \x01(\x05\x12\x11\n\tomaha_url\x18\x08 \x01(\t\x1a\x8e\x01\n\x07Payload\x12\n\n\x02id\x18\x01 \x01(\t\x12\x44\n\x04type\x18\x02 \x01(\x0e\x32\x36.chromiumos.config.api.test.tls.FakeOmaha.Payload.Type\"1\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\x12\t\n\x05\x44\x45LTA\x10\x02\"W\n\x16\x43reateFakeOmahaRequest\x12=\n\nfake_omaha\x18\x01 \x01(\x0b\x32).chromiumos.config.api.test.tls.FakeOmaha\"&\n\x16\x44\x65leteFakeOmahaRequest\x12\x0c\n\x04name\x18\x01 \x01(\t*,\n\x06Output\x12\x0f\n\x0bOUTPUT_PIPE\x10\x00\x12\x11\n\rOUTPUT_STDOUT\x10\x01\x32\xb0\x07\n\x06\x43ommon\x12\x81\x01\n\x0e\x45xecDutCommand\x12\x35.chromiumos.config.api.test.tls.ExecDutCommandRequest\x1a\x36.chromiumos.config.api.test.tls.ExecDutCommandResponse0\x01\x12\x93\x01\n\x0cProvisionDut\x12\x33.chromiumos.config.api.test.tls.ProvisionDutRequest\x1a\x1d.google.longrunning.Operation\"/\xca\x41,\n\x14ProvisionDutResponse\x12\x14ProvisionDutMetadata\x12\x9f\x01\n\x0fProvisionLacros\x12\x36.chromiumos.config.api.test.tls.ProvisionLacrosRequest\x1a\x1d.google.longrunning.Operation\"5\xca\x41\x32\n\x17ProvisionLacrosResponse\x12\x17ProvisionLacrosMetadata\x12\x93\x01\n\x0cProvisionAsh\x12\x33.chromiumos.config.api.test.tls.ProvisionAshRequest\x1a\x1d.google.longrunning.Operation\"/\xca\x41,\n\x14ProvisionAshResponse\x12\x14ProvisionAshMetadata\x12{\n\x0c\x46\x65tchCrashes\x12\x33.chromiumos.config.api.test.tls.FetchCrashesRequest\x1a\x34.chromiumos.config.api.test.tls.FetchCrashesResponse0\x01\x12t\n\x0f\x43reateFakeOmaha\x12\x36.chromiumos.config.api.test.tls.CreateFakeOmahaRequest\x1a).chromiumos.config.api.test.tls.FakeOmaha\x12\x61\n\x0f\x44\x65leteFakeOmaha\x12\x36.chromiumos.config.api.test.tls.DeleteFakeOmahaRequest\x1a\x16.google.protobuf.EmptyB3Z1go.chromium.org/chromiumos/config/go/api/test/tlsb\x06proto3')

_OUTPUT = DESCRIPTOR.enum_types_by_name['Output']
Output = enum_type_wrapper.EnumTypeWrapper(_OUTPUT)
OUTPUT_PIPE = 0
OUTPUT_STDOUT = 1


_EXECDUTCOMMANDREQUEST = DESCRIPTOR.message_types_by_name['ExecDutCommandRequest']
_EXECDUTCOMMANDRESPONSE = DESCRIPTOR.message_types_by_name['ExecDutCommandResponse']
_EXECDUTCOMMANDRESPONSE_EXITINFO = _EXECDUTCOMMANDRESPONSE.nested_types_by_name['ExitInfo']
_PROVISIONDUTREQUEST = DESCRIPTOR.message_types_by_name['ProvisionDutRequest']
_PROVISIONDUTREQUEST_CHROMEOSIMAGE = _PROVISIONDUTREQUEST.nested_types_by_name['ChromeOSImage']
_PROVISIONDUTREQUEST_DLCSPEC = _PROVISIONDUTREQUEST.nested_types_by_name['DLCSpec']
_PROVISIONDUTRESPONSE = DESCRIPTOR.message_types_by_name['ProvisionDutResponse']
_PROVISIONDUTMETADATA = DESCRIPTOR.message_types_by_name['ProvisionDutMetadata']
_PROVISIONLACROSREQUEST = DESCRIPTOR.message_types_by_name['ProvisionLacrosRequest']
_PROVISIONLACROSREQUEST_LACROSIMAGE = _PROVISIONLACROSREQUEST.nested_types_by_name['LacrosImage']
_PROVISIONLACROSRESPONSE = DESCRIPTOR.message_types_by_name['ProvisionLacrosResponse']
_PROVISIONLACROSMETADATA = DESCRIPTOR.message_types_by_name['ProvisionLacrosMetadata']
_PROVISIONASHREQUEST = DESCRIPTOR.message_types_by_name['ProvisionAshRequest']
_PROVISIONASHREQUEST_ASHBUNDLE = _PROVISIONASHREQUEST.nested_types_by_name['AshBundle']
_PROVISIONASHRESPONSE = DESCRIPTOR.message_types_by_name['ProvisionAshResponse']
_PROVISIONASHMETADATA = DESCRIPTOR.message_types_by_name['ProvisionAshMetadata']
_FETCHCRASHESREQUEST = DESCRIPTOR.message_types_by_name['FetchCrashesRequest']
_FETCHCRASHESRESPONSE = DESCRIPTOR.message_types_by_name['FetchCrashesResponse']
_CRASHINFO = DESCRIPTOR.message_types_by_name['CrashInfo']
_CRASHMETADATA = DESCRIPTOR.message_types_by_name['CrashMetadata']
_CRASHBLOB = DESCRIPTOR.message_types_by_name['CrashBlob']
_CHROMEOSIMAGE = DESCRIPTOR.message_types_by_name['ChromeOsImage']
_FAKEOMAHA = DESCRIPTOR.message_types_by_name['FakeOmaha']
_FAKEOMAHA_PAYLOAD = _FAKEOMAHA.nested_types_by_name['Payload']
_CREATEFAKEOMAHAREQUEST = DESCRIPTOR.message_types_by_name['CreateFakeOmahaRequest']
_DELETEFAKEOMAHAREQUEST = DESCRIPTOR.message_types_by_name['DeleteFakeOmahaRequest']
_PROVISIONDUTRESPONSE_REASON = _PROVISIONDUTRESPONSE.enum_types_by_name['Reason']
_PROVISIONLACROSRESPONSE_REASON = _PROVISIONLACROSRESPONSE.enum_types_by_name['Reason']
_PROVISIONASHRESPONSE_REASON = _PROVISIONASHRESPONSE.enum_types_by_name['Reason']
_FAKEOMAHA_PAYLOAD_TYPE = _FAKEOMAHA_PAYLOAD.enum_types_by_name['Type']
ExecDutCommandRequest = _reflection.GeneratedProtocolMessageType('ExecDutCommandRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECDUTCOMMANDREQUEST,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ExecDutCommandRequest)
  })
_sym_db.RegisterMessage(ExecDutCommandRequest)

ExecDutCommandResponse = _reflection.GeneratedProtocolMessageType('ExecDutCommandResponse', (_message.Message,), {

  'ExitInfo' : _reflection.GeneratedProtocolMessageType('ExitInfo', (_message.Message,), {
    'DESCRIPTOR' : _EXECDUTCOMMANDRESPONSE_EXITINFO,
    '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ExecDutCommandResponse.ExitInfo)
    })
  ,
  'DESCRIPTOR' : _EXECDUTCOMMANDRESPONSE,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ExecDutCommandResponse)
  })
_sym_db.RegisterMessage(ExecDutCommandResponse)
_sym_db.RegisterMessage(ExecDutCommandResponse.ExitInfo)

ProvisionDutRequest = _reflection.GeneratedProtocolMessageType('ProvisionDutRequest', (_message.Message,), {

  'ChromeOSImage' : _reflection.GeneratedProtocolMessageType('ChromeOSImage', (_message.Message,), {
    'DESCRIPTOR' : _PROVISIONDUTREQUEST_CHROMEOSIMAGE,
    '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionDutRequest.ChromeOSImage)
    })
  ,

  'DLCSpec' : _reflection.GeneratedProtocolMessageType('DLCSpec', (_message.Message,), {
    'DESCRIPTOR' : _PROVISIONDUTREQUEST_DLCSPEC,
    '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionDutRequest.DLCSpec)
    })
  ,
  'DESCRIPTOR' : _PROVISIONDUTREQUEST,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionDutRequest)
  })
_sym_db.RegisterMessage(ProvisionDutRequest)
_sym_db.RegisterMessage(ProvisionDutRequest.ChromeOSImage)
_sym_db.RegisterMessage(ProvisionDutRequest.DLCSpec)

ProvisionDutResponse = _reflection.GeneratedProtocolMessageType('ProvisionDutResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVISIONDUTRESPONSE,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionDutResponse)
  })
_sym_db.RegisterMessage(ProvisionDutResponse)

ProvisionDutMetadata = _reflection.GeneratedProtocolMessageType('ProvisionDutMetadata', (_message.Message,), {
  'DESCRIPTOR' : _PROVISIONDUTMETADATA,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionDutMetadata)
  })
_sym_db.RegisterMessage(ProvisionDutMetadata)

ProvisionLacrosRequest = _reflection.GeneratedProtocolMessageType('ProvisionLacrosRequest', (_message.Message,), {

  'LacrosImage' : _reflection.GeneratedProtocolMessageType('LacrosImage', (_message.Message,), {
    'DESCRIPTOR' : _PROVISIONLACROSREQUEST_LACROSIMAGE,
    '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionLacrosRequest.LacrosImage)
    })
  ,
  'DESCRIPTOR' : _PROVISIONLACROSREQUEST,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionLacrosRequest)
  })
_sym_db.RegisterMessage(ProvisionLacrosRequest)
_sym_db.RegisterMessage(ProvisionLacrosRequest.LacrosImage)

ProvisionLacrosResponse = _reflection.GeneratedProtocolMessageType('ProvisionLacrosResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVISIONLACROSRESPONSE,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionLacrosResponse)
  })
_sym_db.RegisterMessage(ProvisionLacrosResponse)

ProvisionLacrosMetadata = _reflection.GeneratedProtocolMessageType('ProvisionLacrosMetadata', (_message.Message,), {
  'DESCRIPTOR' : _PROVISIONLACROSMETADATA,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionLacrosMetadata)
  })
_sym_db.RegisterMessage(ProvisionLacrosMetadata)

ProvisionAshRequest = _reflection.GeneratedProtocolMessageType('ProvisionAshRequest', (_message.Message,), {

  'AshBundle' : _reflection.GeneratedProtocolMessageType('AshBundle', (_message.Message,), {
    'DESCRIPTOR' : _PROVISIONASHREQUEST_ASHBUNDLE,
    '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionAshRequest.AshBundle)
    })
  ,
  'DESCRIPTOR' : _PROVISIONASHREQUEST,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionAshRequest)
  })
_sym_db.RegisterMessage(ProvisionAshRequest)
_sym_db.RegisterMessage(ProvisionAshRequest.AshBundle)

ProvisionAshResponse = _reflection.GeneratedProtocolMessageType('ProvisionAshResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVISIONASHRESPONSE,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionAshResponse)
  })
_sym_db.RegisterMessage(ProvisionAshResponse)

ProvisionAshMetadata = _reflection.GeneratedProtocolMessageType('ProvisionAshMetadata', (_message.Message,), {
  'DESCRIPTOR' : _PROVISIONASHMETADATA,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ProvisionAshMetadata)
  })
_sym_db.RegisterMessage(ProvisionAshMetadata)

FetchCrashesRequest = _reflection.GeneratedProtocolMessageType('FetchCrashesRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHCRASHESREQUEST,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.FetchCrashesRequest)
  })
_sym_db.RegisterMessage(FetchCrashesRequest)

FetchCrashesResponse = _reflection.GeneratedProtocolMessageType('FetchCrashesResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHCRASHESRESPONSE,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.FetchCrashesResponse)
  })
_sym_db.RegisterMessage(FetchCrashesResponse)

CrashInfo = _reflection.GeneratedProtocolMessageType('CrashInfo', (_message.Message,), {
  'DESCRIPTOR' : _CRASHINFO,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.CrashInfo)
  })
_sym_db.RegisterMessage(CrashInfo)

CrashMetadata = _reflection.GeneratedProtocolMessageType('CrashMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CRASHMETADATA,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.CrashMetadata)
  })
_sym_db.RegisterMessage(CrashMetadata)

CrashBlob = _reflection.GeneratedProtocolMessageType('CrashBlob', (_message.Message,), {
  'DESCRIPTOR' : _CRASHBLOB,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.CrashBlob)
  })
_sym_db.RegisterMessage(CrashBlob)

ChromeOsImage = _reflection.GeneratedProtocolMessageType('ChromeOsImage', (_message.Message,), {
  'DESCRIPTOR' : _CHROMEOSIMAGE,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.ChromeOsImage)
  })
_sym_db.RegisterMessage(ChromeOsImage)

FakeOmaha = _reflection.GeneratedProtocolMessageType('FakeOmaha', (_message.Message,), {

  'Payload' : _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), {
    'DESCRIPTOR' : _FAKEOMAHA_PAYLOAD,
    '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.FakeOmaha.Payload)
    })
  ,
  'DESCRIPTOR' : _FAKEOMAHA,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.FakeOmaha)
  })
_sym_db.RegisterMessage(FakeOmaha)
_sym_db.RegisterMessage(FakeOmaha.Payload)

CreateFakeOmahaRequest = _reflection.GeneratedProtocolMessageType('CreateFakeOmahaRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFAKEOMAHAREQUEST,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.CreateFakeOmahaRequest)
  })
_sym_db.RegisterMessage(CreateFakeOmahaRequest)

DeleteFakeOmahaRequest = _reflection.GeneratedProtocolMessageType('DeleteFakeOmahaRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFAKEOMAHAREQUEST,
  '__module__' : 'chromiumos.config.api.test.tls.commontls_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.test.tls.DeleteFakeOmahaRequest)
  })
_sym_db.RegisterMessage(DeleteFakeOmahaRequest)

_COMMON = DESCRIPTOR.services_by_name['Common']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1go.chromium.org/chromiumos/config/go/api/test/tls'
  _PROVISIONDUTREQUEST_CHROMEOSIMAGE._options = None
  _PROVISIONDUTREQUEST_CHROMEOSIMAGE._serialized_options = b'\030\001'
  _PROVISIONDUTREQUEST.fields_by_name['image']._options = None
  _PROVISIONDUTREQUEST.fields_by_name['image']._serialized_options = b'\030\001'
  _COMMON.methods_by_name['ProvisionDut']._options = None
  _COMMON.methods_by_name['ProvisionDut']._serialized_options = b'\312A,\n\024ProvisionDutResponse\022\024ProvisionDutMetadata'
  _COMMON.methods_by_name['ProvisionLacros']._options = None
  _COMMON.methods_by_name['ProvisionLacros']._serialized_options = b'\312A2\n\027ProvisionLacrosResponse\022\027ProvisionLacrosMetadata'
  _COMMON.methods_by_name['ProvisionAsh']._options = None
  _COMMON.methods_by_name['ProvisionAsh']._serialized_options = b'\312A,\n\024ProvisionAshResponse\022\024ProvisionAshMetadata'
  _OUTPUT._serialized_start=3545
  _OUTPUT._serialized_end=3589
  _EXECDUTCOMMANDREQUEST._serialized_start=186
  _EXECDUTCOMMANDREQUEST._serialized_end=381
  _EXECDUTCOMMANDRESPONSE._serialized_start=384
  _EXECDUTCOMMANDRESPONSE._serialized_end=610
  _EXECDUTCOMMANDRESPONSE_EXITINFO._serialized_start=526
  _EXECDUTCOMMANDRESPONSE_EXITINFO._serialized_end=610
  _PROVISIONDUTREQUEST._serialized_start=613
  _PROVISIONDUTREQUEST._serialized_end=1071
  _PROVISIONDUTREQUEST_CHROMEOSIMAGE._serialized_start=989
  _PROVISIONDUTREQUEST_CHROMEOSIMAGE._serialized_end=1048
  _PROVISIONDUTREQUEST_DLCSPEC._serialized_start=1050
  _PROVISIONDUTREQUEST_DLCSPEC._serialized_end=1071
  _PROVISIONDUTRESPONSE._serialized_start=1074
  _PROVISIONDUTRESPONSE._serialized_end=1458
  _PROVISIONDUTRESPONSE_REASON._serialized_start=1099
  _PROVISIONDUTRESPONSE_REASON._serialized_end=1458
  _PROVISIONDUTMETADATA._serialized_start=1460
  _PROVISIONDUTMETADATA._serialized_end=1482
  _PROVISIONLACROSREQUEST._serialized_start=1485
  _PROVISIONLACROSREQUEST._serialized_end=1748
  _PROVISIONLACROSREQUEST_LACROSIMAGE._serialized_start=1665
  _PROVISIONLACROSREQUEST_LACROSIMAGE._serialized_end=1748
  _PROVISIONLACROSRESPONSE._serialized_start=1751
  _PROVISIONLACROSRESPONSE._serialized_end=1960
  _PROVISIONLACROSRESPONSE_REASON._serialized_start=1099
  _PROVISIONLACROSRESPONSE_REASON._serialized_end=1280
  _PROVISIONLACROSMETADATA._serialized_start=1962
  _PROVISIONLACROSMETADATA._serialized_end=1987
  _PROVISIONASHREQUEST._serialized_start=1990
  _PROVISIONASHREQUEST._serialized_end=2157
  _PROVISIONASHREQUEST_ASHBUNDLE._serialized_start=2106
  _PROVISIONASHREQUEST_ASHBUNDLE._serialized_end=2157
  _PROVISIONASHRESPONSE._serialized_start=2160
  _PROVISIONASHRESPONSE._serialized_end=2367
  _PROVISIONASHRESPONSE_REASON._serialized_start=2185
  _PROVISIONASHRESPONSE_REASON._serialized_end=2367
  _PROVISIONASHMETADATA._serialized_start=2369
  _PROVISIONASHMETADATA._serialized_end=2391
  _FETCHCRASHESREQUEST._serialized_start=2393
  _FETCHCRASHESREQUEST._serialized_end=2447
  _FETCHCRASHESRESPONSE._serialized_start=2450
  _FETCHCRASHESRESPONSE._serialized_end=2633
  _CRASHINFO._serialized_start=2636
  _CRASHINFO._serialized_end=2826
  _CRASHMETADATA._serialized_start=2828
  _CRASHMETADATA._serialized_end=2870
  _CRASHBLOB._serialized_start=2872
  _CRASHBLOB._serialized_end=2928
  _CHROMEOSIMAGE._serialized_start=2930
  _CHROMEOSIMAGE._serialized_end=2985
  _FAKEOMAHA._serialized_start=2988
  _FAKEOMAHA._serialized_end=3414
  _FAKEOMAHA_PAYLOAD._serialized_start=3272
  _FAKEOMAHA_PAYLOAD._serialized_end=3414
  _FAKEOMAHA_PAYLOAD_TYPE._serialized_start=3365
  _FAKEOMAHA_PAYLOAD_TYPE._serialized_end=3414
  _CREATEFAKEOMAHAREQUEST._serialized_start=3416
  _CREATEFAKEOMAHAREQUEST._serialized_end=3503
  _DELETEFAKEOMAHAREQUEST._serialized_start=3505
  _DELETEFAKEOMAHAREQUEST._serialized_end=3543
  _COMMON._serialized_start=3592
  _COMMON._serialized_end=4536
# @@protoc_insertion_point(module_scope)
