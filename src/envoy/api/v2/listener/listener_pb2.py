# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/api/v2/listener/listener.proto

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
from envoy.api.v2.auth import cert_pb2 as envoy_dot_api_dot_v2_dot_auth_dot_cert__pb2
from envoy.api.v2.core import base_pb2 as envoy_dot_api_dot_v2_dot_core_dot_base__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/api/v2/listener/listener.proto',
  package='envoy.api.v2.listener',
  syntax='proto3',
  serialized_pb=_b('\n$envoy/api/v2/listener/listener.proto\x12\x15\x65nvoy.api.v2.listener\x1a\x1f\x65nvoy/api/v2/core/address.proto\x1a\x1c\x65nvoy/api/v2/auth/cert.proto\x1a\x1c\x65nvoy/api/v2/core/base.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17validate/validate.proto\x1a\x14gogoproto/gogo.proto\"\x93\x01\n\x06\x46ilter\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12-\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x02\x18\x01H\x00\x12,\n\x0ctyped_config\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\r\n\x0b\x63onfig_typeJ\x04\x08\x03\x10\x04\"\xc5\x04\n\x10\x46ilterChainMatch\x12\x45\n\x10\x64\x65stination_port\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\r\xba\xe9\xc0\x03\x08*\x06\x18\xff\xff\x03(\x01\x12\x33\n\rprefix_ranges\x18\x03 \x03(\x0b\x32\x1c.envoy.api.v2.core.CidrRange\x12\x16\n\x0e\x61\x64\x64ress_suffix\x18\x04 \x01(\t\x12\x30\n\nsuffix_len\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12]\n\x0bsource_type\x18\x0c \x01(\x0e\x32<.envoy.api.v2.listener.FilterChainMatch.ConnectionSourceTypeB\n\xba\xe9\xc0\x03\x05\x82\x01\x02\x10\x01\x12:\n\x14source_prefix_ranges\x18\x06 \x03(\x0b\x32\x1c.envoy.api.v2.core.CidrRange\x12\x32\n\x0csource_ports\x18\x07 \x03(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x14\n\x0cserver_names\x18\x0b \x03(\t\x12\x1a\n\x12transport_protocol\x18\t \x01(\t\x12\x1d\n\x15\x61pplication_protocols\x18\n \x03(\t\"8\n\x14\x43onnectionSourceType\x12\x07\n\x03\x41NY\x10\x00\x12\t\n\x05LOCAL\x10\x01\x12\x0c\n\x08\x45XTERNAL\x10\x02J\x04\x08\x01\x10\x02R\x0bsni_domains\"\xe8\x02\n\x0b\x46ilterChain\x12\x43\n\x12\x66ilter_chain_match\x18\x01 \x01(\x0b\x32\'.envoy.api.v2.listener.FilterChainMatch\x12<\n\x0btls_context\x18\x02 \x01(\x0b\x32\'.envoy.api.v2.auth.DownstreamTlsContext\x12\x34\n\x07\x66ilters\x18\x03 \x03(\x0b\x32\x1d.envoy.api.v2.listener.FilterB\x04\xc8\xde\x1f\x00\x12\x33\n\x0fuse_proxy_proto\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\x08metadata\x18\x05 \x01(\x0b\x32\x1b.envoy.api.v2.core.Metadata\x12<\n\x10transport_socket\x18\x06 \x01(\x0b\x32\".envoy.api.v2.core.TransportSocket\"\x95\x01\n\x0eListenerFilter\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12-\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x02\x18\x01H\x00\x12,\n\x0ctyped_config\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\r\n\x0b\x63onfig_typeB^\n#io.envoyproxy.envoy.api.v2.listenerB\rListenerProtoP\x01Z\x08listener\xaa\x02\x17\x45nvoy.Api.V2.ListenerNS\xa8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_address__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_auth_dot_cert__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_core_dot_base__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])



_FILTERCHAINMATCH_CONNECTIONSOURCETYPE = _descriptor.EnumDescriptor(
  name='ConnectionSourceType',
  full_name='envoy.api.v2.listener.FilterChainMatch.ConnectionSourceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=949,
  serialized_end=1005,
)
_sym_db.RegisterEnumDescriptor(_FILTERCHAINMATCH_CONNECTIONSOURCETYPE)


_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='envoy.api.v2.listener.Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.api.v2.listener.Filter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='config', full_name='envoy.api.v2.listener.Filter.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='typed_config', full_name='envoy.api.v2.listener.Filter.typed_config', index=2,
      number=4, type=11, cpp_type=10, label=1,
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
      name='config_type', full_name='envoy.api.v2.listener.Filter.config_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=293,
  serialized_end=440,
)


