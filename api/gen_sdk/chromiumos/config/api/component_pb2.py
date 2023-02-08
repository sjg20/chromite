# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/config/api/component.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.config.api import component_id_pb2 as chromiumos_dot_config_dot_api_dot_component__id__pb2
from chromite.api.gen_sdk.chromiumos.config.api import partner_id_pb2 as chromiumos_dot_config_dot_api_dot_partner__id__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%chromiumos/config/api/component.proto\x12\x15\x63hromiumos.config.api\x1a(chromiumos/config/api/component_id.proto\x1a&chromiumos/config/api/partner_id.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x90\x31\n\tComponent\x12.\n\x02id\x18\x01 \x01(\x0b\x32\".chromiumos.config.api.ComponentId\x12\x39\n\x0fmanufacturer_id\x18\x08 \x01(\x0b\x32 .chromiumos.config.api.PartnerId\x12\x0c\n\x04name\x18\t \x01(\t\x12\x11\n\thwid_type\x18\x19 \x01(\t\x12\x12\n\nhwid_label\x18\x14 \x01(\t\x12\x36\n\x06\x61vl_id\x18\x15 \x01(\x0b\x32&.chromiumos.config.api.Component.AVLId\x12\x13\n\x0bpart_number\x18\x16 \x01(\t\x12\x46\n\x0esupport_status\x18\x1c \x01(\x0e\x32..chromiumos.config.api.Component.SupportStatus\x12\x33\n\x03soc\x18\x02 \x01(\x0b\x32$.chromiumos.config.api.Component.SocH\x00\x12\x39\n\x06memory\x18\x03 \x01(\x0b\x32\'.chromiumos.config.api.Component.MemoryH\x00\x12?\n\tbluetooth\x18\x04 \x01(\x0b\x32*.chromiumos.config.api.Component.BluetoothH\x00\x12\x39\n\x06\x63\x61mera\x18\x05 \x01(\x0b\x32\'.chromiumos.config.api.Component.CameraH\x00\x12=\n\x0btouchscreen\x18\x06 \x01(\x0b\x32&.chromiumos.config.api.Component.TouchH\x00\x12\x35\n\x04wifi\x18\x07 \x01(\x0b\x32%.chromiumos.config.api.Component.WifiH\x00\x12:\n\x08touchpad\x18\n \x01(\x0b\x32&.chromiumos.config.api.Component.TouchH\x00\x12\x46\n\rdisplay_panel\x18\x0b \x01(\x0b\x32-.chromiumos.config.api.Component.DisplayPanelH\x00\x12\x42\n\x0b\x61udio_codec\x18\x0c \x01(\x0b\x32+.chromiumos.config.api.Component.AudioCodecH\x00\x12;\n\x07\x62\x61ttery\x18\r \x01(\x0b\x32(.chromiumos.config.api.Component.BatteryH\x00\x12\x43\n\rec_flash_chip\x18\x0e \x01(\x0b\x32*.chromiumos.config.api.Component.FlashChipH\x00\x12G\n\x11system_flash_chip\x18\x0f \x01(\x0b\x32*.chromiumos.config.api.Component.FlashChipH\x00\x12\x41\n\x02\x65\x63\x18\x10 \x01(\x0b\x32\x33.chromiumos.config.api.Component.EmbeddedControllerH\x00\x12;\n\x07storage\x18\x11 \x01(\x0b\x32(.chromiumos.config.api.Component.StorageH\x00\x12\x33\n\x03tpm\x18\x12 \x01(\x0b\x32$.chromiumos.config.api.Component.TpmH\x00\x12\x42\n\x08usb_host\x18\x13 \x01(\x0b\x32..chromiumos.config.api.Component.Interface.UsbH\x00\x12\x39\n\x06stylus\x18\x17 \x01(\x0b\x32\'.chromiumos.config.api.Component.StylusH\x00\x12?\n\tamplifier\x18\x18 \x01(\x0b\x32*.chromiumos.config.api.Component.AmplifierH\x00\x12M\n\x0c\x64p_converter\x18\x1a \x01(\x0b\x32\x35.chromiumos.config.api.Component.DisplayPortConverterH\x00\x12=\n\x08\x63\x65llular\x18\x1b \x01(\x0b\x32).chromiumos.config.api.Component.CellularH\x00\x1a!\n\x05\x41VLId\x12\x0b\n\x03\x63id\x18\x01 \x01(\x05\x12\x0b\n\x03qid\x18\x02 \x01(\x05\x1a\xc9\x01\n\tInterface\x1a&\n\x03I2C\x12\x0f\n\x07product\x18\x01 \x01(\t\x12\x0e\n\x06vendor\x18\x02 \x01(\t\x1a@\n\x03Usb\x12\x11\n\tvendor_id\x18\x01 \x01(\t\x12\x12\n\nproduct_id\x18\x02 \x01(\t\x12\x12\n\nbcd_device\x18\x03 \x01(\t\x1aR\n\x03Pci\x12\x11\n\tvendor_id\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x13\n\x0brevision_id\x18\x03 \x01(\t\x12\x10\n\x08\x63lass_id\x18\x04 \x01(\t\x1a\x91\x04\n\x03Soc\x12;\n\x06\x66\x61mily\x18\x01 \x01(\x0b\x32+.chromiumos.config.api.Component.Soc.Family\x12\r\n\x05model\x18\x02 \x01(\t\x12\r\n\x05\x63ores\x18\x03 \x01(\x05\x12>\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0e\x32,.chromiumos.config.api.Component.Soc.Feature\x12K\n\x0fvulnerabilities\x18\x05 \x03(\x0e\x32\x32.chromiumos.config.api.Component.Soc.Vulnerability\x1aW\n\x06\x46\x61mily\x12?\n\x04\x61rch\x18\x01 \x01(\x0e\x32\x31.chromiumos.config.api.Component.Soc.Architecture\x12\x0c\n\x04name\x18\x02 \x01(\t\"S\n\x0c\x41rchitecture\x12\x1a\n\x16\x41RCHITECTURE_UNDEFINED\x10\x00\x12\x07\n\x03X86\x10\x01\x12\n\n\x06X86_64\x10\x02\x12\x07\n\x03\x41RM\x10\x03\x12\t\n\x05\x41RM64\x10\x04\"3\n\x07\x46\x65\x61ture\x12\x13\n\x0f\x46\x45\x41TURE_UNKNOWN\x10\x00\x12\x07\n\x03SMT\x10\x01\x12\n\n\x06SHA_NI\x10\x02\"?\n\rVulnerability\x12\x1b\n\x17VULNERABILITY_UNDEFINED\x10\x00\x12\x08\n\x04L1TF\x10\x01\x12\x07\n\x03MDS\x10\x02\x1a\xb4\x02\n\x06Memory\x12@\n\x07profile\x18\x01 \x01(\x0b\x32/.chromiumos.config.api.Component.Memory.Profile\x12\x13\n\x0bpart_number\x18\x02 \x01(\t\x1ap\n\x07Profile\x12:\n\x04type\x18\x01 \x01(\x0e\x32,.chromiumos.config.api.Component.Memory.Type\x12\x11\n\tspeed_mhz\x18\x02 \x01(\x05\x12\x16\n\x0esize_megabytes\x18\x03 \x01(\x05\"[\n\x04Type\x12\x12\n\x0eTYPE_UNDEFINED\x10\x00\x12\x07\n\x03\x44\x44R\x10\x01\x12\x08\n\x04\x44\x44R2\x10\x02\x12\x08\n\x04\x44\x44R3\x10\x03\x12\x08\n\x04\x44\x44R4\x10\x04\x12\x0b\n\x07LP_DDR3\x10\x05\x12\x0b\n\x07LP_DDR4\x10\x06J\x04\x08\x03\x10\x04\x1aZ\n\tBluetooth\x12;\n\x03usb\x18\x04 \x01(\x0b\x32..chromiumos.config.api.Component.Interface.UsbJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\x1a\x93\x03\n\x06\x43\x61mera\x12\x41\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0e\x32/.chromiumos.config.api.Component.Camera.Feature\x12\x45\n\nclock_type\x18\x02 \x01(\x0e\x32\x31.chromiumos.config.api.Component.Camera.ClockType\x12=\n\x03usb\x18\x03 \x01(\x0b\x32..chromiumos.config.api.Component.Interface.UsbH\x00\x12=\n\x03pci\x18\x04 \x01(\x0b\x32..chromiumos.config.api.Component.Interface.PciH\x00\"0\n\x07\x46\x65\x61ture\x12\x13\n\x0f\x46\x45\x41TURE_UNKNOWN\x10\x00\x12\x10\n\x0c\x41\x43TIVITY_LED\x10\x01\"B\n\tClockType\x12\x18\n\x14\x43LOCK_TYPE_UNDEFINED\x10\x00\x12\r\n\tMONOTONIC\x10\x01\x12\x0c\n\x08\x42OOTTIME\x10\x02\x42\x0b\n\tinterface\x1a\xec\x05\n\x0c\x44isplayPanel\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12L\n\nproperties\x18\x02 \x01(\x0b\x32\x38.chromiumos.config.api.Component.DisplayPanel.Properties\x1a\xab\x04\n\nProperties\x12\x10\n\x08width_px\x18\x01 \x01(\x05\x12\x11\n\theight_px\x18\x02 \x01(\x05\x12\x1a\n\x12\x64iagonal_milliinch\x18\x03 \x01(\x05\x12\x15\n\rpixels_per_in\x18\x04 \x01(\x05\x12G\n\x08\x66\x65\x61tures\x18\x05 \x03(\x0e\x32\x35.chromiumos.config.api.Component.DisplayPanel.Feature\x12#\n\x1bmin_visible_backlight_level\x18\x06 \x01(\r\x12@\n\x1aturn_off_screen_timeout_ms\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12#\n\x19no_als_battery_brightness\x18\x08 \x01(\x01H\x00\x12(\n\x1eno_als_battery_brightness_nits\x18\x0b \x01(\x01H\x00\x12\x1e\n\x14no_als_ac_brightness\x18\t \x01(\x01H\x01\x12#\n\x19no_als_ac_brightness_nits\x18\x0c \x01(\x01H\x01\x12;\n\tals_steps\x18\n \x03(\x0b\x32(.chromiumos.config.api.Component.AlsStep\x12\x1d\n\x15max_screen_brightness\x18\r \x01(\x01\x42\x14\n\x12\x62\x61ttery_brightnessB\x0f\n\rac_brightness\"L\n\x07\x46\x65\x61ture\x12\x13\n\x0f\x46\x45\x41TURE_UNKNOWN\x10\x00\x12\x07\n\x03HDR\x10\x01\x12#\n\x1fSEAMLESS_REFRESH_RATE_SWITCHING\x10\x02\x1a\x9e\x02\n\x05Touch\x12\x12\n\nproduct_id\x18\x02 \x01(\t\x12\x12\n\nfw_version\x18\x03 \x01(\t\x12\x16\n\x0eproduct_series\x18\x05 \x01(\t\x12\x13\n\x0b\x66w_checksum\x18\x06 \x01(\t\x12>\n\x04type\x18\x07 \x01(\x0e\x32\x30.chromiumos.config.api.Component.Touch.TouchType\x12;\n\x03usb\x18\x08 \x01(\x0b\x32..chromiumos.config.api.Component.Interface.Usb\"7\n\tTouchType\x12\x18\n\x14TOUCH_TYPE_UNDEFINED\x10\x00\x12\x07\n\x03USB\x10\x01\x12\x07\n\x03I2C\x10\x02J\x04\x08\x01\x10\x02J\x04\x08\x04\x10\x05\x1a\xc8\x02\n\x04Wifi\x12=\n\x03pci\x18\x01 \x01(\x0b\x32..chromiumos.config.api.Component.Interface.PciH\x00\x12T\n\x18supported_wlan_protocols\x18\x02 \x03(\x0e\x32\x32.chromiumos.config.api.Component.Wifi.WLANProtocol\"\x9d\x01\n\x0cWLANProtocol\x12\x19\n\x15WLAN_PROTOCOL_UNKNOWN\x10\x00\x12\x11\n\rIEEE_802_11_A\x10\x01\x12\x11\n\rIEEE_802_11_B\x10\x02\x12\x11\n\rIEEE_802_11_G\x10\x03\x12\x11\n\rIEEE_802_11_N\x10\x04\x12\x12\n\x0eIEEE_802_11_AC\x10\x05\x12\x12\n\x0eIEEE_802_11_AX\x10\x06\x42\x0b\n\tinterface\x1a\xe7\x01\n\rQualification\x12\x38\n\x0c\x63omponent_id\x18\x01 \x01(\x0b\x32\".chromiumos.config.api.ComponentId\x12\x45\n\x06status\x18\x02 \x01(\x0e\x32\x35.chromiumos.config.api.Component.Qualification.Status\"U\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\r\n\tREQUESTED\x10\x01\x12\x19\n\x15TECHNICALLY_QUALIFIED\x10\x02\x12\r\n\tQUALIFIED\x10\x03\x1a\x9a\x01\n\tAmplifier\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x44\n\x08\x66\x65\x61tures\x18\x02 \x03(\x0e\x32\x32.chromiumos.config.api.Component.Amplifier.Feature\"9\n\x07\x46\x65\x61ture\x12\x13\n\x0f\x46\x45\x41TURE_UNKNOWN\x10\x00\x12\x19\n\x15\x42OOT_TIME_CALIBRATION\x10\x01\x1a\x1a\n\nAudioCodec\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x9a\x01\n\x07\x42\x61ttery\x12\r\n\x05model\x18\x01 \x01(\t\x12G\n\ntechnology\x18\x02 \x01(\x0e\x32\x33.chromiumos.config.api.Component.Battery.Technology\"7\n\nTechnology\x12\x10\n\x0cTECH_UNKNOWN\x10\x00\x12\n\n\x06LI_ION\x10\x01\x12\x0b\n\x07LI_POLY\x10\x02\x1a \n\tFlashChip\x12\x13\n\x0bpart_number\x18\x01 \x01(\t\x1a)\n\x12\x45mbeddedController\x12\x13\n\x0bpart_number\x18\x01 \x01(\t\x1a\xdb\x02\n\x07Storage\x12\x14\n\x0c\x65mmc5_fw_ver\x18\x01 \x01(\t\x12\x0e\n\x06manfid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05oemid\x18\x04 \x01(\t\x12\x0b\n\x03prv\x18\x05 \x01(\t\x12\x0f\n\x07sectors\x18\x06 \x01(\t\x12\x42\n\x04type\x18\x07 \x01(\x0e\x32\x34.chromiumos.config.api.Component.Storage.StorageType\x12\x0f\n\x07size_gb\x18\x08 \x01(\r\x12=\n\x03pci\x18\t \x01(\x0b\x32..chromiumos.config.api.Component.Interface.PciH\x00\"N\n\x0bStorageType\x12\x18\n\x14STORAGE_TYPE_UNKNOWN\x10\x00\x12\x08\n\x04\x45MMC\x10\x01\x12\x08\n\x04NVME\x10\x02\x12\x08\n\x04SATA\x10\x03\x12\x07\n\x03UFS\x10\x04\x42\x0b\n\tinterface\x1a\x31\n\x03Tpm\x12\x19\n\x11manufacturer_info\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x1a\x93\x01\n\x06Stylus\x12=\n\x03usb\x18\x01 \x01(\x0b\x32..chromiumos.config.api.Component.Interface.UsbH\x00\x12=\n\x03i2c\x18\x02 \x01(\x0b\x32..chromiumos.config.api.Component.Interface.I2CH\x00\x42\x0b\n\tinterface\x1a$\n\x14\x44isplayPortConverter\x12\x0c\n\x04name\x18\x01 \x01(\t\x1aV\n\x08\x43\x65llular\x12=\n\x03usb\x18\x01 \x01(\x0b\x32..chromiumos.config.api.Component.Interface.UsbH\x00\x42\x0b\n\tinterface\x1a\x91\x02\n\x07\x41lsStep\x12\x1e\n\x14\x61\x63_backlight_percent\x18\x01 \x01(\x01H\x00\x12\x1b\n\x11\x61\x63_backlight_nits\x18\x05 \x01(\x01H\x00\x12#\n\x19\x62\x61ttery_backlight_percent\x18\x02 \x01(\x01H\x01\x12 \n\x16\x62\x61ttery_backlight_nits\x18\x06 \x01(\x01H\x01\x12\x1e\n\x16lux_decrease_threshold\x18\x03 \x01(\x05\x12\x1e\n\x16lux_increase_threshold\x18\x04 \x01(\x05\x12\x1d\n\x15max_screen_brightness\x18\x07 \x01(\x01\x42\x0e\n\x0c\x61\x63_backlightB\x13\n\x11\x62\x61ttery_backlight\"\x80\x01\n\rSupportStatus\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x14\n\x10STATUS_SUPPORTED\x10\x01\x12\x15\n\x11STATUS_DEPRECATED\x10\x02\x12\x16\n\x12STATUS_UNQUALIFIED\x10\x03\x12\x16\n\x12STATUS_UNSUPPORTED\x10\x04\x42\x06\n\x04typeB*Z(go.chromium.org/chromiumos/config/go/apib\x06proto3')



_COMPONENT = DESCRIPTOR.message_types_by_name['Component']
_COMPONENT_AVLID = _COMPONENT.nested_types_by_name['AVLId']
_COMPONENT_INTERFACE = _COMPONENT.nested_types_by_name['Interface']
_COMPONENT_INTERFACE_I2C = _COMPONENT_INTERFACE.nested_types_by_name['I2C']
_COMPONENT_INTERFACE_USB = _COMPONENT_INTERFACE.nested_types_by_name['Usb']
_COMPONENT_INTERFACE_PCI = _COMPONENT_INTERFACE.nested_types_by_name['Pci']
_COMPONENT_SOC = _COMPONENT.nested_types_by_name['Soc']
_COMPONENT_SOC_FAMILY = _COMPONENT_SOC.nested_types_by_name['Family']
_COMPONENT_MEMORY = _COMPONENT.nested_types_by_name['Memory']
_COMPONENT_MEMORY_PROFILE = _COMPONENT_MEMORY.nested_types_by_name['Profile']
_COMPONENT_BLUETOOTH = _COMPONENT.nested_types_by_name['Bluetooth']
_COMPONENT_CAMERA = _COMPONENT.nested_types_by_name['Camera']
_COMPONENT_DISPLAYPANEL = _COMPONENT.nested_types_by_name['DisplayPanel']
_COMPONENT_DISPLAYPANEL_PROPERTIES = _COMPONENT_DISPLAYPANEL.nested_types_by_name['Properties']
_COMPONENT_TOUCH = _COMPONENT.nested_types_by_name['Touch']
_COMPONENT_WIFI = _COMPONENT.nested_types_by_name['Wifi']
_COMPONENT_QUALIFICATION = _COMPONENT.nested_types_by_name['Qualification']
_COMPONENT_AMPLIFIER = _COMPONENT.nested_types_by_name['Amplifier']
_COMPONENT_AUDIOCODEC = _COMPONENT.nested_types_by_name['AudioCodec']
_COMPONENT_BATTERY = _COMPONENT.nested_types_by_name['Battery']
_COMPONENT_FLASHCHIP = _COMPONENT.nested_types_by_name['FlashChip']
_COMPONENT_EMBEDDEDCONTROLLER = _COMPONENT.nested_types_by_name['EmbeddedController']
_COMPONENT_STORAGE = _COMPONENT.nested_types_by_name['Storage']
_COMPONENT_TPM = _COMPONENT.nested_types_by_name['Tpm']
_COMPONENT_STYLUS = _COMPONENT.nested_types_by_name['Stylus']
_COMPONENT_DISPLAYPORTCONVERTER = _COMPONENT.nested_types_by_name['DisplayPortConverter']
_COMPONENT_CELLULAR = _COMPONENT.nested_types_by_name['Cellular']
_COMPONENT_ALSSTEP = _COMPONENT.nested_types_by_name['AlsStep']
_COMPONENT_SOC_ARCHITECTURE = _COMPONENT_SOC.enum_types_by_name['Architecture']
_COMPONENT_SOC_FEATURE = _COMPONENT_SOC.enum_types_by_name['Feature']
_COMPONENT_SOC_VULNERABILITY = _COMPONENT_SOC.enum_types_by_name['Vulnerability']
_COMPONENT_MEMORY_TYPE = _COMPONENT_MEMORY.enum_types_by_name['Type']
_COMPONENT_CAMERA_FEATURE = _COMPONENT_CAMERA.enum_types_by_name['Feature']
_COMPONENT_CAMERA_CLOCKTYPE = _COMPONENT_CAMERA.enum_types_by_name['ClockType']
_COMPONENT_DISPLAYPANEL_FEATURE = _COMPONENT_DISPLAYPANEL.enum_types_by_name['Feature']
_COMPONENT_TOUCH_TOUCHTYPE = _COMPONENT_TOUCH.enum_types_by_name['TouchType']
_COMPONENT_WIFI_WLANPROTOCOL = _COMPONENT_WIFI.enum_types_by_name['WLANProtocol']
_COMPONENT_QUALIFICATION_STATUS = _COMPONENT_QUALIFICATION.enum_types_by_name['Status']
_COMPONENT_AMPLIFIER_FEATURE = _COMPONENT_AMPLIFIER.enum_types_by_name['Feature']
_COMPONENT_BATTERY_TECHNOLOGY = _COMPONENT_BATTERY.enum_types_by_name['Technology']
_COMPONENT_STORAGE_STORAGETYPE = _COMPONENT_STORAGE.enum_types_by_name['StorageType']
_COMPONENT_SUPPORTSTATUS = _COMPONENT.enum_types_by_name['SupportStatus']
Component = _reflection.GeneratedProtocolMessageType('Component', (_message.Message,), {

  'AVLId' : _reflection.GeneratedProtocolMessageType('AVLId', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_AVLID,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.AVLId)
    })
  ,

  'Interface' : _reflection.GeneratedProtocolMessageType('Interface', (_message.Message,), {

    'I2C' : _reflection.GeneratedProtocolMessageType('I2C', (_message.Message,), {
      'DESCRIPTOR' : _COMPONENT_INTERFACE_I2C,
      '__module__' : 'chromiumos.config.api.component_pb2'
      # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Interface.I2C)
      })
    ,

    'Usb' : _reflection.GeneratedProtocolMessageType('Usb', (_message.Message,), {
      'DESCRIPTOR' : _COMPONENT_INTERFACE_USB,
      '__module__' : 'chromiumos.config.api.component_pb2'
      # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Interface.Usb)
      })
    ,

    'Pci' : _reflection.GeneratedProtocolMessageType('Pci', (_message.Message,), {
      'DESCRIPTOR' : _COMPONENT_INTERFACE_PCI,
      '__module__' : 'chromiumos.config.api.component_pb2'
      # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Interface.Pci)
      })
    ,
    'DESCRIPTOR' : _COMPONENT_INTERFACE,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Interface)
    })
  ,

  'Soc' : _reflection.GeneratedProtocolMessageType('Soc', (_message.Message,), {

    'Family' : _reflection.GeneratedProtocolMessageType('Family', (_message.Message,), {
      'DESCRIPTOR' : _COMPONENT_SOC_FAMILY,
      '__module__' : 'chromiumos.config.api.component_pb2'
      # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Soc.Family)
      })
    ,
    'DESCRIPTOR' : _COMPONENT_SOC,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Soc)
    })
  ,

  'Memory' : _reflection.GeneratedProtocolMessageType('Memory', (_message.Message,), {

    'Profile' : _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), {
      'DESCRIPTOR' : _COMPONENT_MEMORY_PROFILE,
      '__module__' : 'chromiumos.config.api.component_pb2'
      # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Memory.Profile)
      })
    ,
    'DESCRIPTOR' : _COMPONENT_MEMORY,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Memory)
    })
  ,

  'Bluetooth' : _reflection.GeneratedProtocolMessageType('Bluetooth', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_BLUETOOTH,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Bluetooth)
    })
  ,

  'Camera' : _reflection.GeneratedProtocolMessageType('Camera', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_CAMERA,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Camera)
    })
  ,

  'DisplayPanel' : _reflection.GeneratedProtocolMessageType('DisplayPanel', (_message.Message,), {

    'Properties' : _reflection.GeneratedProtocolMessageType('Properties', (_message.Message,), {
      'DESCRIPTOR' : _COMPONENT_DISPLAYPANEL_PROPERTIES,
      '__module__' : 'chromiumos.config.api.component_pb2'
      # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.DisplayPanel.Properties)
      })
    ,
    'DESCRIPTOR' : _COMPONENT_DISPLAYPANEL,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.DisplayPanel)
    })
  ,

  'Touch' : _reflection.GeneratedProtocolMessageType('Touch', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_TOUCH,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Touch)
    })
  ,

  'Wifi' : _reflection.GeneratedProtocolMessageType('Wifi', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_WIFI,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Wifi)
    })
  ,

  'Qualification' : _reflection.GeneratedProtocolMessageType('Qualification', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_QUALIFICATION,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Qualification)
    })
  ,

  'Amplifier' : _reflection.GeneratedProtocolMessageType('Amplifier', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_AMPLIFIER,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Amplifier)
    })
  ,

  'AudioCodec' : _reflection.GeneratedProtocolMessageType('AudioCodec', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_AUDIOCODEC,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.AudioCodec)
    })
  ,

  'Battery' : _reflection.GeneratedProtocolMessageType('Battery', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_BATTERY,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Battery)
    })
  ,

  'FlashChip' : _reflection.GeneratedProtocolMessageType('FlashChip', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_FLASHCHIP,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.FlashChip)
    })
  ,

  'EmbeddedController' : _reflection.GeneratedProtocolMessageType('EmbeddedController', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_EMBEDDEDCONTROLLER,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.EmbeddedController)
    })
  ,

  'Storage' : _reflection.GeneratedProtocolMessageType('Storage', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_STORAGE,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Storage)
    })
  ,

  'Tpm' : _reflection.GeneratedProtocolMessageType('Tpm', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_TPM,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Tpm)
    })
  ,

  'Stylus' : _reflection.GeneratedProtocolMessageType('Stylus', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_STYLUS,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Stylus)
    })
  ,

  'DisplayPortConverter' : _reflection.GeneratedProtocolMessageType('DisplayPortConverter', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_DISPLAYPORTCONVERTER,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.DisplayPortConverter)
    })
  ,

  'Cellular' : _reflection.GeneratedProtocolMessageType('Cellular', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_CELLULAR,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.Cellular)
    })
  ,

  'AlsStep' : _reflection.GeneratedProtocolMessageType('AlsStep', (_message.Message,), {
    'DESCRIPTOR' : _COMPONENT_ALSSTEP,
    '__module__' : 'chromiumos.config.api.component_pb2'
    # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component.AlsStep)
    })
  ,
  'DESCRIPTOR' : _COMPONENT,
  '__module__' : 'chromiumos.config.api.component_pb2'
  # @@protoc_insertion_point(class_scope:chromiumos.config.api.Component)
  })
