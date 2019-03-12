# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/data/tap/v2alpha/http.proto

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
from envoy.data.tap.v2alpha import common_pb2 as envoy_dot_data_dot_tap_dot_v2alpha_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/data/tap/v2alpha/http.proto',
  package='envoy.data.tap.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n!envoy/data/tap/v2alpha/http.proto\x12\x16\x65nvoy.data.tap.v2alpha\x1a\x1c\x65nvoy/api/v2/core/base.proto\x1a#envoy/data/tap/v2alpha/common.proto\"\xb7\x02\n\x11HttpBufferedTrace\x12\x42\n\x07request\x18\x01 \x01(\x0b\x32\x31.envoy.data.tap.v2alpha.HttpBufferedTrace.Message\x12\x43\n\x08response\x18\x02 \x01(\x0b\x32\x31.envoy.data.tap.v2alpha.HttpBufferedTrace.Message\x1a\x98\x01\n\x07Message\x12/\n\x07headers\x18\x01 \x03(\x0b\x32\x1e.envoy.api.v2.core.HeaderValue\x12*\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x1c.envoy.data.tap.v2alpha.Body\x12\x30\n\x08trailers\x18\x03 \x03(\x0b\x32\x1e.envoy.api.v2.core.HeaderValue\"\x9e\x03\n\x18HttpStreamedTraceSegment\x12\x10\n\x08trace_id\x18\x01 \x01(\x04\x12\x37\n\x0frequest_headers\x18\x02 \x01(\x0b\x32\x1c.envoy.api.v2.core.HeaderMapH\x00\x12:\n\x12request_body_chunk\x18\x03 \x01(\x0b\x32\x1c.envoy.data.tap.v2alpha.BodyH\x00\x12\x38\n\x10request_trailers\x18\x04 \x01(\x0b\x32\x1c.envoy.api.v2.core.HeaderMapH\x00\x12\x38\n\x10response_headers\x18\x05 \x01(\x0b\x32\x1c.envoy.api.v2.core.HeaderMapH\x00\x12;\n\x13response_body_chunk\x18\x06 \x01(\x0b\x32\x1c.envoy.data.tap.v2alpha.BodyH\x00\x12\x39\n\x11response_trailers\x18\x07 \x01(\x0b\x32\x1c.envoy.api.v2.core.HeaderMapH\x00\x42\x0f\n\rmessage_pieceB3\n$io.envoyproxy.envoy.data.tap.v2alphaB\tHttpProtoP\x01\x62\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_base__pb2.DESCRIPTOR,envoy_dot_data_dot_tap_dot_v2alpha_dot_common__pb2.DESCRIPTOR,])




_HTTPBUFFEREDTRACE_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='envoy.data.tap.v2alpha.HttpBufferedTrace.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='headers', full_name='envoy.data.tap.v2alpha.HttpBufferedTrace.Message.headers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='envoy.data.tap.v2alpha.HttpBufferedTrace.Message.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trailers', full_name='envoy.data.tap.v2alpha.HttpBufferedTrace.Message.trailers', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  ],
  serialized_start=288,
  serialized_end=440,
)

_HTTPBUFFEREDTRACE = _descriptor.Descriptor(
  name='HttpBufferedTrace',
  full_name='envoy.data.tap.v2alpha.HttpBufferedTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='envoy.data.tap.v2alpha.HttpBufferedTrace.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response', full_name='envoy.data.tap.v2alpha.HttpBufferedTrace.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_HTTPBUFFEREDTRACE_MESSAGE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=440,
)


_HTTPSTREAMEDTRACESEGMENT = _descriptor.Descriptor(
  name='HttpStreamedTraceSegment',
  full_name='envoy.data.tap.v2alpha.HttpStreamedTraceSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='envoy.data.tap.v2alpha.HttpStreamedTraceSegment.trace_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_headers', full_name='envoy.data.tap.v2alpha.HttpStreamedTraceSegment.request_headers', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_body_chunk', full_name='envoy.data.tap.v2alpha.HttpStreamedTraceSegment.request_body_chunk', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_trailers', full_name='envoy.data.tap.v2alpha.HttpStreamedTraceSegment.request_trailers', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_headers', full_name='envoy.data.tap.v2alpha.HttpStreamedTraceSegment.response_headers', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_body_chunk', full_name='envoy.data.tap.v2alpha.HttpStreamedTraceSegment.response_body_chunk', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_trailers', full_name='envoy.data.tap.v2alpha.HttpStreamedTraceSegment.response_trailers', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='message_piece', full_name='envoy.data.tap.v2alpha.HttpStreamedTraceSegment.message_piece',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=443,
  serialized_end=857,
)

