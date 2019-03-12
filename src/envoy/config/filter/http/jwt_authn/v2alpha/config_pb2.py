# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/http/jwt_authn/v2alpha/config.proto

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
from envoy.api.v2.core import http_uri_pb2 as envoy_dot_api_dot_v2_dot_core_dot_http__uri__pb2
from envoy.api.v2.route import route_pb2 as envoy_dot_api_dot_v2_dot_route_dot_route__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/filter/http/jwt_authn/v2alpha/config.proto',
  package='envoy.config.filter.http.jwt_authn.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n7envoy/config/filter/http/jwt_authn/v2alpha/config.proto\x12*envoy.config.filter.http.jwt_authn.v2alpha\x1a\x1c\x65nvoy/api/v2/core/base.proto\x1a envoy/api/v2/core/http_uri.proto\x1a\x1e\x65nvoy/api/v2/route/route.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17validate/validate.proto\"\x8f\x03\n\x0bJwtProvider\x12\x19\n\x06issuer\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12\x11\n\taudiences\x18\x02 \x03(\t\x12M\n\x0bremote_jwks\x18\x03 \x01(\x0b\x32\x36.envoy.config.filter.http.jwt_authn.v2alpha.RemoteJwksH\x00\x12\x33\n\nlocal_jwks\x18\x04 \x01(\x0b\x32\x1d.envoy.api.v2.core.DataSourceH\x00\x12\x0f\n\x07\x66orward\x18\x05 \x01(\x08\x12K\n\x0c\x66rom_headers\x18\x06 \x03(\x0b\x32\x35.envoy.config.filter.http.jwt_authn.v2alpha.JwtHeader\x12\x13\n\x0b\x66rom_params\x18\x07 \x03(\t\x12\x1e\n\x16\x66orward_payload_header\x18\x08 \x01(\t\x12\x1b\n\x13payload_in_metadata\x18\t \x01(\tB\x1e\n\x15jwks_source_specifier\x12\x05\xb8\xe9\xc0\x03\x01\"m\n\nRemoteJwks\x12,\n\x08http_uri\x18\x01 \x01(\x0b\x32\x1a.envoy.api.v2.core.HttpUri\x12\x31\n\x0e\x63\x61\x63he_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\":\n\tJwtHeader\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x12\x14\n\x0cvalue_prefix\x18\x02 \x01(\t\"A\n\x15ProviderWithAudiences\x12\x15\n\rprovider_name\x18\x01 \x01(\t\x12\x11\n\taudiences\x18\x02 \x03(\t\"\x8f\x03\n\x0eJwtRequirement\x12\x17\n\rprovider_name\x18\x01 \x01(\tH\x00\x12\x63\n\x16provider_and_audiences\x18\x02 \x01(\x0b\x32\x41.envoy.config.filter.http.jwt_authn.v2alpha.ProviderWithAudiencesH\x00\x12X\n\x0crequires_any\x18\x03 \x01(\x0b\x32@.envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirementOrListH\x00\x12Y\n\x0crequires_all\x18\x04 \x01(\x0b\x32\x41.envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirementAndListH\x00\x12\x39\n\x17\x61llow_missing_or_failed\x18\x05 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x42\x0f\n\rrequires_type\"t\n\x14JwtRequirementOrList\x12\\\n\x0crequirements\x18\x01 \x03(\x0b\x32:.envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirementB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x02\"u\n\x15JwtRequirementAndList\x12\\\n\x0crequirements\x18\x01 \x03(\x0b\x32:.envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirementB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x02\"\x9a\x01\n\x0fRequirementRule\x12\x39\n\x05match\x18\x01 \x01(\x0b\x32\x1e.envoy.api.v2.route.RouteMatchB\n\xba\xe9\xc0\x03\x05\x8a\x01\x02\x10\x01\x12L\n\x08requires\x18\x02 \x01(\x0b\x32:.envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirement\"\xab\x02\n\x11JwtAuthentication\x12_\n\tproviders\x18\x01 \x03(\x0b\x32L.envoy.config.filter.http.jwt_authn.v2alpha.JwtAuthentication.ProvidersEntry\x12J\n\x05rules\x18\x02 \x03(\x0b\x32;.envoy.config.filter.http.jwt_authn.v2alpha.RequirementRule\x1ai\n\x0eProvidersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x46\n\x05value\x18\x02 \x01(\x0b\x32\x37.envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider:\x02\x38\x01\x42I\n8io.envoyproxy.envoy.config.filter.http.jwt_authn.v2alphaB\x0b\x43onfigProtoP\x01\x62\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_core_dot_base__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_core_dot_http__uri__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_route_dot_route__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_JWTPROVIDER = _descriptor.Descriptor(
  name='JwtProvider',
  full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='issuer', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider.issuer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='audiences', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider.audiences', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_jwks', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider.remote_jwks', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_jwks', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider.local_jwks', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forward', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider.forward', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_headers', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider.from_headers', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_params', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider.from_params', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forward_payload_header', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider.forward_payload_header', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_in_metadata', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider.payload_in_metadata', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
      name='jwks_source_specifier', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider.jwks_source_specifier',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=318,
  serialized_end=717,
)


