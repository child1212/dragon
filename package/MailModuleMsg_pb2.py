# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MailModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='MailModuleMsg.proto',
  package='com.common.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13MailModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"\x11\n\x0fMailListRequest\"\xc3\x01\n\x07MailMsg\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\x05\x12\x11\n\tstartTime\x18\x03 \x02(\x03\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x03\x12\r\n\x05label\x18\x05 \x02(\t\x12\x0f\n\x07\x63ontent\x18\x06 \x02(\t\x12+\n\nattachment\x18\x07 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12\x0f\n\x07picture\x18\x08 \x01(\t\x12\x0c\n\x04read\x18\t \x01(\x08\x12\x0e\n\x06reawrd\x18\n \x01(\x08\"=\n\x10MailListResponse\x12)\n\x08mailList\x18\x02 \x03(\x0b\x32\x17.com.common.msg.MailMsg\" \n\x11\x44\x65leteMailRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\"?\n\x12\x44\x65leteMailResponse\x12)\n\x08mailList\x18\x01 \x03(\x0b\x32\x17.com.common.msg.MailMsg\" \n\x11RewardMailRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\"g\n\x12RewardMailResponse\x12)\n\x08mailList\x18\x01 \x03(\x0b\x32\x17.com.common.msg.MailMsg\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"\x1d\n\x0fReadMailRequest\x12\n\n\x02id\x18\x01 \x01(\t\"=\n\x10ReadMailResponse\x12)\n\x08mailList\x18\x01 \x03(\x0b\x32\x17.com.common.msg.MailMsg*\xa1\x01\n\x17MailModuleMsgSubCommand\x12\x1f\n\x1aMAILMODULEMSG_SUB_MAILLIST\x10\x81}\x12!\n\x1cMAILMODULEMSG_SUB_DELETEMAIL\x10\x82}\x12!\n\x1cMAILMODULEMSG_SUB_REWARDMAIL\x10\x83}\x12\x1f\n\x1aMAILMODULEMSG_SUB_READMAIL\x10\x84}'
  ,
  dependencies=[ItemModuleMsg__pb2.DESCRIPTOR,])

_MAILMODULEMSGSUBCOMMAND = _descriptor.EnumDescriptor(
  name='MailModuleMsgSubCommand',
  full_name='com.common.msg.MailModuleMsgSubCommand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MAILMODULEMSG_SUB_MAILLIST', index=0, number=16001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAILMODULEMSG_SUB_DELETEMAIL', index=1, number=16002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAILMODULEMSG_SUB_REWARDMAIL', index=2, number=16003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAILMODULEMSG_SUB_READMAIL', index=3, number=16004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=673,
  serialized_end=834,
)
_sym_db.RegisterEnumDescriptor(_MAILMODULEMSGSUBCOMMAND)

MailModuleMsgSubCommand = enum_type_wrapper.EnumTypeWrapper(_MAILMODULEMSGSUBCOMMAND)
MAILMODULEMSG_SUB_MAILLIST = 16001
MAILMODULEMSG_SUB_DELETEMAIL = 16002
MAILMODULEMSG_SUB_REWARDMAIL = 16003
MAILMODULEMSG_SUB_READMAIL = 16004



_MAILLISTREQUEST = _descriptor.Descriptor(
  name='MailListRequest',
  full_name='com.common.msg.MailListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=77,
)


_MAILMSG = _descriptor.Descriptor(
  name='MailMsg',
  full_name='com.common.msg.MailMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.common.msg.MailMsg.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='com.common.msg.MailMsg.type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='com.common.msg.MailMsg.startTime', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='com.common.msg.MailMsg.endTime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='com.common.msg.MailMsg.label', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='com.common.msg.MailMsg.content', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attachment', full_name='com.common.msg.MailMsg.attachment', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='picture', full_name='com.common.msg.MailMsg.picture', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='read', full_name='com.common.msg.MailMsg.read', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reawrd', full_name='com.common.msg.MailMsg.reawrd', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=275,
)


_MAILLISTRESPONSE = _descriptor.Descriptor(
  name='MailListResponse',
  full_name='com.common.msg.MailListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mailList', full_name='com.common.msg.MailListResponse.mailList', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=338,
)


_DELETEMAILREQUEST = _descriptor.Descriptor(
  name='DeleteMailRequest',
  full_name='com.common.msg.DeleteMailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='com.common.msg.DeleteMailRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=372,
)


_DELETEMAILRESPONSE = _descriptor.Descriptor(
  name='DeleteMailResponse',
  full_name='com.common.msg.DeleteMailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mailList', full_name='com.common.msg.DeleteMailResponse.mailList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=437,
)


_REWARDMAILREQUEST = _descriptor.Descriptor(
  name='RewardMailRequest',
  full_name='com.common.msg.RewardMailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='com.common.msg.RewardMailRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=439,
  serialized_end=471,
)


