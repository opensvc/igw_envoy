# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/network/rbac/v2/rbac.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.rbac.v2alpha import rbac_pb2 as envoy_dot_config_dot_rbac_dot_v2alpha_dot_rbac__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/filter/network/rbac/v2/rbac.proto',
  package='envoy.config.filter.network.rbac.v2',
  syntax='proto3',
  serialized_pb=_b('\n.envoy/config/filter/network/rbac/v2/rbac.proto\x12#envoy.config.filter.network.rbac.v2\x1a$envoy/config/rbac/v2alpha/rbac.proto\x1a\x17validate/validate.proto\x1a\x14gogoproto/gogo.proto\"\xa1\x02\n\x04RBAC\x12.\n\x05rules\x18\x01 \x01(\x0b\x32\x1f.envoy.config.rbac.v2alpha.RBAC\x12\x35\n\x0cshadow_rules\x18\x02 \x01(\x0b\x32\x1f.envoy.config.rbac.v2alpha.RBAC\x12\x1e\n\x0bstat_prefix\x18\x03 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12S\n\x10\x65nforcement_type\x18\x04 \x01(\x0e\x32\x39.envoy.config.filter.network.rbac.v2.RBAC.EnforcementType\"=\n\x0f\x45nforcementType\x12\x1a\n\x16ONE_TIME_ON_FIRST_BYTE\x10\x00\x12\x0e\n\nCONTINUOUS\x10\x01\x42\x44\n1io.envoyproxy.envoy.config.filter.network.rbac.v2B\tRbacProtoP\x01Z\x02v2b\x06proto3')
  ,
  dependencies=[envoy_dot_config_dot_rbac_dot_v2alpha_dot_rbac__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])



_RBAC_ENFORCEMENTTYPE = _descriptor.EnumDescriptor(
  name='EnforcementType',
  full_name='envoy.config.filter.network.rbac.v2.RBAC.EnforcementType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ONE_TIME_ON_FIRST_BYTE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINUOUS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=401,
  serialized_end=462,
)
_sym_db.RegisterEnumDescriptor(_RBAC_ENFORCEMENTTYPE)


_RBAC = _descriptor.Descriptor(
  name='RBAC',
  full_name='envoy.config.filter.network.rbac.v2.RBAC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='envoy.config.filter.network.rbac.v2.RBAC.rules', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shadow_rules', full_name='envoy.config.filter.network.rbac.v2.RBAC.shadow_rules', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stat_prefix', full_name='envoy.config.filter.network.rbac.v2.RBAC.stat_prefix', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='enforcement_type', full_name='envoy.config.filter.network.rbac.v2.RBAC.enforcement_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RBAC_ENFORCEMENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=462,
)

_RBAC.fields_by_name['rules'].message_type = envoy_dot_config_dot_rbac_dot_v2alpha_dot_rbac__pb2._RBAC
_RBAC.fields_by_name['shadow_rules'].message_type = envoy_dot_config_dot_rbac_dot_v2alpha_dot_rbac__pb2._RBAC
_RBAC.fields_by_name['enforcement_type'].enum_type = _RBAC_ENFORCEMENTTYPE
_RBAC_ENFORCEMENTTYPE.containing_type = _RBAC
DESCRIPTOR.message_types_by_name['RBAC'] = _RBAC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RBAC = _reflection.GeneratedProtocolMessageType('RBAC', (_message.Message,), dict(
  DESCRIPTOR = _RBAC,
  __module__ = 'envoy.config.filter.network.rbac.v2.rbac_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.rbac.v2.RBAC)
  ))
_sym_db.RegisterMessage(RBAC)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n1io.envoyproxy.envoy.config.filter.network.rbac.v2B\tRbacProtoP\001Z\002v2'))
_RBAC.fields_by_name['stat_prefix'].has_options = True
_RBAC.fields_by_name['stat_prefix']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
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
