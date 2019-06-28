# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromite/api/api.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=_b('Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api'),
  serialized_pb=_b('\n\x16\x63hromite/api/api.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\"\x12\n\x10MethodGetRequest\"f\n\x11MethodGetResponse\x12\x37\n\x07methods\x18\x01 \x03(\x0b\x32&.chromite.api.MethodGetResponse.Method\x1a\x18\n\x06Method\x12\x0e\n\x06method\x18\x01 \x01(\t\"\x13\n\x11VersionGetRequest\"\x85\x01\n\x12VersionGetResponse\x12\x39\n\x07version\x18\x01 \x01(\x0b\x32(.chromite.api.VersionGetResponse.Version\x1a\x34\n\x07Version\x12\r\n\x05major\x18\x01 \x01(\x05\x12\r\n\x05minor\x18\x02 \x01(\x05\x12\x0b\n\x03\x62ug\x18\x03 \x01(\x05\x32v\n\rMethodService\x12X\n\x03Get\x12\x1e.chromite.api.MethodGetRequest\x1a\x1f.chromite.api.MethodGetResponse\"\x10\xc2\xed\x1a\x0c\n\nGetMethods\x1a\x0b\xc2\xed\x1a\x07\n\x03\x61pi\x10\x02\x32y\n\x0eVersionService\x12Z\n\x03Get\x12\x1f.chromite.api.VersionGetRequest\x1a .chromite.api.VersionGetResponse\"\x10\xc2\xed\x1a\x0c\n\nGetVersion\x1a\x0b\xc2\xed\x1a\x07\n\x03\x61pi\x10\x02\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3')
  ,
  dependencies=[chromite_dot_api_dot_build__api__pb2.DESCRIPTOR,])




_METHODGETREQUEST = _descriptor.Descriptor(
  name='MethodGetRequest',
  full_name='chromite.api.MethodGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=70,
  serialized_end=88,
)


_METHODGETRESPONSE_METHOD = _descriptor.Descriptor(
  name='Method',
  full_name='chromite.api.MethodGetResponse.Method',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='chromite.api.MethodGetResponse.Method.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=168,
  serialized_end=192,
)

_METHODGETRESPONSE = _descriptor.Descriptor(
  name='MethodGetResponse',
  full_name='chromite.api.MethodGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='methods', full_name='chromite.api.MethodGetResponse.methods', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_METHODGETRESPONSE_METHOD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=192,
)


_VERSIONGETREQUEST = _descriptor.Descriptor(
  name='VersionGetRequest',
  full_name='chromite.api.VersionGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=194,
  serialized_end=213,
)


_VERSIONGETRESPONSE_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='chromite.api.VersionGetResponse.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='chromite.api.VersionGetResponse.Version.major', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor', full_name='chromite.api.VersionGetResponse.Version.minor', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bug', full_name='chromite.api.VersionGetResponse.Version.bug', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=297,
  serialized_end=349,
)

_VERSIONGETRESPONSE = _descriptor.Descriptor(
  name='VersionGetResponse',
  full_name='chromite.api.VersionGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='chromite.api.VersionGetResponse.version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VERSIONGETRESPONSE_VERSION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=349,
)

_METHODGETRESPONSE_METHOD.containing_type = _METHODGETRESPONSE
_METHODGETRESPONSE.fields_by_name['methods'].message_type = _METHODGETRESPONSE_METHOD
_VERSIONGETRESPONSE_VERSION.containing_type = _VERSIONGETRESPONSE
_VERSIONGETRESPONSE.fields_by_name['version'].message_type = _VERSIONGETRESPONSE_VERSION
DESCRIPTOR.message_types_by_name['MethodGetRequest'] = _METHODGETREQUEST
DESCRIPTOR.message_types_by_name['MethodGetResponse'] = _METHODGETRESPONSE
DESCRIPTOR.message_types_by_name['VersionGetRequest'] = _VERSIONGETREQUEST
DESCRIPTOR.message_types_by_name['VersionGetResponse'] = _VERSIONGETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MethodGetRequest = _reflection.GeneratedProtocolMessageType('MethodGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _METHODGETREQUEST,
  __module__ = 'chromite.api.api_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.MethodGetRequest)
  ))
_sym_db.RegisterMessage(MethodGetRequest)

MethodGetResponse = _reflection.GeneratedProtocolMessageType('MethodGetResponse', (_message.Message,), dict(

  Method = _reflection.GeneratedProtocolMessageType('Method', (_message.Message,), dict(
    DESCRIPTOR = _METHODGETRESPONSE_METHOD,
    __module__ = 'chromite.api.api_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.MethodGetResponse.Method)
    ))
  ,
  DESCRIPTOR = _METHODGETRESPONSE,
  __module__ = 'chromite.api.api_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.MethodGetResponse)
  ))
_sym_db.RegisterMessage(MethodGetResponse)
_sym_db.RegisterMessage(MethodGetResponse.Method)

VersionGetRequest = _reflection.GeneratedProtocolMessageType('VersionGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _VERSIONGETREQUEST,
  __module__ = 'chromite.api.api_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.VersionGetRequest)
  ))
_sym_db.RegisterMessage(VersionGetRequest)

VersionGetResponse = _reflection.GeneratedProtocolMessageType('VersionGetResponse', (_message.Message,), dict(

  Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), dict(
    DESCRIPTOR = _VERSIONGETRESPONSE_VERSION,
    __module__ = 'chromite.api.api_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.VersionGetResponse.Version)
    ))
  ,
  DESCRIPTOR = _VERSIONGETRESPONSE,
  __module__ = 'chromite.api.api_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.VersionGetResponse)
  ))
_sym_db.RegisterMessage(VersionGetResponse)
_sym_db.RegisterMessage(VersionGetResponse.Version)


DESCRIPTOR._options = None

_METHODSERVICE = _descriptor.ServiceDescriptor(
  name='MethodService',
  full_name='chromite.api.MethodService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\302\355\032\007\n\003api\020\002'),
  serialized_start=351,
  serialized_end=469,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='chromite.api.MethodService.Get',
    index=0,
    containing_service=None,
    input_type=_METHODGETREQUEST,
    output_type=_METHODGETRESPONSE,
    serialized_options=_b('\302\355\032\014\n\nGetMethods'),
  ),
])
_sym_db.RegisterServiceDescriptor(_METHODSERVICE)

DESCRIPTOR.services_by_name['MethodService'] = _METHODSERVICE


_VERSIONSERVICE = _descriptor.ServiceDescriptor(
  name='VersionService',
  full_name='chromite.api.VersionService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=_b('\302\355\032\007\n\003api\020\002'),
  serialized_start=471,
  serialized_end=592,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='chromite.api.VersionService.Get',
    index=0,
    containing_service=None,
    input_type=_VERSIONGETREQUEST,
    output_type=_VERSIONGETRESPONSE,
    serialized_options=_b('\302\355\032\014\n\nGetVersion'),
  ),
])
_sym_db.RegisterServiceDescriptor(_VERSIONSERVICE)

DESCRIPTOR.services_by_name['VersionService'] = _VERSIONSERVICE

# @@protoc_insertion_point(module_scope)
