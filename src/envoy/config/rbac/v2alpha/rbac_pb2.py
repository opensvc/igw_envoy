# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/rbac/v2alpha/rbac.proto

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
from envoy.api.v2.core import address_pb2 as envoy_dot_api_dot_v2_dot_core_dot_address__pb2
from envoy.api.v2.route import route_pb2 as envoy_dot_api_dot_v2_dot_route_dot_route__pb2
from envoy.type.matcher import metadata_pb2 as envoy_dot_type_dot_matcher_dot_metadata__pb2
from envoy.type.matcher import string_pb2 as envoy_dot_type_dot_matcher_dot_string__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/rbac/v2alpha/rbac.proto',
  package='envoy.config.rbac.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n$envoy/config/rbac/v2alpha/rbac.proto\x12\x19\x65nvoy.config.rbac.v2alpha\x1a\x17validate/validate.proto\x1a\x1f\x65nvoy/api/v2/core/address.proto\x1a\x1e\x65nvoy/api/v2/route/route.proto\x1a!envoy/type/matcher/metadata.proto\x1a\x1f\x65nvoy/type/matcher/string.proto\"\xf2\x01\n\x04RBAC\x12\x36\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32&.envoy.config.rbac.v2alpha.RBAC.Action\x12?\n\x08policies\x18\x02 \x03(\x0b\x32-.envoy.config.rbac.v2alpha.RBAC.PoliciesEntry\x1aR\n\rPoliciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.envoy.config.rbac.v2alpha.Policy:\x02\x38\x01\"\x1d\n\x06\x41\x63tion\x12\t\n\x05\x41LLOW\x10\x00\x12\x08\n\x04\x44\x45NY\x10\x01\"\x96\x01\n\x06Policy\x12\x46\n\x0bpermissions\x18\x01 \x03(\x0b\x32%.envoy.config.rbac.v2alpha.PermissionB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x01\x12\x44\n\nprincipals\x18\x02 \x03(\x0b\x32$.envoy.config.rbac.v2alpha.PrincipalB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x01\"\xcb\x04\n\nPermission\x12>\n\tand_rules\x18\x01 \x01(\x0b\x32).envoy.config.rbac.v2alpha.Permission.SetH\x00\x12=\n\x08or_rules\x18\x02 \x01(\x0b\x32).envoy.config.rbac.v2alpha.Permission.SetH\x00\x12\x18\n\x03\x61ny\x18\x03 \x01(\x08\x42\t\xba\xe9\xc0\x03\x04j\x02\x08\x01H\x00\x12\x33\n\x06header\x18\x04 \x01(\x0b\x32!.envoy.api.v2.route.HeaderMatcherH\x00\x12\x36\n\x0e\x64\x65stination_ip\x18\x05 \x01(\x0b\x32\x1c.envoy.api.v2.core.CidrRangeH\x00\x12\'\n\x10\x64\x65stination_port\x18\x06 \x01(\rB\x0b\xba\xe9\xc0\x03\x06*\x04\x18\xff\xff\x03H\x00\x12\x37\n\x08metadata\x18\x07 \x01(\x0b\x32#.envoy.type.matcher.MetadataMatcherH\x00\x12\x39\n\x08not_rule\x18\x08 \x01(\x0b\x32%.envoy.config.rbac.v2alpha.PermissionH\x00\x12\x42\n\x15requested_server_name\x18\t \x01(\x0b\x32!.envoy.type.matcher.StringMatcherH\x00\x1aG\n\x03Set\x12@\n\x05rules\x18\x01 \x03(\x0b\x32%.envoy.config.rbac.v2alpha.PermissionB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x01\x42\r\n\x04rule\x12\x05\xb8\xe9\xc0\x03\x01\"\xf7\x04\n\tPrincipal\x12;\n\x07\x61nd_ids\x18\x01 \x01(\x0b\x32(.envoy.config.rbac.v2alpha.Principal.SetH\x00\x12:\n\x06or_ids\x18\x02 \x01(\x0b\x32(.envoy.config.rbac.v2alpha.Principal.SetH\x00\x12\x18\n\x03\x61ny\x18\x03 \x01(\x08\x42\t\xba\xe9\xc0\x03\x04j\x02\x08\x01H\x00\x12K\n\rauthenticated\x18\x04 \x01(\x0b\x32\x32.envoy.config.rbac.v2alpha.Principal.AuthenticatedH\x00\x12\x31\n\tsource_ip\x18\x05 \x01(\x0b\x32\x1c.envoy.api.v2.core.CidrRangeH\x00\x12\x33\n\x06header\x18\x06 \x01(\x0b\x32!.envoy.api.v2.route.HeaderMatcherH\x00\x12\x37\n\x08metadata\x18\x07 \x01(\x0b\x32#.envoy.type.matcher.MetadataMatcherH\x00\x12\x36\n\x06not_id\x18\x08 \x01(\x0b\x32$.envoy.config.rbac.v2alpha.PrincipalH\x00\x1a\x44\n\x03Set\x12=\n\x03ids\x18\x01 \x03(\x0b\x32$.envoy.config.rbac.v2alpha.PrincipalB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x01\x1aV\n\rAuthenticated\x12\x39\n\x0eprincipal_name\x18\x02 \x01(\x0b\x32!.envoy.type.matcher.StringMatcherJ\x04\x08\x01\x10\x02R\x04nameB\x13\n\nidentifier\x12\x05\xb8\xe9\xc0\x03\x01\x42?\n\'io.envoyproxy.envoy.config.rbac.v2alphaB\tRbacProtoP\x01Z\x07v2alphab\x06proto3')
  ,
  dependencies=[validate_dot_validate__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_core_dot_address__pb2.DESCRIPTOR,envoy_dot_api_dot_v2_dot_route_dot_route__pb2.DESCRIPTOR,envoy_dot_type_dot_matcher_dot_metadata__pb2.DESCRIPTOR,envoy_dot_type_dot_matcher_dot_string__pb2.DESCRIPTOR,])



