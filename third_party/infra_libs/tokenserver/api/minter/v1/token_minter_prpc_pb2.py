# Generated by the pRPC protocol buffer compiler plugin.  DO NOT EDIT!
# source: go.chromium.org/luci/tokenserver/api/minter/v1/token_minter.proto

import base64
import zlib

from chromite.third_party.google.protobuf import descriptor_pb2

# Includes description of the go.chromium.org/luci/tokenserver/api/minter/v1/token_minter.proto and all of its transitive
# dependencies. Includes source code info.
FILE_DESCRIPTOR_SET = descriptor_pb2.FileDescriptorSet()
FILE_DESCRIPTOR_SET.ParseFromString(zlib.decompress(base64.b64decode(
    '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'
    '/WwTQ=')))
_INDEX = {
    f.name: {
      'descriptor': f,
      'services': {s.name: s for s in f.service},
    }
    for f in FILE_DESCRIPTOR_SET.file
}


TokenMinterServiceDescription = {
  'file_descriptor_set': FILE_DESCRIPTOR_SET,
  'file_descriptor': _INDEX[u'go.chromium.org/luci/tokenserver/api/minter/v1/token_minter.proto']['descriptor'],
  'service_descriptor': _INDEX[u'go.chromium.org/luci/tokenserver/api/minter/v1/token_minter.proto']['services'][u'TokenMinter'],
}
