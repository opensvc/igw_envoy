# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/tap/v2alpha/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.route import route_pb2 as envoy_dot_api_dot_v2_dot_route_dot_route__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/service/tap/v2alpha/common.proto',
  package='envoy.service.tap.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n&envoy/service/tap/v2alpha/common.proto\x12\x19\x65nvoy.service.tap.v2alpha\x1a\x1e\x65nvoy/api/v2/route/route.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17validate/validate.proto\"\xa4\x01\n\tTapConfig\x12K\n\x0cmatch_config\x18\x01 \x01(\x0b\x32).envoy.service.tap.v2alpha.MatchPredicateB\n\xba\xe9\xc0\x03\x05\x8a\x01\x02\x10\x01\x12J\n\routput_config\x18\x02 \x01(\x0b\x32\'.envoy.service.tap.v2alpha.OutputConfigB\n\xba\xe9\xc0\x03\x05\x8a\x01\x02\x10\x01\"\xb2\x05\n\x0eMatchPredicate\x12\x46\n\x08or_match\x18\x01 \x01(\x0b\x32\x32.envoy.service.tap.v2alpha.MatchPredicate.MatchSetH\x00\x12G\n\tand_match\x18\x02 \x01(\x0b\x32\x32.envoy.service.tap.v2alpha.MatchPredicate.MatchSetH\x00\x12>\n\tnot_match\x18\x03 \x01(\x0b\x32).envoy.service.tap.v2alpha.MatchPredicateH\x00\x12\x1e\n\tany_match\x18\x04 \x01(\x08\x42\t\xba\xe9\xc0\x03\x04j\x02\x08\x01H\x00\x12Q\n\x1ahttp_request_headers_match\x18\x05 \x01(\x0b\x32+.envoy.service.tap.v2alpha.HttpHeadersMatchH\x00\x12R\n\x1bhttp_request_trailers_match\x18\x06 \x01(\x0b\x32+.envoy.service.tap.v2alpha.HttpHeadersMatchH\x00\x12R\n\x1bhttp_response_headers_match\x18\x07 \x01(\x0b\x32+.envoy.service.tap.v2alpha.HttpHeadersMatchH\x00\x12S\n\x1chttp_response_trailers_match\x18\x08 \x01(\x0b\x32+.envoy.service.tap.v2alpha.HttpHeadersMatchH\x00\x1aP\n\x08MatchSet\x12\x44\n\x05rules\x18\x01 \x03(\x0b\x32).envoy.service.tap.v2alpha.MatchPredicateB\n\xba\xe9\xc0\x03\x05\x92\x01\x02\x08\x02\x42\r\n\x04rule\x12\x05\xb8\xe9\xc0\x03\x01\"F\n\x10HttpHeadersMatch\x12\x32\n\x07headers\x18\x01 \x03(\x0b\x32!.envoy.api.v2.route.HeaderMatcher\"\xdf\x01\n\x0cOutputConfig\x12\x42\n\x05sinks\x18\x01 \x03(\x0b\x32%.envoy.service.tap.v2alpha.OutputSinkB\x0c\xba\xe9\xc0\x03\x07\x92\x01\x04\x08\x01\x10\x01\x12;\n\x15max_buffered_rx_bytes\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12;\n\x15max_buffered_tx_bytes\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x11\n\tstreaming\x18\x04 \x01(\x08\"\xfe\x02\n\nOutputSink\x12H\n\x06\x66ormat\x18\x01 \x01(\x0e\x32,.envoy.service.tap.v2alpha.OutputSink.FormatB\n\xba\xe9\xc0\x03\x05\x82\x01\x02\x10\x01\x12H\n\x0fstreaming_admin\x18\x02 \x01(\x0b\x32-.envoy.service.tap.v2alpha.StreamingAdminSinkH\x00\x12\x41\n\x0c\x66ile_per_tap\x18\x03 \x01(\x0b\x32).envoy.service.tap.v2alpha.FilePerTapSinkH\x00\"~\n\x06\x46ormat\x12\x16\n\x12JSON_BODY_AS_BYTES\x10\x00\x12\x17\n\x13JSON_BODY_AS_STRING\x10\x01\x12\x10\n\x0cPROTO_BINARY\x10\x02\x12!\n\x1dPROTO_BINARY_LENGTH_DELIMITED\x10\x03\x12\x0e\n\nPROTO_TEXT\x10\x04\x42\x19\n\x10output_sink_type\x12\x05\xb8\xe9\xc0\x03\x01\"\x14\n\x12StreamingAdminSink\"0\n\x0e\x46ilePerTapSink\x12\x1e\n\x0bpath_prefix\x18\x01 \x01(\tB\t\xba\xe9\xc0\x03\x04r\x02 \x01\x42\x38\n\'io.envoyproxy.envoy.service.tap.v2alphaB\x0b\x43ommonProtoP\x01\x62\x06proto3')
  ,
  dependencies=[envoy_dot_api_dot_v2_dot_route_dot_route__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])



