# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/cros_tool_runner_container_service_templates.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.test.api import cros_provision_cli_pb2 as chromiumos_dot_test_dot_api_dot_cros__provision__cli__pb2
from chromite.api.gen_sdk.chromiumos.test.lab.api import ip_endpoint_pb2 as chromiumos_dot_test_dot_lab_dot_api_dot_ip__endpoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFchromiumos/test/api/cros_tool_runner_container_service_templates.proto\x12\x13\x63hromiumos.test.api\x1a,chromiumos/test/api/cros_provision_cli.proto\x1a)chromiumos/test/lab/api/ip_endpoint.proto\"\xa8\x03\n\x08Template\x12\x38\n\x08\x63ros_dut\x18\x01 \x01(\x0b\x32$.chromiumos.test.api.CrosDutTemplateH\x00\x12\x44\n\x0e\x63ros_provision\x18\x02 \x01(\x0b\x32*.chromiumos.test.api.CrosProvisionTemplateH\x00\x12:\n\tcros_test\x18\x03 \x01(\x0b\x32%.chromiumos.test.api.CrosTestTemplateH\x00\x12@\n\x0c\x63ros_publish\x18\x04 \x01(\x0b\x32(.chromiumos.test.api.CrosPublishTemplateH\x00\x12O\n\x11\x63ros_fw_provision\x18\x05 \x01(\x0b\x32\x32.chromiumos.test.api.CrosFirmwareProvisionTemplateH\x00\x12@\n\x0c\x63\x61\x63he_server\x18\x06 \x01(\x0b\x32(.chromiumos.test.api.CacheServerTemplateH\x00\x42\x0b\n\tcontainer\"\x92\x01\n\x0f\x43rosDutTemplate\x12\x39\n\x0c\x63\x61\x63he_server\x18\x03 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\x12\x38\n\x0b\x64ut_address\x18\x04 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpointJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"e\n\x15\x43rosProvisionTemplate\x12@\n\rinput_request\x18\x03 \x01(\x0b\x32).chromiumos.test.api.CrosProvisionRequestJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"\x1e\n\x10\x43rosTestTemplateJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03\"\x15\n\x13\x43\x61\x63heServerTemplate\"\xd5\x01\n\x13\x43rosPublishTemplate\x12J\n\x0cpublish_type\x18\x01 \x01(\x0e\x32\x34.chromiumos.test.api.CrosPublishTemplate.PublishType\x12\x17\n\x0fpublish_src_dir\x18\x02 \x01(\t\"Y\n\x0bPublishType\x12\x17\n\x13PUBLISH_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPUBLISH_GCS\x10\x01\x12\x0f\n\x0bPUBLISH_TKO\x10\x02\x12\x0f\n\x0bPUBLISH_RDB\x10\x03\"\x1f\n\x1d\x43rosFirmwareProvisionTemplateB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3')



_TEMPLATE = DESCRIPTOR.message_types_by_name['Template']
_CROSDUTTEMPLATE = DESCRIPTOR.message_types_by_name['CrosDutTemplate']
_CROSPROVISIONTEMPLATE = DESCRIPTOR.message_types_by_name['CrosProvisionTemplate']
_CROSTESTTEMPLATE = DESCRIPTOR.message_types_by_name['CrosTestTemplate']
_CACHESERVERTEMPLATE = DESCRIPTOR.message_types_by_name['CacheServerTemplate']
_CROSPUBLISHTEMPLATE = DESCRIPTOR.message_types_by_name['CrosPublishTemplate']
_CROSFIRMWAREPROVISIONTEMPLATE = DESCRIPTOR.message_types_by_name['CrosFirmwareProvisionTemplate']
_CROSPUBLISHTEMPLATE_PUBLISHTYPE = _CROSPUBLISHTEMPLATE.enum_types_by_name['PublishType']
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

CacheServerTemplate = _reflection.GeneratedProtocolMessageType('CacheServerTemplate', (_message.Message,), {
  'DESCRIPTOR' : _CACHESERVERTEMPLATE,
  '__module__' : 'chromiumos.test.api.cros_tool_runner_container_service_templates_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.CacheServerTemplate)
  })
_sym_db.RegisterMessage(CacheServerTemplate)

CrosPublishTemplate = _reflection.GeneratedProtocolMessageType('CrosPublishTemplate', (_message.Message,), {
  'DESCRIPTOR' : _CROSPUBLISHTEMPLATE,
  '__module__' : 'chromiumos.test.api.cros_tool_runner_container_service_templates_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.CrosPublishTemplate)
  })
_sym_db.RegisterMessage(CrosPublishTemplate)

CrosFirmwareProvisionTemplate = _reflection.GeneratedProtocolMessageType('CrosFirmwareProvisionTemplate', (_message.Message,), {
  'DESCRIPTOR' : _CROSFIRMWAREPROVISIONTEMPLATE,
  '__module__' : 'chromiumos.test.api.cros_tool_runner_container_service_templates_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.test.api.CrosFirmwareProvisionTemplate)
  })
_sym_db.RegisterMessage(CrosFirmwareProvisionTemplate)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-go.chromium.org/chromiumos/config/go/test/api'
  _TEMPLATE._serialized_start=185
  _TEMPLATE._serialized_end=609
  _CROSDUTTEMPLATE._serialized_start=612
  _CROSDUTTEMPLATE._serialized_end=758
  _CROSPROVISIONTEMPLATE._serialized_start=760
  _CROSPROVISIONTEMPLATE._serialized_end=861
  _CROSTESTTEMPLATE._serialized_start=863
  _CROSTESTTEMPLATE._serialized_end=893
  _CACHESERVERTEMPLATE._serialized_start=895
  _CACHESERVERTEMPLATE._serialized_end=916
  _CROSPUBLISHTEMPLATE._serialized_start=919
  _CROSPUBLISHTEMPLATE._serialized_end=1132
  _CROSPUBLISHTEMPLATE_PUBLISHTYPE._serialized_start=1043
  _CROSPUBLISHTEMPLATE_PUBLISHTYPE._serialized_end=1132
  _CROSFIRMWAREPROVISIONTEMPLATE._serialized_start=1134
  _CROSFIRMWAREPROVISIONTEMPLATE._serialized_end=1165
# @@protoc_insertion_point(module_scope)
