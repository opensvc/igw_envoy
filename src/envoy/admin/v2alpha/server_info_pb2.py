# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/admin/v2alpha/server_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/admin/v2alpha/server_info.proto',
  package='envoy.admin.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n%envoy/admin/v2alpha/server_info.proto\x12\x13\x65nvoy.admin.v2alpha\x1a\x1egoogle/protobuf/duration.proto\"\xd2\x02\n\nServerInfo\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x34\n\x05state\x18\x02 \x01(\x0e\x32%.envoy.admin.v2alpha.ServerInfo.State\x12\x37\n\x14uptime_current_epoch\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x34\n\x11uptime_all_epochs\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x45\n\x14\x63ommand_line_options\x18\x06 \x01(\x0b\x32\'.envoy.admin.v2alpha.CommandLineOptions\"G\n\x05State\x12\x08\n\x04LIVE\x10\x00\x12\x0c\n\x08\x44RAINING\x10\x01\x12\x14\n\x10PRE_INITIALIZING\x10\x02\x12\x10\n\x0cINITIALIZING\x10\x03\"\xea\x06\n\x12\x43ommandLineOptions\x12\x0f\n\x07\x62\x61se_id\x18\x01 \x01(\x04\x12\x13\n\x0b\x63oncurrency\x18\x02 \x01(\r\x12\x13\n\x0b\x63onfig_path\x18\x03 \x01(\t\x12\x13\n\x0b\x63onfig_yaml\x18\x04 \x01(\t\x12\x1c\n\x14\x61llow_unknown_fields\x18\x05 \x01(\x08\x12\x1a\n\x12\x61\x64min_address_path\x18\x06 \x01(\t\x12S\n\x18local_address_ip_version\x18\x07 \x01(\x0e\x32\x31.envoy.admin.v2alpha.CommandLineOptions.IpVersion\x12\x11\n\tlog_level\x18\x08 \x01(\t\x12\x1b\n\x13\x63omponent_log_level\x18\t \x01(\t\x12\x12\n\nlog_format\x18\n \x01(\t\x12\x10\n\x08log_path\x18\x0b \x01(\t\x12\x1b\n\x13hot_restart_version\x18\x0c \x01(\x08\x12\x17\n\x0fservice_cluster\x18\r \x01(\t\x12\x14\n\x0cservice_node\x18\x0e \x01(\t\x12\x14\n\x0cservice_zone\x18\x0f \x01(\t\x12\x36\n\x13\x66ile_flush_interval\x18\x10 \x01(\x0b\x32\x19.google.protobuf.Duration\x12-\n\ndrain_time\x18\x11 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\x14parent_shutdown_time\x18\x12 \x01(\x0b\x32\x19.google.protobuf.Duration\x12:\n\x04mode\x18\x13 \x01(\x0e\x32,.envoy.admin.v2alpha.CommandLineOptions.Mode\x12\x11\n\tmax_stats\x18\x14 \x01(\x04\x12\x18\n\x10max_obj_name_len\x18\x15 \x01(\x04\x12\x1b\n\x13\x64isable_hot_restart\x18\x16 \x01(\x08\x12\x1c\n\x14\x65nable_mutex_tracing\x18\x17 \x01(\x08\x12\x15\n\rrestart_epoch\x18\x18 \x01(\r\x12\x16\n\x0e\x63puset_threads\x18\x19 \x01(\x08\"\x1b\n\tIpVersion\x12\x06\n\x02v4\x10\x00\x12\x06\n\x02v6\x10\x01\"-\n\x04Mode\x12\t\n\x05Serve\x10\x00\x12\x0c\n\x08Validate\x10\x01\x12\x0c\n\x08InitOnly\x10\x02\x42\x36\n!io.envoyproxy.envoy.admin.v2alphaB\x0fServerInfoProtoP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])



_SERVERINFO_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='envoy.admin.v2alpha.ServerInfo.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LIVE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRAINING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_INITIALIZING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIALIZING', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=362,
  serialized_end=433,
)
_sym_db.RegisterEnumDescriptor(_SERVERINFO_STATE)

_COMMANDLINEOPTIONS_IPVERSION = _descriptor.EnumDescriptor(
  name='IpVersion',
  full_name='envoy.admin.v2alpha.CommandLineOptions.IpVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='v4', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='v6', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1236,
  serialized_end=1263,
)
_sym_db.RegisterEnumDescriptor(_COMMANDLINEOPTIONS_IPVERSION)

_COMMANDLINEOPTIONS_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='envoy.admin.v2alpha.CommandLineOptions.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Serve', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Validate', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InitOnly', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1265,
  serialized_end=1310,
)
_sym_db.RegisterEnumDescriptor(_COMMANDLINEOPTIONS_MODE)


