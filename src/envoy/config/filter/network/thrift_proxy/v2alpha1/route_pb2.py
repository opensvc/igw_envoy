# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/network/thrift_proxy/v2alpha1/route.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.core import base_pb2 as envoy_dot_api_dot_v2_dot_core_dot_base__pb2
from envoy.api.v2.route import route_pb2 as envoy_dot_api_dot_v2_dot_route_dot_route__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/filter/network/thrift_proxy/v2alpha1/route.proto',
  package='envoy.config.filter.network.thrift_proxy.v2alpha1',
  syntax='proto3',
  serialized_pb=_b('\n=envoy/config/filter/network/thrift_proxy/v2alpha1/route.proto\x12\x31\x65nvoy.config.filter.network.thrift_proxy.v2alpha1\x1a\x1c\x65nvoy/api/v2/core/base.proto\x1a\x1e\x65nvoy/api/v2/route/route.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17validate/validate.proto\x1a\x14gogoproto/gogo.proto\"r\n\x12RouteConfiguration\x12\x0c\n\x04name\x18\x01 \x01(\t\x12N\n\x06routes\x18\x02 \x03(\x0b\x32\x38.envoy.config.filter.network.thrift_proxy.v2alpha1.RouteB\x04\xc8\xde\x1f\x00\"\xc4\x01\n\x05Route\x12\\\n\x05match\x18\x01 \x01(\x0b\x32=.envoy.config.filter.network.thrift_proxy.v2alpha1.RouteMatchB\x0e\xba\xe9\xc0\x03\x05\x8a\x01\x02\x10\x01\xc8\xde\x1f\x00\x12]\n\x05route\x18\x02 \x01(\x0b\x32>.envoy.config.filter.network.thrift_proxy.v2alpha1.RouteActionB\x0e\xba\xe9\xc0\x03\x05\x8a\x01\x02\x10\x01\xc8\xde\x1f\x00\"\x99\x01\n\nRouteMatch\x12\x15\n\x0bmethod_name\x18\x01 \x01(\tH\x00\x12\x16\n\x0cservice_name\x18\x02 \x01(\tH\x00\x12\x0e\n\x06invert\x18\x03 \x01(\x08\x12\x32\n\x07headers\x18\x04 \x03(\x0b\x32!.envoy.api.v2.route.HeaderMatcherB\x18\n\x0fmatch_specifier\x12\x05\xb8\xe9\xc0\x03\x01\"\x91\x02\n\x0bRouteAction\x12\x1c\n\x07\x63luster\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01H\x00\x12_\n\x11weighted_clusters\x18\x02 \x01(\x0b\x32\x42.envoy.config.filter.network.thrift_proxy.v2alpha1.WeightedClusterH\x00\x12\x33\n\x0emetadata_match\x18\x03 \x01(\x0b\x32\x1b.envoy.api.v2.core.Metadata\x12\x32\n\x0brate_limits\x18\x04 \x03(\x0b\x32\x1d.envoy.api.v2.route.RateLimitB\x1a\n\x11\x63luster_specifier\x12\x05\xb8\xe9\xc0\x03\x01\"\x9a\x02\n\x0fWeightedCluster\x12n\n\x08\x63lusters\x18\x01 \x03(\x0b\x32P.envoy.config.filter.network.thrift_proxy.v2alpha1.WeightedCluster.ClusterWeightB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x01\x1a\x96\x01\n\rClusterWeight\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12\x37\n\x06weight\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\t\xba\xe9\xc0\x03\x04*\x02(\x01\x12\x33\n\x0emetadata_match\x18\x03 \x01(\x0b\x32\x1b.envoy.api.v2.core.MetadataBS\n?io.envoyproxy.envoy.config.filter.network.thrift_proxy.v2alpha1B\nRouteProtoP\x01Z\x02v2b\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_base__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_route_dot_route__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_ROUTECONFIGURATION = _descriptor.Descriptor(
  name='RouteConfiguration',
  full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteConfiguration.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='routes', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteConfiguration.routes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=257,
  serialized_end=371,
)


_ROUTE = _descriptor.Descriptor(
  name='Route',
  full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.Route',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.Route.match', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='route', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.Route.route', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001\310\336\037\000'))),
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
  serialized_start=374,
  serialized_end=570,
)


