# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen.chromite.api import image_pb2 as chromite_dot_api_dot_image__pb2
from chromite.api.gen.chromite.api import sysroot_pb2 as chromite_dot_api_dot_sysroot__pb2
from chromite.api.gen.chromiumos import common_pb2 as chromiumos_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chromite/api/test.proto',
  package='chromite.api',
  syntax='proto3',
  serialized_options=_b('Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api'),
  serialized_pb=_b('\n\x17\x63hromite/api/test.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x18\x63hromite/api/image.proto\x1a\x1a\x63hromite/api/sysroot.proto\x1a\x17\x63hromiumos/common.proto\"\x97\x02\n\x1a\x42uildTargetUnitTestRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\x13\n\x0bresult_path\x18\x02 \x01(\t\x12\"\n\x06\x63hroot\x18\x03 \x01(\x0b\x32\x12.chromiumos.Chroot\x12=\n\x05\x66lags\x18\x04 \x01(\x0b\x32..chromite.api.BuildTargetUnitTestRequest.Flags\x12\x32\n\x11package_blacklist\x18\x05 \x03(\x0b\x32\x17.chromiumos.PackageInfo\x1a\x1e\n\x05\x46lags\x12\x15\n\rempty_sysroot\x18\x01 \x01(\x08\"e\n\x1b\x42uildTargetUnitTestResponse\x12\x14\n\x0ctarball_path\x18\x01 \x01(\t\x12\x30\n\x0f\x66\x61iled_packages\x18\x02 \x03(\x0b\x32\x17.chromiumos.PackageInfo\"=\n\x17\x43hromiteUnitTestRequest\x12\"\n\x06\x63hroot\x18\x01 \x01(\x0b\x32\x12.chromiumos.Chroot\"\x1a\n\x18\x43hromiteUnitTestResponse\"b\n\x14\x44\x65\x62ugInfoTestRequest\x12&\n\x07sysroot\x18\x01 \x01(\x0b\x32\x15.chromite.api.Sysroot\x12\"\n\x06\x63hroot\x18\x02 \x01(\x0b\x32\x12.chromiumos.Chroot\"\x17\n\x15\x44\x65\x62ugInfoTestResponse\"\xc6\x03\n\rVmTestRequest\x12-\n\x0c\x62uild_target\x18\x01 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12\"\n\x06\x63hroot\x18\x02 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\'\n\x08vm_image\x18\x03 \x01(\x0b\x32\x15.chromite.api.VmImage\x12;\n\x0bssh_options\x18\x04 \x01(\x0b\x32&.chromite.api.VmTestRequest.SshOptions\x12=\n\x0ctest_harness\x18\x05 \x01(\x0e\x32\'.chromite.api.VmTestRequest.TestHarness\x12\x34\n\x08vm_tests\x18\x06 \x03(\x0b\x32\".chromite.api.VmTestRequest.VmTest\x1a\x34\n\nSshOptions\x12\x18\n\x10private_key_path\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x1a\x19\n\x06VmTest\x12\x0f\n\x07pattern\x18\x01 \x01(\t\"6\n\x0bTestHarness\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04TAST\x10\x01\x12\x0c\n\x08\x41UTOTEST\x10\x02\"\x10\n\x0eVmTestResponse2\x91\x03\n\x0bTestService\x12r\n\x13\x42uildTargetUnitTest\x12(.chromite.api.BuildTargetUnitTestRequest\x1a).chromite.api.BuildTargetUnitTestResponse\"\x06\xc2\xed\x1a\x02\x10\x02\x12\x61\n\x10\x43hromiteUnitTest\x12%.chromite.api.ChromiteUnitTestRequest\x1a&.chromite.api.ChromiteUnitTestResponse\x12X\n\rDebugInfoTest\x12\".chromite.api.DebugInfoTestRequest\x1a#.chromite.api.DebugInfoTestResponse\x12\x43\n\x06VmTest\x12\x1b.chromite.api.VmTestRequest\x1a\x1c.chromite.api.VmTestResponse\x1a\x0c\xc2\xed\x1a\x08\n\x04test\x10\x01\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3')
  ,
  dependencies=[chromite_dot_api_dot_build__api__pb2.DESCRIPTOR,chromite_dot_api_dot_image__pb2.DESCRIPTOR,chromite_dot_api_dot_sysroot__pb2.DESCRIPTOR,chromiumos_dot_common__pb2.DESCRIPTOR,])



