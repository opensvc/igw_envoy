# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/resource_monitor/injected_resource/v2alpha/injected_resource.proto

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
  name='envoy/config/resource_monitor/injected_resource/v2alpha/injected_resource.proto',
  package='envoy.config.resource_monitor.injected_resource.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\nOenvoy/config/resource_monitor/injected_resource/v2alpha/injected_resource.proto\x12\x37\x65nvoy.config.resource_monitor.injected_resource.v2alpha\x1a\x17validate/validate.proto\"5\n\x16InjectedResourceConfig\x12\x1b\n\x08\x66ilename\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x42i\nEio.envoyproxy.envoy.config.resource_monitor.injected_resource.v2alphaB\x15InjectedResourceProtoP\x01Z\x07v2alphab\x06proto3')
  ,
  dependencies=[validate_dot_validate__pb2.DESCRIPTOR,])




_INJECTEDRESOURCECONFIG = _descriptor.Descriptor(
  name='InjectedResourceConfig',
  full_name='envoy.config.resource_monitor.injected_resource.v2alpha.InjectedResourceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='envoy.config.resource_monitor.injected_resource.v2alpha.InjectedResourceConfig.filename', index=0,
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
  ],
  serialized_start=165,
  serialized_end=218,
)

DESCRIPTOR.message_types_by_name['InjectedResourceConfig'] = _INJECTEDRESOURCECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InjectedResourceConfig = _reflection.GeneratedProtocolMessageType('InjectedResourceConfig', (_message.Message,), dict(
  DESCRIPTOR = _INJECTEDRESOURCECONFIG,
  __module__ = 'envoy.config.resource_monitor.injected_resource.v2alpha.injected_resource_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.resource_monitor.injected_resource.v2alpha.InjectedResourceConfig)
  ))
_sym_db.RegisterMessage(InjectedResourceConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\nEio.envoyproxy.envoy.config.resource_monitor.injected_resource.v2alphaB\025InjectedResourceProtoP\001Z\007v2alpha'))
_INJECTEDRESOURCECONFIG.fields_by_name['filename'].has_options = True
_INJECTEDRESOURCECONFIG.fields_by_name['filename']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
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
