# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/admin/v2alpha/config_dump.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2 import cds_pb2 as envoy_dot_api_dot_v2_dot_cds__pb2
from envoy.api.v2 import lds_pb2 as envoy_dot_api_dot_v2_dot_lds__pb2
from envoy.api.v2 import rds_pb2 as envoy_dot_api_dot_v2_dot_rds__pb2
from envoy.config.bootstrap.v2 import bootstrap_pb2 as envoy_dot_config_dot_bootstrap_dot_v2_dot_bootstrap__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/admin/v2alpha/config_dump.proto',
  package='envoy.admin.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n%envoy/admin/v2alpha/config_dump.proto\x12\x13\x65nvoy.admin.v2alpha\x1a\x16\x65nvoy/api/v2/cds.proto\x1a\x16\x65nvoy/api/v2/lds.proto\x1a\x16\x65nvoy/api/v2/rds.proto\x1a)envoy/config/bootstrap/v2/bootstrap.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\"9\n\nConfigDump\x12+\n\x07\x63onfigs\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB\x04\xc8\xde\x1f\x00\"\x86\x01\n\x13\x42ootstrapConfigDump\x12=\n\tbootstrap\x18\x01 \x01(\x0b\x32$.envoy.config.bootstrap.v2.BootstrapB\x04\xc8\xde\x1f\x00\x12\x30\n\x0clast_updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa1\x05\n\x13ListenersConfigDump\x12\x14\n\x0cversion_info\x18\x01 \x01(\t\x12W\n\x10static_listeners\x18\x02 \x03(\x0b\x32\x37.envoy.admin.v2alpha.ListenersConfigDump.StaticListenerB\x04\xc8\xde\x1f\x00\x12`\n\x18\x64ynamic_active_listeners\x18\x03 \x03(\x0b\x32\x38.envoy.admin.v2alpha.ListenersConfigDump.DynamicListenerB\x04\xc8\xde\x1f\x00\x12\x61\n\x19\x64ynamic_warming_listeners\x18\x04 \x03(\x0b\x32\x38.envoy.admin.v2alpha.ListenersConfigDump.DynamicListenerB\x04\xc8\xde\x1f\x00\x12\x62\n\x1a\x64ynamic_draining_listeners\x18\x05 \x03(\x0b\x32\x38.envoy.admin.v2alpha.ListenersConfigDump.DynamicListenerB\x04\xc8\xde\x1f\x00\x1al\n\x0eStaticListener\x12(\n\x08listener\x18\x01 \x01(\x0b\x32\x16.envoy.api.v2.Listener\x12\x30\n\x0clast_updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x83\x01\n\x0f\x44ynamicListener\x12\x14\n\x0cversion_info\x18\x01 \x01(\t\x12(\n\x08listener\x18\x02 \x01(\x0b\x32\x16.envoy.api.v2.Listener\x12\x30\n\x0clast_updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xad\x04\n\x12\x43lustersConfigDump\x12\x14\n\x0cversion_info\x18\x01 \x01(\t\x12T\n\x0fstatic_clusters\x18\x02 \x03(\x0b\x32\x35.envoy.admin.v2alpha.ClustersConfigDump.StaticClusterB\x04\xc8\xde\x1f\x00\x12]\n\x17\x64ynamic_active_clusters\x18\x03 \x03(\x0b\x32\x36.envoy.admin.v2alpha.ClustersConfigDump.DynamicClusterB\x04\xc8\xde\x1f\x00\x12^\n\x18\x64ynamic_warming_clusters\x18\x04 \x03(\x0b\x32\x36.envoy.admin.v2alpha.ClustersConfigDump.DynamicClusterB\x04\xc8\xde\x1f\x00\x1ai\n\rStaticCluster\x12&\n\x07\x63luster\x18\x01 \x01(\x0b\x32\x15.envoy.api.v2.Cluster\x12\x30\n\x0clast_updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x80\x01\n\x0e\x44ynamicCluster\x12\x14\n\x0cversion_info\x18\x01 \x01(\t\x12&\n\x07\x63luster\x18\x02 \x01(\x0b\x32\x15.envoy.api.v2.Cluster\x12\x30\n\x0clast_updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xe4\x03\n\x10RoutesConfigDump\x12[\n\x14static_route_configs\x18\x02 \x03(\x0b\x32\x37.envoy.admin.v2alpha.RoutesConfigDump.StaticRouteConfigB\x04\xc8\xde\x1f\x00\x12]\n\x15\x64ynamic_route_configs\x18\x03 \x03(\x0b\x32\x38.envoy.admin.v2alpha.RoutesConfigDump.DynamicRouteConfigB\x04\xc8\xde\x1f\x00\x1a}\n\x11StaticRouteConfig\x12\x36\n\x0croute_config\x18\x01 \x01(\x0b\x32 .envoy.api.v2.RouteConfiguration\x12\x30\n\x0clast_updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x94\x01\n\x12\x44ynamicRouteConfig\x12\x14\n\x0cversion_info\x18\x01 \x01(\t\x12\x36\n\x0croute_config\x18\x02 \x01(\x0b\x32 .envoy.api.v2.RouteConfiguration\x12\x30\n\x0clast_updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB6\n!io.envoyproxy.envoy.admin.v2alphaB\x0f\x43onfigDumpProtoP\x01\x62\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_cds__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_lds__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_rds__pb2.DESCRIPTOR,envoy_dot_config_dot_bootstrap_dot_v2_dot_bootstrap__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_CONFIGDUMP = _descriptor.Descriptor(
  name='ConfigDump',
  full_name='envoy.admin.v2alpha.ConfigDump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configs', full_name='envoy.admin.v2alpha.ConfigDump.configs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=316,
)