_VMTESTREQUEST_TESTHARNESS = _descriptor.EnumDescriptor(
  name='TestHarness',
  full_name='chromite.api.VmTestRequest.TestHarness',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TAST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOTEST', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1152,
  serialized_end=1206,
)
_sym_db.RegisterEnumDescriptor(_VMTESTREQUEST_TESTHARNESS)


_BUILDTARGETUNITTESTREQUEST_FLAGS = _descriptor.Descriptor(
  name='Flags',
  full_name='chromite.api.BuildTargetUnitTestRequest.Flags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty_sysroot', full_name='chromite.api.BuildTargetUnitTestRequest.Flags.empty_sysroot', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=400,
  serialized_end=430,
)

_BUILDTARGETUNITTESTREQUEST = _descriptor.Descriptor(
  name='BuildTargetUnitTestRequest',
  full_name='chromite.api.BuildTargetUnitTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_target', full_name='chromite.api.BuildTargetUnitTestRequest.build_target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_path', full_name='chromite.api.BuildTargetUnitTestRequest.result_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.BuildTargetUnitTestRequest.chroot', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='chromite.api.BuildTargetUnitTestRequest.flags', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_blacklist', full_name='chromite.api.BuildTargetUnitTestRequest.package_blacklist', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BUILDTARGETUNITTESTREQUEST_FLAGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=430,
)


_BUILDTARGETUNITTESTRESPONSE = _descriptor.Descriptor(
  name='BuildTargetUnitTestResponse',
  full_name='chromite.api.BuildTargetUnitTestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tarball_path', full_name='chromite.api.BuildTargetUnitTestResponse.tarball_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failed_packages', full_name='chromite.api.BuildTargetUnitTestResponse.failed_packages', index=1,
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
  serialized_start=432,
  serialized_end=533,
)


_CHROMITEUNITTESTREQUEST = _descriptor.Descriptor(
  name='ChromiteUnitTestRequest',
  full_name='chromite.api.ChromiteUnitTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.ChromiteUnitTestRequest.chroot', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=535,
  serialized_end=596,
)


_CHROMITEUNITTESTRESPONSE = _descriptor.Descriptor(
  name='ChromiteUnitTestResponse',
  full_name='chromite.api.ChromiteUnitTestResponse',
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
  serialized_start=598,
  serialized_end=624,
)


_DEBUGINFOTESTREQUEST = _descriptor.Descriptor(
  name='DebugInfoTestRequest',
  full_name='chromite.api.DebugInfoTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sysroot', full_name='chromite.api.DebugInfoTestRequest.sysroot', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.DebugInfoTestRequest.chroot', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=626,
  serialized_end=724,
)


_DEBUGINFOTESTRESPONSE = _descriptor.Descriptor(
  name='DebugInfoTestResponse',
  full_name='chromite.api.DebugInfoTestResponse',
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
  serialized_start=726,
  serialized_end=749,
)


_VMTESTREQUEST_SSHOPTIONS = _descriptor.Descriptor(
  name='SshOptions',
  full_name='chromite.api.VmTestRequest.SshOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='private_key_path', full_name='chromite.api.VmTestRequest.SshOptions.private_key_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='chromite.api.VmTestRequest.SshOptions.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=1071,
  serialized_end=1123,
)

_VMTESTREQUEST_VMTEST = _descriptor.Descriptor(
  name='VmTest',
  full_name='chromite.api.VmTestRequest.VmTest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pattern', full_name='chromite.api.VmTestRequest.VmTest.pattern', index=0,
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
  serialized_start=1125,
  serialized_end=1150,
)

_VMTESTREQUEST = _descriptor.Descriptor(
  name='VmTestRequest',
  full_name='chromite.api.VmTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_target', full_name='chromite.api.VmTestRequest.build_target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chroot', full_name='chromite.api.VmTestRequest.chroot', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vm_image', full_name='chromite.api.VmTestRequest.vm_image', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssh_options', full_name='chromite.api.VmTestRequest.ssh_options', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_harness', full_name='chromite.api.VmTestRequest.test_harness', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vm_tests', full_name='chromite.api.VmTestRequest.vm_tests', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VMTESTREQUEST_SSHOPTIONS, _VMTESTREQUEST_VMTEST, ],
  enum_types=[
    _VMTESTREQUEST_TESTHARNESS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=1206,
)


