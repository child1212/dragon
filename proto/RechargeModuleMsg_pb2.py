# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RechargeModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RechargeModuleMsg.proto',
  package='com.common.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17RechargeModuleMsg.proto\x12\x0e\x63om.common.msg\"$\n\x0fRechargeRequest\x12\x11\n\torderInfo\x18\x01 \x01(\t\"(\n\x10RechargeResponse\x12\x14\n\x0cgoldPassTime\x18\x01 \x01(\x03\"/\n\tSubscribe\x12\x11\n\tproductId\x18\x01 \x02(\t\x12\x0f\n\x07\x65xpired\x18\x02 \x02(\x03\"E\n\x14SubscribeInfoRequest\x12-\n\nsubscribes\x18\x01 \x03(\x0b\x32\x19.com.common.msg.Subscribe\"|\n\x15SubscribeInfoResponse\x12\x19\n\x11\x65xpiredSubscribes\x18\x01 \x03(\t\x12-\n\nsubscribes\x18\x02 \x03(\x0b\x32\x19.com.common.msg.Subscribe\x12\x19\n\x11\x63ontineSubscribes\x18\x03 \x03(\t\",\n\x17SubscribeExpiredRequest\x12\x11\n\tproductId\x18\x01 \x02(\t\"\x1a\n\x18SubscribeExpiredResponse\"N\n\x12LimitedTimeProduct\x12\x13\n\x0bproductType\x18\x01 \x02(\x05\x12\x12\n\nexpiryTime\x18\x02 \x02(\x03\x12\x0f\n\x07process\x18\x03 \x01(\x05\"7\n ProcessLimitedTimeProductRequest\x12\x13\n\x0bproductType\x18\x01 \x02(\x05\"#\n!ProcessLimitedTimeProductResponse\"\x15\n\x13\x41\x46ReportListRequest\"*\n\x14\x41\x46ReportListResponse\x12\x12\n\neventnames\x18\x01 \x03(\t\",\n\x16\x41\x46ReportConfirmRequest\x12\x12\n\neventnames\x18\x01 \x03(\t\"\x19\n\x17\x41\x46ReportConfirmResponse\"\x1c\n\x1a\x41\x46ReportHistoryListRequest\"1\n\x1b\x41\x46ReportHistoryListResponse\x12\x12\n\neventnames\x18\x01 \x03(\t*\xd4\x02\n\x1bRechargeModuleMsgSubCommand\x12#\n\x1eRECHARGEMODULEMSG_SUB_RECHARGE\x10\xb9\x17\x12(\n#RECHARGEMODULEMSG_SUB_SUBSCRIBEINFO\x10\xba\x17\x12+\n&RECHARGEMODULEMSG_SUB_SUBSCRIBEEXPIRED\x10\xbb\x17\x12\x34\n/RECHARGEMODULEMSG_SUB_PROCESSLIMITEDTIMEPRODUCT\x10\xbc\x17\x12\'\n\"RECHARGEMODULEMSG_SUB_AFREPORTLIST\x10\xbd\x17\x12*\n%RECHARGEMODULEMSG_SUB_AFREPORTCONFIRM\x10\xbe\x17\x12.\n)RECHARGEMODULEMSG_SUB_AFREPORTHISTORYLIST\x10\xbf\x17'
)

_RECHARGEMODULEMSGSUBCOMMAND = _descriptor.EnumDescriptor(
  name='RechargeModuleMsgSubCommand',
  full_name='com.common.msg.RechargeModuleMsgSubCommand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RECHARGEMODULEMSG_SUB_RECHARGE', index=0, number=3001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECHARGEMODULEMSG_SUB_SUBSCRIBEINFO', index=1, number=3002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECHARGEMODULEMSG_SUB_SUBSCRIBEEXPIRED', index=2, number=3003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECHARGEMODULEMSG_SUB_PROCESSLIMITEDTIMEPRODUCT', index=3, number=3004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECHARGEMODULEMSG_SUB_AFREPORTLIST', index=4, number=3005,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECHARGEMODULEMSG_SUB_AFREPORTCONFIRM', index=5, number=3006,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECHARGEMODULEMSG_SUB_AFREPORTHISTORYLIST', index=6, number=3007,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=839,
  serialized_end=1179,
)
_sym_db.RegisterEnumDescriptor(_RECHARGEMODULEMSGSUBCOMMAND)