_REMOTEJWKS = _descriptor.Descriptor(
  name='RemoteJwks',
  full_name='envoy.config.filter.http.jwt_authn.v2alpha.RemoteJwks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_uri', full_name='envoy.config.filter.http.jwt_authn.v2alpha.RemoteJwks.http_uri', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cache_duration', full_name='envoy.config.filter.http.jwt_authn.v2alpha.RemoteJwks.cache_duration', index=1,
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
  serialized_start=719,
  serialized_end=828,
)


_JWTHEADER = _descriptor.Descriptor(
  name='JwtHeader',
  full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtHeader.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))),
    _descriptor.FieldDescriptor(
      name='value_prefix', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtHeader.value_prefix', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=830,
  serialized_end=888,
)


_PROVIDERWITHAUDIENCES = _descriptor.Descriptor(
  name='ProviderWithAudiences',
  full_name='envoy.config.filter.http.jwt_authn.v2alpha.ProviderWithAudiences',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider_name', full_name='envoy.config.filter.http.jwt_authn.v2alpha.ProviderWithAudiences.provider_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audiences', full_name='envoy.config.filter.http.jwt_authn.v2alpha.ProviderWithAudiences.audiences', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=890,
  serialized_end=955,
)


_JWTREQUIREMENT = _descriptor.Descriptor(
  name='JwtRequirement',
  full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider_name', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirement.provider_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_and_audiences', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirement.provider_and_audiences', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requires_any', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirement.requires_any', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requires_all', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirement.requires_all', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allow_missing_or_failed', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirement.allow_missing_or_failed', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
      name='requires_type', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirement.requires_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=958,
  serialized_end=1357,
)


_JWTREQUIREMENTORLIST = _descriptor.Descriptor(
  name='JwtRequirementOrList',
  full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirementOrList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requirements', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirementOrList.requirements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\002'))),
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
  serialized_start=1359,
  serialized_end=1475,
)


_JWTREQUIREMENTANDLIST = _descriptor.Descriptor(
  name='JwtRequirementAndList',
  full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirementAndList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requirements', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirementAndList.requirements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\002'))),
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
  serialized_start=1477,
  serialized_end=1594,
)


