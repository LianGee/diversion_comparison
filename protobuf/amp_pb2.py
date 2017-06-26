# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: amp.proto

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
  name='amp.proto',
  package='amp',
  syntax='proto2',
  serialized_pb=_b('\n\tamp.proto\x12\x03\x61mp\"M\n\x07TagInfo\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x0e\n\x06weight\x18\x02 \x01(\x07\x12\x13\n\x0b\x65xpire_time\x18\x03 \x01(\x06\x12\x10\n\x08opt_type\x18\x04 \x01(\x07\"T\n\x07\x41mpInfo\x12\x10\n\x08\x61mp_type\x18\x01 \x01(\x07\x12\"\n\x0crpt_tag_info\x18\x02 \x03(\x0b\x32\x0c.amp.TagInfo\x12\x13\n\x0bupdate_type\x18\x03 \x01(\x07\"\x9f\x01\n\x0cQueryReqBody\x12\x0b\n\x03uin\x18\x01 \x01(\x06\x12\x10\n\x08\x61pp_user\x18\x02 \x01(\t\x12\x0f\n\x07plat_id\x18\x03 \x01(\x07\x12\x11\n\tclient_ip\x18\x04 \x01(\x07\x12\x13\n\x0b\x63lient_port\x18\x05 \x01(\x07\x12\x12\n\nquery_type\x18\x06 \x01(\x07\x12\x0f\n\x07version\x18\x07 \x01(\x07\x12\x12\n\nsubversion\x18\x08 \x01(\x07\"q\n\rQueryRespBody\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\x07\x12\x0f\n\x07\x65rr_msg\x18\x02 \x01(\t\x12\x0b\n\x03uin\x18\x03 \x01(\x07\x12\x10\n\x08\x61pp_user\x18\x04 \x01(\t\x12\x1e\n\x08\x61mp_info\x18\x05 \x03(\x0b\x32\x0c.amp.AmpInfo\"\xb1\x01\n\rUpdateReqBody\x12\x0b\n\x03uin\x18\x01 \x01(\x06\x12\x10\n\x08\x61pp_user\x18\x02 \x01(\t\x12\x0f\n\x07plat_id\x18\x03 \x01(\x07\x12\x11\n\tclient_ip\x18\x04 \x01(\x07\x12\x13\n\x0b\x63lient_port\x18\x05 \x01(\x07\x12\x13\n\x0bupdate_type\x18\x06 \x01(\x07\x12\x0f\n\x07version\x18\x07 \x01(\x07\x12\"\n\x0crpt_amp_info\x18\x08 \x03(\x0b\x32\x0c.amp.AmpInfo\"R\n\x0eUpdateRespBody\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\x07\x12\x0f\n\x07\x65rr_msg\x18\x02 \x01(\t\x12\x0b\n\x03uin\x18\x03 \x01(\x07\x12\x10\n\x08\x61pp_user\x18\x04 \x01(\t')
)




_TAGINFO = _descriptor.Descriptor(
  name='TagInfo',
  full_name='amp.TagInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='amp.TagInfo.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight', full_name='amp.TagInfo.weight', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expire_time', full_name='amp.TagInfo.expire_time', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opt_type', full_name='amp.TagInfo.opt_type', index=3,
      number=4, type=7, cpp_type=3, label=1,
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
  serialized_start=18,
  serialized_end=95,
)


_AMPINFO = _descriptor.Descriptor(
  name='AmpInfo',
  full_name='amp.AmpInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amp_type', full_name='amp.AmpInfo.amp_type', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpt_tag_info', full_name='amp.AmpInfo.rpt_tag_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_type', full_name='amp.AmpInfo.update_type', index=2,
      number=3, type=7, cpp_type=3, label=1,
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
  serialized_start=97,
  serialized_end=181,
)


_QUERYREQBODY = _descriptor.Descriptor(
  name='QueryReqBody',
  full_name='amp.QueryReqBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uin', full_name='amp.QueryReqBody.uin', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_user', full_name='amp.QueryReqBody.app_user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plat_id', full_name='amp.QueryReqBody.plat_id', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_ip', full_name='amp.QueryReqBody.client_ip', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_port', full_name='amp.QueryReqBody.client_port', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query_type', full_name='amp.QueryReqBody.query_type', index=5,
      number=6, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='amp.QueryReqBody.version', index=6,
      number=7, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subversion', full_name='amp.QueryReqBody.subversion', index=7,
      number=8, type=7, cpp_type=3, label=1,
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
  serialized_start=184,
  serialized_end=343,
)