_ROUTEMATCH = _descriptor.Descriptor(
  name='RouteMatch',
  full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method_name', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteMatch.method_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteMatch.service_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invert', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteMatch.invert', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='headers', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteMatch.headers', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
    _descriptor.OneofDescriptor(
      name='match_specifier', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteMatch.match_specifier',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=573,
  serialized_end=726,
)


_ROUTEACTION = _descriptor.Descriptor(
  name='RouteAction',
  full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteAction.cluster', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='weighted_clusters', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteAction.weighted_clusters', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata_match', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteAction.metadata_match', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rate_limits', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteAction.rate_limits', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
    _descriptor.OneofDescriptor(
      name='cluster_specifier', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.RouteAction.cluster_specifier',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=729,
  serialized_end=1002,
)


_WEIGHTEDCLUSTER_CLUSTERWEIGHT = _descriptor.Descriptor(
  name='ClusterWeight',
  full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.WeightedCluster.ClusterWeight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.WeightedCluster.ClusterWeight.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='weight', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.WeightedCluster.ClusterWeight.weight', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004*\002(\001'))),
    _descriptor.FieldDescriptor(
      name='metadata_match', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.WeightedCluster.ClusterWeight.metadata_match', index=2,
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
  serialized_start=1137,
  serialized_end=1287,
)

_WEIGHTEDCLUSTER = _descriptor.Descriptor(
  name='WeightedCluster',
  full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.WeightedCluster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clusters', full_name='envoy.config.filter.network.thrift_proxy.v2alpha1.WeightedCluster.clusters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))),
  ],
  extensions=[
  ],
  nested_types=[_WEIGHTEDCLUSTER_CLUSTERWEIGHT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1005,
  serialized_end=1287,
)

_ROUTECONFIGURATION.fields_by_name['routes'].message_type = _ROUTE
_ROUTE.fields_by_name['match'].message_type = _ROUTEMATCH
_ROUTE.fields_by_name['route'].message_type = _ROUTEACTION
_ROUTEMATCH.fields_by_name['headers'].message_type = envoy_dot_api_dot_v2_dot_route_dot_route__pb2._HEADERMATCHER
_ROUTEMATCH.oneofs_by_name['match_specifier'].fields.append(
  _ROUTEMATCH.fields_by_name['method_name'])
_ROUTEMATCH.fields_by_name['method_name'].containing_oneof = _ROUTEMATCH.oneofs_by_name['match_specifier']
_ROUTEMATCH.oneofs_by_name['match_specifier'].fields.append(
  _ROUTEMATCH.fields_by_name['service_name'])
_ROUTEMATCH.fields_by_name['service_name'].containing_oneof = _ROUTEMATCH.oneofs_by_name['match_specifier']
_ROUTEACTION.fields_by_name['weighted_clusters'].message_type = _WEIGHTEDCLUSTER
_ROUTEACTION.fields_by_name['metadata_match'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._METADATA
_ROUTEACTION.fields_by_name['rate_limits'].message_type = envoy_dot_api_dot_v2_dot_route_dot_route__pb2._RATELIMIT
_ROUTEACTION.oneofs_by_name['cluster_specifier'].fields.append(
  _ROUTEACTION.fields_by_name['cluster'])
_ROUTEACTION.fields_by_name['cluster'].containing_oneof = _ROUTEACTION.oneofs_by_name['cluster_specifier']
_ROUTEACTION.oneofs_by_name['cluster_specifier'].fields.append(
  _ROUTEACTION.fields_by_name['weighted_clusters'])
_ROUTEACTION.fields_by_name['weighted_clusters'].containing_oneof = _ROUTEACTION.oneofs_by_name['cluster_specifier']
_WEIGHTEDCLUSTER_CLUSTERWEIGHT.fields_by_name['weight'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_WEIGHTEDCLUSTER_CLUSTERWEIGHT.fields_by_name['metadata_match'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._METADATA
_WEIGHTEDCLUSTER_CLUSTERWEIGHT.containing_type = _WEIGHTEDCLUSTER
_WEIGHTEDCLUSTER.fields_by_name['clusters'].message_type = _WEIGHTEDCLUSTER_CLUSTERWEIGHT
DESCRIPTOR.message_types_by_name['RouteConfiguration'] = _ROUTECONFIGURATION
DESCRIPTOR.message_types_by_name['Route'] = _ROUTE
DESCRIPTOR.message_types_by_name['RouteMatch'] = _ROUTEMATCH
DESCRIPTOR.message_types_by_name['RouteAction'] = _ROUTEACTION
DESCRIPTOR.message_types_by_name['WeightedCluster'] = _WEIGHTEDCLUSTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RouteConfiguration = _reflection.GeneratedProtocolMessageType('RouteConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _ROUTECONFIGURATION,
  __module__ = 'envoy.config.filter.network.thrift_proxy.v2alpha1.route_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.thrift_proxy.v2alpha1.RouteConfiguration)
  ))
_sym_db.RegisterMessage(RouteConfiguration)

Route = _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), dict(
  DESCRIPTOR = _ROUTE,
  __module__ = 'envoy.config.filter.network.thrift_proxy.v2alpha1.route_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.thrift_proxy.v2alpha1.Route)
  ))
