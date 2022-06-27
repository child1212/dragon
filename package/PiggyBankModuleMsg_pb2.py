# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PiggyBankModuleMsg.proto
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
  name='PiggyBankModuleMsg.proto',
  package='com.common.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18PiggyBankModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"U\n\x10PiggyBankInfoMsg\x12\x0e\n\x06\x62\x61nkId\x18\x01 \x01(\t\x12\x11\n\tstartTime\x18\x02 \x01(\x03\x12\x0e\n\x06\x65nergy\x18\x03 \x01(\x05\x12\x0e\n\x06\x62ought\x18\x04 \x01(\x08\"\'\n\x15PiggyBankStartRequest\x12\x0e\n\x06\x62\x61nkId\x18\x01 \x02(\t\"\x18\n\x16PiggyBankStartResponse\"\x1a\n\x18PiggyBankUpdateIdRequest\"\x1b\n\x19PiggyBankUpdateIdResponse*{\n\x1cPiggyBankModuleMsgSubCommand\x12+\n%PIGGYBANKMODULEMSG_SUB_PIGGYBANKSTART\x10\xd1\xd7\x01\x12.\n(PIGGYBANKMODULEMSG_SUB_PIGGYBANKUPDATEID\x10\xd2\xd7\x01'
  ,
  dependencies=[ItemModuleMsg__pb2.DESCRIPTOR,])

_PIGGYBANKMODULEMSGSUBCOMMAND = _descriptor.EnumDescriptor(
  name='PiggyBankModuleMsgSubCommand',
  full_name='com.common.msg.PiggyBankModuleMsgSubCommand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PIGGYBANKMODULEMSG_SUB_PIGGYBANKSTART', index=0, number=27601,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PIGGYBANKMODULEMSG_SUB_PIGGYBANKUPDATEID', index=1, number=27602,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=276,
  serialized_end=399,
)
_sym_db.RegisterEnumDescriptor(_PIGGYBANKMODULEMSGSUBCOMMAND)

PiggyBankModuleMsgSubCommand = enum_type_wrapper.EnumTypeWrapper(_PIGGYBANKMODULEMSGSUBCOMMAND)
PIGGYBANKMODULEMSG_SUB_PIGGYBANKSTART = 27601
PIGGYBANKMODULEMSG_SUB_PIGGYBANKUPDATEID = 27602



_PIGGYBANKINFOMSG = _descriptor.Descriptor(
  name='PiggyBankInfoMsg',
  full_name='com.common.msg.PiggyBankInfoMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bankId', full_name='com.common.msg.PiggyBankInfoMsg.bankId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='com.common.msg.PiggyBankInfoMsg.startTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='energy', full_name='com.common.msg.PiggyBankInfoMsg.energy', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bought', full_name='com.common.msg.PiggyBankInfoMsg.bought', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=65,
  serialized_end=150,
)


_PIGGYBANKSTARTREQUEST = _descriptor.Descriptor(
  name='PiggyBankStartRequest',
  full_name='com.common.msg.PiggyBankStartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bankId', full_name='com.common.msg.PiggyBankStartRequest.bankId', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=152,
  serialized_end=191,
)


_PIGGYBANKSTARTRESPONSE = _descriptor.Descriptor(
  name='PiggyBankStartResponse',
  full_name='com.common.msg.PiggyBankStartResponse',
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
  serialized_start=193,
  serialized_end=217,
)


_PIGGYBANKUPDATEIDREQUEST = _descriptor.Descriptor(
  name='PiggyBankUpdateIdRequest',
  full_name='com.common.msg.PiggyBankUpdateIdRequest',
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
  serialized_start=219,
  serialized_end=245,
)


_PIGGYBANKUPDATEIDRESPONSE = _descriptor.Descriptor(
  name='PiggyBankUpdateIdResponse',
  full_name='com.common.msg.PiggyBankUpdateIdResponse',
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
  serialized_start=247,
  serialized_end=274,
)

DESCRIPTOR.message_types_by_name['PiggyBankInfoMsg'] = _PIGGYBANKINFOMSG
DESCRIPTOR.message_types_by_name['PiggyBankStartRequest'] = _PIGGYBANKSTARTREQUEST
DESCRIPTOR.message_types_by_name['PiggyBankStartResponse'] = _PIGGYBANKSTARTRESPONSE
DESCRIPTOR.message_types_by_name['PiggyBankUpdateIdRequest'] = _PIGGYBANKUPDATEIDREQUEST
DESCRIPTOR.message_types_by_name['PiggyBankUpdateIdResponse'] = _PIGGYBANKUPDATEIDRESPONSE
DESCRIPTOR.enum_types_by_name['PiggyBankModuleMsgSubCommand'] = _PIGGYBANKMODULEMSGSUBCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PiggyBankInfoMsg = _reflection.GeneratedProtocolMessageType('PiggyBankInfoMsg', (_message.Message,), {
  'DESCRIPTOR' : _PIGGYBANKINFOMSG,
  '__module__' : 'PiggyBankModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.PiggyBankInfoMsg)
  })
_sym_db.RegisterMessage(PiggyBankInfoMsg)

PiggyBankStartRequest = _reflection.GeneratedProtocolMessageType('PiggyBankStartRequest', (_message.Message,), {
  'DESCRIPTOR' : _PIGGYBANKSTARTREQUEST,
  '__module__' : 'PiggyBankModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.PiggyBankStartRequest)
  })
_sym_db.RegisterMessage(PiggyBankStartRequest)

PiggyBankStartResponse = _reflection.GeneratedProtocolMessageType('PiggyBankStartResponse', (_message.Message,), {
  'DESCRIPTOR' : _PIGGYBANKSTARTRESPONSE,
  '__module__' : 'PiggyBankModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.PiggyBankStartResponse)
  })
_sym_db.RegisterMessage(PiggyBankStartResponse)

PiggyBankUpdateIdRequest = _reflection.GeneratedProtocolMessageType('PiggyBankUpdateIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _PIGGYBANKUPDATEIDREQUEST,
  '__module__' : 'PiggyBankModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.PiggyBankUpdateIdRequest)
  })
_sym_db.RegisterMessage(PiggyBankUpdateIdRequest)

PiggyBankUpdateIdResponse = _reflection.GeneratedProtocolMessageType('PiggyBankUpdateIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _PIGGYBANKUPDATEIDRESPONSE,
  '__module__' : 'PiggyBankModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.PiggyBankUpdateIdResponse)
  })
_sym_db.RegisterMessage(PiggyBankUpdateIdResponse)


# @@protoc_insertion_point(module_scope)