_FILTERCHAINMATCH = _descriptor.Descriptor(
  name='FilterChainMatch',
  full_name='envoy.api.v2.listener.FilterChainMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='destination_port', full_name='envoy.api.v2.listener.FilterChainMatch.destination_port', index=0,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\010*\006\030\377\377\003(\001'))),
    _descriptor.FieldDescriptor(
      name='prefix_ranges', full_name='envoy.api.v2.listener.FilterChainMatch.prefix_ranges', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address_suffix', full_name='envoy.api.v2.listener.FilterChainMatch.address_suffix', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='suffix_len', full_name='envoy.api.v2.listener.FilterChainMatch.suffix_len', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_type', full_name='envoy.api.v2.listener.FilterChainMatch.source_type', index=4,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))),
    _descriptor.FieldDescriptor(
      name='source_prefix_ranges', full_name='envoy.api.v2.listener.FilterChainMatch.source_prefix_ranges', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_ports', full_name='envoy.api.v2.listener.FilterChainMatch.source_ports', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_names', full_name='envoy.api.v2.listener.FilterChainMatch.server_names', index=7,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transport_protocol', full_name='envoy.api.v2.listener.FilterChainMatch.transport_protocol', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='application_protocols', full_name='envoy.api.v2.listener.FilterChainMatch.application_protocols', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FILTERCHAINMATCH_CONNECTIONSOURCETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=443,
  serialized_end=1024,
)


_FILTERCHAIN = _descriptor.Descriptor(
  name='FilterChain',
  full_name='envoy.api.v2.listener.FilterChain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter_chain_match', full_name='envoy.api.v2.listener.FilterChain.filter_chain_match', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tls_context', full_name='envoy.api.v2.listener.FilterChain.tls_context', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters', full_name='envoy.api.v2.listener.FilterChain.filters', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='use_proxy_proto', full_name='envoy.api.v2.listener.FilterChain.use_proxy_proto', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='envoy.api.v2.listener.FilterChain.metadata', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transport_socket', full_name='envoy.api.v2.listener.FilterChain.transport_socket', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=1027,
  serialized_end=1387,
)


_LISTENERFILTER = _descriptor.Descriptor(
  name='ListenerFilter',
  full_name='envoy.api.v2.listener.ListenerFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.api.v2.listener.ListenerFilter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='config', full_name='envoy.api.v2.listener.ListenerFilter.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='typed_config', full_name='envoy.api.v2.listener.ListenerFilter.typed_config', index=2,
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
      name='config_type', full_name='envoy.api.v2.listener.ListenerFilter.config_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1390,
  serialized_end=1539,
)

_FILTER.fields_by_name['config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_FILTER.fields_by_name['typed_config'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_FILTER.oneofs_by_name['config_type'].fields.append(
  _FILTER.fields_by_name['config'])
_FILTER.fields_by_name['config'].containing_oneof = _FILTER.oneofs_by_name['config_type']
_FILTER.oneofs_by_name['config_type'].fields.append(
  _FILTER.fields_by_name['typed_config'])