_OUTPUTSINK_FORMAT = _descriptor.EnumDescriptor(
  name='Format',
  full_name='envoy.service.tap.v2alpha.OutputSink.Format',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JSON_BODY_AS_BYTES', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JSON_BODY_AS_STRING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTO_BINARY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTO_BINARY_LENGTH_DELIMITED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTO_TEXT', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1546,
  serialized_end=1672,
)
_sym_db.RegisterEnumDescriptor(_OUTPUTSINK_FORMAT)


_TAPCONFIG = _descriptor.Descriptor(
  name='TapConfig',
  full_name='envoy.service.tap.v2alpha.TapConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match_config', full_name='envoy.service.tap.v2alpha.TapConfig.match_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001'))),
    _descriptor.FieldDescriptor(
      name='output_config', full_name='envoy.service.tap.v2alpha.TapConfig.output_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001'))),
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
  serialized_start=159,
  serialized_end=323,
)


_MATCHPREDICATE_MATCHSET = _descriptor.Descriptor(
  name='MatchSet',
  full_name='envoy.service.tap.v2alpha.MatchPredicate.MatchSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='envoy.service.tap.v2alpha.MatchPredicate.MatchSet.rules', index=0,
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
  serialized_start=921,
  serialized_end=1001,
)

_MATCHPREDICATE = _descriptor.Descriptor(
  name='MatchPredicate',
  full_name='envoy.service.tap.v2alpha.MatchPredicate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='or_match', full_name='envoy.service.tap.v2alpha.MatchPredicate.or_match', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='and_match', full_name='envoy.service.tap.v2alpha.MatchPredicate.and_match', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='not_match', full_name='envoy.service.tap.v2alpha.MatchPredicate.not_match', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='any_match', full_name='envoy.service.tap.v2alpha.MatchPredicate.any_match', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004j\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='http_request_headers_match', full_name='envoy.service.tap.v2alpha.MatchPredicate.http_request_headers_match', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='http_request_trailers_match', full_name='envoy.service.tap.v2alpha.MatchPredicate.http_request_trailers_match', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='http_response_headers_match', full_name='envoy.service.tap.v2alpha.MatchPredicate.http_response_headers_match', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='http_response_trailers_match', full_name='envoy.service.tap.v2alpha.MatchPredicate.http_response_trailers_match', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MATCHPREDICATE_MATCHSET, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='rule', full_name='envoy.service.tap.v2alpha.MatchPredicate.rule',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=326,
  serialized_end=1016,
)


_HTTPHEADERSMATCH = _descriptor.Descriptor(
  name='HttpHeadersMatch',
  full_name='envoy.service.tap.v2alpha.HttpHeadersMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='headers', full_name='envoy.service.tap.v2alpha.HttpHeadersMatch.headers', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1018,
  serialized_end=1088,
)