_HTTPBUFFEREDTRACE_MESSAGE.fields_by_name['headers'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._HEADERVALUE
_HTTPBUFFEREDTRACE_MESSAGE.fields_by_name['body'].message_type = envoy_dot_data_dot_tap_dot_v2alpha_dot_common__pb2._BODY
_HTTPBUFFEREDTRACE_MESSAGE.fields_by_name['trailers'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._HEADERVALUE
_HTTPBUFFEREDTRACE_MESSAGE.containing_type = _HTTPBUFFEREDTRACE
_HTTPBUFFEREDTRACE.fields_by_name['request'].message_type = _HTTPBUFFEREDTRACE_MESSAGE
_HTTPBUFFEREDTRACE.fields_by_name['response'].message_type = _HTTPBUFFEREDTRACE_MESSAGE
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['request_headers'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._HEADERMAP
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['request_body_chunk'].message_type = envoy_dot_data_dot_tap_dot_v2alpha_dot_common__pb2._BODY
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['request_trailers'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._HEADERMAP
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['response_headers'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._HEADERMAP
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['response_body_chunk'].message_type = envoy_dot_data_dot_tap_dot_v2alpha_dot_common__pb2._BODY
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['response_trailers'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._HEADERMAP
_HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece'].fields.append(
  _HTTPSTREAMEDTRACESEGMENT.fields_by_name['request_headers'])
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['request_headers'].containing_oneof = _HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece']
_HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece'].fields.append(
  _HTTPSTREAMEDTRACESEGMENT.fields_by_name['request_body_chunk'])
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['request_body_chunk'].containing_oneof = _HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece']
_HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece'].fields.append(
  _HTTPSTREAMEDTRACESEGMENT.fields_by_name['request_trailers'])
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['request_trailers'].containing_oneof = _HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece']
_HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece'].fields.append(
  _HTTPSTREAMEDTRACESEGMENT.fields_by_name['response_headers'])
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['response_headers'].containing_oneof = _HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece']
_HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece'].fields.append(
  _HTTPSTREAMEDTRACESEGMENT.fields_by_name['response_body_chunk'])
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['response_body_chunk'].containing_oneof = _HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece']
_HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece'].fields.append(
  _HTTPSTREAMEDTRACESEGMENT.fields_by_name['response_trailers'])
_HTTPSTREAMEDTRACESEGMENT.fields_by_name['response_trailers'].containing_oneof = _HTTPSTREAMEDTRACESEGMENT.oneofs_by_name['message_piece']
DESCRIPTOR.message_types_by_name['HttpBufferedTrace'] = _HTTPBUFFEREDTRACE
DESCRIPTOR.message_types_by_name['HttpStreamedTraceSegment'] = _HTTPSTREAMEDTRACESEGMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HttpBufferedTrace = _reflection.GeneratedProtocolMessageType('HttpBufferedTrace', (_message.Message,), dict(

  Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
    DESCRIPTOR = _HTTPBUFFEREDTRACE_MESSAGE,
    __module__ = 'envoy.data.tap.v2alpha.http_pb2'
    # @@protoc_insertion_point(class_scope:envoy.data.tap.v2alpha.HttpBufferedTrace.Message)
    ))
  ,
  DESCRIPTOR = _HTTPBUFFEREDTRACE,
  __module__ = 'envoy.data.tap.v2alpha.http_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.tap.v2alpha.HttpBufferedTrace)
  ))
_sym_db.RegisterMessage(HttpBufferedTrace)
_sym_db.RegisterMessage(HttpBufferedTrace.Message)

HttpStreamedTraceSegment = _reflection.GeneratedProtocolMessageType('HttpStreamedTraceSegment', (_message.Message,), dict(
  DESCRIPTOR = _HTTPSTREAMEDTRACESEGMENT,
  __module__ = 'envoy.data.tap.v2alpha.http_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.tap.v2alpha.HttpStreamedTraceSegment)
  ))
_sym_db.RegisterMessage(HttpStreamedTraceSegment)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$io.envoyproxy.envoy.data.tap.v2alphaB\tHttpProtoP\001'))
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