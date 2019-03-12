# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/metrics/v2/stats.proto

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
from envoy.type.matcher import string_pb2 as envoy_dot_type_dot_matcher_dot_string__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/metrics/v2/stats.proto',
  package='envoy.config.metrics.v2',
  syntax='proto3',
  serialized_pb=_b('\n#envoy/config/metrics/v2/stats.proto\x12\x17\x65nvoy.config.metrics.v2\x1a\x1f\x65nvoy/api/v2/core/address.proto\x1a\x1f\x65nvoy/type/matcher/string.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17validate/validate.proto\"\x85\x01\n\tStatsSink\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x02\x18\x01H\x00\x12,\n\x0ctyped_config\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\r\n\x0b\x63onfig_type\"\xc0\x01\n\x0bStatsConfig\x12\x39\n\nstats_tags\x18\x01 \x03(\x0b\x32%.envoy.config.metrics.v2.TagSpecifier\x12\x38\n\x14use_all_default_tags\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\rstats_matcher\x18\x03 \x01(\x0b\x32%.envoy.config.metrics.v2.StatsMatcher\"\xbe\x01\n\x0cStatsMatcher\x12\x14\n\nreject_all\x18\x01 \x01(\x08H\x00\x12?\n\x0e\x65xclusion_list\x18\x02 \x01(\x0b\x32%.envoy.type.matcher.ListStringMatcherH\x00\x12?\n\x0einclusion_list\x18\x03 \x01(\x0b\x32%.envoy.type.matcher.ListStringMatcherH\x00\x42\x16\n\rstats_matcher\x12\x05\xb8\xe9\xc0\x03\x01\"a\n\x0cTagSpecifier\x12\x10\n\x08tag_name\x18\x01 \x01(\t\x12\x1b\n\x05regex\x18\x02 \x01(\tB\n\xba\xe9\xc0\x03\x05r\x03(\x80\x08H\x00\x12\x15\n\x0b\x66ixed_value\x18\x03 \x01(\tH\x00\x42\x0b\n\ttag_value\"\x82\x01\n\nStatsdSink\x12-\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1a.envoy.api.v2.core.AddressH\x00\x12\x1a\n\x10tcp_cluster_name\x18\x02 \x01(\tH\x00\x12\x0e\n\x06prefix\x18\x03 \x01(\tB\x19\n\x10statsd_specifier\x12\x05\xb8\xe9\xc0\x03\x01\"s\n\rDogStatsdSink\x12-\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1a.envoy.api.v2.core.AddressH\x00\x12\x0e\n\x06prefix\x18\x03 \x01(\tB\x1d\n\x14\x64og_statsd_specifier\x12\x05\xb8\xe9\xc0\x03\x01J\x04\x08\x02\x10\x03\"\"\n\x0bHystrixSink\x12\x13\n\x0bnum_buckets\x18\x01 \x01(\x03\x42\x39\n%io.envoyproxy.envoy.config.metrics.v2B\nStatsProtoP\x01Z\x02v2b\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_address__pb2.DESCRIPTOR,envoy_dot_type_dot_matcher_dot_string__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_STATSSINK = _descriptor.Descriptor(
  name='StatsSink',
  full_name='envoy.config.metrics.v2.StatsSink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.config.metrics.v2.StatsSink.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config', full_name='envoy.config.metrics.v2.StatsSink.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='typed_config', full_name='envoy.config.metrics.v2.StatsSink.typed_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='config_type', full_name='envoy.config.metrics.v2.StatsSink.config_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=245,
  serialized_end=378,
)


_STATSCONFIG = _descriptor.Descriptor(
  name='StatsConfig',
  full_name='envoy.config.metrics.v2.StatsConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stats_tags', full_name='envoy.config.metrics.v2.StatsConfig.stats_tags', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_all_default_tags', full_name='envoy.config.metrics.v2.StatsConfig.use_all_default_tags', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats_matcher', full_name='envoy.config.metrics.v2.StatsConfig.stats_matcher', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=381,
  serialized_end=573,
)


_STATSMATCHER = _descriptor.Descriptor(
  name='StatsMatcher',
  full_name='envoy.config.metrics.v2.StatsMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reject_all', full_name='envoy.config.metrics.v2.StatsMatcher.reject_all', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exclusion_list', full_name='envoy.config.metrics.v2.StatsMatcher.exclusion_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inclusion_list', full_name='envoy.config.metrics.v2.StatsMatcher.inclusion_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='stats_matcher', full_name='envoy.config.metrics.v2.StatsMatcher.stats_matcher',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=576,
  serialized_end=766,
)


