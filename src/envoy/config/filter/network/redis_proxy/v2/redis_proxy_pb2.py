# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/network/redis_proxy/v2/redis_proxy.proto

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
from validate import validate_pb2 as validate_dot_validate__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/filter/network/redis_proxy/v2/redis_proxy.proto',
  package='envoy.config.filter.network.redis_proxy.v2',
  syntax='proto3',
  serialized_pb=_b('\n<envoy/config/filter/network/redis_proxy/v2/redis_proxy.proto\x12*envoy.config.filter.network.redis_proxy.v2\x1a\x1egoogle/protobuf/duration.proto\x1a\x17validate/validate.proto\x1a\x14gogoproto/gogo.proto\"\x9e\x02\n\nRedisProxy\x12\x1e\n\x0bstat_prefix\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12\x1a\n\x07\x63luster\x18\x02 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12\x65\n\x08settings\x18\x03 \x01(\x0b\x32G.envoy.config.filter.network.redis_proxy.v2.RedisProxy.ConnPoolSettingsB\n\xba\xe9\xc0\x03\x05\x8a\x01\x02\x10\x01\x1am\n\x10\x43onnPoolSettings\x12=\n\nop_timeout\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0e\xba\xe9\xc0\x03\x05\xaa\x01\x02\x08\x01\x98\xdf\x1f\x01\x12\x1a\n\x12\x65nable_hashtagging\x18\x02 \x01(\x08\x42Q\n8io.envoyproxy.envoy.config.filter.network.redis_proxy.v2B\x0fRedisProxyProtoP\x01Z\x02v2b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_REDISPROXY_CONNPOOLSETTINGS = _descriptor.Descriptor(
  name='ConnPoolSettings',
  full_name='envoy.config.filter.network.redis_proxy.v2.RedisProxy.ConnPoolSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op_timeout', full_name='envoy.config.filter.network.redis_proxy.v2.RedisProxy.ConnPoolSettings.op_timeout', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\252\001\002\010\001\230\337\037\001'))),
    _descriptor.FieldDescriptor(
      name='enable_hashtagging', full_name='envoy.config.filter.network.redis_proxy.v2.RedisProxy.ConnPoolSettings.enable_hashtagging', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=365,
  serialized_end=474,
)

_REDISPROXY = _descriptor.Descriptor(
  name='RedisProxy',
  full_name='envoy.config.filter.network.redis_proxy.v2.RedisProxy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stat_prefix', full_name='envoy.config.filter.network.redis_proxy.v2.RedisProxy.stat_prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='cluster', full_name='envoy.config.filter.network.redis_proxy.v2.RedisProxy.cluster', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='settings', full_name='envoy.config.filter.network.redis_proxy.v2.RedisProxy.settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[_REDISPROXY_CONNPOOLSETTINGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=474,
)

_REDISPROXY_CONNPOOLSETTINGS.fields_by_name['op_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_REDISPROXY_CONNPOOLSETTINGS.containing_type = _REDISPROXY
_REDISPROXY.fields_by_name['settings'].message_type = _REDISPROXY_CONNPOOLSETTINGS
DESCRIPTOR.message_types_by_name['RedisProxy'] = _REDISPROXY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedisProxy = _reflection.GeneratedProtocolMessageType('RedisProxy', (_message.Message,), dict(

  ConnPoolSettings = _reflection.GeneratedProtocolMessageType('ConnPoolSettings', (_message.Message,), dict(
    DESCRIPTOR = _REDISPROXY_CONNPOOLSETTINGS,
    __module__ = 'envoy.config.filter.network.redis_proxy.v2.redis_proxy_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.network.redis_proxy.v2.RedisProxy.ConnPoolSettings)
    ))
  ,
  DESCRIPTOR = _REDISPROXY,
  __module__ = 'envoy.config.filter.network.redis_proxy.v2.redis_proxy_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.redis_proxy.v2.RedisProxy)
  ))
_sym_db.RegisterMessage(RedisProxy)
_sym_db.RegisterMessage(RedisProxy.ConnPoolSettings)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n8io.envoyproxy.envoy.config.filter.network.redis_proxy.v2B\017RedisProxyProtoP\001Z\002v2'))
_REDISPROXY_CONNPOOLSETTINGS.fields_by_name['op_timeout'].has_options = True
_REDISPROXY_CONNPOOLSETTINGS.fields_by_name['op_timeout']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\252\001\002\010\001\230\337\037\001'))
_REDISPROXY.fields_by_name['stat_prefix'].has_options = True
_REDISPROXY.fields_by_name['stat_prefix']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_REDISPROXY.fields_by_name['cluster'].has_options = True
_REDISPROXY.fields_by_name['cluster']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_REDISPROXY.fields_by_name['settings'].has_options = True
_REDISPROXY.fields_by_name['settings']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001'))
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