_OUTPUTCONFIG = _descriptor.Descriptor(
  name='OutputConfig',
  full_name='envoy.service.tap.v2alpha.OutputConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sinks', full_name='envoy.service.tap.v2alpha.OutputConfig.sinks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\007\222\001\004\010\001\020\001'))),
    _descriptor.FieldDescriptor(
      name='max_buffered_rx_bytes', full_name='envoy.service.tap.v2alpha.OutputConfig.max_buffered_rx_bytes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_buffered_tx_bytes', full_name='envoy.service.tap.v2alpha.OutputConfig.max_buffered_tx_bytes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='streaming', full_name='envoy.service.tap.v2alpha.OutputConfig.streaming', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=1091,
  serialized_end=1314,
)


_OUTPUTSINK = _descriptor.Descriptor(
  name='OutputSink',
  full_name='envoy.service.tap.v2alpha.OutputSink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='envoy.service.tap.v2alpha.OutputSink.format', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))),
    _descriptor.FieldDescriptor(
      name='streaming_admin', full_name='envoy.service.tap.v2alpha.OutputSink.streaming_admin', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_per_tap', full_name='envoy.service.tap.v2alpha.OutputSink.file_per_tap', index=2,
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
    _OUTPUTSINK_FORMAT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='output_sink_type', full_name='envoy.service.tap.v2alpha.OutputSink.output_sink_type',
      index=0, containing_type=None, fields=[], options=_descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))),
  ],
  serialized_start=1317,
  serialized_end=1699,
)


_STREAMINGADMINSINK = _descriptor.Descriptor(
  name='StreamingAdminSink',
  full_name='envoy.service.tap.v2alpha.StreamingAdminSink',
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
  serialized_start=1701,
  serialized_end=1721,
)


_FILEPERTAPSINK = _descriptor.Descriptor(
  name='FilePerTapSink',
  full_name='envoy.service.tap.v2alpha.FilePerTapSink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path_prefix', full_name='envoy.service.tap.v2alpha.FilePerTapSink.path_prefix', index=0,
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
  serialized_start=1723,
  serialized_end=1771,
)

_TAPCONFIG.fields_by_name['match_config'].message_type = _MATCHPREDICATE
_TAPCONFIG.fields_by_name['output_config'].message_type = _OUTPUTCONFIG
_MATCHPREDICATE_MATCHSET.fields_by_name['rules'].message_type = _MATCHPREDICATE
_MATCHPREDICATE_MATCHSET.containing_type = _MATCHPREDICATE
_MATCHPREDICATE.fields_by_name['or_match'].message_type = _MATCHPREDICATE_MATCHSET
_MATCHPREDICATE.fields_by_name['and_match'].message_type = _MATCHPREDICATE_MATCHSET
_MATCHPREDICATE.fields_by_name['not_match'].message_type = _MATCHPREDICATE
_MATCHPREDICATE.fields_by_name['http_request_headers_match'].message_type = _HTTPHEADERSMATCH
_MATCHPREDICATE.fields_by_name['http_request_trailers_match'].message_type = _HTTPHEADERSMATCH
_MATCHPREDICATE.fields_by_name['http_response_headers_match'].message_type = _HTTPHEADERSMATCH
_MATCHPREDICATE.fields_by_name['http_response_trailers_match'].message_type = _HTTPHEADERSMATCH
_MATCHPREDICATE.oneofs_by_name['rule'].fields.append(
  _MATCHPREDICATE.fields_by_name['or_match'])
_MATCHPREDICATE.fields_by_name['or_match'].containing_oneof = _MATCHPREDICATE.oneofs_by_name['rule']
_MATCHPREDICATE.oneofs_by_name['rule'].fields.append(
  _MATCHPREDICATE.fields_by_name['and_match'])
_MATCHPREDICATE.fields_by_name['and_match'].containing_oneof = _MATCHPREDICATE.oneofs_by_name['rule']
_MATCHPREDICATE.oneofs_by_name['rule'].fields.append(
  _MATCHPREDICATE.fields_by_name['not_match'])
_MATCHPREDICATE.fields_by_name['not_match'].containing_oneof = _MATCHPREDICATE.oneofs_by_name['rule']
_MATCHPREDICATE.oneofs_by_name['rule'].fields.append(
  _MATCHPREDICATE.fields_by_name['any_match'])