_REWARDMAILRESPONSE = _descriptor.Descriptor(
  name='RewardMailResponse',
  full_name='com.common.msg.RewardMailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mailList', full_name='com.common.msg.RewardMailResponse.mailList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='com.common.msg.RewardMailResponse.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=576,
)


_READMAILREQUEST = _descriptor.Descriptor(
  name='ReadMailRequest',
  full_name='com.common.msg.ReadMailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.common.msg.ReadMailRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=607,
)


_READMAILRESPONSE = _descriptor.Descriptor(
  name='ReadMailResponse',
  full_name='com.common.msg.ReadMailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mailList', full_name='com.common.msg.ReadMailResponse.mailList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=670,
)

_MAILMSG.fields_by_name['attachment'].message_type = ItemModuleMsg__pb2._ITEMMSG
_MAILLISTRESPONSE.fields_by_name['mailList'].message_type = _MAILMSG
_DELETEMAILRESPONSE.fields_by_name['mailList'].message_type = _MAILMSG
_REWARDMAILRESPONSE.fields_by_name['mailList'].message_type = _MAILMSG
_REWARDMAILRESPONSE.fields_by_name['items'].message_type = ItemModuleMsg__pb2._ITEMMSG
_READMAILRESPONSE.fields_by_name['mailList'].message_type = _MAILMSG
DESCRIPTOR.message_types_by_name['MailListRequest'] = _MAILLISTREQUEST
DESCRIPTOR.message_types_by_name['MailMsg'] = _MAILMSG
DESCRIPTOR.message_types_by_name['MailListResponse'] = _MAILLISTRESPONSE
DESCRIPTOR.message_types_by_name['DeleteMailRequest'] = _DELETEMAILREQUEST
DESCRIPTOR.message_types_by_name['DeleteMailResponse'] = _DELETEMAILRESPONSE
DESCRIPTOR.message_types_by_name['RewardMailRequest'] = _REWARDMAILREQUEST
DESCRIPTOR.message_types_by_name['RewardMailResponse'] = _REWARDMAILRESPONSE
DESCRIPTOR.message_types_by_name['ReadMailRequest'] = _READMAILREQUEST
DESCRIPTOR.message_types_by_name['ReadMailResponse'] = _READMAILRESPONSE
DESCRIPTOR.enum_types_by_name['MailModuleMsgSubCommand'] = _MAILMODULEMSGSUBCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MailListRequest = _reflection.GeneratedProtocolMessageType('MailListRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAILLISTREQUEST,
  '__module__' : 'MailModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.MailListRequest)
  })
_sym_db.RegisterMessage(MailListRequest)

MailMsg = _reflection.GeneratedProtocolMessageType('MailMsg', (_message.Message,), {
  'DESCRIPTOR' : _MAILMSG,
  '__module__' : 'MailModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.MailMsg)
  })
_sym_db.RegisterMessage(MailMsg)

MailListResponse = _reflection.GeneratedProtocolMessageType('MailListResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAILLISTRESPONSE,
  '__module__' : 'MailModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.MailListResponse)
  })
_sym_db.RegisterMessage(MailListResponse)

DeleteMailRequest = _reflection.GeneratedProtocolMessageType('DeleteMailRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMAILREQUEST,
  '__module__' : 'MailModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.DeleteMailRequest)
  })
_sym_db.RegisterMessage(DeleteMailRequest)

DeleteMailResponse = _reflection.GeneratedProtocolMessageType('DeleteMailResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMAILRESPONSE,
  '__module__' : 'MailModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.DeleteMailResponse)
  })
_sym_db.RegisterMessage(DeleteMailResponse)

RewardMailRequest = _reflection.GeneratedProtocolMessageType('RewardMailRequest', (_message.Message,), {
  'DESCRIPTOR' : _REWARDMAILREQUEST,
  '__module__' : 'MailModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.RewardMailRequest)
  })
_sym_db.RegisterMessage(RewardMailRequest)

RewardMailResponse = _reflection.GeneratedProtocolMessageType('RewardMailResponse', (_message.Message,), {
  'DESCRIPTOR' : _REWARDMAILRESPONSE,
  '__module__' : 'MailModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.RewardMailResponse)
  })
_sym_db.RegisterMessage(RewardMailResponse)

ReadMailRequest = _reflection.GeneratedProtocolMessageType('ReadMailRequest', (_message.Message,), {
  'DESCRIPTOR' : _READMAILREQUEST,
  '__module__' : 'MailModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ReadMailRequest)
  })
_sym_db.RegisterMessage(ReadMailRequest)

ReadMailResponse = _reflection.GeneratedProtocolMessageType('ReadMailResponse', (_message.Message,), {
  'DESCRIPTOR' : _READMAILRESPONSE,
  '__module__' : 'MailModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ReadMailResponse)
  })
_sym_db.RegisterMessage(ReadMailResponse)


# @@protoc_insertion_point(module_scope)
