# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActivityGiftModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ActivityGiftModuleMsg.proto',
  package='com.common.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x41\x63tivityGiftModuleMsg.proto\x12\x0e\x63om.common.msg\"\xc4\x01\n\x18\x41\x63tivityGiftInfoResponse\x12\x12\n\nactivityId\x18\x01 \x02(\t\x12\x0e\n\x06shopId\x18\x02 \x02(\t\x12\x0e\n\x06itemId\x18\x03 \x03(\t\x12\x0f\n\x07itemCnt\x18\x04 \x03(\x05\x12\x11\n\tstartTime\x18\x05 \x02(\x03\x12\x11\n\tgiftIndex\x18\x06 \x02(\x05\x12\x12\n\nnewTrigger\x18\x07 \x02(\x08\x12\x14\n\x0c\x64iamondPrice\x18\x08 \x02(\x05\x12\x13\n\x0bpurchaseCnt\x18\t \x02(\x05'
)




_ACTIVITYGIFTINFORESPONSE = _descriptor.Descriptor(
  name='ActivityGiftInfoResponse',
  full_name='com.common.msg.ActivityGiftInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='com.common.msg.ActivityGiftInfoResponse.activityId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shopId', full_name='com.common.msg.ActivityGiftInfoResponse.shopId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemId', full_name='com.common.msg.ActivityGiftInfoResponse.itemId', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCnt', full_name='com.common.msg.ActivityGiftInfoResponse.itemCnt', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='com.common.msg.ActivityGiftInfoResponse.startTime', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='giftIndex', full_name='com.common.msg.ActivityGiftInfoResponse.giftIndex', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='newTrigger', full_name='com.common.msg.ActivityGiftInfoResponse.newTrigger', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='diamondPrice', full_name='com.common.msg.ActivityGiftInfoResponse.diamondPrice', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='purchaseCnt', full_name='com.common.msg.ActivityGiftInfoResponse.purchaseCnt', index=8,
      number=9, type=5, cpp_type=1, label=2,
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
  serialized_start=48,
  serialized_end=244,
)

DESCRIPTOR.message_types_by_name['ActivityGiftInfoResponse'] = _ACTIVITYGIFTINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActivityGiftInfoResponse = _reflection.GeneratedProtocolMessageType('ActivityGiftInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYGIFTINFORESPONSE,
  '__module__' : 'ActivityGiftModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ActivityGiftInfoResponse)
  })
_sym_db.RegisterMessage(ActivityGiftInfoResponse)


# @@protoc_insertion_point(module_scope)