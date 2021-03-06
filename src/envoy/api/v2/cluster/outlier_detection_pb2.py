# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/api/v2/cluster/outlier_detection.proto

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
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/api/v2/cluster/outlier_detection.proto',
  package='envoy.api.v2.cluster',
  syntax='proto3',
  serialized_pb=_b('\n,envoy/api/v2/cluster/outlier_detection.proto\x12\x14\x65nvoy.api.v2.cluster\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17validate/validate.proto\x1a\x14gogoproto/gogo.proto\"\x82\x06\n\x10OutlierDetection\x12\x35\n\x0f\x63onsecutive_5xx\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x37\n\x08interval\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xba\xe9\xc0\x03\x05\xaa\x01\x02*\x00\x12\x41\n\x12\x62\x61se_ejection_time\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xba\xe9\xc0\x03\x05\xaa\x01\x02*\x00\x12\x45\n\x14max_ejection_percent\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\t\xba\xe9\xc0\x03\x04*\x02\x18\x64\x12J\n\x19\x65nforcing_consecutive_5xx\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\t\xba\xe9\xc0\x03\x04*\x02\x18\x64\x12G\n\x16\x65nforcing_success_rate\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\t\xba\xe9\xc0\x03\x04*\x02\x18\x64\x12@\n\x1asuccess_rate_minimum_hosts\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x41\n\x1bsuccess_rate_request_volume\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12?\n\x19success_rate_stdev_factor\x18\t \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x41\n\x1b\x63onsecutive_gateway_failure\x18\n \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12V\n%enforcing_consecutive_gateway_failure\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\t\xba\xe9\xc0\x03\x04*\x02\x18\x64\x42Z\n\"io.envoyproxy.envoy.api.v2.clusterB\x15OutlierDetectionProtoP\x01\xaa\x02\x16\x45nvoy.Api.V2.ClusterNS\xa8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_OUTLIERDETECTION = _descriptor.Descriptor(
  name='OutlierDetection',
  full_name='envoy.api.v2.cluster.OutlierDetection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='consecutive_5xx', full_name='envoy.api.v2.cluster.OutlierDetection.consecutive_5xx', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interval', full_name='envoy.api.v2.cluster.OutlierDetection.interval', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\252\001\002*\000'))),
    _descriptor.FieldDescriptor(
      name='base_ejection_time', full_name='envoy.api.v2.cluster.OutlierDetection.base_ejection_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\252\001\002*\000'))),
    _descriptor.FieldDescriptor(
      name='max_ejection_percent', full_name='envoy.api.v2.cluster.OutlierDetection.max_ejection_percent', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004*\002\030d'))),
    _descriptor.FieldDescriptor(
      name='enforcing_consecutive_5xx', full_name='envoy.api.v2.cluster.OutlierDetection.enforcing_consecutive_5xx', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004*\002\030d'))),
    _descriptor.FieldDescriptor(
      name='enforcing_success_rate', full_name='envoy.api.v2.cluster.OutlierDetection.enforcing_success_rate', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004*\002\030d'))),
    _descriptor.FieldDescriptor(
      name='success_rate_minimum_hosts', full_name='envoy.api.v2.cluster.OutlierDetection.success_rate_minimum_hosts', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='success_rate_request_volume', full_name='envoy.api.v2.cluster.OutlierDetection.success_rate_request_volume', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='success_rate_stdev_factor', full_name='envoy.api.v2.cluster.OutlierDetection.success_rate_stdev_factor', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consecutive_gateway_failure', full_name='envoy.api.v2.cluster.OutlierDetection.consecutive_gateway_failure', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enforcing_consecutive_gateway_failure', full_name='envoy.api.v2.cluster.OutlierDetection.enforcing_consecutive_gateway_failure', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004*\002\030d'))),
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
  serialized_start=182,
  serialized_end=952,
)

_OUTLIERDETECTION.fields_by_name['consecutive_5xx'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_OUTLIERDETECTION.fields_by_name['interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_OUTLIERDETECTION.fields_by_name['base_ejection_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_OUTLIERDETECTION.fields_by_name['max_ejection_percent'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_OUTLIERDETECTION.fields_by_name['enforcing_consecutive_5xx'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_OUTLIERDETECTION.fields_by_name['enforcing_success_rate'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_OUTLIERDETECTION.fields_by_name['success_rate_minimum_hosts'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_OUTLIERDETECTION.fields_by_name['success_rate_request_volume'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_OUTLIERDETECTION.fields_by_name['success_rate_stdev_factor'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_OUTLIERDETECTION.fields_by_name['consecutive_gateway_failure'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_OUTLIERDETECTION.fields_by_name['enforcing_consecutive_gateway_failure'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
DESCRIPTOR.message_types_by_name['OutlierDetection'] = _OUTLIERDETECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OutlierDetection = _reflection.GeneratedProtocolMessageType('OutlierDetection', (_message.Message,), dict(
  DESCRIPTOR = _OUTLIERDETECTION,
  __module__ = 'envoy.api.v2.cluster.outlier_detection_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.cluster.OutlierDetection)
  ))
_sym_db.RegisterMessage(OutlierDetection)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"io.envoyproxy.envoy.api.v2.clusterB\025OutlierDetectionProtoP\001\252\002\026Envoy.Api.V2.ClusterNS\250\342\036\001'))
_OUTLIERDETECTION.fields_by_name['interval'].has_options = True
_OUTLIERDETECTION.fields_by_name['interval']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\252\001\002*\000'))
_OUTLIERDETECTION.fields_by_name['base_ejection_time'].has_options = True
_OUTLIERDETECTION.fields_by_name['base_ejection_time']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\252\001\002*\000'))
_OUTLIERDETECTION.fields_by_name['max_ejection_percent'].has_options = True
_OUTLIERDETECTION.fields_by_name['max_ejection_percent']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004*\002\030d'))
_OUTLIERDETECTION.fields_by_name['enforcing_consecutive_5xx'].has_options = True
_OUTLIERDETECTION.fields_by_name['enforcing_consecutive_5xx']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004*\002\030d'))
_OUTLIERDETECTION.fields_by_name['enforcing_success_rate'].has_options = True
_OUTLIERDETECTION.fields_by_name['enforcing_success_rate']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004*\002\030d'))
_OUTLIERDETECTION.fields_by_name['enforcing_consecutive_gateway_failure'].has_options = True
_OUTLIERDETECTION.fields_by_name['enforcing_consecutive_gateway_failure']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004*\002\030d'))
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
