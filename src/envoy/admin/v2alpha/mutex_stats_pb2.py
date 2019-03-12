# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/admin/v2alpha/mutex_stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/admin/v2alpha/mutex_stats.proto',
  package='envoy.admin.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n%envoy/admin/v2alpha/mutex_stats.proto\x12\x13\x65nvoy.admin.v2alpha\"`\n\nMutexStats\x12\x17\n\x0fnum_contentions\x18\x01 \x01(\x04\x12\x1b\n\x13\x63urrent_wait_cycles\x18\x02 \x01(\x04\x12\x1c\n\x14lifetime_wait_cycles\x18\x03 \x01(\x04\x42\x36\n!io.envoyproxy.envoy.admin.v2alphaB\x0fMutexStatsProtoP\x01\x62\x06proto3')
)




_MUTEXSTATS = _descriptor.Descriptor(
  name='MutexStats',
  full_name='envoy.admin.v2alpha.MutexStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_contentions', full_name='envoy.admin.v2alpha.MutexStats.num_contentions', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_wait_cycles', full_name='envoy.admin.v2alpha.MutexStats.current_wait_cycles', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lifetime_wait_cycles', full_name='envoy.admin.v2alpha.MutexStats.lifetime_wait_cycles', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=62,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['MutexStats'] = _MUTEXSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MutexStats = _reflection.GeneratedProtocolMessageType('MutexStats', (_message.Message,), dict(
  DESCRIPTOR = _MUTEXSTATS,
  __module__ = 'envoy.admin.v2alpha.mutex_stats_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.MutexStats)
  ))
_sym_db.RegisterMessage(MutexStats)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!io.envoyproxy.envoy.admin.v2alphaB\017MutexStatsProtoP\001'))
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