_sym_db.RegisterMessage(Route)

RouteMatch = _reflection.GeneratedProtocolMessageType('RouteMatch', (_message.Message,), dict(
  DESCRIPTOR = _ROUTEMATCH,
  __module__ = 'envoy.config.filter.network.thrift_proxy.v2alpha1.route_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.thrift_proxy.v2alpha1.RouteMatch)
  ))
_sym_db.RegisterMessage(RouteMatch)

RouteAction = _reflection.GeneratedProtocolMessageType('RouteAction', (_message.Message,), dict(
  DESCRIPTOR = _ROUTEACTION,
  __module__ = 'envoy.config.filter.network.thrift_proxy.v2alpha1.route_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.thrift_proxy.v2alpha1.RouteAction)
  ))
_sym_db.RegisterMessage(RouteAction)

WeightedCluster = _reflection.GeneratedProtocolMessageType('WeightedCluster', (_message.Message,), dict(

  ClusterWeight = _reflection.GeneratedProtocolMessageType('ClusterWeight', (_message.Message,), dict(
    DESCRIPTOR = _WEIGHTEDCLUSTER_CLUSTERWEIGHT,
    __module__ = 'envoy.config.filter.network.thrift_proxy.v2alpha1.route_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.network.thrift_proxy.v2alpha1.WeightedCluster.ClusterWeight)
    ))
  ,
  DESCRIPTOR = _WEIGHTEDCLUSTER,
  __module__ = 'envoy.config.filter.network.thrift_proxy.v2alpha1.route_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.thrift_proxy.v2alpha1.WeightedCluster)
  ))
_sym_db.RegisterMessage(WeightedCluster)
_sym_db.RegisterMessage(WeightedCluster.ClusterWeight)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n?io.envoyproxy.envoy.config.filter.network.thrift_proxy.v2alpha1B\nRouteProtoP\001Z\002v2'))
_ROUTECONFIGURATION.fields_by_name['routes'].has_options = True
_ROUTECONFIGURATION.fields_by_name['routes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_ROUTE.fields_by_name['match'].has_options = True
_ROUTE.fields_by_name['match']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001\310\336\037\000'))
_ROUTE.fields_by_name['route'].has_options = True
_ROUTE.fields_by_name['route']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001\310\336\037\000'))
_ROUTEMATCH.oneofs_by_name['match_specifier'].has_options = True
_ROUTEMATCH.oneofs_by_name['match_specifier']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_ROUTEACTION.oneofs_by_name['cluster_specifier'].has_options = True
_ROUTEACTION.oneofs_by_name['cluster_specifier']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_ROUTEACTION.fields_by_name['cluster'].has_options = True
_ROUTEACTION.fields_by_name['cluster']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_WEIGHTEDCLUSTER_CLUSTERWEIGHT.fields_by_name['name'].has_options = True
_WEIGHTEDCLUSTER_CLUSTERWEIGHT.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_WEIGHTEDCLUSTER_CLUSTERWEIGHT.fields_by_name['weight'].has_options = True
_WEIGHTEDCLUSTER_CLUSTERWEIGHT.fields_by_name['weight']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004*\002(\001'))
_WEIGHTEDCLUSTER.fields_by_name['clusters'].has_options = True
_WEIGHTEDCLUSTER.fields_by_name['clusters']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))
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
