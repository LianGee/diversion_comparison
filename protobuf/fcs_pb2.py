# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fcs.proto

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
  name='fcs.proto',
  package='fcs',
  syntax='proto2',
  serialized_pb=_b('\n\tfcs.proto\x12\x03\x66\x63s\"\xbb\x03\n\x07\x46\x63sInfo\x12\x15\n\ruint32_action\x18\x01 \x01(\r\x12,\n\rrpt_freq_info\x18\x02 \x03(\x0b\x32\x15.fcs.FcsInfo.FreqInfo\x12\x0c\n\x04\x66lag\x18\x03 \x01(\r\x12\x13\n\x0bstr_appuser\x18\x04 \x01(\t\x12\x0b\n\x03uin\x18\x05 \x01(\x04\x12\x11\n\tstr_appid\x18\x06 \x01(\t\x12\x0f\n\x07user_ip\x18\x07 \x01(\r\x12\x10\n\x08\x65rr_code\x18\x08 \x01(\r\x12\x15\n\rstr_old_appid\x18\t \x01(\t\x12\x19\n\x11\x63lassification_id\x18\n \x01(\r\x12\x12\n\nstr_viewid\x18\x0b \x01(\t\x1ag\n\x0c\x46reqKeyValue\x12\x13\n\x0bstr_freq_id\x18\x01 \x01(\t\x12\x1a\n\x12uint32_expire_time\x18\x02 \x01(\r\x12\x14\n\x0cuint32_value\x18\x03 \x01(\r\x12\x10\n\x08str_soid\x18\x04 \x01(\t\x1aV\n\x08\x46reqInfo\x12\x13\n\x0buint32_type\x18\x01 \x01(\r\x12\x35\n\x12rpt_freq_key_value\x18\x02 \x03(\x0b\x32\x19.fcs.FcsInfo.FreqKeyValue')
)




_FCSINFO_FREQKEYVALUE = _descriptor.Descriptor(
  name='FreqKeyValue',
  full_name='fcs.FcsInfo.FreqKeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='str_freq_id', full_name='fcs.FcsInfo.FreqKeyValue.str_freq_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint32_expire_time', full_name='fcs.FcsInfo.FreqKeyValue.uint32_expire_time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint32_value', full_name='fcs.FcsInfo.FreqKeyValue.uint32_value', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_soid', full_name='fcs.FcsInfo.FreqKeyValue.str_soid', index=3,
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
  serialized_start=271,
  serialized_end=374,
)

_FCSINFO_FREQINFO = _descriptor.Descriptor(
  name='FreqInfo',
  full_name='fcs.FcsInfo.FreqInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uint32_type', full_name='fcs.FcsInfo.FreqInfo.uint32_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpt_freq_key_value', full_name='fcs.FcsInfo.FreqInfo.rpt_freq_key_value', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=376,
  serialized_end=462,
)

_FCSINFO = _descriptor.Descriptor(
  name='FcsInfo',
  full_name='fcs.FcsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uint32_action', full_name='fcs.FcsInfo.uint32_action', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpt_freq_info', full_name='fcs.FcsInfo.rpt_freq_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='fcs.FcsInfo.flag', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_appuser', full_name='fcs.FcsInfo.str_appuser', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uin', full_name='fcs.FcsInfo.uin', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_appid', full_name='fcs.FcsInfo.str_appid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_ip', full_name='fcs.FcsInfo.user_ip', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err_code', full_name='fcs.FcsInfo.err_code', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_old_appid', full_name='fcs.FcsInfo.str_old_appid', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classification_id', full_name='fcs.FcsInfo.classification_id', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_viewid', full_name='fcs.FcsInfo.str_viewid', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FCSINFO_FREQKEYVALUE, _FCSINFO_FREQINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=462,
)

_FCSINFO_FREQKEYVALUE.containing_type = _FCSINFO
_FCSINFO_FREQINFO.fields_by_name['rpt_freq_key_value'].message_type = _FCSINFO_FREQKEYVALUE
_FCSINFO_FREQINFO.containing_type = _FCSINFO
_FCSINFO.fields_by_name['rpt_freq_info'].message_type = _FCSINFO_FREQINFO
DESCRIPTOR.message_types_by_name['FcsInfo'] = _FCSINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FcsInfo = _reflection.GeneratedProtocolMessageType('FcsInfo', (_message.Message,), dict(

  FreqKeyValue = _reflection.GeneratedProtocolMessageType('FreqKeyValue', (_message.Message,), dict(
    DESCRIPTOR = _FCSINFO_FREQKEYVALUE,
    __module__ = 'fcs_pb2'
    # @@protoc_insertion_point(class_scope:fcs.FcsInfo.FreqKeyValue)
    ))
  ,

  FreqInfo = _reflection.GeneratedProtocolMessageType('FreqInfo', (_message.Message,), dict(
    DESCRIPTOR = _FCSINFO_FREQINFO,
    __module__ = 'fcs_pb2'
    # @@protoc_insertion_point(class_scope:fcs.FcsInfo.FreqInfo)
    ))
  ,
  DESCRIPTOR = _FCSINFO,
  __module__ = 'fcs_pb2'
  # @@protoc_insertion_point(class_scope:fcs.FcsInfo)
  ))
_sym_db.RegisterMessage(FcsInfo)
_sym_db.RegisterMessage(FcsInfo.FreqKeyValue)
_sym_db.RegisterMessage(FcsInfo.FreqInfo)


# @@protoc_insertion_point(module_scope)