_REQUIREMENTRULE = _descriptor.Descriptor(
  name='RequirementRule',
  full_name='envoy.config.filter.http.jwt_authn.v2alpha.RequirementRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match', full_name='envoy.config.filter.http.jwt_authn.v2alpha.RequirementRule.match', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001'))),
    _descriptor.FieldDescriptor(
      name='requires', full_name='envoy.config.filter.http.jwt_authn.v2alpha.RequirementRule.requires', index=1,
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
  serialized_start=1597,
  serialized_end=1751,
)


_JWTAUTHENTICATION_PROVIDERSENTRY = _descriptor.Descriptor(
  name='ProvidersEntry',
  full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtAuthentication.ProvidersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtAuthentication.ProvidersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtAuthentication.ProvidersEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1948,
  serialized_end=2053,
)

_JWTAUTHENTICATION = _descriptor.Descriptor(
  name='JwtAuthentication',
  full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtAuthentication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='providers', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtAuthentication.providers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rules', full_name='envoy.config.filter.http.jwt_authn.v2alpha.JwtAuthentication.rules', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_JWTAUTHENTICATION_PROVIDERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1754,
  serialized_end=2053,
)

_JWTPROVIDER.fields_by_name['remote_jwks'].message_type = _REMOTEJWKS
_JWTPROVIDER.fields_by_name['local_jwks'].message_type = envoy_dot_api_dot_v2_dot_core_dot_base__pb2._DATASOURCE
_JWTPROVIDER.fields_by_name['from_headers'].message_type = _JWTHEADER
_JWTPROVIDER.oneofs_by_name['jwks_source_specifier'].fields.append(
  _JWTPROVIDER.fields_by_name['remote_jwks'])
_JWTPROVIDER.fields_by_name['remote_jwks'].containing_oneof = _JWTPROVIDER.oneofs_by_name['jwks_source_specifier']
_JWTPROVIDER.oneofs_by_name['jwks_source_specifier'].fields.append(
  _JWTPROVIDER.fields_by_name['local_jwks'])
_JWTPROVIDER.fields_by_name['local_jwks'].containing_oneof = _JWTPROVIDER.oneofs_by_name['jwks_source_specifier']
_REMOTEJWKS.fields_by_name['http_uri'].message_type = envoy_dot_api_dot_v2_dot_core_dot_http__uri__pb2._HTTPURI
_REMOTEJWKS.fields_by_name['cache_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_JWTREQUIREMENT.fields_by_name['provider_and_audiences'].message_type = _PROVIDERWITHAUDIENCES
_JWTREQUIREMENT.fields_by_name['requires_any'].message_type = _JWTREQUIREMENTORLIST
_JWTREQUIREMENT.fields_by_name['requires_all'].message_type = _JWTREQUIREMENTANDLIST
_JWTREQUIREMENT.fields_by_name['allow_missing_or_failed'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_JWTREQUIREMENT.oneofs_by_name['requires_type'].fields.append(
  _JWTREQUIREMENT.fields_by_name['provider_name'])
_JWTREQUIREMENT.fields_by_name['provider_name'].containing_oneof = _JWTREQUIREMENT.oneofs_by_name['requires_type']
_JWTREQUIREMENT.oneofs_by_name['requires_type'].fields.append(
  _JWTREQUIREMENT.fields_by_name['provider_and_audiences'])
_JWTREQUIREMENT.fields_by_name['provider_and_audiences'].containing_oneof = _JWTREQUIREMENT.oneofs_by_name['requires_type']
_JWTREQUIREMENT.oneofs_by_name['requires_type'].fields.append(
  _JWTREQUIREMENT.fields_by_name['requires_any'])
_JWTREQUIREMENT.fields_by_name['requires_any'].containing_oneof = _JWTREQUIREMENT.oneofs_by_name['requires_type']
_JWTREQUIREMENT.oneofs_by_name['requires_type'].fields.append(
  _JWTREQUIREMENT.fields_by_name['requires_all'])
_JWTREQUIREMENT.fields_by_name['requires_all'].containing_oneof = _JWTREQUIREMENT.oneofs_by_name['requires_type']
_JWTREQUIREMENT.oneofs_by_name['requires_type'].fields.append(
  _JWTREQUIREMENT.fields_by_name['allow_missing_or_failed'])
_JWTREQUIREMENT.fields_by_name['allow_missing_or_failed'].containing_oneof = _JWTREQUIREMENT.oneofs_by_name['requires_type']
_JWTREQUIREMENTORLIST.fields_by_name['requirements'].message_type = _JWTREQUIREMENT
_JWTREQUIREMENTANDLIST.fields_by_name['requirements'].message_type = _JWTREQUIREMENT
_REQUIREMENTRULE.fields_by_name['match'].message_type = envoy_dot_api_dot_v2_dot_route_dot_route__pb2._ROUTEMATCH
_REQUIREMENTRULE.fields_by_name['requires'].message_type = _JWTREQUIREMENT
_JWTAUTHENTICATION_PROVIDERSENTRY.fields_by_name['value'].message_type = _JWTPROVIDER
_JWTAUTHENTICATION_PROVIDERSENTRY.containing_type = _JWTAUTHENTICATION
_JWTAUTHENTICATION.fields_by_name['providers'].message_type = _JWTAUTHENTICATION_PROVIDERSENTRY
_JWTAUTHENTICATION.fields_by_name['rules'].message_type = _REQUIREMENTRULE
DESCRIPTOR.message_types_by_name['JwtProvider'] = _JWTPROVIDER
DESCRIPTOR.message_types_by_name['RemoteJwks'] = _REMOTEJWKS
DESCRIPTOR.message_types_by_name['JwtHeader'] = _JWTHEADER
DESCRIPTOR.message_types_by_name['ProviderWithAudiences'] = _PROVIDERWITHAUDIENCES
DESCRIPTOR.message_types_by_name['JwtRequirement'] = _JWTREQUIREMENT
DESCRIPTOR.message_types_by_name['JwtRequirementOrList'] = _JWTREQUIREMENTORLIST
DESCRIPTOR.message_types_by_name['JwtRequirementAndList'] = _JWTREQUIREMENTANDLIST
DESCRIPTOR.message_types_by_name['RequirementRule'] = _REQUIREMENTRULE
DESCRIPTOR.message_types_by_name['JwtAuthentication'] = _JWTAUTHENTICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JwtProvider = _reflection.GeneratedProtocolMessageType('JwtProvider', (_message.Message,), dict(
  DESCRIPTOR = _JWTPROVIDER,
  __module__ = 'envoy.config.filter.http.jwt_authn.v2alpha.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.jwt_authn.v2alpha.JwtProvider)
  ))
_sym_db.RegisterMessage(JwtProvider)

RemoteJwks = _reflection.GeneratedProtocolMessageType('RemoteJwks', (_message.Message,), dict(
  DESCRIPTOR = _REMOTEJWKS,
  __module__ = 'envoy.config.filter.http.jwt_authn.v2alpha.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.jwt_authn.v2alpha.RemoteJwks)
  ))
_sym_db.RegisterMessage(RemoteJwks)

JwtHeader = _reflection.GeneratedProtocolMessageType('JwtHeader', (_message.Message,), dict(
  DESCRIPTOR = _JWTHEADER,
  __module__ = 'envoy.config.filter.http.jwt_authn.v2alpha.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.jwt_authn.v2alpha.JwtHeader)
  ))
_sym_db.RegisterMessage(JwtHeader)

ProviderWithAudiences = _reflection.GeneratedProtocolMessageType('ProviderWithAudiences', (_message.Message,), dict(
  DESCRIPTOR = _PROVIDERWITHAUDIENCES,
  __module__ = 'envoy.config.filter.http.jwt_authn.v2alpha.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.jwt_authn.v2alpha.ProviderWithAudiences)
  ))
_sym_db.RegisterMessage(ProviderWithAudiences)

JwtRequirement = _reflection.GeneratedProtocolMessageType('JwtRequirement', (_message.Message,), dict(
  DESCRIPTOR = _JWTREQUIREMENT,
  __module__ = 'envoy.config.filter.http.jwt_authn.v2alpha.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirement)
  ))
_sym_db.RegisterMessage(JwtRequirement)

JwtRequirementOrList = _reflection.GeneratedProtocolMessageType('JwtRequirementOrList', (_message.Message,), dict(
  DESCRIPTOR = _JWTREQUIREMENTORLIST,
  __module__ = 'envoy.config.filter.http.jwt_authn.v2alpha.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirementOrList)
  ))
_sym_db.RegisterMessage(JwtRequirementOrList)

JwtRequirementAndList = _reflection.GeneratedProtocolMessageType('JwtRequirementAndList', (_message.Message,), dict(
  DESCRIPTOR = _JWTREQUIREMENTANDLIST,
  __module__ = 'envoy.config.filter.http.jwt_authn.v2alpha.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.jwt_authn.v2alpha.JwtRequirementAndList)
  ))
_sym_db.RegisterMessage(JwtRequirementAndList)

RequirementRule = _reflection.GeneratedProtocolMessageType('RequirementRule', (_message.Message,), dict(
  DESCRIPTOR = _REQUIREMENTRULE,
  __module__ = 'envoy.config.filter.http.jwt_authn.v2alpha.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.jwt_authn.v2alpha.RequirementRule)
  ))
_sym_db.RegisterMessage(RequirementRule)

JwtAuthentication = _reflection.GeneratedProtocolMessageType('JwtAuthentication', (_message.Message,), dict(

  ProvidersEntry = _reflection.GeneratedProtocolMessageType('ProvidersEntry', (_message.Message,), dict(
    DESCRIPTOR = _JWTAUTHENTICATION_PROVIDERSENTRY,
    __module__ = 'envoy.config.filter.http.jwt_authn.v2alpha.config_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.http.jwt_authn.v2alpha.JwtAuthentication.ProvidersEntry)
    ))
  ,
  DESCRIPTOR = _JWTAUTHENTICATION,
  __module__ = 'envoy.config.filter.http.jwt_authn.v2alpha.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.jwt_authn.v2alpha.JwtAuthentication)
  ))
_sym_db.RegisterMessage(JwtAuthentication)
_sym_db.RegisterMessage(JwtAuthentication.ProvidersEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n8io.envoyproxy.envoy.config.filter.http.jwt_authn.v2alphaB\013ConfigProtoP\001'))
_JWTPROVIDER.oneofs_by_name['jwks_source_specifier'].has_options = True
_JWTPROVIDER.oneofs_by_name['jwks_source_specifier']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_JWTPROVIDER.fields_by_name['issuer'].has_options = True
_JWTPROVIDER.fields_by_name['issuer']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_JWTHEADER.fields_by_name['name'].has_options = True
_JWTHEADER.fields_by_name['name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
_JWTREQUIREMENTORLIST.fields_by_name['requirements'].has_options = True
_JWTREQUIREMENTORLIST.fields_by_name['requirements']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\002'))
_JWTREQUIREMENTANDLIST.fields_by_name['requirements'].has_options = True
_JWTREQUIREMENTANDLIST.fields_by_name['requirements']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\002'))
_REQUIREMENTRULE.fields_by_name['match'].has_options = True
_REQUIREMENTRULE.fields_by_name['match']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001'))
_JWTAUTHENTICATION_PROVIDERSENTRY.has_options = True
_JWTAUTHENTICATION_PROVIDERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
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
