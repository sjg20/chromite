# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/software/camera_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2chromiumos/config/api/software/camera_config.proto\x12\x1e\x63hromiumos.config.api.software\"+\n\nResolution\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\"\x97\x01\n\x0c\x43\x61meraConfig\x12\x1f\n\x17generate_media_profiles\x18\x01 \x01(\x08\x12I\n\x15\x63\x61mcorder_resolutions\x18\x02 \x03(\x0b\x32*.chromiumos.config.api.software.Resolution\x12\x1b\n\x13has_external_camera\x18\x03 \x01(\x08\x42\x33Z1go.chromium.org/chromiumos/config/go/api/softwareb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.config.api.software.camera_config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1go.chromium.org/chromiumos/config/go/api/software'
  _RESOLUTION._serialized_start=86
  _RESOLUTION._serialized_end=129
  _CAMERACONFIG._serialized_start=132
  _CAMERACONFIG._serialized_end=283
# @@protoc_insertion_point(module_scope)
