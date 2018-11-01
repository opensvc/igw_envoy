# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/http/header_to_metadata/v2/header_to_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/filter/http/header_to_metadata/v2/header_to_metadata.proto',
  package='envoy.config.filter.http.header_to_metadata.v2',
  syntax='proto3',
  serialized_pb=_b('\nGenvoy/config/filter/http/header_to_metadata/v2/header_to_metadata.proto\x12.envoy.config.filter.http.header_to_metadata.v2\x1a\x17validate/validate.proto\"\xee\x04\n\x06\x43onfig\x12R\n\rrequest_rules\x18\x01 \x03(\x0b\x32;.envoy.config.filter.http.header_to_metadata.v2.Config.Rule\x12S\n\x0eresponse_rules\x18\x02 \x03(\x0b\x32;.envoy.config.filter.http.header_to_metadata.v2.Config.Rule\x1a\xa1\x01\n\x0cKeyValuePair\x12\x1a\n\x12metadata_namespace\x18\x01 \x01(\t\x12\x16\n\x03key\x18\x02 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12\r\n\x05value\x18\x03 \x01(\t\x12N\n\x04type\x18\x04 \x01(\x0e\x32@.envoy.config.filter.http.header_to_metadata.v2.Config.ValueType\x1a\xf1\x01\n\x04Rule\x12\x19\n\x06header\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12^\n\x11on_header_present\x18\x02 \x01(\x0b\x32\x43.envoy.config.filter.http.header_to_metadata.v2.Config.KeyValuePair\x12^\n\x11on_header_missing\x18\x03 \x01(\x0b\x32\x43.envoy.config.filter.http.header_to_metadata.v2.Config.KeyValuePair\x12\x0e\n\x06remove\x18\x04 \x01(\x08\"#\n\tValueType\x12\n\n\x06STRING\x10\x00\x12\n\n\x06NUMBER\x10\x01\x42\x04Z\x02v2b\x06proto3')
  ,
  dependencies=[validate_dot_validate__pb2.DESCRIPTOR,])



_CONFIG_VALUETYPE = _descriptor.EnumDescriptor(
  name='ValueType',
  full_name='envoy.config.filter.http.header_to_metadata.v2.Config.ValueType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMBER', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=736,
  serialized_end=771,
)
_sym_db.RegisterEnumDescriptor(_CONFIG_VALUETYPE)


_CONFIG_KEYVALUEPAIR = _descriptor.Descriptor(
  name='KeyValuePair',
  full_name='envoy.config.filter.http.header_to_metadata.v2.Config.KeyValuePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata_namespace', full_name='envoy.config.filter.http.header_to_metadata.v2.Config.KeyValuePair.metadata_namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.config.filter.http.header_to_metadata.v2.Config.KeyValuePair.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='value', full_name='envoy.config.filter.http.header_to_metadata.v2.Config.KeyValuePair.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='envoy.config.filter.http.header_to_metadata.v2.Config.KeyValuePair.type', index=3,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=490,
)

_CONFIG_RULE = _descriptor.Descriptor(
  name='Rule',
  full_name='envoy.config.filter.http.header_to_metadata.v2.Config.Rule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='envoy.config.filter.http.header_to_metadata.v2.Config.Rule.header', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='on_header_present', full_name='envoy.config.filter.http.header_to_metadata.v2.Config.Rule.on_header_present', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='on_header_missing', full_name='envoy.config.filter.http.header_to_metadata.v2.Config.Rule.on_header_missing', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remove', full_name='envoy.config.filter.http.header_to_metadata.v2.Config.Rule.remove', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=493,
  serialized_end=734,
)

_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='envoy.config.filter.http.header_to_metadata.v2.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_rules', full_name='envoy.config.filter.http.header_to_metadata.v2.Config.request_rules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_rules', full_name='envoy.config.filter.http.header_to_metadata.v2.Config.response_rules', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONFIG_KEYVALUEPAIR, _CONFIG_RULE, ],
  enum_types=[
    _CONFIG_VALUETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=771,
)

_CONFIG_KEYVALUEPAIR.fields_by_name['type'].enum_type = _CONFIG_VALUETYPE
_CONFIG_KEYVALUEPAIR.containing_type = _CONFIG
_CONFIG_RULE.fields_by_name['on_header_present'].message_type = _CONFIG_KEYVALUEPAIR
_CONFIG_RULE.fields_by_name['on_header_missing'].message_type = _CONFIG_KEYVALUEPAIR
_CONFIG_RULE.containing_type = _CONFIG
_CONFIG.fields_by_name['request_rules'].message_type = _CONFIG_RULE
_CONFIG.fields_by_name['response_rules'].message_type = _CONFIG_RULE
_CONFIG_VALUETYPE.containing_type = _CONFIG
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(

  KeyValuePair = _reflection.GeneratedProtocolMessageType('KeyValuePair', (_message.Message,), dict(
    DESCRIPTOR = _CONFIG_KEYVALUEPAIR,
    __module__ = 'envoy.config.filter.http.header_to_metadata.v2.header_to_metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.http.header_to_metadata.v2.Config.KeyValuePair)
    ))
  ,

  Rule = _reflection.GeneratedProtocolMessageType('Rule', (_message.Message,), dict(
    DESCRIPTOR = _CONFIG_RULE,
    __module__ = 'envoy.config.filter.http.header_to_metadata.v2.header_to_metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.http.header_to_metadata.v2.Config.Rule)
    ))
  ,
  DESCRIPTOR = _CONFIG,
  __module__ = 'envoy.config.filter.http.header_to_metadata.v2.header_to_metadata_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.header_to_metadata.v2.Config)
  ))
_sym_db.RegisterMessage(Config)
_sym_db.RegisterMessage(Config.KeyValuePair)
_sym_db.RegisterMessage(Config.Rule)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\002v2'))
_CONFIG_KEYVALUEPAIR.fields_by_name['key'].has_options = True
_CONFIG_KEYVALUEPAIR.fields_by_name['key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_CONFIG_RULE.fields_by_name['header'].has_options = True
_CONFIG_RULE.fields_by_name['header']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
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