_TAGSPECIFIER = _descriptor.Descriptor(
  name='TagSpecifier',
  full_name='envoy.config.metrics.v2.TagSpecifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag_name', full_name='envoy.config.metrics.v2.TagSpecifier.tag_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='regex', full_name='envoy.config.metrics.v2.TagSpecifier.regex', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005r\003(\200\010'))),
    _descriptor.FieldDescriptor(
      name='fixed_value', full_name='envoy.config.metrics.v2.TagSpecifier.fixed_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='tag_value', full_name='envoy.config.metrics.v2.TagSpecifier.tag_value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=768,
  serialized_end=865,
)


_STATSDSINK = _descriptor.Descriptor(
  name='StatsdSink',
  full_name='envoy.config.metrics.v2.StatsdSink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='envoy.config.metrics.v2.StatsdSink.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tcp_cluster_name', full_name='envoy.config.metrics.v2.StatsdSink.tcp_cluster_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='envoy.config.metrics.v2.StatsdSink.prefix', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='statsd_specifier', full_name='envoy.config.metrics.v2.StatsdSink.statsd_specifier',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=868,
  serialized_end=998,
)


_DOGSTATSDSINK = _descriptor.Descriptor(
  name='DogStatsdSink',
  full_name='envoy.config.metrics.v2.DogStatsdSink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='envoy.config.metrics.v2.DogStatsdSink.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='envoy.config.metrics.v2.DogStatsdSink.prefix', index=1,
      number=3, type=9, cpp_type=9, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='dog_statsd_specifier', full_name='envoy.config.metrics.v2.DogStatsdSink.dog_statsd_specifier',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=1000,
  serialized_end=1115,
)


_HYSTRIXSINK = _descriptor.Descriptor(
  name='HystrixSink',
  full_name='envoy.config.metrics.v2.HystrixSink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_buckets', full_name='envoy.config.metrics.v2.HystrixSink.num_buckets', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=1117,
  serialized_end=1151,
)

_STATSSINK.fields_by_name['config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_STATSSINK.fields_by_name['typed_config'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_STATSSINK.oneofs_by_name['config_type'].fields.append(
  _STATSSINK.fields_by_name['config'])
_STATSSINK.fields_by_name['config'].containing_oneof = _STATSSINK.oneofs_by_name['config_type']
_STATSSINK.oneofs_by_name['config_type'].fields.append(
  _STATSSINK.fields_by_name['typed_config'])
