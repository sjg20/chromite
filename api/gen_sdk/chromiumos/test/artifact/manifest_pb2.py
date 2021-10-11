# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/artifact/manifest.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/test/artifact/manifest.proto',
  package='chromiumos.test.artifact',
  syntax='proto3',
  serialized_options=b'Z2go.chromium.org/chromiumos/config/go/test/artifact',
  serialized_pb=b'\n\'chromiumos/test/artifact/manifest.proto\x12\x18\x63hromiumos.test.artifact\"R\n\x08Manifest\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x35\n\tartifacts\x18\x02 \x03(\x0b\x32\".chromiumos.test.artifact.Artifact\"\x99\x01\n\x08\x41rtifact\x12=\n\x04type\x18\x01 \x01(\x0e\x32/.chromiumos.test.artifact.Artifact.ArtifactType\x12\x0e\n\x06gs_url\x18\x02 \x01(\t\">\n\x0c\x41rtifactType\x12\x1d\n\x19\x41RTIFACT_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bTEST_RESULT\x10\x01\x42\x34Z2go.chromium.org/chromiumos/config/go/test/artifactb\x06proto3'
)



_ARTIFACT_ARTIFACTTYPE = _descriptor.EnumDescriptor(
  name='ArtifactType',
  full_name='chromiumos.test.artifact.Artifact.ArtifactType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ARTIFACT_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEST_RESULT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=245,
  serialized_end=307,
)
_sym_db.RegisterEnumDescriptor(_ARTIFACT_ARTIFACTTYPE)


_MANIFEST = _descriptor.Descriptor(
  name='Manifest',
  full_name='chromiumos.test.artifact.Manifest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='chromiumos.test.artifact.Manifest.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifacts', full_name='chromiumos.test.artifact.Manifest.artifacts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=151,
)


_ARTIFACT = _descriptor.Descriptor(
  name='Artifact',
  full_name='chromiumos.test.artifact.Artifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='chromiumos.test.artifact.Artifact.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gs_url', full_name='chromiumos.test.artifact.Artifact.gs_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ARTIFACT_ARTIFACTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=307,
)

_MANIFEST.fields_by_name['artifacts'].message_type = _ARTIFACT
_ARTIFACT.fields_by_name['type'].enum_type = _ARTIFACT_ARTIFACTTYPE
_ARTIFACT_ARTIFACTTYPE.containing_type = _ARTIFACT
DESCRIPTOR.message_types_by_name['Manifest'] = _MANIFEST
DESCRIPTOR.message_types_by_name['Artifact'] = _ARTIFACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Manifest = _reflection.GeneratedProtocolMessageType('Manifest', (_message.Message,), {
  'DESCRIPTOR' : _MANIFEST,
  '__module__' : 'chromiumos.test.artifact.manifest_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.Manifest)
  })
_sym_db.RegisterMessage(Manifest)

Artifact = _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), {
  'DESCRIPTOR' : _ARTIFACT,
  '__module__' : 'chromiumos.test.artifact.manifest_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.artifact.Artifact)
  })
_sym_db.RegisterMessage(Artifact)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