_BOOTSTRAPCONFIGDUMP = _descriptor.Descriptor(
  name='BootstrapConfigDump',
  full_name='envoy.admin.v2alpha.BootstrapConfigDump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bootstrap', full_name='envoy.admin.v2alpha.BootstrapConfigDump.bootstrap', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='envoy.admin.v2alpha.BootstrapConfigDump.last_updated', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=453,
)


_LISTENERSCONFIGDUMP_STATICLISTENER = _descriptor.Descriptor(
  name='StaticListener',
  full_name='envoy.admin.v2alpha.ListenersConfigDump.StaticListener',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='listener', full_name='envoy.admin.v2alpha.ListenersConfigDump.StaticListener.listener', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='envoy.admin.v2alpha.ListenersConfigDump.StaticListener.last_updated', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=995,
)

_LISTENERSCONFIGDUMP_DYNAMICLISTENER = _descriptor.Descriptor(
  name='DynamicListener',
  full_name='envoy.admin.v2alpha.ListenersConfigDump.DynamicListener',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version_info', full_name='envoy.admin.v2alpha.ListenersConfigDump.DynamicListener.version_info', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='listener', full_name='envoy.admin.v2alpha.ListenersConfigDump.DynamicListener.listener', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='envoy.admin.v2alpha.ListenersConfigDump.DynamicListener.last_updated', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=998,
  serialized_end=1129,
)

_LISTENERSCONFIGDUMP = _descriptor.Descriptor(
  name='ListenersConfigDump',
  full_name='envoy.admin.v2alpha.ListenersConfigDump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version_info', full_name='envoy.admin.v2alpha.ListenersConfigDump.version_info', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='static_listeners', full_name='envoy.admin.v2alpha.ListenersConfigDump.static_listeners', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='dynamic_active_listeners', full_name='envoy.admin.v2alpha.ListenersConfigDump.dynamic_active_listeners', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='dynamic_warming_listeners', full_name='envoy.admin.v2alpha.ListenersConfigDump.dynamic_warming_listeners', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='dynamic_draining_listeners', full_name='envoy.admin.v2alpha.ListenersConfigDump.dynamic_draining_listeners', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
  ],
  extensions=[
  ],
  nested_types=[_LISTENERSCONFIGDUMP_STATICLISTENER, _LISTENERSCONFIGDUMP_DYNAMICLISTENER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=456,
  serialized_end=1129,
)


_CLUSTERSCONFIGDUMP_STATICCLUSTER = _descriptor.Descriptor(
  name='StaticCluster',
  full_name='envoy.admin.v2alpha.ClustersConfigDump.StaticCluster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster', full_name='envoy.admin.v2alpha.ClustersConfigDump.StaticCluster.cluster', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='envoy.admin.v2alpha.ClustersConfigDump.StaticCluster.last_updated', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1453,
  serialized_end=1558,
)

_CLUSTERSCONFIGDUMP_DYNAMICCLUSTER = _descriptor.Descriptor(
  name='DynamicCluster',
  full_name='envoy.admin.v2alpha.ClustersConfigDump.DynamicCluster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version_info', full_name='envoy.admin.v2alpha.ClustersConfigDump.DynamicCluster.version_info', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cluster', full_name='envoy.admin.v2alpha.ClustersConfigDump.DynamicCluster.cluster', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='envoy.admin.v2alpha.ClustersConfigDump.DynamicCluster.last_updated', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1561,
  serialized_end=1689,
)