_RBAC_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='envoy.config.rbac.v2alpha.RBAC.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALLOW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DENY', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=439,
  serialized_end=468,
)
_sym_db.RegisterEnumDescriptor(_RBAC_ACTION)


_RBAC_POLICIESENTRY = _descriptor.Descriptor(
  name='PoliciesEntry',
  full_name='envoy.config.rbac.v2alpha.RBAC.PoliciesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.config.rbac.v2alpha.RBAC.PoliciesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='envoy.config.rbac.v2alpha.RBAC.PoliciesEntry.value', index=1,
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
  serialized_start=355,
  serialized_end=437,
)

_RBAC = _descriptor.Descriptor(
  name='RBAC',
  full_name='envoy.config.rbac.v2alpha.RBAC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='envoy.config.rbac.v2alpha.RBAC.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policies', full_name='envoy.config.rbac.v2alpha.RBAC.policies', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RBAC_POLICIESENTRY, ],
  enum_types=[
    _RBAC_ACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=468,
)


_POLICY = _descriptor.Descriptor(
  name='Policy',
  full_name='envoy.config.rbac.v2alpha.Policy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='permissions', full_name='envoy.config.rbac.v2alpha.Policy.permissions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='principals', full_name='envoy.config.rbac.v2alpha.Policy.principals', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))),
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
  serialized_start=471,
  serialized_end=621,
)


_PERMISSION_SET = _descriptor.Descriptor(
  name='Set',
  full_name='envoy.config.rbac.v2alpha.Permission.Set',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='envoy.config.rbac.v2alpha.Permission.Set.rules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))),
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
  serialized_start=1125,
  serialized_end=1196,
)

_PERMISSION = _descriptor.Descriptor(
  name='Permission',
  full_name='envoy.config.rbac.v2alpha.Permission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='and_rules', full_name='envoy.config.rbac.v2alpha.Permission.and_rules', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='or_rules', full_name='envoy.config.rbac.v2alpha.Permission.or_rules', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='any', full_name='envoy.config.rbac.v2alpha.Permission.any', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004j\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='header', full_name='envoy.config.rbac.v2alpha.Permission.header', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination_ip', full_name='envoy.config.rbac.v2alpha.Permission.destination_ip', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination_port', full_name='envoy.config.rbac.v2alpha.Permission.destination_port', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\006*\004\030\377\377\003'))),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='envoy.config.rbac.v2alpha.Permission.metadata', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='not_rule', full_name='envoy.config.rbac.v2alpha.Permission.not_rule', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requested_server_name', full_name='envoy.config.rbac.v2alpha.Permission.requested_server_name', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERMISSION_SET, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='rule', full_name='envoy.config.rbac.v2alpha.Permission.rule',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=624,
  serialized_end=1211,
)


