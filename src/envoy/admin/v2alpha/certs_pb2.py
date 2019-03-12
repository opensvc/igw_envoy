# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/admin/v2alpha/certs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/admin/v2alpha/certs.proto',
  package='envoy.admin.v2alpha',
  syntax='proto3',
  serialized_pb=_b('\n\x1f\x65nvoy/admin/v2alpha/certs.proto\x12\x13\x65nvoy.admin.v2alpha\x1a\x1fgoogle/protobuf/timestamp.proto\"F\n\x0c\x43\x65rtificates\x12\x36\n\x0c\x63\x65rtificates\x18\x01 \x03(\x0b\x32 .envoy.admin.v2alpha.Certificate\"\x84\x01\n\x0b\x43\x65rtificate\x12\x38\n\x07\x63\x61_cert\x18\x01 \x03(\x0b\x32\'.envoy.admin.v2alpha.CertificateDetails\x12;\n\ncert_chain\x18\x02 \x03(\x0b\x32\'.envoy.admin.v2alpha.CertificateDetails\"\x83\x02\n\x12\x43\x65rtificateDetails\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x15\n\rserial_number\x18\x02 \x01(\t\x12\x44\n\x11subject_alt_names\x18\x03 \x03(\x0b\x32).envoy.admin.v2alpha.SubjectAlternateName\x12\x1d\n\x15\x64\x61ys_until_expiration\x18\x04 \x01(\x04\x12.\n\nvalid_from\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0f\x65xpiration_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"<\n\x14SubjectAlternateName\x12\r\n\x03\x64ns\x18\x01 \x01(\tH\x00\x12\r\n\x03uri\x18\x02 \x01(\tH\x00\x42\x06\n\x04nameB1\n!io.envoyproxy.envoy.admin.v2alphaB\nCertsProtoP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CERTIFICATES = _descriptor.Descriptor(
  name='Certificates',
  full_name='envoy.admin.v2alpha.Certificates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='certificates', full_name='envoy.admin.v2alpha.Certificates.certificates', index=0,
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
  serialized_start=89,
  serialized_end=159,
)


_CERTIFICATE = _descriptor.Descriptor(
  name='Certificate',
  full_name='envoy.admin.v2alpha.Certificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ca_cert', full_name='envoy.admin.v2alpha.Certificate.ca_cert', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cert_chain', full_name='envoy.admin.v2alpha.Certificate.cert_chain', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=162,
  serialized_end=294,
)


_CERTIFICATEDETAILS = _descriptor.Descriptor(
  name='CertificateDetails',
  full_name='envoy.admin.v2alpha.CertificateDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='envoy.admin.v2alpha.CertificateDetails.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='envoy.admin.v2alpha.CertificateDetails.serial_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subject_alt_names', full_name='envoy.admin.v2alpha.CertificateDetails.subject_alt_names', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='days_until_expiration', full_name='envoy.admin.v2alpha.CertificateDetails.days_until_expiration', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valid_from', full_name='envoy.admin.v2alpha.CertificateDetails.valid_from', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiration_time', full_name='envoy.admin.v2alpha.CertificateDetails.expiration_time', index=5,
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
  serialized_start=297,
  serialized_end=556,
)


_SUBJECTALTERNATENAME = _descriptor.Descriptor(
  name='SubjectAlternateName',
  full_name='envoy.admin.v2alpha.SubjectAlternateName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dns', full_name='envoy.admin.v2alpha.SubjectAlternateName.dns', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uri', full_name='envoy.admin.v2alpha.SubjectAlternateName.uri', index=1,
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
    _descriptor.OneofDescriptor(
      name='name', full_name='envoy.admin.v2alpha.SubjectAlternateName.name',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=558,
  serialized_end=618,
)

_CERTIFICATES.fields_by_name['certificates'].message_type = _CERTIFICATE
_CERTIFICATE.fields_by_name['ca_cert'].message_type = _CERTIFICATEDETAILS
_CERTIFICATE.fields_by_name['cert_chain'].message_type = _CERTIFICATEDETAILS
_CERTIFICATEDETAILS.fields_by_name['subject_alt_names'].message_type = _SUBJECTALTERNATENAME
_CERTIFICATEDETAILS.fields_by_name['valid_from'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CERTIFICATEDETAILS.fields_by_name['expiration_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SUBJECTALTERNATENAME.oneofs_by_name['name'].fields.append(
  _SUBJECTALTERNATENAME.fields_by_name['dns'])
_SUBJECTALTERNATENAME.fields_by_name['dns'].containing_oneof = _SUBJECTALTERNATENAME.oneofs_by_name['name']
_SUBJECTALTERNATENAME.oneofs_by_name['name'].fields.append(
  _SUBJECTALTERNATENAME.fields_by_name['uri'])
_SUBJECTALTERNATENAME.fields_by_name['uri'].containing_oneof = _SUBJECTALTERNATENAME.oneofs_by_name['name']
DESCRIPTOR.message_types_by_name['Certificates'] = _CERTIFICATES
DESCRIPTOR.message_types_by_name['Certificate'] = _CERTIFICATE
DESCRIPTOR.message_types_by_name['CertificateDetails'] = _CERTIFICATEDETAILS
DESCRIPTOR.message_types_by_name['SubjectAlternateName'] = _SUBJECTALTERNATENAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Certificates = _reflection.GeneratedProtocolMessageType('Certificates', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATES,
  __module__ = 'envoy.admin.v2alpha.certs_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.Certificates)
  ))
_sym_db.RegisterMessage(Certificates)

Certificate = _reflection.GeneratedProtocolMessageType('Certificate', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATE,
  __module__ = 'envoy.admin.v2alpha.certs_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.Certificate)
  ))
_sym_db.RegisterMessage(Certificate)

CertificateDetails = _reflection.GeneratedProtocolMessageType('CertificateDetails', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATEDETAILS,
  __module__ = 'envoy.admin.v2alpha.certs_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.CertificateDetails)
  ))
_sym_db.RegisterMessage(CertificateDetails)

SubjectAlternateName = _reflection.GeneratedProtocolMessageType('SubjectAlternateName', (_message.Message,), dict(
  DESCRIPTOR = _SUBJECTALTERNATENAME,
  __module__ = 'envoy.admin.v2alpha.certs_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.SubjectAlternateName)
  ))
_sym_db.RegisterMessage(SubjectAlternateName)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!io.envoyproxy.envoy.admin.v2alphaB\nCertsProtoP\001'))
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