_MATCHPREDICATE.fields_by_name['any_match'].containing_oneof = _MATCHPREDICATE.oneofs_by_name['rule']
_MATCHPREDICATE.oneofs_by_name['rule'].fields.append(
  _MATCHPREDICATE.fields_by_name['http_request_headers_match'])
_MATCHPREDICATE.fields_by_name['http_request_headers_match'].containing_oneof = _MATCHPREDICATE.oneofs_by_name['rule']
_MATCHPREDICATE.oneofs_by_name['rule'].fields.append(
  _MATCHPREDICATE.fields_by_name['http_request_trailers_match'])
_MATCHPREDICATE.fields_by_name['http_request_trailers_match'].containing_oneof = _MATCHPREDICATE.oneofs_by_name['rule']
_MATCHPREDICATE.oneofs_by_name['rule'].fields.append(
  _MATCHPREDICATE.fields_by_name['http_response_headers_match'])
_MATCHPREDICATE.fields_by_name['http_response_headers_match'].containing_oneof = _MATCHPREDICATE.oneofs_by_name['rule']
_MATCHPREDICATE.oneofs_by_name['rule'].fields.append(
  _MATCHPREDICATE.fields_by_name['http_response_trailers_match'])
_MATCHPREDICATE.fields_by_name['http_response_trailers_match'].containing_oneof = _MATCHPREDICATE.oneofs_by_name['rule']
_HTTPHEADERSMATCH.fields_by_name['headers'].message_type = envoy_dot_api_dot_v2_dot_route_dot_route__pb2._HEADERMATCHER
_OUTPUTCONFIG.fields_by_name['sinks'].message_type = _OUTPUTSINK
_OUTPUTCONFIG.fields_by_name['max_buffered_rx_bytes'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_OUTPUTCONFIG.fields_by_name['max_buffered_tx_bytes'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_OUTPUTSINK.fields_by_name['format'].enum_type = _OUTPUTSINK_FORMAT
_OUTPUTSINK.fields_by_name['streaming_admin'].message_type = _STREAMINGADMINSINK
_OUTPUTSINK.fields_by_name['file_per_tap'].message_type = _FILEPERTAPSINK
_OUTPUTSINK_FORMAT.containing_type = _OUTPUTSINK
_OUTPUTSINK.oneofs_by_name['output_sink_type'].fields.append(
  _OUTPUTSINK.fields_by_name['streaming_admin'])
_OUTPUTSINK.fields_by_name['streaming_admin'].containing_oneof = _OUTPUTSINK.oneofs_by_name['output_sink_type']
_OUTPUTSINK.oneofs_by_name['output_sink_type'].fields.append(
  _OUTPUTSINK.fields_by_name['file_per_tap'])
_OUTPUTSINK.fields_by_name['file_per_tap'].containing_oneof = _OUTPUTSINK.oneofs_by_name['output_sink_type']
DESCRIPTOR.message_types_by_name['TapConfig'] = _TAPCONFIG
DESCRIPTOR.message_types_by_name['MatchPredicate'] = _MATCHPREDICATE
DESCRIPTOR.message_types_by_name['HttpHeadersMatch'] = _HTTPHEADERSMATCH
DESCRIPTOR.message_types_by_name['OutputConfig'] = _OUTPUTCONFIG
DESCRIPTOR.message_types_by_name['OutputSink'] = _OUTPUTSINK
DESCRIPTOR.message_types_by_name['StreamingAdminSink'] = _STREAMINGADMINSINK
DESCRIPTOR.message_types_by_name['FilePerTapSink'] = _FILEPERTAPSINK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TapConfig = _reflection.GeneratedProtocolMessageType('TapConfig', (_message.Message,), dict(
  DESCRIPTOR = _TAPCONFIG,
  __module__ = 'envoy.service.tap.v2alpha.common_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.tap.v2alpha.TapConfig)
  ))
_sym_db.RegisterMessage(TapConfig)

MatchPredicate = _reflection.GeneratedProtocolMessageType('MatchPredicate', (_message.Message,), dict(

  MatchSet = _reflection.GeneratedProtocolMessageType('MatchSet', (_message.Message,), dict(
    DESCRIPTOR = _MATCHPREDICATE_MATCHSET,
    __module__ = 'envoy.service.tap.v2alpha.common_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.tap.v2alpha.MatchPredicate.MatchSet)
    ))
  ,
  DESCRIPTOR = _MATCHPREDICATE,
  __module__ = 'envoy.service.tap.v2alpha.common_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.tap.v2alpha.MatchPredicate)
  ))
_sym_db.RegisterMessage(MatchPredicate)
_sym_db.RegisterMessage(MatchPredicate.MatchSet)

HttpHeadersMatch = _reflection.GeneratedProtocolMessageType('HttpHeadersMatch', (_message.Message,), dict(
  DESCRIPTOR = _HTTPHEADERSMATCH,
  __module__ = 'envoy.service.tap.v2alpha.common_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.tap.v2alpha.HttpHeadersMatch)
  ))
_sym_db.RegisterMessage(HttpHeadersMatch)

OutputConfig = _reflection.GeneratedProtocolMessageType('OutputConfig', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTCONFIG,
  __module__ = 'envoy.service.tap.v2alpha.common_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.tap.v2alpha.OutputConfig)
  ))
_sym_db.RegisterMessage(OutputConfig)

OutputSink = _reflection.GeneratedProtocolMessageType('OutputSink', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTSINK,
  __module__ = 'envoy.service.tap.v2alpha.common_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.tap.v2alpha.OutputSink)
  ))
