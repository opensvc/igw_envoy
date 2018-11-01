# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/ratelimit/v2/rls.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.core import grpc_service_pb2 as envoy_dot_api_dot_v2_dot_core_dot_grpc__service__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/ratelimit/v2/rls.proto',
  package='envoy.config.ratelimit.v2',
  syntax='proto3',
  serialized_pb=_b('\n#envoy/config/ratelimit/v2/rls.proto\x12\x19\x65nvoy.config.ratelimit.v2\x1a$envoy/api/v2/core/grpc_service.proto\x1a\x17validate/validate.proto\"\xb3\x01\n\x16RateLimitServiceConfig\x12#\n\x0c\x63luster_name\x18\x01 \x01(\tB\x0b\x18\x01\xba\xe9\xc0\x03\x04r\x02 \x01H\x00\x12\x36\n\x0cgrpc_service\x18\x02 \x01(\x0b\x32\x1e.envoy.api.v2.core.GrpcServiceH\x00\x12 \n\x14use_data_plane_proto\x18\x03 \x01(\x08\x42\x02\x18\x01\x42\x1a\n\x11service_specifier\x12\x05\xb8\xe9\xc0\x03\x01\x42\x04Z\x02v2b\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_grpc__service__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_RATELIMITSERVICECONFIG = _descriptor.Descriptor(
  name='RateLimitServiceConfig',
  full_name='envoy.config.ratelimit.v2.RateLimitServiceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_name', full_name='envoy.config.ratelimit.v2.RateLimitServiceConfig.cluster_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='grpc_service', full_name='envoy.config.ratelimit.v2.RateLimitServiceConfig.grpc_service', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_data_plane_proto', full_name='envoy.config.ratelimit.v2.RateLimitServiceConfig.use_data_plane_proto', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
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
      name='service_specifier', full_name='envoy.config.ratelimit.v2.RateLimitServiceConfig.service_specifier',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=130,
  serialized_end=309,
)

_RATELIMITSERVICECONFIG.fields_by_name['grpc_service'].message_type = envoy_dot_api_dot_v2_dot_core_dot_grpc__service__pb2._GRPCSERVICE
_RATELIMITSERVICECONFIG.oneofs_by_name['service_specifier'].fields.append(
  _RATELIMITSERVICECONFIG.fields_by_name['cluster_name'])
_RATELIMITSERVICECONFIG.fields_by_name['cluster_name'].containing_oneof = _RATELIMITSERVICECONFIG.oneofs_by_name['service_specifier']
_RATELIMITSERVICECONFIG.oneofs_by_name['service_specifier'].fields.append(
  _RATELIMITSERVICECONFIG.fields_by_name['grpc_service'])
_RATELIMITSERVICECONFIG.fields_by_name['grpc_service'].containing_oneof = _RATELIMITSERVICECONFIG.oneofs_by_name['service_specifier']
DESCRIPTOR.message_types_by_name['RateLimitServiceConfig'] = _RATELIMITSERVICECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RateLimitServiceConfig = _reflection.GeneratedProtocolMessageType('RateLimitServiceConfig', (_message.Message,), dict(
  DESCRIPTOR = _RATELIMITSERVICECONFIG,
  __module__ = 'envoy.config.ratelimit.v2.rls_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.ratelimit.v2.RateLimitServiceConfig)
  ))
_sym_db.RegisterMessage(RateLimitServiceConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\002v2'))
_RATELIMITSERVICECONFIG.oneofs_by_name['service_specifier'].has_options = True
_RATELIMITSERVICECONFIG.oneofs_by_name['service_specifier']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_RATELIMITSERVICECONFIG.fields_by_name['cluster_name'].has_options = True
_RATELIMITSERVICECONFIG.fields_by_name['cluster_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001\272\351\300\003\004r\002 \001'))
_RATELIMITSERVICECONFIG.fields_by_name['use_data_plane_proto'].has_options = True
_RATELIMITSERVICECONFIG.fields_by_name['use_data_plane_proto']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
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
