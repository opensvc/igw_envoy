# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/data/core/v2alpha/health_check_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.core import address_pb2 as envoy_dot_api_dot_v2_dot_core_dot_address__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/data/core/v2alpha/health_check_event.proto',
  package='envoy.data.core.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n0envoy/data/core/v2alpha/health_check_event.proto\x12\x17\x65nvoy.data.core.v2alpha\x1a\x1f\x65nvoy/api/v2/core/address.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\x1a\x14gogoproto/gogo.proto\"\x8d\x05\n\x10HealthCheckEvent\x12S\n\x13health_checker_type\x18\x01 \x01(\x0e\x32*.envoy.data.core.v2alpha.HealthCheckerTypeB\n\xba\xe9\xc0\x03\x05\x82\x01\x02\x10\x01\x12(\n\x04host\x18\x02 \x01(\x0b\x32\x1a.envoy.api.v2.core.Address\x12\x1f\n\x0c\x63luster_name\x18\x03 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12S\n\x15\x65ject_unhealthy_event\x18\x04 \x01(\x0b\x32\x32.envoy.data.core.v2alpha.HealthCheckEjectUnhealthyH\x00\x12K\n\x11\x61\x64\x64_healthy_event\x18\x05 \x01(\x0b\x32..envoy.data.core.v2alpha.HealthCheckAddHealthyH\x00\x12Q\n\x1ahealth_check_failure_event\x18\x07 \x01(\x0b\x32+.envoy.data.core.v2alpha.HealthCheckFailureH\x00\x12M\n\x15\x64\x65graded_healthy_host\x18\x08 \x01(\x0b\x32,.envoy.data.core.v2alpha.DegradedHealthyHostH\x00\x12P\n\x17no_longer_degraded_host\x18\t \x01(\x0b\x32-.envoy.data.core.v2alpha.NoLongerDegradedHostH\x00\x12\x33\n\ttimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x42\x0e\n\x05\x65vent\x12\x05\xb8\xe9\xc0\x03\x01\"n\n\x19HealthCheckEjectUnhealthy\x12Q\n\x0c\x66\x61ilure_type\x18\x01 \x01(\x0e\x32/.envoy.data.core.v2alpha.HealthCheckFailureTypeB\n\xba\xe9\xc0\x03\x05\x82\x01\x02\x10\x01\",\n\x15HealthCheckAddHealthy\x12\x13\n\x0b\x66irst_check\x18\x01 \x01(\x08\"|\n\x12HealthCheckFailure\x12Q\n\x0c\x66\x61ilure_type\x18\x01 \x01(\x0e\x32/.envoy.data.core.v2alpha.HealthCheckFailureTypeB\n\xba\xe9\xc0\x03\x05\x82\x01\x02\x10\x01\x12\x13\n\x0b\x66irst_check\x18\x02 \x01(\x08\"\x15\n\x13\x44\x65gradedHealthyHost\"\x16\n\x14NoLongerDegradedHost*>\n\x16HealthCheckFailureType\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\x0b\n\x07PASSIVE\x10\x01\x12\x0b\n\x07NETWORK\x10\x02*;\n\x11HealthCheckerType\x12\x08\n\x04HTTP\x10\x00\x12\x07\n\x03TCP\x10\x01\x12\x08\n\x04GRPC\x10\x02\x12\t\n\x05REDIS\x10\x03\x42\x44\n%io.envoyproxy.envoy.data.core.v2alphaB\x15HealthCheckEventProtoP\x01\xa8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_address__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])

_HEALTHCHECKFAILURETYPE = _descriptor.EnumDescriptor(
  name='HealthCheckFailureType',
  full_name='envoy.data.core.v2alpha.HealthCheckFailureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NETWORK', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1177,
  serialized_end=1239,
)
_sym_db.RegisterEnumDescriptor(_HEALTHCHECKFAILURETYPE)

HealthCheckFailureType = enum_type_wrapper.EnumTypeWrapper(_HEALTHCHECKFAILURETYPE)
_HEALTHCHECKERTYPE = _descriptor.EnumDescriptor(
  name='HealthCheckerType',
  full_name='envoy.data.core.v2alpha.HealthCheckerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HTTP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TCP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRPC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDIS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1241,
  serialized_end=1300,
)
_sym_db.RegisterEnumDescriptor(_HEALTHCHECKERTYPE)

HealthCheckerType = enum_type_wrapper.EnumTypeWrapper(_HEALTHCHECKERTYPE)
ACTIVE = 0
PASSIVE = 1
NETWORK = 2
HTTP = 0
TCP = 1
GRPC = 2
REDIS = 3