_VMTESTRESPONSE = _descriptor.Descriptor(
  name='VmTestResponse',
  full_name='chromite.api.VmTestResponse',
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
  serialized_start=1208,
  serialized_end=1224,
)

_BUILDTARGETUNITTESTREQUEST_FLAGS.containing_type = _BUILDTARGETUNITTESTREQUEST
_BUILDTARGETUNITTESTREQUEST.fields_by_name['build_target'].message_type = chromiumos_dot_common__pb2._BUILDTARGET
_BUILDTARGETUNITTESTREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_BUILDTARGETUNITTESTREQUEST.fields_by_name['flags'].message_type = _BUILDTARGETUNITTESTREQUEST_FLAGS
_BUILDTARGETUNITTESTREQUEST.fields_by_name['package_blacklist'].message_type = chromiumos_dot_common__pb2._PACKAGEINFO
_BUILDTARGETUNITTESTRESPONSE.fields_by_name['failed_packages'].message_type = chromiumos_dot_common__pb2._PACKAGEINFO
_CHROMITEUNITTESTREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_DEBUGINFOTESTREQUEST.fields_by_name['sysroot'].message_type = chromite_dot_api_dot_sysroot__pb2._SYSROOT
_DEBUGINFOTESTREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_VMTESTREQUEST_SSHOPTIONS.containing_type = _VMTESTREQUEST
_VMTESTREQUEST_VMTEST.containing_type = _VMTESTREQUEST
_VMTESTREQUEST.fields_by_name['build_target'].message_type = chromiumos_dot_common__pb2._BUILDTARGET
_VMTESTREQUEST.fields_by_name['chroot'].message_type = chromiumos_dot_common__pb2._CHROOT
_VMTESTREQUEST.fields_by_name['vm_image'].message_type = chromite_dot_api_dot_image__pb2._VMIMAGE
_VMTESTREQUEST.fields_by_name['ssh_options'].message_type = _VMTESTREQUEST_SSHOPTIONS
_VMTESTREQUEST.fields_by_name['test_harness'].enum_type = _VMTESTREQUEST_TESTHARNESS
_VMTESTREQUEST.fields_by_name['vm_tests'].message_type = _VMTESTREQUEST_VMTEST
_VMTESTREQUEST_TESTHARNESS.containing_type = _VMTESTREQUEST
DESCRIPTOR.message_types_by_name['BuildTargetUnitTestRequest'] = _BUILDTARGETUNITTESTREQUEST
DESCRIPTOR.message_types_by_name['BuildTargetUnitTestResponse'] = _BUILDTARGETUNITTESTRESPONSE
DESCRIPTOR.message_types_by_name['ChromiteUnitTestRequest'] = _CHROMITEUNITTESTREQUEST
DESCRIPTOR.message_types_by_name['ChromiteUnitTestResponse'] = _CHROMITEUNITTESTRESPONSE
DESCRIPTOR.message_types_by_name['DebugInfoTestRequest'] = _DEBUGINFOTESTREQUEST
DESCRIPTOR.message_types_by_name['DebugInfoTestResponse'] = _DEBUGINFOTESTRESPONSE
DESCRIPTOR.message_types_by_name['VmTestRequest'] = _VMTESTREQUEST
DESCRIPTOR.message_types_by_name['VmTestResponse'] = _VMTESTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildTargetUnitTestRequest = _reflection.GeneratedProtocolMessageType('BuildTargetUnitTestRequest', (_message.Message,), dict(

  Flags = _reflection.GeneratedProtocolMessageType('Flags', (_message.Message,), dict(
    DESCRIPTOR = _BUILDTARGETUNITTESTREQUEST_FLAGS,
    __module__ = 'chromite.api.test_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.BuildTargetUnitTestRequest.Flags)
    ))
  ,
  DESCRIPTOR = _BUILDTARGETUNITTESTREQUEST,
  __module__ = 'chromite.api.test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BuildTargetUnitTestRequest)
  ))
_sym_db.RegisterMessage(BuildTargetUnitTestRequest)
_sym_db.RegisterMessage(BuildTargetUnitTestRequest.Flags)

