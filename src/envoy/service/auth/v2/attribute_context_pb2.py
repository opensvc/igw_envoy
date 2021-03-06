# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/auth/v2/attribute_context.proto

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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/service/auth/v2/attribute_context.proto',
  package='envoy.service.auth.v2',
  syntax='proto3',
  serialized_pb=_b('\n-envoy/service/auth/v2/attribute_context.proto\x12\x15\x65nvoy.service.auth.v2\x1a\x1f\x65nvoy/api/v2/core/address.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd2\x07\n\x10\x41ttributeContext\x12<\n\x06source\x18\x01 \x01(\x0b\x32,.envoy.service.auth.v2.AttributeContext.Peer\x12\x41\n\x0b\x64\x65stination\x18\x02 \x01(\x0b\x32,.envoy.service.auth.v2.AttributeContext.Peer\x12@\n\x07request\x18\x04 \x01(\x0b\x32/.envoy.service.auth.v2.AttributeContext.Request\x12Z\n\x12\x63ontext_extensions\x18\n \x03(\x0b\x32>.envoy.service.auth.v2.AttributeContext.ContextExtensionsEntry\x1a\xd0\x01\n\x04Peer\x12+\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1a.envoy.api.v2.core.Address\x12\x0f\n\x07service\x18\x02 \x01(\t\x12H\n\x06labels\x18\x03 \x03(\x0b\x32\x38.envoy.service.auth.v2.AttributeContext.Peer.LabelsEntry\x12\x11\n\tprincipal\x18\x04 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1av\n\x07Request\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\x04http\x18\x02 \x01(\x0b\x32\x33.envoy.service.auth.v2.AttributeContext.HttpRequest\x1a\x99\x02\n\x0bHttpRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12Q\n\x07headers\x18\x03 \x03(\x0b\x32@.envoy.service.auth.v2.AttributeContext.HttpRequest.HeadersEntry\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0e\n\x06scheme\x18\x06 \x01(\t\x12\r\n\x05query\x18\x07 \x01(\t\x12\x10\n\x08\x66ragment\x18\x08 \x01(\t\x12\x0c\n\x04size\x18\t \x01(\x03\x12\x10\n\x08protocol\x18\n \x01(\t\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16\x43ontextExtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42>\n#io.envoyproxy.envoy.service.auth.v2B\x15\x41ttributeContextProtoP\x01\x62\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_address__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ATTRIBUTECONTEXT_PEER_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='envoy.service.auth.v2.AttributeContext.Peer.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.service.auth.v2.AttributeContext.Peer.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='envoy.service.auth.v2.AttributeContext.Peer.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=655,
)

_ATTRIBUTECONTEXT_PEER = _descriptor.Descriptor(
  name='Peer',
  full_name='envoy.service.auth.v2.AttributeContext.Peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='envoy.service.auth.v2.AttributeContext.Peer.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service', full_name='envoy.service.auth.v2.AttributeContext.Peer.service', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='envoy.service.auth.v2.AttributeContext.Peer.labels', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='principal', full_name='envoy.service.auth.v2.AttributeContext.Peer.principal', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTECONTEXT_PEER_LABELSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=655,
)

_ATTRIBUTECONTEXT_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='envoy.service.auth.v2.AttributeContext.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='envoy.service.auth.v2.AttributeContext.Request.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='http', full_name='envoy.service.auth.v2.AttributeContext.Request.http', index=1,
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
  serialized_start=657,
  serialized_end=775,
)

_ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY = _descriptor.Descriptor(
  name='HeadersEntry',
  full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.HeadersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.HeadersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.HeadersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1013,
  serialized_end=1059,
)

_ATTRIBUTECONTEXT_HTTPREQUEST = _descriptor.Descriptor(
  name='HttpRequest',
  full_name='envoy.service.auth.v2.AttributeContext.HttpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.method', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='headers', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.host', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scheme', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.scheme', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.query', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fragment', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.fragment', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.size', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='envoy.service.auth.v2.AttributeContext.HttpRequest.protocol', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=1059,
)

_ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY = _descriptor.Descriptor(
  name='ContextExtensionsEntry',
  full_name='envoy.service.auth.v2.AttributeContext.ContextExtensionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.service.auth.v2.AttributeContext.ContextExtensionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='envoy.service.auth.v2.AttributeContext.ContextExtensionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1061,
  serialized_end=1117,
)

