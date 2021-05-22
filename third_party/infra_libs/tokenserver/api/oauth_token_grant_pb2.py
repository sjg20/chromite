# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: go.chromium.org/luci/tokenserver/api/oauth_token_grant.proto

from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.third_party.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='go.chromium.org/luci/tokenserver/api/oauth_token_grant.proto',
  package='tokenserver',
  syntax='proto3',
  serialized_options=b'Z0go.chromium.org/luci/tokenserver/api;tokenserver',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<go.chromium.org/luci/tokenserver/api/oauth_token_grant.proto\x12\x0btokenserver\x1a\x1fgoogle/protobuf/timestamp.proto\"\xab\x01\n\x13OAuthTokenGrantBody\x12\x10\n\x08token_id\x18\x01 \x01(\x03\x12\x17\n\x0fservice_account\x18\x02 \x01(\t\x12\r\n\x05proxy\x18\x03 \x01(\t\x12\x10\n\x08\x65nd_user\x18\x04 \x01(\t\x12-\n\tissued_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x11validity_duration\x18\x06 \x01(\x03\"W\n\x17OAuthTokenGrantEnvelope\x12\x12\n\ntoken_body\x18\x01 \x01(\x0c\x12\x0e\n\x06key_id\x18\x02 \x01(\t\x12\x18\n\x10pkcs1_sha256_sig\x18\x03 \x01(\x0c\x42\x32Z0go.chromium.org/luci/tokenserver/api;tokenserverb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_OAUTHTOKENGRANTBODY = _descriptor.Descriptor(
  name='OAuthTokenGrantBody',
  full_name='tokenserver.OAuthTokenGrantBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token_id', full_name='tokenserver.OAuthTokenGrantBody.token_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account', full_name='tokenserver.OAuthTokenGrantBody.service_account', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxy', full_name='tokenserver.OAuthTokenGrantBody.proxy', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_user', full_name='tokenserver.OAuthTokenGrantBody.end_user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issued_at', full_name='tokenserver.OAuthTokenGrantBody.issued_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validity_duration', full_name='tokenserver.OAuthTokenGrantBody.validity_duration', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=111,
  serialized_end=282,
)


_OAUTHTOKENGRANTENVELOPE = _descriptor.Descriptor(
  name='OAuthTokenGrantEnvelope',
  full_name='tokenserver.OAuthTokenGrantEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token_body', full_name='tokenserver.OAuthTokenGrantEnvelope.token_body', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_id', full_name='tokenserver.OAuthTokenGrantEnvelope.key_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pkcs1_sha256_sig', full_name='tokenserver.OAuthTokenGrantEnvelope.pkcs1_sha256_sig', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=284,
  serialized_end=371,
)

_OAUTHTOKENGRANTBODY.fields_by_name['issued_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['OAuthTokenGrantBody'] = _OAUTHTOKENGRANTBODY
DESCRIPTOR.message_types_by_name['OAuthTokenGrantEnvelope'] = _OAUTHTOKENGRANTENVELOPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OAuthTokenGrantBody = _reflection.GeneratedProtocolMessageType('OAuthTokenGrantBody', (_message.Message,), {
  'DESCRIPTOR' : _OAUTHTOKENGRANTBODY,
  '__module__' : 'go.chromium.org.luci.tokenserver.api.oauth_token_grant_pb2'
  # @@protoc_insertion_point(class_scope:tokenserver.OAuthTokenGrantBody)
  })
_sym_db.RegisterMessage(OAuthTokenGrantBody)

OAuthTokenGrantEnvelope = _reflection.GeneratedProtocolMessageType('OAuthTokenGrantEnvelope', (_message.Message,), {
  'DESCRIPTOR' : _OAUTHTOKENGRANTENVELOPE,
  '__module__' : 'go.chromium.org.luci.tokenserver.api.oauth_token_grant_pb2'
  # @@protoc_insertion_point(class_scope:tokenserver.OAuthTokenGrantEnvelope)
  })
_sym_db.RegisterMessage(OAuthTokenGrantEnvelope)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