BuildTargetUnitTestResponse = _reflection.GeneratedProtocolMessageType('BuildTargetUnitTestResponse', (_message.Message,), dict(
  DESCRIPTOR = _BUILDTARGETUNITTESTRESPONSE,
  __module__ = 'chromite.api.test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.BuildTargetUnitTestResponse)
  ))
_sym_db.RegisterMessage(BuildTargetUnitTestResponse)

ChromiteUnitTestRequest = _reflection.GeneratedProtocolMessageType('ChromiteUnitTestRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHROMITEUNITTESTREQUEST,
  __module__ = 'chromite.api.test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.ChromiteUnitTestRequest)
  ))
_sym_db.RegisterMessage(ChromiteUnitTestRequest)

ChromiteUnitTestResponse = _reflection.GeneratedProtocolMessageType('ChromiteUnitTestResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHROMITEUNITTESTRESPONSE,
  __module__ = 'chromite.api.test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.ChromiteUnitTestResponse)
  ))
_sym_db.RegisterMessage(ChromiteUnitTestResponse)

DebugInfoTestRequest = _reflection.GeneratedProtocolMessageType('DebugInfoTestRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGINFOTESTREQUEST,
  __module__ = 'chromite.api.test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.DebugInfoTestRequest)
  ))
_sym_db.RegisterMessage(DebugInfoTestRequest)

DebugInfoTestResponse = _reflection.GeneratedProtocolMessageType('DebugInfoTestResponse', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGINFOTESTRESPONSE,
  __module__ = 'chromite.api.test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.DebugInfoTestResponse)
  ))
_sym_db.RegisterMessage(DebugInfoTestResponse)

VmTestRequest = _reflection.GeneratedProtocolMessageType('VmTestRequest', (_message.Message,), dict(

  SshOptions = _reflection.GeneratedProtocolMessageType('SshOptions', (_message.Message,), dict(
    DESCRIPTOR = _VMTESTREQUEST_SSHOPTIONS,
    __module__ = 'chromite.api.test_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.VmTestRequest.SshOptions)
    ))
  ,

  VmTest = _reflection.GeneratedProtocolMessageType('VmTest', (_message.Message,), dict(
    DESCRIPTOR = _VMTESTREQUEST_VMTEST,
    __module__ = 'chromite.api.test_pb2'
    # @@protoc_insertion_point(class_scope:chromite.api.VmTestRequest.VmTest)
    ))
  ,
  DESCRIPTOR = _VMTESTREQUEST,
  __module__ = 'chromite.api.test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.VmTestRequest)
  ))
_sym_db.RegisterMessage(VmTestRequest)
_sym_db.RegisterMessage(VmTestRequest.SshOptions)
_sym_db.RegisterMessage(VmTestRequest.VmTest)

VmTestResponse = _reflection.GeneratedProtocolMessageType('VmTestResponse', (_message.Message,), dict(
  DESCRIPTOR = _VMTESTRESPONSE,
  __module__ = 'chromite.api.test_pb2'
  # @@protoc_insertion_point(class_scope:chromite.api.VmTestResponse)
  ))
_sym_db.RegisterMessage(VmTestResponse)


DESCRIPTOR._options = None

_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='chromite.api.TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\302\355\032\010\n\004test\020\001'),
  serialized_start=1227,
  serialized_end=1628,
  methods=[
  _descriptor.MethodDescriptor(
    name='BuildTargetUnitTest',
    full_name='chromite.api.TestService.BuildTargetUnitTest',
    index=0,
    containing_service=None,
    input_type=_BUILDTARGETUNITTESTREQUEST,
    output_type=_BUILDTARGETUNITTESTRESPONSE,
    serialized_options=_b('\302\355\032\002\020\002'),
  ),
  _descriptor.MethodDescriptor(
    name='ChromiteUnitTest',
    full_name='chromite.api.TestService.ChromiteUnitTest',
    index=1,
    containing_service=None,
    input_type=_CHROMITEUNITTESTREQUEST,
    output_type=_CHROMITEUNITTESTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DebugInfoTest',
    full_name='chromite.api.TestService.DebugInfoTest',
    index=2,
    containing_service=None,
    input_type=_DEBUGINFOTESTREQUEST,
    output_type=_DEBUGINFOTESTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='VmTest',
    full_name='chromite.api.TestService.VmTest',
    index=3,
    containing_service=None,
    input_type=_VMTESTREQUEST,
    output_type=_VMTESTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)
