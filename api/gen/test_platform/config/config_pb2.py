# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/config/config.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import message as _message
from chromite.third_party.google.protobuf import reflection as _reflection
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.test_platform.migration.test_runner import config_pb2 as test__platform_dot_migration_dot_test__runner_dot_config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/config/config.proto',
  package='test_platform.config',
  syntax='proto3',
  serialized_options=b'Z>go.chromium.org/chromiumos/infra/proto/go/test_platform/config',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!test_platform/config/config.proto\x12\x14test_platform.config\x1a\x30test_platform/migration/test_runner/config.proto\"\xef\t\n\x06\x43onfig\x12>\n\x0fskylab_swarming\x18\x01 \x01(\x0b\x32%.test_platform.config.Config.Swarming\x12<\n\x0eskylab_isolate\x18\x03 \x01(\x0b\x32$.test_platform.config.Config.Isolate\x12@\n\rskylab_worker\x18\x04 \x01(\x0b\x32).test_platform.config.Config.SkylabWorker\x12;\n\nversioning\x18\x07 \x01(\x0b\x32\'.test_platform.config.Config.Versioning\x12<\n\x0btest_runner\x18\x08 \x01(\x0b\x32\'.test_platform.config.Config.TestRunner\x12J\n\x15test_runner_migration\x18\t \x01(\x0b\x32+.test_platform.migration.test_runner.Config\x12\x37\n\x06pubsub\x18\n \x01(\x0b\x32#.test_platform.config.Config.PubSubB\x02\x18\x01\x12@\n\x13result_flow_channel\x18\x0b \x01(\x0b\x32#.test_platform.config.Config.PubSub\x1a\x32\n\x08Swarming\x12\x0e\n\x06server\x18\x01 \x01(\t\x12\x16\n\x0e\x61uth_json_path\x18\x02 \x01(\t\x1a!\n\x07Isolate\x12\x16\n\x0e\x61uth_json_path\x18\x01 \x01(\t\x1a:\n\x0cSkylabWorker\x12\x14\n\x0cluci_project\x18\x01 \x01(\t\x12\x14\n\x0clog_dog_host\x18\x02 \x01(\t\x1a\x9d\x01\n\nVersioning\x12\x61\n\x19\x63ros_test_platform_binary\x18\x01 \x01(\x0b\x32>.test_platform.config.Config.Versioning.CrosTestPlatformBinary\x1a,\n\x16\x43rosTestPlatformBinary\x12\x12\n\ncipd_label\x18\x01 \x01(\t\x1aM\n\x0b\x42uildbucket\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x0e\n\x06\x62ucket\x18\x03 \x01(\t\x12\x0f\n\x07\x62uilder\x18\x04 \x01(\t\x1a(\n\x06PubSub\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x1a\xa4\x02\n\nTestRunner\x12=\n\x0b\x62uildbucket\x18\x01 \x01(\x0b\x32(.test_platform.config.Config.Buildbucket\x12\x37\n\x06pubsub\x18\x02 \x01(\x0b\x32#.test_platform.config.Config.PubSubB\x02\x18\x01\x12@\n\x13result_flow_channel\x18\x03 \x01(\x0b\x32#.test_platform.config.Config.PubSub\x12\x45\n\x18\x62\x62_status_update_channel\x18\x04 \x01(\x0b\x32#.test_platform.config.Config.PubSub\x12\x15\n\rswarming_pool\x18\x05 \x01(\tJ\x04\x08\x02\x10\x03J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07\x42@Z>go.chromium.org/chromiumos/infra/proto/go/test_platform/configb\x06proto3'
  ,
  dependencies=[test__platform_dot_migration_dot_test__runner_dot_config__pb2.DESCRIPTOR,])




_CONFIG_SWARMING = _descriptor.Descriptor(
  name='Swarming',
  full_name='test_platform.config.Config.Swarming',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='test_platform.config.Config.Swarming.server', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auth_json_path', full_name='test_platform.config.Config.Swarming.auth_json_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=634,
  serialized_end=684,
)

_CONFIG_ISOLATE = _descriptor.Descriptor(
  name='Isolate',
  full_name='test_platform.config.Config.Isolate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_json_path', full_name='test_platform.config.Config.Isolate.auth_json_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=686,
  serialized_end=719,
)