_QUERYRESPBODY = _descriptor.Descriptor(
  name='QueryRespBody',
  full_name='amp.QueryRespBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='amp.QueryRespBody.err_code', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='amp.QueryRespBody.err_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uin', full_name='amp.QueryRespBody.uin', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_user', full_name='amp.QueryRespBody.app_user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amp_info', full_name='amp.QueryRespBody.amp_info', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=458,
)


_UPDATEREQBODY = _descriptor.Descriptor(
  name='UpdateReqBody',
  full_name='amp.UpdateReqBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uin', full_name='amp.UpdateReqBody.uin', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_user', full_name='amp.UpdateReqBody.app_user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plat_id', full_name='amp.UpdateReqBody.plat_id', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_ip', full_name='amp.UpdateReqBody.client_ip', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_port', full_name='amp.UpdateReqBody.client_port', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_type', full_name='amp.UpdateReqBody.update_type', index=5,
      number=6, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='amp.UpdateReqBody.version', index=6,
      number=7, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpt_amp_info', full_name='amp.UpdateReqBody.rpt_amp_info', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=638,
)


_UPDATERESPBODY = _descriptor.Descriptor(
  name='UpdateRespBody',
  full_name='amp.UpdateRespBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='amp.UpdateRespBody.err_code', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='amp.UpdateRespBody.err_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uin', full_name='amp.UpdateRespBody.uin', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_user', full_name='amp.UpdateRespBody.app_user', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=640,
  serialized_end=722,
)

_AMPINFO.fields_by_name['rpt_tag_info'].message_type = _TAGINFO
_QUERYRESPBODY.fields_by_name['amp_info'].message_type = _AMPINFO
_UPDATEREQBODY.fields_by_name['rpt_amp_info'].message_type = _AMPINFO
DESCRIPTOR.message_types_by_name['TagInfo'] = _TAGINFO
DESCRIPTOR.message_types_by_name['AmpInfo'] = _AMPINFO
DESCRIPTOR.message_types_by_name['QueryReqBody'] = _QUERYREQBODY
DESCRIPTOR.message_types_by_name['QueryRespBody'] = _QUERYRESPBODY
DESCRIPTOR.message_types_by_name['UpdateReqBody'] = _UPDATEREQBODY
DESCRIPTOR.message_types_by_name['UpdateRespBody'] = _UPDATERESPBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TagInfo = _reflection.GeneratedProtocolMessageType('TagInfo', (_message.Message,), dict(
  DESCRIPTOR = _TAGINFO,
  __module__ = 'amp_pb2'
  # @@protoc_insertion_point(class_scope:amp.TagInfo)
  ))
_sym_db.RegisterMessage(TagInfo)

AmpInfo = _reflection.GeneratedProtocolMessageType('AmpInfo', (_message.Message,), dict(
  DESCRIPTOR = _AMPINFO,
  __module__ = 'amp_pb2'
  # @@protoc_insertion_point(class_scope:amp.AmpInfo)
  ))
_sym_db.RegisterMessage(AmpInfo)

QueryReqBody = _reflection.GeneratedProtocolMessageType('QueryReqBody', (_message.Message,), dict(
  DESCRIPTOR = _QUERYREQBODY,
  __module__ = 'amp_pb2'
  # @@protoc_insertion_point(class_scope:amp.QueryReqBody)
  ))
_sym_db.RegisterMessage(QueryReqBody)

QueryRespBody = _reflection.GeneratedProtocolMessageType('QueryRespBody', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESPBODY,
  __module__ = 'amp_pb2'
  # @@protoc_insertion_point(class_scope:amp.QueryRespBody)
  ))
_sym_db.RegisterMessage(QueryRespBody)

UpdateReqBody = _reflection.GeneratedProtocolMessageType('UpdateReqBody', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREQBODY,
  __module__ = 'amp_pb2'
  # @@protoc_insertion_point(class_scope:amp.UpdateReqBody)
  ))
_sym_db.RegisterMessage(UpdateReqBody)

UpdateRespBody = _reflection.GeneratedProtocolMessageType('UpdateRespBody', (_message.Message,), dict(
  DESCRIPTOR = _UPDATERESPBODY,
  __module__ = 'amp_pb2'
  # @@protoc_insertion_point(class_scope:amp.UpdateRespBody)
  ))
_sym_db.RegisterMessage(UpdateRespBody)


# @@protoc_insertion_point(module_scope)
