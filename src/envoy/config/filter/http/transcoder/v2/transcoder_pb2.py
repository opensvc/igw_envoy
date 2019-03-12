# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/http/transcoder/v2/transcoder.proto

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
  name='envoy/config/filter/http/transcoder/v2/transcoder.proto',
  package='envoy.config.filter.http.transcoder.v2',
  syntax='proto3',
  serialized_pb=_b('\n7envoy/config/filter/http/transcoder/v2/transcoder.proto\x12&envoy.config.filter.http.transcoder.v2\x1a\x17validate/validate.proto\"\xc7\x03\n\x12GrpcJsonTranscoder\x12\x1a\n\x10proto_descriptor\x18\x01 \x01(\tH\x00\x12\x1e\n\x14proto_descriptor_bin\x18\x04 \x01(\x0cH\x00\x12\x1c\n\x08services\x18\x02 \x03(\tB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x01\x12^\n\rprint_options\x18\x03 \x01(\x0b\x32G.envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.PrintOptions\x12$\n\x1cmatch_incoming_request_route\x18\x05 \x01(\x08\x12 \n\x18ignored_query_parameters\x18\x06 \x03(\t\x1a\x95\x01\n\x0cPrintOptions\x12\x16\n\x0e\x61\x64\x64_whitespace\x18\x01 \x01(\x08\x12%\n\x1d\x61lways_print_primitive_fields\x18\x02 \x01(\x08\x12\"\n\x1a\x61lways_print_enums_as_ints\x18\x03 \x01(\x08\x12\"\n\x1apreserve_proto_field_names\x18\x04 \x01(\x08\x42\x17\n\x0e\x64\x65scriptor_set\x12\x05\xb8\xe9\xc0\x03\x01\x42M\n4io.envoyproxy.envoy.config.filter.http.transcoder.v2B\x0fTranscoderProtoP\x01Z\x02v2b\x06proto3')
  ,
  dependencies=[validate_dot_validate__pb2.DESCRIPTOR,])




_GRPCJSONTRANSCODER_PRINTOPTIONS = _descriptor.Descriptor(
  name='PrintOptions',
  full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.PrintOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='add_whitespace', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.PrintOptions.add_whitespace', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='always_print_primitive_fields', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.PrintOptions.always_print_primitive_fields', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='always_print_enums_as_ints', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.PrintOptions.always_print_enums_as_ints', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preserve_proto_field_names', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.PrintOptions.preserve_proto_field_names', index=3,
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
  serialized_start=406,
  serialized_end=555,
)

_GRPCJSONTRANSCODER = _descriptor.Descriptor(
  name='GrpcJsonTranscoder',
  full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proto_descriptor', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.proto_descriptor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proto_descriptor_bin', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.proto_descriptor_bin', index=1,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='services', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.services', index=2,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='print_options', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.print_options', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_incoming_request_route', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.match_incoming_request_route', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignored_query_parameters', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.ignored_query_parameters', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GRPCJSONTRANSCODER_PRINTOPTIONS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='descriptor_set', full_name='envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.descriptor_set',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=125,
  serialized_end=580,
)

_GRPCJSONTRANSCODER_PRINTOPTIONS.containing_type = _GRPCJSONTRANSCODER
_GRPCJSONTRANSCODER.fields_by_name['print_options'].message_type = _GRPCJSONTRANSCODER_PRINTOPTIONS
_GRPCJSONTRANSCODER.oneofs_by_name['descriptor_set'].fields.append(
  _GRPCJSONTRANSCODER.fields_by_name['proto_descriptor'])
_GRPCJSONTRANSCODER.fields_by_name['proto_descriptor'].containing_oneof = _GRPCJSONTRANSCODER.oneofs_by_name['descriptor_set']
_GRPCJSONTRANSCODER.oneofs_by_name['descriptor_set'].fields.append(
  _GRPCJSONTRANSCODER.fields_by_name['proto_descriptor_bin'])
_GRPCJSONTRANSCODER.fields_by_name['proto_descriptor_bin'].containing_oneof = _GRPCJSONTRANSCODER.oneofs_by_name['descriptor_set']
DESCRIPTOR.message_types_by_name['GrpcJsonTranscoder'] = _GRPCJSONTRANSCODER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GrpcJsonTranscoder = _reflection.GeneratedProtocolMessageType('GrpcJsonTranscoder', (_message.Message,), dict(

  PrintOptions = _reflection.GeneratedProtocolMessageType('PrintOptions', (_message.Message,), dict(
    DESCRIPTOR = _GRPCJSONTRANSCODER_PRINTOPTIONS,
    __module__ = 'envoy.config.filter.http.transcoder.v2.transcoder_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder.PrintOptions)
    ))
  ,
  DESCRIPTOR = _GRPCJSONTRANSCODER,
  __module__ = 'envoy.config.filter.http.transcoder.v2.transcoder_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.transcoder.v2.GrpcJsonTranscoder)
  ))
_sym_db.RegisterMessage(GrpcJsonTranscoder)
_sym_db.RegisterMessage(GrpcJsonTranscoder.PrintOptions)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n4io.envoyproxy.envoy.config.filter.http.transcoder.v2B\017TranscoderProtoP\001Z\002v2'))
_GRPCJSONTRANSCODER.oneofs_by_name['descriptor_set'].has_options = True
_GRPCJSONTRANSCODER.oneofs_by_name['descriptor_set']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_GRPCJSONTRANSCODER.fields_by_name['services'].has_options = True
_GRPCJSONTRANSCODER.fields_by_name['services']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))
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
