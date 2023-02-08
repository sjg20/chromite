# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/cros_tool_runner_container_service_templates.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.test.api import cros_provision_cli_pb2 as chromiumos_dot_test_dot_api_dot_cros__provision__cli__pb2
from chromite.api.gen_sdk.chromiumos.test.lab.api import ip_endpoint_pb2 as chromiumos_dot_test_dot_lab_dot_api_dot_ip__endpoint__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromiumos/test/api/cros_tool_runner_container_service_templates.proto',
  package='chromiumos.test.api',
  syntax='proto3',
  serialized_options=b'Z-go.chromium.org/chromiumos/config/go/test/api',
  serialized_pb=b'\nFchromiumos/test/api/cros_tool_runner_container_service_templates.proto\x12\x13\x63hromiumos.test.api\x1a,chromiumos/test/api/cros_provision_cli.proto\x1a)chromiumos/test/lab/api/ip_endpoint.proto\"\xd3\x01\n\x08Template\x12\x38\n\x08\x63ros_dut\x18\x01 \x01(\x0b\x32$.chromiumos.test.api.CrosDutTemplateH\x00\x12\x44\n\x0e\x63ros_provision\x18\x02 \x01(\x0b\x32*.chromiumos.test.api.CrosProvisionTemplateH\x00\x12:\n\tcros_test\x18\x03 \x01(\x0b\x32%.chromiumos.test.api.CrosTestTemplateH\x00\x42\x0b\n\tcontainer\"\xad\x01\n\x0f\x43rosDutTemplate\x12\x0f\n\x07network\x18\x01 \x01(\t\x12\x14\n\x0c\x61rtifact_dir\x18\x02 \x01(\t\x12\x39\n\x0c\x63\x61\x63he_server\x18\x03 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\x12\x38\n\x0b\x64ut_address\x18\x04 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\"\x80\x01\n\x15\x43rosProvisionTemplate\x12\x0f\n\x07network\x18\x01 \x01(\t\x12\x14\n\x0c\x61rtifact_dir\x18\x02 \x01(\t\x12@\n\rinput_request\x18\x03 \x01(\x0b\x32).chromiumos.test.api.CrosProvisionRequest\"9\n\x10\x43rosTestTemplate\x12\x0f\n\x07network\x18\x01 \x01(\t\x12\x14\n\x0c\x61rtifact_dir\x18\x02 \x01(\tB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3'
  ,
  dependencies=[chromiumos_dot_test_dot_api_dot_cros__provision__cli__pb2.DESCRIPTOR,chromiumos_dot_test_dot_lab_dot_api_dot_ip__endpoint__pb2.DESCRIPTOR,])




_TEMPLATE = _descriptor.Descriptor(
  name='Template',
  full_name='chromiumos.test.api.Template',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cros_dut', full_name='chromiumos.test.api.Template.cros_dut', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cros_provision', full_name='chromiumos.test.api.Template.cros_provision', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cros_test', full_name='chromiumos.test.api.Template.cros_test', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='container', full_name='chromiumos.test.api.Template.container',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=185,
  serialized_end=396,
)


_CROSDUTTEMPLATE = _descriptor.Descriptor(
  name='CrosDutTemplate',
  full_name='chromiumos.test.api.CrosDutTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network', full_name='chromiumos.test.api.CrosDutTemplate.network', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifact_dir', full_name='chromiumos.test.api.CrosDutTemplate.artifact_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cache_server', full_name='chromiumos.test.api.CrosDutTemplate.cache_server', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dut_address', full_name='chromiumos.test.api.CrosDutTemplate.dut_address', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=399,
  serialized_end=572,
)


_CROSPROVISIONTEMPLATE = _descriptor.Descriptor(
  name='CrosProvisionTemplate',
  full_name='chromiumos.test.api.CrosProvisionTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network', full_name='chromiumos.test.api.CrosProvisionTemplate.network', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifact_dir', full_name='chromiumos.test.api.CrosProvisionTemplate.artifact_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_request', full_name='chromiumos.test.api.CrosProvisionTemplate.input_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=575,
  serialized_end=703,
)


