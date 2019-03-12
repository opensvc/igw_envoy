# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/api/v2/core/address.proto

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
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/api/v2/core/address.proto',
  package='envoy.api.v2.core',
  syntax='proto3',
  serialized_pb=_b('\n\x1f\x65nvoy/api/v2/core/address.proto\x12\x11\x65nvoy.api.v2.core\x1a\x1c\x65nvoy/api/v2/core/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17validate/validate.proto\x1a\x14gogoproto/gogo.proto\"\x1f\n\x04Pipe\x12\x17\n\x04path\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\"\x96\x02\n\rSocketAddress\x12G\n\x08protocol\x18\x01 \x01(\x0e\x32).envoy.api.v2.core.SocketAddress.ProtocolB\n\xba\xe9\xc0\x03\x05\x82\x01\x02\x10\x01\x12\x1a\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12!\n\nport_value\x18\x03 \x01(\rB\x0b\xba\xe9\xc0\x03\x06*\x04\x18\xff\xff\x03H\x00\x12\x14\n\nnamed_port\x18\x04 \x01(\tH\x00\x12\x15\n\rresolver_name\x18\x05 \x01(\t\x12\x13\n\x0bipv4_compat\x18\x06 \x01(\x08\"\"\n\x08Protocol\x12\x07\n\x03TCP\x10\x00\x12\x07\n\x03UDP\x10\x01\x1a\x04\x88\xa3\x1e\x00\x42\x17\n\x0eport_specifier\x12\x05\xb8\xe9\xc0\x03\x01\"\xb6\x01\n\x0cTcpKeepalive\x12\x36\n\x10keepalive_probes\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x34\n\x0ekeepalive_time\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x38\n\x12keepalive_interval\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"\xbd\x01\n\nBindConfig\x12H\n\x0esource_address\x18\x01 \x01(\x0b\x32 .envoy.api.v2.core.SocketAddressB\x0e\xba\xe9\xc0\x03\x05\x8a\x01\x02\x10\x01\xc8\xde\x1f\x00\x12,\n\x08\x66reebind\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x37\n\x0esocket_options\x18\x03 \x03(\x0b\x32\x1f.envoy.api.v2.core.SocketOption\"\x80\x01\n\x07\x41\x64\x64ress\x12:\n\x0esocket_address\x18\x01 \x01(\x0b\x32 .envoy.api.v2.core.SocketAddressH\x00\x12\'\n\x04pipe\x18\x02 \x01(\x0b\x32\x17.envoy.api.v2.core.PipeH\x00\x42\x10\n\x07\x61\x64\x64ress\x12\x05\xb8\xe9\xc0\x03\x01\"l\n\tCidrRange\x12!\n\x0e\x61\x64\x64ress_prefix\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12<\n\nprefix_len\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\n\xba\xe9\xc0\x03\x05*\x03\x18\x80\x01\x42\x35\n\x1fio.envoyproxy.envoy.api.v2.coreB\x0c\x41\x64\x64ressProtoP\x01\xa8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_base__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])



_SOCKETADDRESS_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='envoy.api.v2.core.SocketAddress.Protocol',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TCP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UDP', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\210\243\036\000')),
  serialized_start=416,
  serialized_end=450,
)
_sym_db.RegisterEnumDescriptor(_SOCKETADDRESS_PROTOCOL)


_PIPE = _descriptor.Descriptor(
  name='Pipe',
  full_name='envoy.api.v2.core.Pipe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='envoy.api.v2.core.Pipe.path', index=0,
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
  serialized_start=163,
  serialized_end=194,
)


