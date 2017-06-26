# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wemedia.proto

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
  name='wemedia.proto',
  package='wemedia',
  syntax='proto2',
  serialized_pb=_b('\n\rwemedia.proto\x12\x07wemedia\"N\n\x0eNewsMediaOwner\x12\x13\n\x0btime_update\x18\x01 \x01(\x03\x12\x10\n\x08media_id\x18\x02 \x01(\t\x12\x15\n\ris_flow_owner\x18\x03 \x01(\x05\"\x1b\n\x07ReqBody\x12\x10\n\x08media_id\x18\x01 \x01(\t\"I\n\x08RespBody\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\x07\x12+\n\nmedia_info\x18\x02 \x01(\x0b\x32\x17.wemedia.NewsMediaOwner')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_NEWSMEDIAOWNER = _descriptor.Descriptor(
  name='NewsMediaOwner',
  full_name='wemedia.NewsMediaOwner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_update', full_name='wemedia.NewsMediaOwner.time_update', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_id', full_name='wemedia.NewsMediaOwner.media_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_flow_owner', full_name='wemedia.NewsMediaOwner.is_flow_owner', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=104,
)


_REQBODY = _descriptor.Descriptor(
  name='ReqBody',
  full_name='wemedia.ReqBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='media_id', full_name='wemedia.ReqBody.media_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=133,
)


_RESPBODY = _descriptor.Descriptor(
  name='RespBody',
  full_name='wemedia.RespBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='wemedia.RespBody.err_code', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='media_info', full_name='wemedia.RespBody.media_info', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=208,
)

_RESPBODY.fields_by_name['media_info'].message_type = _NEWSMEDIAOWNER
DESCRIPTOR.message_types_by_name['NewsMediaOwner'] = _NEWSMEDIAOWNER
DESCRIPTOR.message_types_by_name['ReqBody'] = _REQBODY
DESCRIPTOR.message_types_by_name['RespBody'] = _RESPBODY

NewsMediaOwner = _reflection.GeneratedProtocolMessageType('NewsMediaOwner', (_message.Message,), dict(
  DESCRIPTOR = _NEWSMEDIAOWNER,
  __module__ = 'wemedia_pb2'
  # @@protoc_insertion_point(class_scope:wemedia.NewsMediaOwner)
  ))
_sym_db.RegisterMessage(NewsMediaOwner)

ReqBody = _reflection.GeneratedProtocolMessageType('ReqBody', (_message.Message,), dict(
  DESCRIPTOR = _REQBODY,
  __module__ = 'wemedia_pb2'
  # @@protoc_insertion_point(class_scope:wemedia.ReqBody)
  ))
_sym_db.RegisterMessage(ReqBody)

RespBody = _reflection.GeneratedProtocolMessageType('RespBody', (_message.Message,), dict(
  DESCRIPTOR = _RESPBODY,
  __module__ = 'wemedia_pb2'
  # @@protoc_insertion_point(class_scope:wemedia.RespBody)
  ))
_sym_db.RegisterMessage(RespBody)


# @@protoc_insertion_point(module_scope)