_HEALTHCHECKEVENT = _descriptor.Descriptor(
  name='HealthCheckEvent',
  full_name='envoy.data.core.v2alpha.HealthCheckEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='health_checker_type', full_name='envoy.data.core.v2alpha.HealthCheckEvent.health_checker_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))),
    _descriptor.FieldDescriptor(
      name='host', full_name='envoy.data.core.v2alpha.HealthCheckEvent.host', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cluster_name', full_name='envoy.data.core.v2alpha.HealthCheckEvent.cluster_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='eject_unhealthy_event', full_name='envoy.data.core.v2alpha.HealthCheckEvent.eject_unhealthy_event', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_healthy_event', full_name='envoy.data.core.v2alpha.HealthCheckEvent.add_healthy_event', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='health_check_failure_event', full_name='envoy.data.core.v2alpha.HealthCheckEvent.health_check_failure_event', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='degraded_healthy_host', full_name='envoy.data.core.v2alpha.HealthCheckEvent.degraded_healthy_host', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='no_longer_degraded_host', full_name='envoy.data.core.v2alpha.HealthCheckEvent.no_longer_degraded_host', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='envoy.data.core.v2alpha.HealthCheckEvent.timestamp', index=8,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001'))),
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
      name='event', full_name='envoy.data.core.v2alpha.HealthCheckEvent.event',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=191,
  serialized_end=844,
)


_HEALTHCHECKEJECTUNHEALTHY = _descriptor.Descriptor(
  name='HealthCheckEjectUnhealthy',
  full_name='envoy.data.core.v2alpha.HealthCheckEjectUnhealthy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failure_type', full_name='envoy.data.core.v2alpha.HealthCheckEjectUnhealthy.failure_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))),
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
  serialized_start=846,
  serialized_end=956,
)


_HEALTHCHECKADDHEALTHY = _descriptor.Descriptor(
  name='HealthCheckAddHealthy',
  full_name='envoy.data.core.v2alpha.HealthCheckAddHealthy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_check', full_name='envoy.data.core.v2alpha.HealthCheckAddHealthy.first_check', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=958,
  serialized_end=1002,
)


_HEALTHCHECKFAILURE = _descriptor.Descriptor(
  name='HealthCheckFailure',
  full_name='envoy.data.core.v2alpha.HealthCheckFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failure_type', full_name='envoy.data.core.v2alpha.HealthCheckFailure.failure_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))),
    _descriptor.FieldDescriptor(
      name='first_check', full_name='envoy.data.core.v2alpha.HealthCheckFailure.first_check', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=1004,
  serialized_end=1128,
)


_DEGRADEDHEALTHYHOST = _descriptor.Descriptor(
  name='DegradedHealthyHost',
  full_name='envoy.data.core.v2alpha.DegradedHealthyHost',
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
  serialized_start=1130,
  serialized_end=1151,
)


_NOLONGERDEGRADEDHOST = _descriptor.Descriptor(
  name='NoLongerDegradedHost',
  full_name='envoy.data.core.v2alpha.NoLongerDegradedHost',
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
  serialized_start=1153,
  serialized_end=1175,
)

_HEALTHCHECKEVENT.fields_by_name['health_checker_type'].enum_type = _HEALTHCHECKERTYPE
_HEALTHCHECKEVENT.fields_by_name['host'].message_type = envoy_dot_api_dot_v2_dot_core_dot_address__pb2._ADDRESS
_HEALTHCHECKEVENT.fields_by_name['eject_unhealthy_event'].message_type = _HEALTHCHECKEJECTUNHEALTHY
_HEALTHCHECKEVENT.fields_by_name['add_healthy_event'].message_type = _HEALTHCHECKADDHEALTHY
_HEALTHCHECKEVENT.fields_by_name['health_check_failure_event'].message_type = _HEALTHCHECKFAILURE
_HEALTHCHECKEVENT.fields_by_name['degraded_healthy_host'].message_type = _DEGRADEDHEALTHYHOST
_HEALTHCHECKEVENT.fields_by_name['no_longer_degraded_host'].message_type = _NOLONGERDEGRADEDHOST
_HEALTHCHECKEVENT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HEALTHCHECKEVENT.oneofs_by_name['event'].fields.append(
  _HEALTHCHECKEVENT.fields_by_name['eject_unhealthy_event'])
_HEALTHCHECKEVENT.fields_by_name['eject_unhealthy_event'].containing_oneof = _HEALTHCHECKEVENT.oneofs_by_name['event']
_HEALTHCHECKEVENT.oneofs_by_name['event'].fields.append(
  _HEALTHCHECKEVENT.fields_by_name['add_healthy_event'])
_HEALTHCHECKEVENT.fields_by_name['add_healthy_event'].containing_oneof = _HEALTHCHECKEVENT.oneofs_by_name['event']
_HEALTHCHECKEVENT.oneofs_by_name['event'].fields.append(
  _HEALTHCHECKEVENT.fields_by_name['health_check_failure_event'])
_HEALTHCHECKEVENT.fields_by_name['health_check_failure_event'].containing_oneof = _HEALTHCHECKEVENT.oneofs_by_name['event']
_HEALTHCHECKEVENT.oneofs_by_name['event'].fields.append(
  _HEALTHCHECKEVENT.fields_by_name['degraded_healthy_host'])
_HEALTHCHECKEVENT.fields_by_name['degraded_healthy_host'].containing_oneof = _HEALTHCHECKEVENT.oneofs_by_name['event']
_HEALTHCHECKEVENT.oneofs_by_name['event'].fields.append(
  _HEALTHCHECKEVENT.fields_by_name['no_longer_degraded_host'])
_HEALTHCHECKEVENT.fields_by_name['no_longer_degraded_host'].containing_oneof = _HEALTHCHECKEVENT.oneofs_by_name['event']
_HEALTHCHECKEJECTUNHEALTHY.fields_by_name['failure_type'].enum_type = _HEALTHCHECKFAILURETYPE
_HEALTHCHECKFAILURE.fields_by_name['failure_type'].enum_type = _HEALTHCHECKFAILURETYPE
DESCRIPTOR.message_types_by_name['HealthCheckEvent'] = _HEALTHCHECKEVENT
DESCRIPTOR.message_types_by_name['HealthCheckEjectUnhealthy'] = _HEALTHCHECKEJECTUNHEALTHY
DESCRIPTOR.message_types_by_name['HealthCheckAddHealthy'] = _HEALTHCHECKADDHEALTHY
DESCRIPTOR.message_types_by_name['HealthCheckFailure'] = _HEALTHCHECKFAILURE
DESCRIPTOR.message_types_by_name['DegradedHealthyHost'] = _DEGRADEDHEALTHYHOST
DESCRIPTOR.message_types_by_name['NoLongerDegradedHost'] = _NOLONGERDEGRADEDHOST
DESCRIPTOR.enum_types_by_name['HealthCheckFailureType'] = _HEALTHCHECKFAILURETYPE
DESCRIPTOR.enum_types_by_name['HealthCheckerType'] = _HEALTHCHECKERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HealthCheckEvent = _reflection.GeneratedProtocolMessageType('HealthCheckEvent', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKEVENT,
  __module__ = 'envoy.data.core.v2alpha.health_check_event_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.core.v2alpha.HealthCheckEvent)
  ))