_PRINCIPAL_SET = _descriptor.Descriptor(
  name='Set',
  full_name='envoy.config.rbac.v2alpha.Principal.Set',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='envoy.config.rbac.v2alpha.Principal.Set.ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))),
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
  serialized_start=1668,
  serialized_end=1736,
)

_PRINCIPAL_AUTHENTICATED = _descriptor.Descriptor(
  name='Authenticated',
  full_name='envoy.config.rbac.v2alpha.Principal.Authenticated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='principal_name', full_name='envoy.config.rbac.v2alpha.Principal.Authenticated.principal_name', index=0,
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
  serialized_start=1738,
  serialized_end=1824,
)

_PRINCIPAL = _descriptor.Descriptor(
  name='Principal',
  full_name='envoy.config.rbac.v2alpha.Principal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='and_ids', full_name='envoy.config.rbac.v2alpha.Principal.and_ids', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='or_ids', full_name='envoy.config.rbac.v2alpha.Principal.or_ids', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='any', full_name='envoy.config.rbac.v2alpha.Principal.any', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004j\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='authenticated', full_name='envoy.config.rbac.v2alpha.Principal.authenticated', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_ip', full_name='envoy.config.rbac.v2alpha.Principal.source_ip', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='envoy.config.rbac.v2alpha.Principal.header', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='envoy.config.rbac.v2alpha.Principal.metadata', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='not_id', full_name='envoy.config.rbac.v2alpha.Principal.not_id', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PRINCIPAL_SET, _PRINCIPAL_AUTHENTICATED, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='identifier', full_name='envoy.config.rbac.v2alpha.Principal.identifier',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=1214,
  serialized_end=1845,
)

_RBAC_POLICIESENTRY.fields_by_name['value'].message_type = _POLICY
_RBAC_POLICIESENTRY.containing_type = _RBAC
_RBAC.fields_by_name['action'].enum_type = _RBAC_ACTION
_RBAC.fields_by_name['policies'].message_type = _RBAC_POLICIESENTRY
_RBAC_ACTION.containing_type = _RBAC
_POLICY.fields_by_name['permissions'].message_type = _PERMISSION
_POLICY.fields_by_name['principals'].message_type = _PRINCIPAL
_PERMISSION_SET.fields_by_name['rules'].message_type = _PERMISSION
_PERMISSION_SET.containing_type = _PERMISSION
_PERMISSION.fields_by_name['and_rules'].message_type = _PERMISSION_SET
_PERMISSION.fields_by_name['or_rules'].message_type = _PERMISSION_SET
_PERMISSION.fields_by_name['header'].message_type = envoy_dot_api_dot_v2_dot_route_dot_route__pb2._HEADERMATCHER
_PERMISSION.fields_by_name['destination_ip'].message_type = envoy_dot_api_dot_v2_dot_core_dot_address__pb2._CIDRRANGE
_PERMISSION.fields_by_name['metadata'].message_type = envoy_dot_type_dot_matcher_dot_metadata__pb2._METADATAMATCHER
_PERMISSION.fields_by_name['not_rule'].message_type = _PERMISSION
_PERMISSION.fields_by_name['requested_server_name'].message_type = envoy_dot_type_dot_matcher_dot_string__pb2._STRINGMATCHER
_PERMISSION.oneofs_by_name['rule'].fields.append(
  _PERMISSION.fields_by_name['and_rules'])
_PERMISSION.fields_by_name['and_rules'].containing_oneof = _PERMISSION.oneofs_by_name['rule']
_PERMISSION.oneofs_by_name['rule'].fields.append(
  _PERMISSION.fields_by_name['or_rules'])
_PERMISSION.fields_by_name['or_rules'].containing_oneof = _PERMISSION.oneofs_by_name['rule']
_PERMISSION.oneofs_by_name['rule'].fields.append(
  _PERMISSION.fields_by_name['any'])
_PERMISSION.fields_by_name['any'].containing_oneof = _PERMISSION.oneofs_by_name['rule']
_PERMISSION.oneofs_by_name['rule'].fields.append(
  _PERMISSION.fields_by_name['header'])
_PERMISSION.fields_by_name['header'].containing_oneof = _PERMISSION.oneofs_by_name['rule']
_PERMISSION.oneofs_by_name['rule'].fields.append(
  _PERMISSION.fields_by_name['destination_ip'])
_PERMISSION.fields_by_name['destination_ip'].containing_oneof = _PERMISSION.oneofs_by_name['rule']
_PERMISSION.oneofs_by_name['rule'].fields.append(
  _PERMISSION.fields_by_name['destination_port'])