_sym_db.RegisterMessage(OutputSink)

StreamingAdminSink = _reflection.GeneratedProtocolMessageType('StreamingAdminSink', (_message.Message,), dict(
  DESCRIPTOR = _STREAMINGADMINSINK,
  __module__ = 'envoy.service.tap.v2alpha.common_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.tap.v2alpha.StreamingAdminSink)
  ))
_sym_db.RegisterMessage(StreamingAdminSink)

FilePerTapSink = _reflection.GeneratedProtocolMessageType('FilePerTapSink', (_message.Message,), dict(
  DESCRIPTOR = _FILEPERTAPSINK,
  __module__ = 'envoy.service.tap.v2alpha.common_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.tap.v2alpha.FilePerTapSink)
  ))
_sym_db.RegisterMessage(FilePerTapSink)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\'io.envoyproxy.envoy.service.tap.v2alphaB\013CommonProtoP\001'))
_TAPCONFIG.fields_by_name['match_config'].has_options = True
_TAPCONFIG.fields_by_name['match_config']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001'))
_TAPCONFIG.fields_by_name['output_config'].has_options = True
_TAPCONFIG.fields_by_name['output_config']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\212\001\002\020\001'))
_MATCHPREDICATE_MATCHSET.fields_by_name['rules'].has_options = True
_MATCHPREDICATE_MATCHSET.fields_by_name['rules']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\222\001\002\010\002'))
_MATCHPREDICATE.oneofs_by_name['rule'].has_options = True
_MATCHPREDICATE.oneofs_by_name['rule']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_MATCHPREDICATE.fields_by_name['any_match'].has_options = True
_MATCHPREDICATE.fields_by_name['any_match']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004j\002\010\001'))
_OUTPUTCONFIG.fields_by_name['sinks'].has_options = True
_OUTPUTCONFIG.fields_by_name['sinks']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\007\222\001\004\010\001\020\001'))
_OUTPUTSINK.oneofs_by_name['output_sink_type'].has_options = True
_OUTPUTSINK.oneofs_by_name['output_sink_type']._options = _descriptor._ParseOptions(descriptor_pb2.OneofOptions(), _b('\270\351\300\003\001'))
_OUTPUTSINK.fields_by_name['format'].has_options = True
_OUTPUTSINK.fields_by_name['format']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\005\202\001\002\020\001'))
_FILEPERTAPSINK.fields_by_name['path_prefix'].has_options = True
_FILEPERTAPSINK.fields_by_name['path_prefix']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\272\351\300\003\004r\002 \001'))
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
