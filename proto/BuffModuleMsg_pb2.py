# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BuffModuleMsg.proto
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
  name='BuffModuleMsg.proto',
  package='com.common.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x42uffModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"C\n\x07\x42uffMsg\x12\x0e\n\x06\x62uffId\x18\x01 \x01(\x03\x12\x16\n\x0e\x62uffTemplateId\x18\x02 \x01(\t\x12\x10\n\x08\x64uration\x18\x03 \x01(\x03\"\x11\n\x0f\x42uffListRequest\"C\n\x10\x42uffListResponse\x12/\n\x0e\x65\x66\x66\x65\x63tiveBuffs\x18\x01 \x03(\x0b\x32\x17.com.common.msg.BuffMsg\"#\n\x11\x42uffActiveRequest\x12\x0e\n\x06itemId\x18\x01 \x01(\t\"f\n\x12\x42uffActiveResponse\x12(\n\x07\x62uffMsg\x18\x01 \x01(\x0b\x32\x17.com.common.msg.BuffMsg\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.com.common.msg.ItemMsg*]\n\x17\x42uffModuleMsgSubCommand\x12\x1f\n\x1a\x42UFFMODULEMSG_SUB_BUFFLIST\x10\xf9U\x12!\n\x1c\x42UFFMODULEMSG_SUB_BUFFACTIVE\x10\xfaU'
  ,
  dependencies=[ItemModuleMsg__pb2.DESCRIPTOR,])

_BUFFMODULEMSGSUBCOMMAND = _descriptor.EnumDescriptor(
  name='BuffModuleMsgSubCommand',
  full_name='com.common.msg.BuffModuleMsgSubCommand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUFFMODULEMSG_SUB_BUFFLIST', index=0, number=11001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUFFMODULEMSG_SUB_BUFFACTIVE', index=1, number=11002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=358,
  serialized_end=451,
)
_sym_db.RegisterEnumDescriptor(_BUFFMODULEMSGSUBCOMMAND)

BuffModuleMsgSubCommand = enum_type_wrapper.EnumTypeWrapper(_BUFFMODULEMSGSUBCOMMAND)
BUFFMODULEMSG_SUB_BUFFLIST = 11001
BUFFMODULEMSG_SUB_BUFFACTIVE = 11002



_BUFFMSG = _descriptor.Descriptor(
  name='BuffMsg',
  full_name='com.common.msg.BuffMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffId', full_name='com.common.msg.BuffMsg.buffId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buffTemplateId', full_name='com.common.msg.BuffMsg.buffTemplateId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration', full_name='com.common.msg.BuffMsg.duration', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=60,
  serialized_end=127,
)


_BUFFLISTREQUEST = _descriptor.Descriptor(
  name='BuffListRequest',
  full_name='com.common.msg.BuffListRequest',
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
  serialized_start=129,
  serialized_end=146,
)


_BUFFLISTRESPONSE = _descriptor.Descriptor(
  name='BuffListResponse',
  full_name='com.common.msg.BuffListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='effectiveBuffs', full_name='com.common.msg.BuffListResponse.effectiveBuffs', index=0,
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
  serialized_start=148,
  serialized_end=215,
)


_BUFFACTIVEREQUEST = _descriptor.Descriptor(
  name='BuffActiveRequest',
  full_name='com.common.msg.BuffActiveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='itemId', full_name='com.common.msg.BuffActiveRequest.itemId', index=0,
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
  serialized_start=217,
  serialized_end=252,
)


_BUFFACTIVERESPONSE = _descriptor.Descriptor(
  name='BuffActiveResponse',
  full_name='com.common.msg.BuffActiveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffMsg', full_name='com.common.msg.BuffActiveResponse.buffMsg', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='com.common.msg.BuffActiveResponse.items', index=1,
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
  serialized_start=254,
  serialized_end=356,
)

_BUFFLISTRESPONSE.fields_by_name['effectiveBuffs'].message_type = _BUFFMSG
_BUFFACTIVERESPONSE.fields_by_name['buffMsg'].message_type = _BUFFMSG
_BUFFACTIVERESPONSE.fields_by_name['items'].message_type = ItemModuleMsg__pb2._ITEMMSG
DESCRIPTOR.message_types_by_name['BuffMsg'] = _BUFFMSG
DESCRIPTOR.message_types_by_name['BuffListRequest'] = _BUFFLISTREQUEST
DESCRIPTOR.message_types_by_name['BuffListResponse'] = _BUFFLISTRESPONSE
DESCRIPTOR.message_types_by_name['BuffActiveRequest'] = _BUFFACTIVEREQUEST
DESCRIPTOR.message_types_by_name['BuffActiveResponse'] = _BUFFACTIVERESPONSE
DESCRIPTOR.enum_types_by_name['BuffModuleMsgSubCommand'] = _BUFFMODULEMSGSUBCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuffMsg = _reflection.GeneratedProtocolMessageType('BuffMsg', (_message.Message,), {
  'DESCRIPTOR' : _BUFFMSG,
  '__module__' : 'BuffModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.BuffMsg)
  })
_sym_db.RegisterMessage(BuffMsg)

BuffListRequest = _reflection.GeneratedProtocolMessageType('BuffListRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUFFLISTREQUEST,
  '__module__' : 'BuffModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.BuffListRequest)
  })
_sym_db.RegisterMessage(BuffListRequest)

BuffListResponse = _reflection.GeneratedProtocolMessageType('BuffListResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUFFLISTRESPONSE,
  '__module__' : 'BuffModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.BuffListResponse)
  })
_sym_db.RegisterMessage(BuffListResponse)

BuffActiveRequest = _reflection.GeneratedProtocolMessageType('BuffActiveRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUFFACTIVEREQUEST,
  '__module__' : 'BuffModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.BuffActiveRequest)
  })
_sym_db.RegisterMessage(BuffActiveRequest)

BuffActiveResponse = _reflection.GeneratedProtocolMessageType('BuffActiveResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUFFACTIVERESPONSE,
  '__module__' : 'BuffModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.BuffActiveResponse)
  })
_sym_db.RegisterMessage(BuffActiveResponse)


# @@protoc_insertion_point(module_scope)