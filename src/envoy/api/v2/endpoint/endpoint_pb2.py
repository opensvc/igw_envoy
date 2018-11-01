# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/api/v2/endpoint/endpoint.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.core import address_pb2 as envoy_dot_api_dot_v2_dot_core_dot_address__pb2
from envoy.api.v2.core import base_pb2 as envoy_dot_api_dot_v2_dot_core_dot_base__pb2
from envoy.api.v2.core import health_check_pb2 as envoy_dot_api_dot_v2_dot_core_dot_health__check__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/api/v2/endpoint/endpoint.proto',
  package='envoy.api.v2.endpoint',
  syntax='proto3',
  serialized_pb=_b('\n$envoy/api/v2/endpoint/endpoint.proto\x12\x15\x65nvoy.api.v2.endpoint\x1a\x1f\x65nvoy/api/v2/core/address.proto\x1a\x1c\x65nvoy/api/v2/core/base.proto\x1a$envoy/api/v2/core/health_check.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17validate/validate.proto\x1a\x14gogoproto/gogo.proto\"\xb0\x01\n\x08\x45ndpoint\x12+\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1a.envoy.api.v2.core.Address\x12N\n\x13health_check_config\x18\x02 \x01(\x0b\x32\x31.envoy.api.v2.endpoint.Endpoint.HealthCheckConfig\x1a\'\n\x11HealthCheckConfig\x12\x12\n\nport_value\x18\x01 \x01(\r\"\xf1\x01\n\nLbEndpoint\x12\x31\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32\x1f.envoy.api.v2.endpoint.Endpoint\x12\x36\n\rhealth_status\x18\x02 \x01(\x0e\x32\x1f.envoy.api.v2.core.HealthStatus\x12-\n\x08metadata\x18\x03 \x01(\x0b\x32\x1b.envoy.api.v2.core.Metadata\x12I\n\x15load_balancing_weight\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x0c\xba\xe9\xc0\x03\x07*\x05\x18\x80\x01(\x01\"\xe0\x01\n\x13LocalityLbEndpoints\x12-\n\x08locality\x18\x01 \x01(\x0b\x32\x1b.envoy.api.v2.core.Locality\x12=\n\x0clb_endpoints\x18\x02 \x03(\x0b\x32!.envoy.api.v2.endpoint.LbEndpointB\x04\xc8\xde\x1f\x00\x12I\n\x15load_balancing_weight\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x0c\xba\xe9\xc0\x03\x07*\x05\x18\x80\x01(\x01\x12\x10\n\x08priority\x18\x05 \x01(\rB\x0eZ\x08\x65ndpoint\xa8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_address__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_core_dot_base__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_core_dot_health__check__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_ENDPOINT_HEALTHCHECKCONFIG = _descriptor.Descriptor(
  name='HealthCheckConfig',
  full_name='envoy.api.v2.endpoint.Endpoint.HealthCheckConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_value', full_name='envoy.api.v2.endpoint.Endpoint.HealthCheckConfig.port_value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=381,
  serialized_end=420,
)

_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='envoy.api.v2.endpoint.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='envoy.api.v2.endpoint.Endpoint.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='health_check_config', full_name='envoy.api.v2.endpoint.Endpoint.health_check_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENDPOINT_HEALTHCHECKCONFIG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=420,
)


_LBENDPOINT = _descriptor.Descriptor(
  name='LbEndpoint',
  full_name='envoy.api.v2.endpoint.LbEndpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='envoy.api.v2.endpoint.LbEndpoint.endpoint', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='health_status', full_name='envoy.api.v2.endpoint.LbEndpoint.health_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='envoy.api.v2.endpoint.LbEndpoint.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='load_balancing_weight', full_name='envoy.api.v2.endpoint.LbEndpoint.load_balancing_weight', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\007*\005\030\200\001(\001'))),
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
  serialized_start=423,
  serialized_end=664,
)


