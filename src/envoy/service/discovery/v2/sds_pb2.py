# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/discovery/v2/sds.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2 import discovery_pb2 as envoy_dot_api_dot_v2_dot_discovery__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/service/discovery/v2/sds.proto',
  package='envoy.service.discovery.v2',
  syntax='proto3',
  serialized_pb=_b('\n$envoy/service/discovery/v2/sds.proto\x12\x1a\x65nvoy.service.discovery.v2\x1a\x1c\x65nvoy/api/v2/discovery.proto\x1a\x1cgoogle/api/annotations.proto\"\n\n\x08SdsDummy2\xe3\x01\n\x16SecretDiscoveryService\x12V\n\rStreamSecrets\x12\x1e.envoy.api.v2.DiscoveryRequest\x1a\x1f.envoy.api.v2.DiscoveryResponse\"\x00(\x01\x30\x01\x12q\n\x0c\x46\x65tchSecrets\x12\x1e.envoy.api.v2.DiscoveryRequest\x1a\x1f.envoy.api.v2.DiscoveryResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v2/discovery:secrets:\x01*b\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_discovery__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SDSDUMMY = _descriptor.Descriptor(
  name='SdsDummy',
  full_name='envoy.service.discovery.v2.SdsDummy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=128,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['SdsDummy'] = _SDSDUMMY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SdsDummy = _reflection.GeneratedProtocolMessageType('SdsDummy', (_message.Message,), dict(
  DESCRIPTOR = _SDSDUMMY,
  __module__ = 'envoy.service.discovery.v2.sds_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.discovery.v2.SdsDummy)
  ))
_sym_db.RegisterMessage(SdsDummy)



_SECRETDISCOVERYSERVICE = _descriptor.ServiceDescriptor(
  name='SecretDiscoveryService',
  full_name='envoy.service.discovery.v2.SecretDiscoveryService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=141,
  serialized_end=368,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamSecrets',
    full_name='envoy.service.discovery.v2.SecretDiscoveryService.StreamSecrets',
    index=0,
    containing_service=None,
    input_type=envoy_dot_api_dot_v2_dot_discovery__pb2._DISCOVERYREQUEST,
    output_type=envoy_dot_api_dot_v2_dot_discovery__pb2._DISCOVERYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FetchSecrets',
    full_name='envoy.service.discovery.v2.SecretDiscoveryService.FetchSecrets',
    index=1,
    containing_service=None,
    input_type=envoy_dot_api_dot_v2_dot_discovery__pb2._DISCOVERYREQUEST,
    output_type=envoy_dot_api_dot_v2_dot_discovery__pb2._DISCOVERYRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\032\"\025/v2/discovery:secrets:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_SECRETDISCOVERYSERVICE)

DESCRIPTOR.services_by_name['SecretDiscoveryService'] = _SECRETDISCOVERYSERVICE

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class SecretDiscoveryServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.StreamSecrets = channel.stream_stream(
          '/envoy.service.discovery.v2.SecretDiscoveryService/StreamSecrets',
          request_serializer=envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryRequest.SerializeToString,
          response_deserializer=envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryResponse.FromString,
          )
      self.FetchSecrets = channel.unary_unary(
          '/envoy.service.discovery.v2.SecretDiscoveryService/FetchSecrets',
          request_serializer=envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryRequest.SerializeToString,
          response_deserializer=envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryResponse.FromString,
          )


  class SecretDiscoveryServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def StreamSecrets(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def FetchSecrets(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_SecretDiscoveryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'StreamSecrets': grpc.stream_stream_rpc_method_handler(
            servicer.StreamSecrets,
            request_deserializer=envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryRequest.FromString,
            response_serializer=envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryResponse.SerializeToString,
        ),
        'FetchSecrets': grpc.unary_unary_rpc_method_handler(
            servicer.FetchSecrets,
            request_deserializer=envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryRequest.FromString,
            response_serializer=envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'envoy.service.discovery.v2.SecretDiscoveryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaSecretDiscoveryServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def StreamSecrets(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def FetchSecrets(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaSecretDiscoveryServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def StreamSecrets(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    def FetchSecrets(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    FetchSecrets.future = None


  def beta_create_SecretDiscoveryService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('envoy.service.discovery.v2.SecretDiscoveryService', 'FetchSecrets'): envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryRequest.FromString,
      ('envoy.service.discovery.v2.SecretDiscoveryService', 'StreamSecrets'): envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryRequest.FromString,
    }
    response_serializers = {
      ('envoy.service.discovery.v2.SecretDiscoveryService', 'FetchSecrets'): envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryResponse.SerializeToString,
      ('envoy.service.discovery.v2.SecretDiscoveryService', 'StreamSecrets'): envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryResponse.SerializeToString,
    }
    method_implementations = {
      ('envoy.service.discovery.v2.SecretDiscoveryService', 'FetchSecrets'): face_utilities.unary_unary_inline(servicer.FetchSecrets),
      ('envoy.service.discovery.v2.SecretDiscoveryService', 'StreamSecrets'): face_utilities.stream_stream_inline(servicer.StreamSecrets),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_SecretDiscoveryService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('envoy.service.discovery.v2.SecretDiscoveryService', 'FetchSecrets'): envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryRequest.SerializeToString,
      ('envoy.service.discovery.v2.SecretDiscoveryService', 'StreamSecrets'): envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryRequest.SerializeToString,
    }
    response_deserializers = {
      ('envoy.service.discovery.v2.SecretDiscoveryService', 'FetchSecrets'): envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryResponse.FromString,
      ('envoy.service.discovery.v2.SecretDiscoveryService', 'StreamSecrets'): envoy_dot_api_dot_v2_dot_discovery__pb2.DiscoveryResponse.FromString,
    }
    cardinalities = {
      'FetchSecrets': cardinality.Cardinality.UNARY_UNARY,
      'StreamSecrets': cardinality.Cardinality.STREAM_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'envoy.service.discovery.v2.SecretDiscoveryService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