_sym_db.RegisterMessage(HealthCheckEvent)

HealthCheckEjectUnhealthy = _reflection.GeneratedProtocolMessageType('HealthCheckEjectUnhealthy', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKEJECTUNHEALTHY,
  __module__ = 'envoy.data.core.v2alpha.health_check_event_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.core.v2alpha.HealthCheckEjectUnhealthy)
  ))
_sym_db.RegisterMessage(HealthCheckEjectUnhealthy)

HealthCheckAddHealthy = _reflection.GeneratedProtocolMessageType('HealthCheckAddHealthy', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKADDHEALTHY,
  __module__ = 'envoy.data.core.v2alpha.health_check_event_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.core.v2alpha.HealthCheckAddHealthy)
  ))
_sym_db.RegisterMessage(HealthCheckAddHealthy)

HealthCheckFailure = _reflection.GeneratedProtocolMessageType('HealthCheckFailure', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKFAILURE,
  __module__ = 'envoy.data.core.v2alpha.health_check_event_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.core.v2alpha.HealthCheckFailure)
  ))
_sym_db.RegisterMessage(HealthCheckFailure)

DegradedHealthyHost = _reflection.GeneratedProtocolMessageType('DegradedHealthyHost', (_message.Message,), dict(
  DESCRIPTOR = _DEGRADEDHEALTHYHOST,
  __module__ = 'envoy.data.core.v2alpha.health_check_event_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.core.v2alpha.DegradedHealthyHost)
  ))
_sym_db.RegisterMessage(DegradedHealthyHost)

NoLongerDegradedHost = _reflection.GeneratedProtocolMessageType('NoLongerDegradedHost', (_message.Message,), dict(
  DESCRIPTOR = _NOLONGERDEGRADEDHOST,
  __module__ = 'envoy.data.core.v2alpha.health_check_event_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.core.v2alpha.NoLongerDegradedHost)
  ))
_sym_db.RegisterMessage(NoLongerDegradedHost)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%io.envoyproxy.envoy.data.core.v2alphaB\025HealthCheckEventProtoP\001\250\342\036\001'))
_HEALTHCHECKEVENT.oneofs_by_name['event'].has_options = True
_HEALTHCHECKEVENT.oneofs_by_name['event']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_HEALTHCHECKEVENT.fields_by_name['health_checker_type'].has_options = True
_HEALTHCHECKEVENT.fields_by_name['health_checker_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))
_HEALTHCHECKEVENT.fields_by_name['cluster_name'].has_options = True
_HEALTHCHECKEVENT.fields_by_name['cluster_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_HEALTHCHECKEVENT.fields_by_name['timestamp'].has_options = True
_HEALTHCHECKEVENT.fields_by_name['timestamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\220\337\037\001'))
_HEALTHCHECKEJECTUNHEALTHY.fields_by_name['failure_type'].has_options = True
_HEALTHCHECKEJECTUNHEALTHY.fields_by_name['failure_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))
_HEALTHCHECKFAILURE.fields_by_name['failure_type'].has_options = True
_HEALTHCHECKFAILURE.fields_by_name['failure_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))
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