_CONFIG_SKYLABWORKER = _descriptor.Descriptor(
  name='SkylabWorker',
  full_name='test_platform.config.Config.SkylabWorker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='luci_project', full_name='test_platform.config.Config.SkylabWorker.luci_project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log_dog_host', full_name='test_platform.config.Config.SkylabWorker.log_dog_host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=721,
  serialized_end=779,
)

_CONFIG_VERSIONING_CROSTESTPLATFORMBINARY = _descriptor.Descriptor(
  name='CrosTestPlatformBinary',
  full_name='test_platform.config.Config.Versioning.CrosTestPlatformBinary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cipd_label', full_name='test_platform.config.Config.Versioning.CrosTestPlatformBinary.cipd_label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=895,
  serialized_end=939,
)

_CONFIG_VERSIONING = _descriptor.Descriptor(
  name='Versioning',
  full_name='test_platform.config.Config.Versioning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cros_test_platform_binary', full_name='test_platform.config.Config.Versioning.cros_test_platform_binary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONFIG_VERSIONING_CROSTESTPLATFORMBINARY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=782,
  serialized_end=939,
)

_CONFIG_BUILDBUCKET = _descriptor.Descriptor(
  name='Buildbucket',
  full_name='test_platform.config.Config.Buildbucket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='test_platform.config.Config.Buildbucket.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project', full_name='test_platform.config.Config.Buildbucket.project', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='test_platform.config.Config.Buildbucket.bucket', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='builder', full_name='test_platform.config.Config.Buildbucket.builder', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=941,
  serialized_end=1018,
)

_CONFIG_PUBSUB = _descriptor.Descriptor(
  name='PubSub',
  full_name='test_platform.config.Config.PubSub',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='test_platform.config.Config.PubSub.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic', full_name='test_platform.config.Config.PubSub.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1020,
  serialized_end=1060,
)

_CONFIG_TESTRUNNER = _descriptor.Descriptor(
  name='TestRunner',
  full_name='test_platform.config.Config.TestRunner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buildbucket', full_name='test_platform.config.Config.TestRunner.buildbucket', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pubsub', full_name='test_platform.config.Config.TestRunner.pubsub', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_flow_channel', full_name='test_platform.config.Config.TestRunner.result_flow_channel', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bb_status_update_channel', full_name='test_platform.config.Config.TestRunner.bb_status_update_channel', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swarming_pool', full_name='test_platform.config.Config.TestRunner.swarming_pool', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1063,
  serialized_end=1355,
)

_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='test_platform.config.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='skylab_swarming', full_name='test_platform.config.Config.skylab_swarming', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skylab_isolate', full_name='test_platform.config.Config.skylab_isolate', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skylab_worker', full_name='test_platform.config.Config.skylab_worker', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='versioning', full_name='test_platform.config.Config.versioning', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_runner', full_name='test_platform.config.Config.test_runner', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_runner_migration', full_name='test_platform.config.Config.test_runner_migration', index=5,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pubsub', full_name='test_platform.config.Config.pubsub', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_flow_channel', full_name='test_platform.config.Config.result_flow_channel', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONFIG_SWARMING, _CONFIG_ISOLATE, _CONFIG_SKYLABWORKER, _CONFIG_VERSIONING, _CONFIG_BUILDBUCKET, _CONFIG_PUBSUB, _CONFIG_TESTRUNNER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=1373,
)