_LOCALITYLBENDPOINTS = _descriptor.Descriptor(
  name='LocalityLbEndpoints',
  full_name='envoy.api.v2.endpoint.LocalityLbEndpoints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='locality', full_name='envoy.api.v2.endpoint.LocalityLbEndpoints.locality', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lb_endpoints', full_name='envoy.api.v2.endpoint.LocalityLbEndpoints.lb_endpoints', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='load_balancing_weight', full_name='envoy.api.v2.endpoint.LocalityLbEndpoints.load_balancing_weight', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\007*\005\030\200\001(\001'))),
    _descriptor.FieldDescriptor(
      name='priority', full_name='envoy.api.v2.endpoint.LocalityLbEndpoints.priority', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=667,
  serialized_end=891,
)

_ENDPOINT_HEALTHCHECKCONFIG.containing_type = _ENDPOINT
_ENDPOINT.fields_by_name['address'].message_type = envoy_dot_api_dot_v2_dot_core_dot_address__pb2._ADDRESS
_ENDPOINT.fields_by_name['health_check_config'].message_type = _ENDPOINT_HEALTHCHECKCONFIG
_LBENDPOINT.fields_by_name['endpoint'].message_type = _ENDPOINT
_LBENDPOINT.fields_by_name['health_status'].enum_type = envoy_dot_api_dot_v2_dot_core_dot_health__check__pb2._HEALTHSTATUS
_LBENDPOINT.fields_by_name['metadata'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._METADATA
_LBENDPOINT.fields_by_name['load_balancing_weight'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_LOCALITYLBENDPOINTS.fields_by_name['locality'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._LOCALITY
_LOCALITYLBENDPOINTS.fields_by_name['lb_endpoints'].message_type = _LBENDPOINT
_LOCALITYLBENDPOINTS.fields_by_name['load_balancing_weight'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
DESCRIPTOR.message_types_by_name['LbEndpoint'] = _LBENDPOINT
DESCRIPTOR.message_types_by_name['LocalityLbEndpoints'] = _LOCALITYLBENDPOINTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), dict(

  HealthCheckConfig = _reflection.GeneratedProtocolMessageType('HealthCheckConfig', (_message.Message,), dict(
    DESCRIPTOR = _ENDPOINT_HEALTHCHECKCONFIG,
    __module__ = 'envoy.api.v2.endpoint.endpoint_pb2'
    # @@protoc_insertion_point(class_scope:envoy.api.v2.endpoint.Endpoint.HealthCheckConfig)
    ))
  ,
  DESCRIPTOR = _ENDPOINT,
  __module__ = 'envoy.api.v2.endpoint.endpoint_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.endpoint.Endpoint)
  ))
_sym_db.RegisterMessage(Endpoint)
_sym_db.RegisterMessage(Endpoint.HealthCheckConfig)

LbEndpoint = _reflection.GeneratedProtocolMessageType('LbEndpoint', (_message.Message,), dict(
  DESCRIPTOR = _LBENDPOINT,
  __module__ = 'envoy.api.v2.endpoint.endpoint_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.endpoint.LbEndpoint)
  ))
_sym_db.RegisterMessage(LbEndpoint)

LocalityLbEndpoints = _reflection.GeneratedProtocolMessageType('LocalityLbEndpoints', (_message.Message,), dict(
  DESCRIPTOR = _LOCALITYLBENDPOINTS,
  __module__ = 'envoy.api.v2.endpoint.endpoint_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.endpoint.LocalityLbEndpoints)
  ))
_sym_db.RegisterMessage(LocalityLbEndpoints)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\010endpoint\250\342\036\001'))
_LBENDPOINT.fields_by_name['load_balancing_weight'].has_options = True
_LBENDPOINT.fields_by_name['load_balancing_weight']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\007*\005\030\200\001(\001'))
_LOCALITYLBENDPOINTS.fields_by_name['lb_endpoints'].has_options = True
_LOCALITYLBENDPOINTS.fields_by_name['lb_endpoints']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_LOCALITYLBENDPOINTS.fields_by_name['load_balancing_weight'].has_options = True
_LOCALITYLBENDPOINTS.fields_by_name['load_balancing_weight']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\007*\005\030\200\001(\001'))
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