_SERVERINFO = _descriptor.Descriptor(
  name='ServerInfo',
  full_name='envoy.admin.v2alpha.ServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='envoy.admin.v2alpha.ServerInfo.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='envoy.admin.v2alpha.ServerInfo.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uptime_current_epoch', full_name='envoy.admin.v2alpha.ServerInfo.uptime_current_epoch', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uptime_all_epochs', full_name='envoy.admin.v2alpha.ServerInfo.uptime_all_epochs', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command_line_options', full_name='envoy.admin.v2alpha.ServerInfo.command_line_options', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERINFO_STATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=433,
)


_COMMANDLINEOPTIONS = _descriptor.Descriptor(
  name='CommandLineOptions',
  full_name='envoy.admin.v2alpha.CommandLineOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_id', full_name='envoy.admin.v2alpha.CommandLineOptions.base_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='concurrency', full_name='envoy.admin.v2alpha.CommandLineOptions.concurrency', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config_path', full_name='envoy.admin.v2alpha.CommandLineOptions.config_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config_yaml', full_name='envoy.admin.v2alpha.CommandLineOptions.config_yaml', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allow_unknown_fields', full_name='envoy.admin.v2alpha.CommandLineOptions.allow_unknown_fields', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='admin_address_path', full_name='envoy.admin.v2alpha.CommandLineOptions.admin_address_path', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_address_ip_version', full_name='envoy.admin.v2alpha.CommandLineOptions.local_address_ip_version', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_level', full_name='envoy.admin.v2alpha.CommandLineOptions.log_level', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='component_log_level', full_name='envoy.admin.v2alpha.CommandLineOptions.component_log_level', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_format', full_name='envoy.admin.v2alpha.CommandLineOptions.log_format', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_path', full_name='envoy.admin.v2alpha.CommandLineOptions.log_path', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hot_restart_version', full_name='envoy.admin.v2alpha.CommandLineOptions.hot_restart_version', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_cluster', full_name='envoy.admin.v2alpha.CommandLineOptions.service_cluster', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_node', full_name='envoy.admin.v2alpha.CommandLineOptions.service_node', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_zone', full_name='envoy.admin.v2alpha.CommandLineOptions.service_zone', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_flush_interval', full_name='envoy.admin.v2alpha.CommandLineOptions.file_flush_interval', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drain_time', full_name='envoy.admin.v2alpha.CommandLineOptions.drain_time', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_shutdown_time', full_name='envoy.admin.v2alpha.CommandLineOptions.parent_shutdown_time', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='envoy.admin.v2alpha.CommandLineOptions.mode', index=18,
      number=19, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_stats', full_name='envoy.admin.v2alpha.CommandLineOptions.max_stats', index=19,
      number=20, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_obj_name_len', full_name='envoy.admin.v2alpha.CommandLineOptions.max_obj_name_len', index=20,
      number=21, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disable_hot_restart', full_name='envoy.admin.v2alpha.CommandLineOptions.disable_hot_restart', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enable_mutex_tracing', full_name='envoy.admin.v2alpha.CommandLineOptions.enable_mutex_tracing', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='restart_epoch', full_name='envoy.admin.v2alpha.CommandLineOptions.restart_epoch', index=23,
      number=24, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpuset_threads', full_name='envoy.admin.v2alpha.CommandLineOptions.cpuset_threads', index=24,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMANDLINEOPTIONS_IPVERSION,
    _COMMANDLINEOPTIONS_MODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=1310,
)

_SERVERINFO.fields_by_name['state'].enum_type = _SERVERINFO_STATE
_SERVERINFO.fields_by_name['uptime_current_epoch'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_SERVERINFO.fields_by_name['uptime_all_epochs'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_SERVERINFO.fields_by_name['command_line_options'].message_type = _COMMANDLINEOPTIONS
_SERVERINFO_STATE.containing_type = _SERVERINFO
_COMMANDLINEOPTIONS.fields_by_name['local_address_ip_version'].enum_type = _COMMANDLINEOPTIONS_IPVERSION
_COMMANDLINEOPTIONS.fields_by_name['file_flush_interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_COMMANDLINEOPTIONS.fields_by_name['drain_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_COMMANDLINEOPTIONS.fields_by_name['parent_shutdown_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_COMMANDLINEOPTIONS.fields_by_name['mode'].enum_type = _COMMANDLINEOPTIONS_MODE
_COMMANDLINEOPTIONS_IPVERSION.containing_type = _COMMANDLINEOPTIONS
_COMMANDLINEOPTIONS_MODE.containing_type = _COMMANDLINEOPTIONS
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['CommandLineOptions'] = _COMMANDLINEOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), dict(
  DESCRIPTOR = _SERVERINFO,
  __module__ = 'envoy.admin.v2alpha.server_info_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ServerInfo)
  ))
_sym_db.RegisterMessage(ServerInfo)

CommandLineOptions = _reflection.GeneratedProtocolMessageType('CommandLineOptions', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDLINEOPTIONS,
  __module__ = 'envoy.admin.v2alpha.server_info_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.CommandLineOptions)
  ))
_sym_db.RegisterMessage(CommandLineOptions)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!io.envoyproxy.envoy.admin.v2alphaB\017ServerInfoProtoP\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