_CLUSTERSCONFIGDUMP = _descriptor.Descriptor(
  name='ClustersConfigDump',
  full_name='envoy.admin.v2alpha.ClustersConfigDump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version_info', full_name='envoy.admin.v2alpha.ClustersConfigDump.version_info', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='static_clusters', full_name='envoy.admin.v2alpha.ClustersConfigDump.static_clusters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='dynamic_active_clusters', full_name='envoy.admin.v2alpha.ClustersConfigDump.dynamic_active_clusters', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='dynamic_warming_clusters', full_name='envoy.admin.v2alpha.ClustersConfigDump.dynamic_warming_clusters', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
  ],
  extensions=[
  ],
  nested_types=[_CLUSTERSCONFIGDUMP_STATICCLUSTER, _CLUSTERSCONFIGDUMP_DYNAMICCLUSTER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1132,
  serialized_end=1689,
)


_ROUTESCONFIGDUMP_STATICROUTECONFIG = _descriptor.Descriptor(
  name='StaticRouteConfig',
  full_name='envoy.admin.v2alpha.RoutesConfigDump.StaticRouteConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route_config', full_name='envoy.admin.v2alpha.RoutesConfigDump.StaticRouteConfig.route_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='envoy.admin.v2alpha.RoutesConfigDump.StaticRouteConfig.last_updated', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1900,
  serialized_end=2025,
)

_ROUTESCONFIGDUMP_DYNAMICROUTECONFIG = _descriptor.Descriptor(
  name='DynamicRouteConfig',
  full_name='envoy.admin.v2alpha.RoutesConfigDump.DynamicRouteConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version_info', full_name='envoy.admin.v2alpha.RoutesConfigDump.DynamicRouteConfig.version_info', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='route_config', full_name='envoy.admin.v2alpha.RoutesConfigDump.DynamicRouteConfig.route_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='envoy.admin.v2alpha.RoutesConfigDump.DynamicRouteConfig.last_updated', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2028,
  serialized_end=2176,
)

_ROUTESCONFIGDUMP = _descriptor.Descriptor(
  name='RoutesConfigDump',
  full_name='envoy.admin.v2alpha.RoutesConfigDump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='static_route_configs', full_name='envoy.admin.v2alpha.RoutesConfigDump.static_route_configs', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='dynamic_route_configs', full_name='envoy.admin.v2alpha.RoutesConfigDump.dynamic_route_configs', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
  ],
  extensions=[
  ],
  nested_types=[_ROUTESCONFIGDUMP_STATICROUTECONFIG, _ROUTESCONFIGDUMP_DYNAMICROUTECONFIG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1692,
  serialized_end=2176,
)