_CROSTESTTEMPLATE = _descriptor.Descriptor(
  name='CrosTestTemplate',
  full_name='chromiumos.test.api.CrosTestTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network', full_name='chromiumos.test.api.CrosTestTemplate.network', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifact_dir', full_name='chromiumos.test.api.CrosTestTemplate.artifact_dir', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=705,
  serialized_end=762,
)

_TEMPLATE.fields_by_name['cros_dut'].message_type = _CROSDUTTEMPLATE
_TEMPLATE.fields_by_name['cros_provision'].message_type = _CROSPROVISIONTEMPLATE
_TEMPLATE.fields_by_name['cros_test'].message_type = _CROSTESTTEMPLATE
_TEMPLATE.oneofs_by_name['container'].fields.append(
  _TEMPLATE.fields_by_name['cros_dut'])
_TEMPLATE.fields_by_name['cros_dut'].containing_oneof = _TEMPLATE.oneofs_by_name['container']
_TEMPLATE.oneofs_by_name['container'].fields.append(
  _TEMPLATE.fields_by_name['cros_provision'])
_TEMPLATE.fields_by_name['cros_provision'].containing_oneof = _TEMPLATE.oneofs_by_name['container']
_TEMPLATE.oneofs_by_name['container'].fields.append(
  _TEMPLATE.fields_by_name['cros_test'])
_TEMPLATE.fields_by_name['cros_test'].containing_oneof = _TEMPLATE.oneofs_by_name['container']
_CROSDUTTEMPLATE.fields_by_name['cache_server'].message_type = chromiumos_dot_test_dot_lab_dot_api_dot_ip__endpoint__pb2._IPENDPOINT
_CROSDUTTEMPLATE.fields_by_name['dut_address'].message_type = chromiumos_dot_test_dot_lab_dot_api_dot_ip__endpoint__pb2._IPENDPOINT
_CROSPROVISIONTEMPLATE.fields_by_name['input_request'].message_type = chromiumos_dot_test_dot_api_dot_cros__provision__cli__pb2._CROSPROVISIONREQUEST
DESCRIPTOR.message_types_by_name['Template'] = _TEMPLATE
DESCRIPTOR.message_types_by_name['CrosDutTemplate'] = _CROSDUTTEMPLATE
DESCRIPTOR.message_types_by_name['CrosProvisionTemplate'] = _CROSPROVISIONTEMPLATE
DESCRIPTOR.message_types_by_name['CrosTestTemplate'] = _CROSTESTTEMPLATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Template = _reflection.GeneratedProtocolMessageType('Template', (_message.Message,), {
  'DESCRIPTOR' : _TEMPLATE,
  '__module__' : 'chromiumos.test.api.cros_tool_runner_container_service_templates_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.Template)
  })
_sym_db.RegisterMessage(Template)

CrosDutTemplate = _reflection.GeneratedProtocolMessageType('CrosDutTemplate', (_message.Message,), {
  'DESCRIPTOR' : _CROSDUTTEMPLATE,
  '__module__' : 'chromiumos.test.api.cros_tool_runner_container_service_templates_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.CrosDutTemplate)
  })
_sym_db.RegisterMessage(CrosDutTemplate)

CrosProvisionTemplate = _reflection.GeneratedProtocolMessageType('CrosProvisionTemplate', (_message.Message,), {
  'DESCRIPTOR' : _CROSPROVISIONTEMPLATE,
  '__module__' : 'chromiumos.test.api.cros_tool_runner_container_service_templates_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.CrosProvisionTemplate)
  })
_sym_db.RegisterMessage(CrosProvisionTemplate)

CrosTestTemplate = _reflection.GeneratedProtocolMessageType('CrosTestTemplate', (_message.Message,), {
  'DESCRIPTOR' : _CROSTESTTEMPLATE,
  '__module__' : 'chromiumos.test.api.cros_tool_runner_container_service_templates_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.CrosTestTemplate)
  })
_sym_db.RegisterMessage(CrosTestTemplate)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