_STATSSINK.fields_by_name['typed_config'].containing_oneof = _STATSSINK.oneofs_by_name['config_type']
_STATSCONFIG.fields_by_name['stats_tags'].message_type = _TAGSPECIFIER
_STATSCONFIG.fields_by_name['use_all_default_tags'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_STATSCONFIG.fields_by_name['stats_matcher'].message_type = _STATSMATCHER
_STATSMATCHER.fields_by_name['exclusion_list'].message_type = envoy_dot_type_dot_matcher_dot_string__pb2._LISTSTRINGMATCHER
_STATSMATCHER.fields_by_name['inclusion_list'].message_type = envoy_dot_type_dot_matcher_dot_string__pb2._LISTSTRINGMATCHER
_STATSMATCHER.oneofs_by_name['stats_matcher'].fields.append(
  _STATSMATCHER.fields_by_name['reject_all'])
_STATSMATCHER.fields_by_name['reject_all'].containing_oneof = _STATSMATCHER.oneofs_by_name['stats_matcher']
_STATSMATCHER.oneofs_by_name['stats_matcher'].fields.append(
  _STATSMATCHER.fields_by_name['exclusion_list'])
_STATSMATCHER.fields_by_name['exclusion_list'].containing_oneof = _STATSMATCHER.oneofs_by_name['stats_matcher']
_STATSMATCHER.oneofs_by_name['stats_matcher'].fields.append(
  _STATSMATCHER.fields_by_name['inclusion_list'])
_STATSMATCHER.fields_by_name['inclusion_list'].containing_oneof = _STATSMATCHER.oneofs_by_name['stats_matcher']
_TAGSPECIFIER.oneofs_by_name['tag_value'].fields.append(
  _TAGSPECIFIER.fields_by_name['regex'])
_TAGSPECIFIER.fields_by_name['regex'].containing_oneof = _TAGSPECIFIER.oneofs_by_name['tag_value']
_TAGSPECIFIER.oneofs_by_name['tag_value'].fields.append(
  _TAGSPECIFIER.fields_by_name['fixed_value'])
_TAGSPECIFIER.fields_by_name['fixed_value'].containing_oneof = _TAGSPECIFIER.oneofs_by_name['tag_value']
_STATSDSINK.fields_by_name['address'].message_type = envoy_dot_api_dot_v2_dot_core_dot_address__pb2._ADDRESS
_STATSDSINK.oneofs_by_name['statsd_specifier'].fields.append(
  _STATSDSINK.fields_by_name['address'])
_STATSDSINK.fields_by_name['address'].containing_oneof = _STATSDSINK.oneofs_by_name['statsd_specifier']
_STATSDSINK.oneofs_by_name['statsd_specifier'].fields.append(
  _STATSDSINK.fields_by_name['tcp_cluster_name'])
_STATSDSINK.fields_by_name['tcp_cluster_name'].containing_oneof = _STATSDSINK.oneofs_by_name['statsd_specifier']
_DOGSTATSDSINK.fields_by_name['address'].message_type = envoy_dot_api_dot_v2_dot_core_dot_address__pb2._ADDRESS
_DOGSTATSDSINK.oneofs_by_name['dog_statsd_specifier'].fields.append(
  _DOGSTATSDSINK.fields_by_name['address'])
_DOGSTATSDSINK.fields_by_name['address'].containing_oneof = _DOGSTATSDSINK.oneofs_by_name['dog_statsd_specifier']
DESCRIPTOR.message_types_by_name['StatsSink'] = _STATSSINK
DESCRIPTOR.message_types_by_name['StatsConfig'] = _STATSCONFIG
DESCRIPTOR.message_types_by_name['StatsMatcher'] = _STATSMATCHER
DESCRIPTOR.message_types_by_name['TagSpecifier'] = _TAGSPECIFIER
DESCRIPTOR.message_types_by_name['StatsdSink'] = _STATSDSINK
DESCRIPTOR.message_types_by_name['DogStatsdSink'] = _DOGSTATSDSINK
DESCRIPTOR.message_types_by_name['HystrixSink'] = _HYSTRIXSINK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatsSink = _reflection.GeneratedProtocolMessageType('StatsSink', (_message.Message,), dict(
  DESCRIPTOR = _STATSSINK,
  __module__ = 'envoy.config.metrics.v2.stats_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.metrics.v2.StatsSink)
  ))
_sym_db.RegisterMessage(StatsSink)

StatsConfig = _reflection.GeneratedProtocolMessageType('StatsConfig', (_message.Message,), dict(
  DESCRIPTOR = _STATSCONFIG,
  __module__ = 'envoy.config.metrics.v2.stats_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.metrics.v2.StatsConfig)
  ))
_sym_db.RegisterMessage(StatsConfig)

StatsMatcher = _reflection.GeneratedProtocolMessageType('StatsMatcher', (_message.Message,), dict(
  DESCRIPTOR = _STATSMATCHER,
  __module__ = 'envoy.config.metrics.v2.stats_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.metrics.v2.StatsMatcher)
  ))
_sym_db.RegisterMessage(StatsMatcher)

TagSpecifier = _reflection.GeneratedProtocolMessageType('TagSpecifier', (_message.Message,), dict(
  DESCRIPTOR = _TAGSPECIFIER,
  __module__ = 'envoy.config.metrics.v2.stats_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.metrics.v2.TagSpecifier)
  ))
_sym_db.RegisterMessage(TagSpecifier)

StatsdSink = _reflection.GeneratedProtocolMessageType('StatsdSink', (_message.Message,), dict(
  DESCRIPTOR = _STATSDSINK,
  __module__ = 'envoy.config.metrics.v2.stats_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.metrics.v2.StatsdSink)
  ))
_sym_db.RegisterMessage(StatsdSink)

DogStatsdSink = _reflection.GeneratedProtocolMessageType('DogStatsdSink', (_message.Message,), dict(
  DESCRIPTOR = _DOGSTATSDSINK,
  __module__ = 'envoy.config.metrics.v2.stats_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.metrics.v2.DogStatsdSink)
  ))
_sym_db.RegisterMessage(DogStatsdSink)

HystrixSink = _reflection.GeneratedProtocolMessageType('HystrixSink', (_message.Message,), dict(
  DESCRIPTOR = _HYSTRIXSINK,
  __module__ = 'envoy.config.metrics.v2.stats_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.metrics.v2.HystrixSink)
  ))
_sym_db.RegisterMessage(HystrixSink)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%io.envoyproxy.envoy.config.metrics.v2B\nStatsProtoP\001Z\002v2'))
_STATSSINK.fields_by_name['config'].has_options = True
_STATSSINK.fields_by_name['config']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_STATSMATCHER.oneofs_by_name['stats_matcher'].has_options = True
_STATSMATCHER.oneofs_by_name['stats_matcher']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_TAGSPECIFIER.fields_by_name['regex'].has_options = True
_TAGSPECIFIER.fields_by_name['regex']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005r\003(\200\010'))
_STATSDSINK.oneofs_by_name['statsd_specifier'].has_options = True
_STATSDSINK.oneofs_by_name['statsd_specifier']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_DOGSTATSDSINK.oneofs_by_name['dog_statsd_specifier'].has_options = True
_DOGSTATSDSINK.oneofs_by_name['dog_statsd_specifier']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
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