RechargeModuleMsgSubCommand = enum_type_wrapper.EnumTypeWrapper(_RECHARGEMODULEMSGSUBCOMMAND)
RECHARGEMODULEMSG_SUB_RECHARGE = 3001
RECHARGEMODULEMSG_SUB_SUBSCRIBEINFO = 3002
RECHARGEMODULEMSG_SUB_SUBSCRIBEEXPIRED = 3003
RECHARGEMODULEMSG_SUB_PROCESSLIMITEDTIMEPRODUCT = 3004
RECHARGEMODULEMSG_SUB_AFREPORTLIST = 3005
RECHARGEMODULEMSG_SUB_AFREPORTCONFIRM = 3006
RECHARGEMODULEMSG_SUB_AFREPORTHISTORYLIST = 3007



_RECHARGEREQUEST = _descriptor.Descriptor(
  name='RechargeRequest',
  full_name='com.common.msg.RechargeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderInfo', full_name='com.common.msg.RechargeRequest.orderInfo', index=0,
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
  serialized_start=43,
  serialized_end=79,
)


_RECHARGERESPONSE = _descriptor.Descriptor(
  name='RechargeResponse',
  full_name='com.common.msg.RechargeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='goldPassTime', full_name='com.common.msg.RechargeResponse.goldPassTime', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=81,
  serialized_end=121,
)


_SUBSCRIBE = _descriptor.Descriptor(
  name='Subscribe',
  full_name='com.common.msg.Subscribe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='productId', full_name='com.common.msg.Subscribe.productId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expired', full_name='com.common.msg.Subscribe.expired', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  serialized_start=123,
  serialized_end=170,
)


_SUBSCRIBEINFOREQUEST = _descriptor.Descriptor(
  name='SubscribeInfoRequest',
  full_name='com.common.msg.SubscribeInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subscribes', full_name='com.common.msg.SubscribeInfoRequest.subscribes', index=0,
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
  serialized_start=172,
  serialized_end=241,
)


_SUBSCRIBEINFORESPONSE = _descriptor.Descriptor(
  name='SubscribeInfoResponse',
  full_name='com.common.msg.SubscribeInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='expiredSubscribes', full_name='com.common.msg.SubscribeInfoResponse.expiredSubscribes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subscribes', full_name='com.common.msg.SubscribeInfoResponse.subscribes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contineSubscribes', full_name='com.common.msg.SubscribeInfoResponse.contineSubscribes', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=243,
  serialized_end=367,
)


_SUBSCRIBEEXPIREDREQUEST = _descriptor.Descriptor(
  name='SubscribeExpiredRequest',
  full_name='com.common.msg.SubscribeExpiredRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='productId', full_name='com.common.msg.SubscribeExpiredRequest.productId', index=0,
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
  serialized_start=369,
  serialized_end=413,
)


_SUBSCRIBEEXPIREDRESPONSE = _descriptor.Descriptor(
  name='SubscribeExpiredResponse',
  full_name='com.common.msg.SubscribeExpiredResponse',
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
  serialized_start=415,
  serialized_end=441,
)


_LIMITEDTIMEPRODUCT = _descriptor.Descriptor(
  name='LimitedTimeProduct',
  full_name='com.common.msg.LimitedTimeProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='productType', full_name='com.common.msg.LimitedTimeProduct.productType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expiryTime', full_name='com.common.msg.LimitedTimeProduct.expiryTime', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='process', full_name='com.common.msg.LimitedTimeProduct.process', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=443,
  serialized_end=521,
)


_PROCESSLIMITEDTIMEPRODUCTREQUEST = _descriptor.Descriptor(
  name='ProcessLimitedTimeProductRequest',
  full_name='com.common.msg.ProcessLimitedTimeProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='productType', full_name='com.common.msg.ProcessLimitedTimeProductRequest.productType', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=523,
  serialized_end=578,
)


_PROCESSLIMITEDTIMEPRODUCTRESPONSE = _descriptor.Descriptor(
  name='ProcessLimitedTimeProductResponse',
  full_name='com.common.msg.ProcessLimitedTimeProductResponse',
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
  serialized_start=580,
  serialized_end=615,
)