_PERMISSION.fields_by_name['destination_port'].containing_oneof = _PERMISSION.oneofs_by_name['rule']
_PERMISSION.oneofs_by_name['rule'].fields.append(
  _PERMISSION.fields_by_name['metadata'])
_PERMISSION.fields_by_name['metadata'].containing_oneof = _PERMISSION.oneofs_by_name['rule']
_PERMISSION.oneofs_by_name['rule'].fields.append(
  _PERMISSION.fields_by_name['not_rule'])
_PERMISSION.fields_by_name['not_rule'].containing_oneof = _PERMISSION.oneofs_by_name['rule']
_PERMISSION.oneofs_by_name['rule'].fields.append(
  _PERMISSION.fields_by_name['requested_server_name'])
_PERMISSION.fields_by_name['requested_server_name'].containing_oneof = _PERMISSION.oneofs_by_name['rule']
_PRINCIPAL_SET.fields_by_name['ids'].message_type = _PRINCIPAL
_PRINCIPAL_SET.containing_type = _PRINCIPAL
_PRINCIPAL_AUTHENTICATED.fields_by_name['principal_name'].message_type = envoy_dot_type_dot_matcher_dot_string__pb2._STRINGMATCHER
_PRINCIPAL_AUTHENTICATED.containing_type = _PRINCIPAL
_PRINCIPAL.fields_by_name['and_ids'].message_type = _PRINCIPAL_SET
_PRINCIPAL.fields_by_name['or_ids'].message_type = _PRINCIPAL_SET
_PRINCIPAL.fields_by_name['authenticated'].message_type = _PRINCIPAL_AUTHENTICATED
_PRINCIPAL.fields_by_name['source_ip'].message_type = envoy_dot_api_dot_v2_dot_core_dot_address__pb2._CIDRRANGE
_PRINCIPAL.fields_by_name['header'].message_type = envoy_dot_api_dot_v2_dot_route_dot_route__pb2._HEADERMATCHER
_PRINCIPAL.fields_by_name['metadata'].message_type = envoy_dot_type_dot_matcher_dot_metadata__pb2._METADATAMATCHER
_PRINCIPAL.fields_by_name['not_id'].message_type = _PRINCIPAL
_PRINCIPAL.oneofs_by_name['identifier'].fields.append(
  _PRINCIPAL.fields_by_name['and_ids'])
_PRINCIPAL.fields_by_name['and_ids'].containing_oneof = _PRINCIPAL.oneofs_by_name['identifier']
_PRINCIPAL.oneofs_by_name['identifier'].fields.append(
  _PRINCIPAL.fields_by_name['or_ids'])
_PRINCIPAL.fields_by_name['or_ids'].containing_oneof = _PRINCIPAL.oneofs_by_name['identifier']
_PRINCIPAL.oneofs_by_name['identifier'].fields.append(
  _PRINCIPAL.fields_by_name['any'])
_PRINCIPAL.fields_by_name['any'].containing_oneof = _PRINCIPAL.oneofs_by_name['identifier']
_PRINCIPAL.oneofs_by_name['identifier'].fields.append(
  _PRINCIPAL.fields_by_name['authenticated'])
_PRINCIPAL.fields_by_name['authenticated'].containing_oneof = _PRINCIPAL.oneofs_by_name['identifier']
_PRINCIPAL.oneofs_by_name['identifier'].fields.append(
  _PRINCIPAL.fields_by_name['source_ip'])
_PRINCIPAL.fields_by_name['source_ip'].containing_oneof = _PRINCIPAL.oneofs_by_name['identifier']
_PRINCIPAL.oneofs_by_name['identifier'].fields.append(
  _PRINCIPAL.fields_by_name['header'])
_PRINCIPAL.fields_by_name['header'].containing_oneof = _PRINCIPAL.oneofs_by_name['identifier']
_PRINCIPAL.oneofs_by_name['identifier'].fields.append(
  _PRINCIPAL.fields_by_name['metadata'])
_PRINCIPAL.fields_by_name['metadata'].containing_oneof = _PRINCIPAL.oneofs_by_name['identifier']
_PRINCIPAL.oneofs_by_name['identifier'].fields.append(
  _PRINCIPAL.fields_by_name['not_id'])