_CONFIG_SWARMING.containing_type = _CONFIG
_CONFIG_ISOLATE.containing_type = _CONFIG
_CONFIG_SKYLABWORKER.containing_type = _CONFIG
_CONFIG_VERSIONING_CROSTESTPLATFORMBINARY.containing_type = _CONFIG_VERSIONING
_CONFIG_VERSIONING.fields_by_name['cros_test_platform_binary'].message_type = _CONFIG_VERSIONING_CROSTESTPLATFORMBINARY
_CONFIG_VERSIONING.containing_type = _CONFIG
_CONFIG_BUILDBUCKET.containing_type = _CONFIG
_CONFIG_PUBSUB.containing_type = _CONFIG
_CONFIG_TESTRUNNER.fields_by_name['buildbucket'].message_type = _CONFIG_BUILDBUCKET
_CONFIG_TESTRUNNER.fields_by_name['pubsub'].message_type = _CONFIG_PUBSUB
_CONFIG_TESTRUNNER.fields_by_name['result_flow_channel'].message_type = _CONFIG_PUBSUB
_CONFIG_TESTRUNNER.fields_by_name['bb_status_update_channel'].message_type = _CONFIG_PUBSUB
_CONFIG_TESTRUNNER.containing_type = _CONFIG
_CONFIG.fields_by_name['skylab_swarming'].message_type = _CONFIG_SWARMING
_CONFIG.fields_by_name['skylab_isolate'].message_type = _CONFIG_ISOLATE
_CONFIG.fields_by_name['skylab_worker'].message_type = _CONFIG_SKYLABWORKER
_CONFIG.fields_by_name['versioning'].message_type = _CONFIG_VERSIONING
_CONFIG.fields_by_name['test_runner'].message_type = _CONFIG_TESTRUNNER
_CONFIG.fields_by_name['test_runner_migration'].message_type = test__platform_dot_migration_dot_test__runner_dot_config__pb2._CONFIG
_CONFIG.fields_by_name['pubsub'].message_type = _CONFIG_PUBSUB
_CONFIG.fields_by_name['result_flow_channel'].message_type = _CONFIG_PUBSUB
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {

  'Swarming' : _reflection.GeneratedProtocolMessageType('Swarming', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_SWARMING,
    '__module__' : 'test_platform.config.config_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.config.Config.Swarming)
    })
  ,

  'Isolate' : _reflection.GeneratedProtocolMessageType('Isolate', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_ISOLATE,
    '__module__' : 'test_platform.config.config_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.config.Config.Isolate)
    })
  ,

  'SkylabWorker' : _reflection.GeneratedProtocolMessageType('SkylabWorker', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_SKYLABWORKER,
    '__module__' : 'test_platform.config.config_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.config.Config.SkylabWorker)
    })
  ,

  'Versioning' : _reflection.GeneratedProtocolMessageType('Versioning', (_message.Message,), {

    'CrosTestPlatformBinary' : _reflection.GeneratedProtocolMessageType('CrosTestPlatformBinary', (_message.Message,), {
      'DESCRIPTOR' : _CONFIG_VERSIONING_CROSTESTPLATFORMBINARY,
      '__module__' : 'test_platform.config.config_pb2'
      # @@protoc_insertion_point(class_scope:test_platform.config.Config.Versioning.CrosTestPlatformBinary)
      })
    ,
    'DESCRIPTOR' : _CONFIG_VERSIONING,
    '__module__' : 'test_platform.config.config_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.config.Config.Versioning)
    })
  ,

  'Buildbucket' : _reflection.GeneratedProtocolMessageType('Buildbucket', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_BUILDBUCKET,
    '__module__' : 'test_platform.config.config_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.config.Config.Buildbucket)
    })
  ,

  'PubSub' : _reflection.GeneratedProtocolMessageType('PubSub', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_PUBSUB,
    '__module__' : 'test_platform.config.config_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.config.Config.PubSub)
    })
  ,

  'TestRunner' : _reflection.GeneratedProtocolMessageType('TestRunner', (_message.Message,), {
    'DESCRIPTOR' : _CONFIG_TESTRUNNER,
    '__module__' : 'test_platform.config.config_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.config.Config.TestRunner)
    })
  ,
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'test_platform.config.config_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.config.Config)
  })
_sym_db.RegisterMessage(Config)
_sym_db.RegisterMessage(Config.Swarming)
_sym_db.RegisterMessage(Config.Isolate)
_sym_db.RegisterMessage(Config.SkylabWorker)
_sym_db.RegisterMessage(Config.Versioning)
_sym_db.RegisterMessage(Config.Versioning.CrosTestPlatformBinary)
_sym_db.RegisterMessage(Config.Buildbucket)
_sym_db.RegisterMessage(Config.PubSub)
_sym_db.RegisterMessage(Config.TestRunner)


DESCRIPTOR._options = None
_CONFIG_TESTRUNNER.fields_by_name['pubsub']._options = None
_CONFIG.fields_by_name['pubsub']._options = None
# @@protoc_insertion_point(module_scope)