_AFREPORTLISTREQUEST = _descriptor.Descriptor(
  name='AFReportListRequest',
  full_name='com.common.msg.AFReportListRequest',
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
  serialized_start=617,
  serialized_end=638,
)


_AFREPORTLISTRESPONSE = _descriptor.Descriptor(
  name='AFReportListResponse',
  full_name='com.common.msg.AFReportListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='eventnames', full_name='com.common.msg.AFReportListResponse.eventnames', index=0,
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
  serialized_start=640,
  serialized_end=682,
)


_AFREPORTCONFIRMREQUEST = _descriptor.Descriptor(
  name='AFReportConfirmRequest',
  full_name='com.common.msg.AFReportConfirmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='eventnames', full_name='com.common.msg.AFReportConfirmRequest.eventnames', index=0,
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
  serialized_start=684,
  serialized_end=728,
)


_AFREPORTCONFIRMRESPONSE = _descriptor.Descriptor(
  name='AFReportConfirmResponse',
  full_name='com.common.msg.AFReportConfirmResponse',
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
  serialized_start=730,
  serialized_end=755,
)


_AFREPORTHISTORYLISTREQUEST = _descriptor.Descriptor(
  name='AFReportHistoryListRequest',
  full_name='com.common.msg.AFReportHistoryListRequest',
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
  serialized_start=757,
  serialized_end=785,
)


_AFREPORTHISTORYLISTRESPONSE = _descriptor.Descriptor(
  name='AFReportHistoryListResponse',
  full_name='com.common.msg.AFReportHistoryListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='eventnames', full_name='com.common.msg.AFReportHistoryListResponse.eventnames', index=0,
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
  serialized_start=787,
  serialized_end=836,
)

_SUBSCRIBEINFOREQUEST.fields_by_name['subscribes'].message_type = _SUBSCRIBE
_SUBSCRIBEINFORESPONSE.fields_by_name['subscribes'].message_type = _SUBSCRIBE
DESCRIPTOR.message_types_by_name['RechargeRequest'] = _RECHARGEREQUEST
DESCRIPTOR.message_types_by_name['RechargeResponse'] = _RECHARGERESPONSE
DESCRIPTOR.message_types_by_name['Subscribe'] = _SUBSCRIBE
DESCRIPTOR.message_types_by_name['SubscribeInfoRequest'] = _SUBSCRIBEINFOREQUEST
DESCRIPTOR.message_types_by_name['SubscribeInfoResponse'] = _SUBSCRIBEINFORESPONSE
DESCRIPTOR.message_types_by_name['SubscribeExpiredRequest'] = _SUBSCRIBEEXPIREDREQUEST
DESCRIPTOR.message_types_by_name['SubscribeExpiredResponse'] = _SUBSCRIBEEXPIREDRESPONSE
DESCRIPTOR.message_types_by_name['LimitedTimeProduct'] = _LIMITEDTIMEPRODUCT
DESCRIPTOR.message_types_by_name['ProcessLimitedTimeProductRequest'] = _PROCESSLIMITEDTIMEPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['ProcessLimitedTimeProductResponse'] = _PROCESSLIMITEDTIMEPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['AFReportListRequest'] = _AFREPORTLISTREQUEST
DESCRIPTOR.message_types_by_name['AFReportListResponse'] = _AFREPORTLISTRESPONSE
DESCRIPTOR.message_types_by_name['AFReportConfirmRequest'] = _AFREPORTCONFIRMREQUEST
DESCRIPTOR.message_types_by_name['AFReportConfirmResponse'] = _AFREPORTCONFIRMRESPONSE
DESCRIPTOR.message_types_by_name['AFReportHistoryListRequest'] = _AFREPORTHISTORYLISTREQUEST
DESCRIPTOR.message_types_by_name['AFReportHistoryListResponse'] = _AFREPORTHISTORYLISTRESPONSE
DESCRIPTOR.enum_types_by_name['RechargeModuleMsgSubCommand'] = _RECHARGEMODULEMSGSUBCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RechargeRequest = _reflection.GeneratedProtocolMessageType('RechargeRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECHARGEREQUEST,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.RechargeRequest)
  })
_sym_db.RegisterMessage(RechargeRequest)