_sym_db.RegisterMessage(Component)
_sym_db.RegisterMessage(Component.AVLId)
_sym_db.RegisterMessage(Component.Interface)
_sym_db.RegisterMessage(Component.Interface.I2C)
_sym_db.RegisterMessage(Component.Interface.Usb)
_sym_db.RegisterMessage(Component.Interface.Pci)
_sym_db.RegisterMessage(Component.Soc)
_sym_db.RegisterMessage(Component.Soc.Family)
_sym_db.RegisterMessage(Component.Memory)
_sym_db.RegisterMessage(Component.Memory.Profile)
_sym_db.RegisterMessage(Component.Bluetooth)
_sym_db.RegisterMessage(Component.Camera)
_sym_db.RegisterMessage(Component.DisplayPanel)
_sym_db.RegisterMessage(Component.DisplayPanel.Properties)
_sym_db.RegisterMessage(Component.Touch)
_sym_db.RegisterMessage(Component.Wifi)
_sym_db.RegisterMessage(Component.Qualification)
_sym_db.RegisterMessage(Component.Amplifier)
_sym_db.RegisterMessage(Component.AudioCodec)
_sym_db.RegisterMessage(Component.Battery)
_sym_db.RegisterMessage(Component.FlashChip)
_sym_db.RegisterMessage(Component.EmbeddedController)
_sym_db.RegisterMessage(Component.Storage)
_sym_db.RegisterMessage(Component.Tpm)
_sym_db.RegisterMessage(Component.Stylus)
_sym_db.RegisterMessage(Component.DisplayPortConverter)
_sym_db.RegisterMessage(Component.Cellular)
_sym_db.RegisterMessage(Component.AlsStep)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(go.chromium.org/chromiumos/config/go/api'
  _COMPONENT._serialized_start=179
  _COMPONENT._serialized_end=6467
  _COMPONENT_AVLID._serialized_start=1773
  _COMPONENT_AVLID._serialized_end=1806
  _COMPONENT_INTERFACE._serialized_start=1809
  _COMPONENT_INTERFACE._serialized_end=2010
  _COMPONENT_INTERFACE_I2C._serialized_start=1822
  _COMPONENT_INTERFACE_I2C._serialized_end=1860
  _COMPONENT_INTERFACE_USB._serialized_start=1862
  _COMPONENT_INTERFACE_USB._serialized_end=1926
  _COMPONENT_INTERFACE_PCI._serialized_start=1928
  _COMPONENT_INTERFACE_PCI._serialized_end=2010
  _COMPONENT_SOC._serialized_start=2013
  _COMPONENT_SOC._serialized_end=2542
  _COMPONENT_SOC_FAMILY._serialized_start=2252
  _COMPONENT_SOC_FAMILY._serialized_end=2339
  _COMPONENT_SOC_ARCHITECTURE._serialized_start=2341
  _COMPONENT_SOC_ARCHITECTURE._serialized_end=2424
  _COMPONENT_SOC_FEATURE._serialized_start=2426
  _COMPONENT_SOC_FEATURE._serialized_end=2477
  _COMPONENT_SOC_VULNERABILITY._serialized_start=2479
  _COMPONENT_SOC_VULNERABILITY._serialized_end=2542
  _COMPONENT_MEMORY._serialized_start=2545
  _COMPONENT_MEMORY._serialized_end=2853
  _COMPONENT_MEMORY_PROFILE._serialized_start=2642
  _COMPONENT_MEMORY_PROFILE._serialized_end=2754
  _COMPONENT_MEMORY_TYPE._serialized_start=2756
  _COMPONENT_MEMORY_TYPE._serialized_end=2847
  _COMPONENT_BLUETOOTH._serialized_start=2855
  _COMPONENT_BLUETOOTH._serialized_end=2945
  _COMPONENT_CAMERA._serialized_start=2948
  _COMPONENT_CAMERA._serialized_end=3351
  _COMPONENT_CAMERA_FEATURE._serialized_start=3222
  _COMPONENT_CAMERA_FEATURE._serialized_end=3270
  _COMPONENT_CAMERA_CLOCKTYPE._serialized_start=3272
  _COMPONENT_CAMERA_CLOCKTYPE._serialized_end=3338
  _COMPONENT_DISPLAYPANEL._serialized_start=3354
  _COMPONENT_DISPLAYPANEL._serialized_end=4102
  _COMPONENT_DISPLAYPANEL_PROPERTIES._serialized_start=3469
  _COMPONENT_DISPLAYPANEL_PROPERTIES._serialized_end=4024
  _COMPONENT_DISPLAYPANEL_FEATURE._serialized_start=4026
  _COMPONENT_DISPLAYPANEL_FEATURE._serialized_end=4102
  _COMPONENT_TOUCH._serialized_start=4105
  _COMPONENT_TOUCH._serialized_end=4391
  _COMPONENT_TOUCH_TOUCHTYPE._serialized_start=4324
  _COMPONENT_TOUCH_TOUCHTYPE._serialized_end=4379
  _COMPONENT_WIFI._serialized_start=4394
  _COMPONENT_WIFI._serialized_end=4722
  _COMPONENT_WIFI_WLANPROTOCOL._serialized_start=4552
  _COMPONENT_WIFI_WLANPROTOCOL._serialized_end=4709
  _COMPONENT_QUALIFICATION._serialized_start=4725
  _COMPONENT_QUALIFICATION._serialized_end=4956
  _COMPONENT_QUALIFICATION_STATUS._serialized_start=4871
  _COMPONENT_QUALIFICATION_STATUS._serialized_end=4956
  _COMPONENT_AMPLIFIER._serialized_start=4959
  _COMPONENT_AMPLIFIER._serialized_end=5113
  _COMPONENT_AMPLIFIER_FEATURE._serialized_start=5056
  _COMPONENT_AMPLIFIER_FEATURE._serialized_end=5113
  _COMPONENT_AUDIOCODEC._serialized_start=5115
  _COMPONENT_AUDIOCODEC._serialized_end=5141
  _COMPONENT_BATTERY._serialized_start=5144
  _COMPONENT_BATTERY._serialized_end=5298
  _COMPONENT_BATTERY_TECHNOLOGY._serialized_start=5243
  _COMPONENT_BATTERY_TECHNOLOGY._serialized_end=5298
  _COMPONENT_FLASHCHIP._serialized_start=5300
  _COMPONENT_FLASHCHIP._serialized_end=5332
  _COMPONENT_EMBEDDEDCONTROLLER._serialized_start=5334
  _COMPONENT_EMBEDDEDCONTROLLER._serialized_end=5375
  _COMPONENT_STORAGE._serialized_start=5378
  _COMPONENT_STORAGE._serialized_end=5725
  _COMPONENT_STORAGE_STORAGETYPE._serialized_start=5634
  _COMPONENT_STORAGE_STORAGETYPE._serialized_end=5712
  _COMPONENT_TPM._serialized_start=5727
  _COMPONENT_TPM._serialized_end=5776
  _COMPONENT_STYLUS._serialized_start=5779
  _COMPONENT_STYLUS._serialized_end=5926
  _COMPONENT_DISPLAYPORTCONVERTER._serialized_start=5928
  _COMPONENT_DISPLAYPORTCONVERTER._serialized_end=5964
  _COMPONENT_CELLULAR._serialized_start=5966
  _COMPONENT_CELLULAR._serialized_end=6052
  _COMPONENT_ALSSTEP._serialized_start=6055
  _COMPONENT_ALSSTEP._serialized_end=6328
  _COMPONENT_SUPPORTSTATUS._serialized_start=6331
  _COMPONENT_SUPPORTSTATUS._serialized_end=6459
# @@protoc_insertion_point(module_scope)