_CONFIGDUMP.fields_by_name['configs'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_BOOTSTRAPCONFIGDUMP.fields_by_name['bootstrap'].message_type = envoy_dot_config_dot_bootstrap_dot_v2_dot_bootstrap__pb2._BOOTSTRAP
_BOOTSTRAPCONFIGDUMP.fields_by_name['last_updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTENERSCONFIGDUMP_STATICLISTENER.fields_by_name['listener'].message_type = envoy_dot_api_dot_v2_dot_lds__pb2._LISTENER
_LISTENERSCONFIGDUMP_STATICLISTENER.fields_by_name['last_updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTENERSCONFIGDUMP_STATICLISTENER.containing_type = _LISTENERSCONFIGDUMP
_LISTENERSCONFIGDUMP_DYNAMICLISTENER.fields_by_name['listener'].message_type = envoy_dot_api_dot_v2_dot_lds__pb2._LISTENER
_LISTENERSCONFIGDUMP_DYNAMICLISTENER.fields_by_name['last_updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTENERSCONFIGDUMP_DYNAMICLISTENER.containing_type = _LISTENERSCONFIGDUMP
_LISTENERSCONFIGDUMP.fields_by_name['static_listeners'].message_type = _LISTENERSCONFIGDUMP_STATICLISTENER
_LISTENERSCONFIGDUMP.fields_by_name['dynamic_active_listeners'].message_type = _LISTENERSCONFIGDUMP_DYNAMICLISTENER
_LISTENERSCONFIGDUMP.fields_by_name['dynamic_warming_listeners'].message_type = _LISTENERSCONFIGDUMP_DYNAMICLISTENER
_LISTENERSCONFIGDUMP.fields_by_name['dynamic_draining_listeners'].message_type = _LISTENERSCONFIGDUMP_DYNAMICLISTENER
_CLUSTERSCONFIGDUMP_STATICCLUSTER.fields_by_name['cluster'].message_type = envoy_dot_api_dot_v2_dot_cds__pb2._CLUSTER
_CLUSTERSCONFIGDUMP_STATICCLUSTER.fields_by_name['last_updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLUSTERSCONFIGDUMP_STATICCLUSTER.containing_type = _CLUSTERSCONFIGDUMP
_CLUSTERSCONFIGDUMP_DYNAMICCLUSTER.fields_by_name['cluster'].message_type = envoy_dot_api_dot_v2_dot_cds__pb2._CLUSTER
_CLUSTERSCONFIGDUMP_DYNAMICCLUSTER.fields_by_name['last_updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLUSTERSCONFIGDUMP_DYNAMICCLUSTER.containing_type = _CLUSTERSCONFIGDUMP
_CLUSTERSCONFIGDUMP.fields_by_name['static_clusters'].message_type = _CLUSTERSCONFIGDUMP_STATICCLUSTER
_CLUSTERSCONFIGDUMP.fields_by_name['dynamic_active_clusters'].message_type = _CLUSTERSCONFIGDUMP_DYNAMICCLUSTER
_CLUSTERSCONFIGDUMP.fields_by_name['dynamic_warming_clusters'].message_type = _CLUSTERSCONFIGDUMP_DYNAMICCLUSTER
_ROUTESCONFIGDUMP_STATICROUTECONFIG.fields_by_name['route_config'].message_type = envoy_dot_api_dot_v2_dot_rds__pb2._ROUTECONFIGURATION
_ROUTESCONFIGDUMP_STATICROUTECONFIG.fields_by_name['last_updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ROUTESCONFIGDUMP_STATICROUTECONFIG.containing_type = _ROUTESCONFIGDUMP
_ROUTESCONFIGDUMP_DYNAMICROUTECONFIG.fields_by_name['route_config'].message_type = envoy_dot_api_dot_v2_dot_rds__pb2._ROUTECONFIGURATION
_ROUTESCONFIGDUMP_DYNAMICROUTECONFIG.fields_by_name['last_updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ROUTESCONFIGDUMP_DYNAMICROUTECONFIG.containing_type = _ROUTESCONFIGDUMP
_ROUTESCONFIGDUMP.fields_by_name['static_route_configs'].message_type = _ROUTESCONFIGDUMP_STATICROUTECONFIG
_ROUTESCONFIGDUMP.fields_by_name['dynamic_route_configs'].message_type = _ROUTESCONFIGDUMP_DYNAMICROUTECONFIG
DESCRIPTOR.message_types_by_name['ConfigDump'] = _CONFIGDUMP
DESCRIPTOR.message_types_by_name['BootstrapConfigDump'] = _BOOTSTRAPCONFIGDUMP
DESCRIPTOR.message_types_by_name['ListenersConfigDump'] = _LISTENERSCONFIGDUMP
DESCRIPTOR.message_types_by_name['ClustersConfigDump'] = _CLUSTERSCONFIGDUMP
DESCRIPTOR.message_types_by_name['RoutesConfigDump'] = _ROUTESCONFIGDUMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigDump = _reflection.GeneratedProtocolMessageType('ConfigDump', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGDUMP,
  __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ConfigDump)
  ))
_sym_db.RegisterMessage(ConfigDump)

BootstrapConfigDump = _reflection.GeneratedProtocolMessageType('BootstrapConfigDump', (_message.Message,), dict(
  DESCRIPTOR = _BOOTSTRAPCONFIGDUMP,
  __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.BootstrapConfigDump)
  ))
_sym_db.RegisterMessage(BootstrapConfigDump)

ListenersConfigDump = _reflection.GeneratedProtocolMessageType('ListenersConfigDump', (_message.Message,), dict(

  StaticListener = _reflection.GeneratedProtocolMessageType('StaticListener', (_message.Message,), dict(
    DESCRIPTOR = _LISTENERSCONFIGDUMP_STATICLISTENER,
    __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ListenersConfigDump.StaticListener)
    ))
  ,

  DynamicListener = _reflection.GeneratedProtocolMessageType('DynamicListener', (_message.Message,), dict(
    DESCRIPTOR = _LISTENERSCONFIGDUMP_DYNAMICLISTENER,
    __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ListenersConfigDump.DynamicListener)
    ))
  ,
  DESCRIPTOR = _LISTENERSCONFIGDUMP,
  __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ListenersConfigDump)
  ))
_sym_db.RegisterMessage(ListenersConfigDump)
_sym_db.RegisterMessage(ListenersConfigDump.StaticListener)
_sym_db.RegisterMessage(ListenersConfigDump.DynamicListener)

ClustersConfigDump = _reflection.GeneratedProtocolMessageType('ClustersConfigDump', (_message.Message,), dict(

  StaticCluster = _reflection.GeneratedProtocolMessageType('StaticCluster', (_message.Message,), dict(
    DESCRIPTOR = _CLUSTERSCONFIGDUMP_STATICCLUSTER,
    __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ClustersConfigDump.StaticCluster)
    ))
  ,

  DynamicCluster = _reflection.GeneratedProtocolMessageType('DynamicCluster', (_message.Message,), dict(
    DESCRIPTOR = _CLUSTERSCONFIGDUMP_DYNAMICCLUSTER,
    __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ClustersConfigDump.DynamicCluster)
    ))
  ,
  DESCRIPTOR = _CLUSTERSCONFIGDUMP,
  __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ClustersConfigDump)
  ))