RechargeResponse = _reflection.GeneratedProtocolMessageType('RechargeResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECHARGERESPONSE,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.RechargeResponse)
  })
_sym_db.RegisterMessage(RechargeResponse)

Subscribe = _reflection.GeneratedProtocolMessageType('Subscribe', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.Subscribe)
  })
_sym_db.RegisterMessage(Subscribe)

SubscribeInfoRequest = _reflection.GeneratedProtocolMessageType('SubscribeInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEINFOREQUEST,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.SubscribeInfoRequest)
  })
_sym_db.RegisterMessage(SubscribeInfoRequest)

SubscribeInfoResponse = _reflection.GeneratedProtocolMessageType('SubscribeInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEINFORESPONSE,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.SubscribeInfoResponse)
  })
_sym_db.RegisterMessage(SubscribeInfoResponse)

SubscribeExpiredRequest = _reflection.GeneratedProtocolMessageType('SubscribeExpiredRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEEXPIREDREQUEST,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.SubscribeExpiredRequest)
  })
_sym_db.RegisterMessage(SubscribeExpiredRequest)

SubscribeExpiredResponse = _reflection.GeneratedProtocolMessageType('SubscribeExpiredResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEEXPIREDRESPONSE,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.SubscribeExpiredResponse)
  })
_sym_db.RegisterMessage(SubscribeExpiredResponse)

LimitedTimeProduct = _reflection.GeneratedProtocolMessageType('LimitedTimeProduct', (_message.Message,), {
  'DESCRIPTOR' : _LIMITEDTIMEPRODUCT,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.LimitedTimeProduct)
  })
_sym_db.RegisterMessage(LimitedTimeProduct)

ProcessLimitedTimeProductRequest = _reflection.GeneratedProtocolMessageType('ProcessLimitedTimeProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSLIMITEDTIMEPRODUCTREQUEST,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ProcessLimitedTimeProductRequest)
  })
_sym_db.RegisterMessage(ProcessLimitedTimeProductRequest)

ProcessLimitedTimeProductResponse = _reflection.GeneratedProtocolMessageType('ProcessLimitedTimeProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSLIMITEDTIMEPRODUCTRESPONSE,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ProcessLimitedTimeProductResponse)
  })
_sym_db.RegisterMessage(ProcessLimitedTimeProductResponse)

AFReportListRequest = _reflection.GeneratedProtocolMessageType('AFReportListRequest', (_message.Message,), {
  'DESCRIPTOR' : _AFREPORTLISTREQUEST,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AFReportListRequest)
  })
_sym_db.RegisterMessage(AFReportListRequest)

AFReportListResponse = _reflection.GeneratedProtocolMessageType('AFReportListResponse', (_message.Message,), {
  'DESCRIPTOR' : _AFREPORTLISTRESPONSE,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AFReportListResponse)
  })
_sym_db.RegisterMessage(AFReportListResponse)

AFReportConfirmRequest = _reflection.GeneratedProtocolMessageType('AFReportConfirmRequest', (_message.Message,), {
  'DESCRIPTOR' : _AFREPORTCONFIRMREQUEST,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AFReportConfirmRequest)
  })
_sym_db.RegisterMessage(AFReportConfirmRequest)

AFReportConfirmResponse = _reflection.GeneratedProtocolMessageType('AFReportConfirmResponse', (_message.Message,), {
  'DESCRIPTOR' : _AFREPORTCONFIRMRESPONSE,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AFReportConfirmResponse)
  })
_sym_db.RegisterMessage(AFReportConfirmResponse)

AFReportHistoryListRequest = _reflection.GeneratedProtocolMessageType('AFReportHistoryListRequest', (_message.Message,), {
  'DESCRIPTOR' : _AFREPORTHISTORYLISTREQUEST,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AFReportHistoryListRequest)
  })
_sym_db.RegisterMessage(AFReportHistoryListRequest)

AFReportHistoryListResponse = _reflection.GeneratedProtocolMessageType('AFReportHistoryListResponse', (_message.Message,), {
  'DESCRIPTOR' : _AFREPORTHISTORYLISTRESPONSE,
  '__module__' : 'RechargeModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AFReportHistoryListResponse)
  })
_sym_db.RegisterMessage(AFReportHistoryListResponse)


# @@protoc_insertion_point(module_scope)