_PRINCIPAL.fields_by_name['not_id'].containing_oneof = _PRINCIPAL.oneofs_by_name['identifier']
DESCRIPTOR.message_types_by_name['RBAC'] = _RBAC
DESCRIPTOR.message_types_by_name['Policy'] = _POLICY
DESCRIPTOR.message_types_by_name['Permission'] = _PERMISSION
DESCRIPTOR.message_types_by_name['Principal'] = _PRINCIPAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RBAC = _reflection.GeneratedProtocolMessageType('RBAC', (_message.Message,), dict(

  PoliciesEntry = _reflection.GeneratedProtocolMessageType('PoliciesEntry', (_message.Message,), dict(
    DESCRIPTOR = _RBAC_POLICIESENTRY,
    __module__ = 'envoy.config.rbac.v2alpha.rbac_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.rbac.v2alpha.RBAC.PoliciesEntry)
    ))
  ,
  DESCRIPTOR = _RBAC,
  __module__ = 'envoy.config.rbac.v2alpha.rbac_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.rbac.v2alpha.RBAC)
  ))
_sym_db.RegisterMessage(RBAC)
_sym_db.RegisterMessage(RBAC.PoliciesEntry)

Policy = _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), dict(
  DESCRIPTOR = _POLICY,
  __module__ = 'envoy.config.rbac.v2alpha.rbac_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.rbac.v2alpha.Policy)
  ))
_sym_db.RegisterMessage(Policy)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), dict(

  Set = _reflection.GeneratedProtocolMessageType('Set', (_message.Message,), dict(
    DESCRIPTOR = _PERMISSION_SET,
    __module__ = 'envoy.config.rbac.v2alpha.rbac_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.rbac.v2alpha.Permission.Set)
    ))
  ,
  DESCRIPTOR = _PERMISSION,
  __module__ = 'envoy.config.rbac.v2alpha.rbac_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.rbac.v2alpha.Permission)
  ))
_sym_db.RegisterMessage(Permission)
_sym_db.RegisterMessage(Permission.Set)

Principal = _reflection.GeneratedProtocolMessageType('Principal', (_message.Message,), dict(

  Set = _reflection.GeneratedProtocolMessageType('Set', (_message.Message,), dict(
    DESCRIPTOR = _PRINCIPAL_SET,
    __module__ = 'envoy.config.rbac.v2alpha.rbac_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.rbac.v2alpha.Principal.Set)
    ))
  ,

  Authenticated = _reflection.GeneratedProtocolMessageType('Authenticated', (_message.Message,), dict(
    DESCRIPTOR = _PRINCIPAL_AUTHENTICATED,
    __module__ = 'envoy.config.rbac.v2alpha.rbac_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.rbac.v2alpha.Principal.Authenticated)
    ))
  ,
  DESCRIPTOR = _PRINCIPAL,
  __module__ = 'envoy.config.rbac.v2alpha.rbac_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.rbac.v2alpha.Principal)
  ))
_sym_db.RegisterMessage(Principal)
_sym_db.RegisterMessage(Principal.Set)
_sym_db.RegisterMessage(Principal.Authenticated)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\'io.envoyproxy.envoy.config.rbac.v2alphaB\tRbacProtoP\001Z\007v2alpha'))
_RBAC_POLICIESENTRY.has_options = True
_RBAC_POLICIESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_POLICY.fields_by_name['permissions'].has_options = True
_POLICY.fields_by_name['permissions']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))
_POLICY.fields_by_name['principals'].has_options = True
_POLICY.fields_by_name['principals']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))
_PERMISSION_SET.fields_by_name['rules'].has_options = True
_PERMISSION_SET.fields_by_name['rules']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))
_PERMISSION.oneofs_by_name['rule'].has_options = True
_PERMISSION.oneofs_by_name['rule']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_PERMISSION.fields_by_name['any'].has_options = True
_PERMISSION.fields_by_name['any']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004j\002\010\001'))
_PERMISSION.fields_by_name['destination_port'].has_options = True
_PERMISSION.fields_by_name['destination_port']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\006*\004\030\377\377\003'))
_PRINCIPAL_SET.fields_by_name['ids'].has_options = True
_PRINCIPAL_SET.fields_by_name['ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\001'))
_PRINCIPAL.oneofs_by_name['identifier'].has_options = True
_PRINCIPAL.oneofs_by_name['identifier']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_PRINCIPAL.fields_by_name['any'].has_options = True
_PRINCIPAL.fields_by_name['any']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004j\002\010\001'))
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