_sym_db.RegisterMessage(ClustersConfigDump)
_sym_db.RegisterMessage(ClustersConfigDump.StaticCluster)
_sym_db.RegisterMessage(ClustersConfigDump.DynamicCluster)

RoutesConfigDump = _reflection.GeneratedProtocolMessageType('RoutesConfigDump', (_message.Message,), dict(

  StaticRouteConfig = _reflection.GeneratedProtocolMessageType('StaticRouteConfig', (_message.Message,), dict(
    DESCRIPTOR = _ROUTESCONFIGDUMP_STATICROUTECONFIG,
    __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.RoutesConfigDump.StaticRouteConfig)
    ))
  ,

  DynamicRouteConfig = _reflection.GeneratedProtocolMessageType('DynamicRouteConfig', (_message.Message,), dict(
    DESCRIPTOR = _ROUTESCONFIGDUMP_DYNAMICROUTECONFIG,
    __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.RoutesConfigDump.DynamicRouteConfig)
    ))
  ,
  DESCRIPTOR = _ROUTESCONFIGDUMP,
  __module__ = 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.RoutesConfigDump)
  ))
_sym_db.RegisterMessage(RoutesConfigDump)
_sym_db.RegisterMessage(RoutesConfigDump.StaticRouteConfig)
_sym_db.RegisterMessage(RoutesConfigDump.DynamicRouteConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!io.envoyproxy.envoy.admin.v2alphaB\017ConfigDumpProtoP\001'))
_CONFIGDUMP.fields_by_name['configs'].has_options = True
_CONFIGDUMP.fields_by_name['configs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_BOOTSTRAPCONFIGDUMP.fields_by_name['bootstrap'].has_options = True
_BOOTSTRAPCONFIGDUMP.fields_by_name['bootstrap']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_LISTENERSCONFIGDUMP.fields_by_name['static_listeners'].has_options = True
_LISTENERSCONFIGDUMP.fields_by_name['static_listeners']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_LISTENERSCONFIGDUMP.fields_by_name['dynamic_active_listeners'].has_options = True
_LISTENERSCONFIGDUMP.fields_by_name['dynamic_active_listeners']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_LISTENERSCONFIGDUMP.fields_by_name['dynamic_warming_listeners'].has_options = True
_LISTENERSCONFIGDUMP.fields_by_name['dynamic_warming_listeners']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_LISTENERSCONFIGDUMP.fields_by_name['dynamic_draining_listeners'].has_options = True
_LISTENERSCONFIGDUMP.fields_by_name['dynamic_draining_listeners']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_CLUSTERSCONFIGDUMP.fields_by_name['static_clusters'].has_options = True
_CLUSTERSCONFIGDUMP.fields_by_name['static_clusters']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_CLUSTERSCONFIGDUMP.fields_by_name['dynamic_active_clusters'].has_options = True
_CLUSTERSCONFIGDUMP.fields_by_name['dynamic_active_clusters']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_CLUSTERSCONFIGDUMP.fields_by_name['dynamic_warming_clusters'].has_options = True
_CLUSTERSCONFIGDUMP.fields_by_name['dynamic_warming_clusters']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_ROUTESCONFIGDUMP.fields_by_name['static_route_configs'].has_options = True
_ROUTESCONFIGDUMP.fields_by_name['static_route_configs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_ROUTESCONFIGDUMP.fields_by_name['dynamic_route_configs'].has_options = True
_ROUTESCONFIGDUMP.fields_by_name['dynamic_route_configs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
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