_SOCKETADDRESS = _descriptor.Descriptor(
  name='SocketAddress',
  full_name='envoy.api.v2.core.SocketAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol', full_name='envoy.api.v2.core.SocketAddress.protocol', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))),
    _descriptor.FieldDescriptor(
      name='address', full_name='envoy.api.v2.core.SocketAddress.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='port_value', full_name='envoy.api.v2.core.SocketAddress.port_value', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\006*\004\030\377\377\003'))),
    _descriptor.FieldDescriptor(
      name='named_port', full_name='envoy.api.v2.core.SocketAddress.named_port', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resolver_name', full_name='envoy.api.v2.core.SocketAddress.resolver_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipv4_compat', full_name='envoy.api.v2.core.SocketAddress.ipv4_compat', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SOCKETADDRESS_PROTOCOL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='port_specifier', full_name='envoy.api.v2.core.SocketAddress.port_specifier',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=197,
  serialized_end=475,
)


_TCPKEEPALIVE = _descriptor.Descriptor(
  name='TcpKeepalive',
  full_name='envoy.api.v2.core.TcpKeepalive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keepalive_probes', full_name='envoy.api.v2.core.TcpKeepalive.keepalive_probes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keepalive_time', full_name='envoy.api.v2.core.TcpKeepalive.keepalive_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keepalive_interval', full_name='envoy.api.v2.core.TcpKeepalive.keepalive_interval', index=2,
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
  serialized_start=478,
  serialized_end=660,
)


_BINDCONFIG = _descriptor.Descriptor(
  name='BindConfig',
  full_name='envoy.api.v2.core.BindConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_address', full_name='envoy.api.v2.core.BindConfig.source_address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001\310\336\037\000'))),
    _descriptor.FieldDescriptor(
      name='freebind', full_name='envoy.api.v2.core.BindConfig.freebind', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='socket_options', full_name='envoy.api.v2.core.BindConfig.socket_options', index=2,
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
  serialized_start=663,
  serialized_end=852,
)


_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='envoy.api.v2.core.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='socket_address', full_name='envoy.api.v2.core.Address.socket_address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pipe', full_name='envoy.api.v2.core.Address.pipe', index=1,
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
    _descriptor.OneofDescriptor(
      name='address', full_name='envoy.api.v2.core.Address.address',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=855,
  serialized_end=983,
)


_CIDRRANGE = _descriptor.Descriptor(
  name='CidrRange',
  full_name='envoy.api.v2.core.CidrRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_prefix', full_name='envoy.api.v2.core.CidrRange.address_prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='prefix_len', full_name='envoy.api.v2.core.CidrRange.prefix_len', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005*\003\030\200\001'))),
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
  serialized_start=985,
  serialized_end=1093,
)

_SOCKETADDRESS.fields_by_name['protocol'].enum_type = _SOCKETADDRESS_PROTOCOL
_SOCKETADDRESS_PROTOCOL.containing_type = _SOCKETADDRESS
_SOCKETADDRESS.oneofs_by_name['port_specifier'].fields.append(
  _SOCKETADDRESS.fields_by_name['port_value'])
_SOCKETADDRESS.fields_by_name['port_value'].containing_oneof = _SOCKETADDRESS.oneofs_by_name['port_specifier']
_SOCKETADDRESS.oneofs_by_name['port_specifier'].fields.append(
  _SOCKETADDRESS.fields_by_name['named_port'])