_FILTER.fields_by_name['typed_config'].containing_oneof = _FILTER.oneofs_by_name['config_type']
_FILTERCHAINMATCH.fields_by_name['destination_port'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_FILTERCHAINMATCH.fields_by_name['prefix_ranges'].message_type = envoy_dot_api_dot_v2_dot_core_dot_address__pb2._CIDRRANGE
_FILTERCHAINMATCH.fields_by_name['suffix_len'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_FILTERCHAINMATCH.fields_by_name['source_type'].enum_type = _FILTERCHAINMATCH_CONNECTIONSOURCETYPE
_FILTERCHAINMATCH.fields_by_name['source_prefix_ranges'].message_type = envoy_dot_api_dot_v2_dot_core_dot_address__pb2._CIDRRANGE
_FILTERCHAINMATCH.fields_by_name['source_ports'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_FILTERCHAINMATCH_CONNECTIONSOURCETYPE.containing_type = _FILTERCHAINMATCH
_FILTERCHAIN.fields_by_name['filter_chain_match'].message_type = _FILTERCHAINMATCH
_FILTERCHAIN.fields_by_name['tls_context'].message_type = envoy_dot_api_dot_v2_dot_auth_dot_cert__pb2._DOWNSTREAMTLSCONTEXT
_FILTERCHAIN.fields_by_name['filters'].message_type = _FILTER
_FILTERCHAIN.fields_by_name['use_proxy_proto'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_FILTERCHAIN.fields_by_name['metadata'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._METADATA
_FILTERCHAIN.fields_by_name['transport_socket'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._TRANSPORTSOCKET
_LISTENERFILTER.fields_by_name['config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LISTENERFILTER.fields_by_name['typed_config'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_LISTENERFILTER.oneofs_by_name['config_type'].fields.append(
  _LISTENERFILTER.fields_by_name['config'])
_LISTENERFILTER.fields_by_name['config'].containing_oneof = _LISTENERFILTER.oneofs_by_name['config_type']
_LISTENERFILTER.oneofs_by_name['config_type'].fields.append(
  _LISTENERFILTER.fields_by_name['typed_config'])
_LISTENERFILTER.fields_by_name['typed_config'].containing_oneof = _LISTENERFILTER.oneofs_by_name['config_type']
DESCRIPTOR.message_types_by_name['Filter'] = _FILTER
DESCRIPTOR.message_types_by_name['FilterChainMatch'] = _FILTERCHAINMATCH
DESCRIPTOR.message_types_by_name['FilterChain'] = _FILTERCHAIN
DESCRIPTOR.message_types_by_name['ListenerFilter'] = _LISTENERFILTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), dict(
  DESCRIPTOR = _FILTER,
  __module__ = 'envoy.api.v2.listener.listener_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.listener.Filter)
  ))
_sym_db.RegisterMessage(Filter)

FilterChainMatch = _reflection.GeneratedProtocolMessageType('FilterChainMatch', (_message.Message,), dict(
  DESCRIPTOR = _FILTERCHAINMATCH,
  __module__ = 'envoy.api.v2.listener.listener_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.listener.FilterChainMatch)
  ))
_sym_db.RegisterMessage(FilterChainMatch)

FilterChain = _reflection.GeneratedProtocolMessageType('FilterChain', (_message.Message,), dict(
  DESCRIPTOR = _FILTERCHAIN,
  __module__ = 'envoy.api.v2.listener.listener_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.listener.FilterChain)
  ))
_sym_db.RegisterMessage(FilterChain)

ListenerFilter = _reflection.GeneratedProtocolMessageType('ListenerFilter', (_message.Message,), dict(
  DESCRIPTOR = _LISTENERFILTER,
  __module__ = 'envoy.api.v2.listener.listener_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.listener.ListenerFilter)
  ))
_sym_db.RegisterMessage(ListenerFilter)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#io.envoyproxy.envoy.api.v2.listenerB\rListenerProtoP\001Z\010listener\252\002\027Envoy.Api.V2.ListenerNS\250\342\036\001'))
_FILTER.fields_by_name['name'].has_options = True
_FILTER.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_FILTER.fields_by_name['config'].has_options = True
_FILTER.fields_by_name['config']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_FILTERCHAINMATCH.fields_by_name['destination_port'].has_options = True
_FILTERCHAINMATCH.fields_by_name['destination_port']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\010*\006\030\377\377\003(\001'))
_FILTERCHAINMATCH.fields_by_name['source_type'].has_options = True
_FILTERCHAINMATCH.fields_by_name['source_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))
_FILTERCHAIN.fields_by_name['filters'].has_options = True
_FILTERCHAIN.fields_by_name['filters']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_LISTENERFILTER.fields_by_name['name'].has_options = True
_LISTENERFILTER.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_LISTENERFILTER.fields_by_name['config'].has_options = True
_LISTENERFILTER.fields_by_name['config']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
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
