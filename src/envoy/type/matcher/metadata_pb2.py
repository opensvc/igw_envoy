# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/matcher/metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.type.matcher import value_pb2 as envoy_dot_type_dot_matcher_dot_value__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/matcher/metadata.proto',
  package='envoy.type.matcher',
  syntax='proto3',
  serialized_pb=_b('\n!envoy/type/matcher/metadata.proto\x12\x12\x65nvoy.type.matcher\x1a\x1e\x65nvoy/type/matcher/value.proto\x1a\x17validate/validate.proto\"\xef\x01\n\x0fMetadataMatcher\x12\x19\n\x06\x66ilter\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12I\n\x04path\x18\x02 \x03(\x0b\x32/.envoy.type.matcher.MetadataMatcher.PathSegmentB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x01\x12;\n\x05value\x18\x03 \x01(\x0b\x32 .envoy.type.matcher.ValueMatcherB\n\xba\xe9\xc0\x03\x05\x8a\x01\x02\x10\x01\x1a\x39\n\x0bPathSegment\x12\x18\n\x03key\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01H\x00\x42\x10\n\x07segment\x12\x05\xb8\xe9\xc0\x03\x01\x42<\n io.envoyproxy.envoy.type.matcherB\rMetadataProtoP\x01Z\x07matcherb\x06proto3')
  ,
  dependencies=[envoy_dot_type_dot_matcher_dot_value__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_METADATAMATCHER_PATHSEGMENT = _descriptor.Descriptor(
  name='PathSegment',
  full_name='envoy.type.matcher.MetadataMatcher.PathSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.type.matcher.MetadataMatcher.PathSegment.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
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
      name='segment', full_name='envoy.type.matcher.MetadataMatcher.PathSegment.segment',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=297,
  serialized_end=354,
)

_METADATAMATCHER = _descriptor.Descriptor(
  name='MetadataMatcher',
  full_name='envoy.type.matcher.MetadataMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter', full_name='envoy.type.matcher.MetadataMatcher.filter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='path', full_name='envoy.type.matcher.MetadataMatcher.path', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='value', full_name='envoy.type.matcher.MetadataMatcher.value', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[_METADATAMATCHER_PATHSEGMENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=354,
)

_METADATAMATCHER_PATHSEGMENT.containing_type = _METADATAMATCHER
_METADATAMATCHER_PATHSEGMENT.oneofs_by_name['segment'].fields.append(
  _METADATAMATCHER_PATHSEGMENT.fields_by_name['key'])
_METADATAMATCHER_PATHSEGMENT.fields_by_name['key'].containing_oneof = _METADATAMATCHER_PATHSEGMENT.oneofs_by_name['segment']
_METADATAMATCHER.fields_by_name['path'].message_type = _METADATAMATCHER_PATHSEGMENT
_METADATAMATCHER.fields_by_name['value'].message_type = envoy_dot_type_dot_matcher_dot_value__pb2._VALUEMATCHER
DESCRIPTOR.message_types_by_name['MetadataMatcher'] = _METADATAMATCHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetadataMatcher = _reflection.GeneratedProtocolMessageType('MetadataMatcher', (_message.Message,), dict(

  PathSegment = _reflection.GeneratedProtocolMessageType('PathSegment', (_message.Message,), dict(
    DESCRIPTOR = _METADATAMATCHER_PATHSEGMENT,
    __module__ = 'envoy.type.matcher.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.matcher.MetadataMatcher.PathSegment)
    ))
  ,
  DESCRIPTOR = _METADATAMATCHER,
  __module__ = 'envoy.type.matcher.metadata_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.MetadataMatcher)
  ))
_sym_db.RegisterMessage(MetadataMatcher)
_sym_db.RegisterMessage(MetadataMatcher.PathSegment)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n io.envoyproxy.envoy.type.matcherB\rMetadataProtoP\001Z\007matcher'))
_METADATAMATCHER_PATHSEGMENT.oneofs_by_name['segment'].has_options = True
_METADATAMATCHER_PATHSEGMENT.oneofs_by_name['segment']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_METADATAMATCHER_PATHSEGMENT.fields_by_name['key'].has_options = True
_METADATAMATCHER_PATHSEGMENT.fields_by_name['key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_METADATAMATCHER.fields_by_name['filter'].has_options = True
_METADATAMATCHER.fields_by_name['filter']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_METADATAMATCHER.fields_by_name['path'].has_options = True
_METADATAMATCHER.fields_by_name['path']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))
_METADATAMATCHER.fields_by_name['value'].has_options = True
_METADATAMATCHER.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001'))
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