_SOCKETADDRESS.fields_by_name['named_port'].containing_oneof = _SOCKETADDRESS.oneofs_by_name['port_specifier']
_TCPKEEPALIVE.fields_by_name['keepalive_probes'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TCPKEEPALIVE.fields_by_name['keepalive_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TCPKEEPALIVE.fields_by_name['keepalive_interval'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_BINDCONFIG.fields_by_name['source_address'].message_type = _SOCKETADDRESS
_BINDCONFIG.fields_by_name['freebind'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_BINDCONFIG.fields_by_name['socket_options'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._SOCKETOPTION
_ADDRESS.fields_by_name['socket_address'].message_type = _SOCKETADDRESS
_ADDRESS.fields_by_name['pipe'].message_type = _PIPE
_ADDRESS.oneofs_by_name['address'].fields.append(
  _ADDRESS.fields_by_name['socket_address'])
_ADDRESS.fields_by_name['socket_address'].containing_oneof = _ADDRESS.oneofs_by_name['address']
_ADDRESS.oneofs_by_name['address'].fields.append(
  _ADDRESS.fields_by_name['pipe'])
_ADDRESS.fields_by_name['pipe'].containing_oneof = _ADDRESS.oneofs_by_name['address']
_CIDRRANGE.fields_by_name['prefix_len'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
DESCRIPTOR.message_types_by_name['Pipe'] = _PIPE
DESCRIPTOR.message_types_by_name['SocketAddress'] = _SOCKETADDRESS
DESCRIPTOR.message_types_by_name['TcpKeepalive'] = _TCPKEEPALIVE
DESCRIPTOR.message_types_by_name['BindConfig'] = _BINDCONFIG
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
DESCRIPTOR.message_types_by_name['CidrRange'] = _CIDRRANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pipe = _reflection.GeneratedProtocolMessageType('Pipe', (_message.Message,), dict(
  DESCRIPTOR = _PIPE,
  __module__ = 'envoy.api.v2.core.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.core.Pipe)
  ))
_sym_db.RegisterMessage(Pipe)

SocketAddress = _reflection.GeneratedProtocolMessageType('SocketAddress', (_message.Message,), dict(
  DESCRIPTOR = _SOCKETADDRESS,
  __module__ = 'envoy.api.v2.core.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.core.SocketAddress)
  ))
_sym_db.RegisterMessage(SocketAddress)

TcpKeepalive = _reflection.GeneratedProtocolMessageType('TcpKeepalive', (_message.Message,), dict(
  DESCRIPTOR = _TCPKEEPALIVE,
  __module__ = 'envoy.api.v2.core.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.core.TcpKeepalive)
  ))
_sym_db.RegisterMessage(TcpKeepalive)

BindConfig = _reflection.GeneratedProtocolMessageType('BindConfig', (_message.Message,), dict(
  DESCRIPTOR = _BINDCONFIG,
  __module__ = 'envoy.api.v2.core.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.core.BindConfig)
  ))
_sym_db.RegisterMessage(BindConfig)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESS,
  __module__ = 'envoy.api.v2.core.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.core.Address)
  ))
_sym_db.RegisterMessage(Address)

CidrRange = _reflection.GeneratedProtocolMessageType('CidrRange', (_message.Message,), dict(
  DESCRIPTOR = _CIDRRANGE,
  __module__ = 'envoy.api.v2.core.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.api.v2.core.CidrRange)
  ))
_sym_db.RegisterMessage(CidrRange)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037io.envoyproxy.envoy.api.v2.coreB\014AddressProtoP\001\250\342\036\001'))
_PIPE.fields_by_name['path'].has_options = True
_PIPE.fields_by_name['path']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_SOCKETADDRESS.oneofs_by_name['port_specifier'].has_options = True
_SOCKETADDRESS.oneofs_by_name['port_specifier']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_SOCKETADDRESS_PROTOCOL.has_options = True
_SOCKETADDRESS_PROTOCOL._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\210\243\036\000'))
_SOCKETADDRESS.fields_by_name['protocol'].has_options = True
_SOCKETADDRESS.fields_by_name['protocol']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))
_SOCKETADDRESS.fields_by_name['address'].has_options = True
_SOCKETADDRESS.fields_by_name['address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_SOCKETADDRESS.fields_by_name['port_value'].has_options = True
_SOCKETADDRESS.fields_by_name['port_value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\006*\004\030\377\377\003'))
_BINDCONFIG.fields_by_name['source_address'].has_options = True
_BINDCONFIG.fields_by_name['source_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001\310\336\037\000'))
_ADDRESS.oneofs_by_name['address'].has_options = True
_ADDRESS.oneofs_by_name['address']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_CIDRRANGE.fields_by_name['address_prefix'].has_options = True
_CIDRRANGE.fields_by_name['address_prefix']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_CIDRRANGE.fields_by_name['prefix_len'].has_options = True
_CIDRRANGE.fields_by_name['prefix_len']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005*\003\030\200\001'))
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