_ATTRIBUTECONTEXT = _descriptor.Descriptor(
  name='AttributeContext',
  full_name='envoy.service.auth.v2.AttributeContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='envoy.service.auth.v2.AttributeContext.source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination', full_name='envoy.service.auth.v2.AttributeContext.destination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request', full_name='envoy.service.auth.v2.AttributeContext.request', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context_extensions', full_name='envoy.service.auth.v2.AttributeContext.context_extensions', index=3,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTECONTEXT_PEER, _ATTRIBUTECONTEXT_REQUEST, _ATTRIBUTECONTEXT_HTTPREQUEST, _ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=1117,
)

_ATTRIBUTECONTEXT_PEER_LABELSENTRY.containing_type = _ATTRIBUTECONTEXT_PEER
_ATTRIBUTECONTEXT_PEER.fields_by_name['address'].message_type = envoy_dot_api_dot_v2_dot_core_dot_address__pb2._ADDRESS
_ATTRIBUTECONTEXT_PEER.fields_by_name['labels'].message_type = _ATTRIBUTECONTEXT_PEER_LABELSENTRY
_ATTRIBUTECONTEXT_PEER.containing_type = _ATTRIBUTECONTEXT
_ATTRIBUTECONTEXT_REQUEST.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTRIBUTECONTEXT_REQUEST.fields_by_name['http'].message_type = _ATTRIBUTECONTEXT_HTTPREQUEST
_ATTRIBUTECONTEXT_REQUEST.containing_type = _ATTRIBUTECONTEXT
_ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY.containing_type = _ATTRIBUTECONTEXT_HTTPREQUEST
_ATTRIBUTECONTEXT_HTTPREQUEST.fields_by_name['headers'].message_type = _ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY
_ATTRIBUTECONTEXT_HTTPREQUEST.containing_type = _ATTRIBUTECONTEXT
_ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY.containing_type = _ATTRIBUTECONTEXT
_ATTRIBUTECONTEXT.fields_by_name['source'].message_type = _ATTRIBUTECONTEXT_PEER
_ATTRIBUTECONTEXT.fields_by_name['destination'].message_type = _ATTRIBUTECONTEXT_PEER
_ATTRIBUTECONTEXT.fields_by_name['request'].message_type = _ATTRIBUTECONTEXT_REQUEST
_ATTRIBUTECONTEXT.fields_by_name['context_extensions'].message_type = _ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY
DESCRIPTOR.message_types_by_name['AttributeContext'] = _ATTRIBUTECONTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttributeContext = _reflection.GeneratedProtocolMessageType('AttributeContext', (_message.Message,), dict(

  Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), dict(

    LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
      DESCRIPTOR = _ATTRIBUTECONTEXT_PEER_LABELSENTRY,
      __module__ = 'envoy.service.auth.v2.attribute_context_pb2'
      # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.Peer.LabelsEntry)
      ))
    ,
    DESCRIPTOR = _ATTRIBUTECONTEXT_PEER,
    __module__ = 'envoy.service.auth.v2.attribute_context_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.Peer)
    ))
  ,

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTECONTEXT_REQUEST,
    __module__ = 'envoy.service.auth.v2.attribute_context_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.Request)
    ))
  ,

  HttpRequest = _reflection.GeneratedProtocolMessageType('HttpRequest', (_message.Message,), dict(

    HeadersEntry = _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), dict(
      DESCRIPTOR = _ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY,
      __module__ = 'envoy.service.auth.v2.attribute_context_pb2'
      # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.HttpRequest.HeadersEntry)
      ))
    ,
    DESCRIPTOR = _ATTRIBUTECONTEXT_HTTPREQUEST,
    __module__ = 'envoy.service.auth.v2.attribute_context_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.HttpRequest)
    ))
  ,

  ContextExtensionsEntry = _reflection.GeneratedProtocolMessageType('ContextExtensionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY,
    __module__ = 'envoy.service.auth.v2.attribute_context_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.ContextExtensionsEntry)
    ))
  ,
  DESCRIPTOR = _ATTRIBUTECONTEXT,
  __module__ = 'envoy.service.auth.v2.attribute_context_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext)
  ))
_sym_db.RegisterMessage(AttributeContext)
_sym_db.RegisterMessage(AttributeContext.Peer)
_sym_db.RegisterMessage(AttributeContext.Peer.LabelsEntry)
_sym_db.RegisterMessage(AttributeContext.Request)
_sym_db.RegisterMessage(AttributeContext.HttpRequest)
_sym_db.RegisterMessage(AttributeContext.HttpRequest.HeadersEntry)
_sym_db.RegisterMessage(AttributeContext.ContextExtensionsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#io.envoyproxy.envoy.service.auth.v2B\025AttributeContextProtoP\001'))
_ATTRIBUTECONTEXT_PEER_LABELSENTRY.has_options = True
_ATTRIBUTECONTEXT_PEER_LABELSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY.has_options = True
_ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY.has_options = True
_ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
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
