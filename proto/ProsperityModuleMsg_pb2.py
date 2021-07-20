# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProsperityModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ProsperityModuleMsg.proto',
  package='com.common.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19ProsperityModuleMsg.proto\x12\x0e\x63om.common.msg\"S\n\x16ProsperityInfoResponse\x12\x10\n\x08maxLevel\x18\x02 \x02(\x05\x12\x14\n\x0clevelUpGifts\x18\x03 \x03(\x05\x12\x11\n\tshopGifts\x18\x04 \x03(\x05\"#\n\x12LevelUpGiftRequest\x12\r\n\x05level\x18\x01 \x02(\x05\"\x15\n\x13LevelUpGiftResponse\"\x11\n\x0fRankListRequest\"\x88\x01\n\x0bRankInfoMsg\x12\x10\n\x08playerId\x18\x01 \x02(\t\x12\r\n\x05index\x18\x02 \x01(\x05\x12\r\n\x05score\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x06 \x01(\t\x12\r\n\x05level\x18\x07 \x01(\x05\x12\r\n\x05isVip\x18\x08 \x01(\x08\"X\n\x10RankListResponse\x12\x31\n\x0crankInfoMsgs\x18\x01 \x03(\x0b\x32\x1b.com.common.msg.RankInfoMsg\x12\x11\n\trankIndex\x18\x02 \x01(\x05\",\n\x1b\x42uyPreferentialGoodsRequest\x12\r\n\x05level\x18\x01 \x02(\x05\"\x1e\n\x1c\x42uyPreferentialGoodsResponse*\xd8\x01\n\x17ProsperityErrorCodeEnum\x12+\n%PROSPERITY_LEVELUP_GIFT_ALREADY_TOKEN\x10\xf1\xab\x01\x12!\n\x1bPROSPERITY_LEVEL_NOT_ENOUGH\x10\xf2\xab\x01\x12)\n#PROSPERITY_SHOP_GITF_ALREADY_BOUGHT\x10\xf3\xab\x01\x12\x1f\n\x19PROSPERITY_DATA_NOT_EXIST\x10\xf4\xab\x01\x12!\n\x1bPROSPERITY_MONEY_NOT_ENOUGH\x10\xf5\xab\x01*\xa6\x01\n\x1dProsperityModuleMsgSubCommand\x12)\n#PROSPERITYMODULEMSG_SUB_LEVELUPGIFT\x10\xf1\xab\x01\x12&\n PROSPERITYMODULEMSG_SUB_RANKLIST\x10\xf2\xab\x01\x12\x32\n,PROSPERITYMODULEMSG_SUB_BUYPREFERENTIALGOODS\x10\xf3\xab\x01'
)

_PROSPERITYERRORCODEENUM = _descriptor.EnumDescriptor(
  name='ProsperityErrorCodeEnum',
  full_name='com.common.msg.ProsperityErrorCodeEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROSPERITY_LEVELUP_GIFT_ALREADY_TOKEN', index=0, number=22001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROSPERITY_LEVEL_NOT_ENOUGH', index=1, number=22002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROSPERITY_SHOP_GITF_ALREADY_BOUGHT', index=2, number=22003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROSPERITY_DATA_NOT_EXIST', index=3, number=22004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROSPERITY_MONEY_NOT_ENOUGH', index=4, number=22005,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=517,
  serialized_end=733,
)
_sym_db.RegisterEnumDescriptor(_PROSPERITYERRORCODEENUM)

ProsperityErrorCodeEnum = enum_type_wrapper.EnumTypeWrapper(_PROSPERITYERRORCODEENUM)
_PROSPERITYMODULEMSGSUBCOMMAND = _descriptor.EnumDescriptor(
  name='ProsperityModuleMsgSubCommand',
  full_name='com.common.msg.ProsperityModuleMsgSubCommand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROSPERITYMODULEMSG_SUB_LEVELUPGIFT', index=0, number=22001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROSPERITYMODULEMSG_SUB_RANKLIST', index=1, number=22002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROSPERITYMODULEMSG_SUB_BUYPREFERENTIALGOODS', index=2, number=22003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=736,
  serialized_end=902,
)
_sym_db.RegisterEnumDescriptor(_PROSPERITYMODULEMSGSUBCOMMAND)

ProsperityModuleMsgSubCommand = enum_type_wrapper.EnumTypeWrapper(_PROSPERITYMODULEMSGSUBCOMMAND)
PROSPERITY_LEVELUP_GIFT_ALREADY_TOKEN = 22001
PROSPERITY_LEVEL_NOT_ENOUGH = 22002
PROSPERITY_SHOP_GITF_ALREADY_BOUGHT = 22003
PROSPERITY_DATA_NOT_EXIST = 22004
PROSPERITY_MONEY_NOT_ENOUGH = 22005
PROSPERITYMODULEMSG_SUB_LEVELUPGIFT = 22001
PROSPERITYMODULEMSG_SUB_RANKLIST = 22002
PROSPERITYMODULEMSG_SUB_BUYPREFERENTIALGOODS = 22003



_PROSPERITYINFORESPONSE = _descriptor.Descriptor(
  name='ProsperityInfoResponse',
  full_name='com.common.msg.ProsperityInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maxLevel', full_name='com.common.msg.ProsperityInfoResponse.maxLevel', index=0,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='levelUpGifts', full_name='com.common.msg.ProsperityInfoResponse.levelUpGifts', index=1,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shopGifts', full_name='com.common.msg.ProsperityInfoResponse.shopGifts', index=2,
      number=4, type=5, cpp_type=1, label=3,
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
  serialized_start=45,
  serialized_end=128,
)


_LEVELUPGIFTREQUEST = _descriptor.Descriptor(
  name='LevelUpGiftRequest',
  full_name='com.common.msg.LevelUpGiftRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='com.common.msg.LevelUpGiftRequest.level', index=0,
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
  serialized_start=130,
  serialized_end=165,
)


_LEVELUPGIFTRESPONSE = _descriptor.Descriptor(
  name='LevelUpGiftResponse',
  full_name='com.common.msg.LevelUpGiftResponse',
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
  serialized_start=167,
  serialized_end=188,
)


_RANKLISTREQUEST = _descriptor.Descriptor(
  name='RankListRequest',
  full_name='com.common.msg.RankListRequest',
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
  serialized_start=190,
  serialized_end=207,
)


_RANKINFOMSG = _descriptor.Descriptor(
  name='RankInfoMsg',
  full_name='com.common.msg.RankInfoMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerId', full_name='com.common.msg.RankInfoMsg.playerId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='com.common.msg.RankInfoMsg.index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='com.common.msg.RankInfoMsg.score', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.common.msg.RankInfoMsg.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icon', full_name='com.common.msg.RankInfoMsg.icon', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account', full_name='com.common.msg.RankInfoMsg.account', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='com.common.msg.RankInfoMsg.level', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isVip', full_name='com.common.msg.RankInfoMsg.isVip', index=7,
      number=8, type=8, cpp_type=7, label=1,
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
  serialized_start=210,
  serialized_end=346,
)


_RANKLISTRESPONSE = _descriptor.Descriptor(
  name='RankListResponse',
  full_name='com.common.msg.RankListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rankInfoMsgs', full_name='com.common.msg.RankListResponse.rankInfoMsgs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rankIndex', full_name='com.common.msg.RankListResponse.rankIndex', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=348,
  serialized_end=436,
)


_BUYPREFERENTIALGOODSREQUEST = _descriptor.Descriptor(
  name='BuyPreferentialGoodsRequest',
  full_name='com.common.msg.BuyPreferentialGoodsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='com.common.msg.BuyPreferentialGoodsRequest.level', index=0,
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
  serialized_start=438,
  serialized_end=482,
)


_BUYPREFERENTIALGOODSRESPONSE = _descriptor.Descriptor(
  name='BuyPreferentialGoodsResponse',
  full_name='com.common.msg.BuyPreferentialGoodsResponse',
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
  serialized_start=484,
  serialized_end=514,
)

_RANKLISTRESPONSE.fields_by_name['rankInfoMsgs'].message_type = _RANKINFOMSG
DESCRIPTOR.message_types_by_name['ProsperityInfoResponse'] = _PROSPERITYINFORESPONSE
DESCRIPTOR.message_types_by_name['LevelUpGiftRequest'] = _LEVELUPGIFTREQUEST
DESCRIPTOR.message_types_by_name['LevelUpGiftResponse'] = _LEVELUPGIFTRESPONSE
DESCRIPTOR.message_types_by_name['RankListRequest'] = _RANKLISTREQUEST
DESCRIPTOR.message_types_by_name['RankInfoMsg'] = _RANKINFOMSG
DESCRIPTOR.message_types_by_name['RankListResponse'] = _RANKLISTRESPONSE
DESCRIPTOR.message_types_by_name['BuyPreferentialGoodsRequest'] = _BUYPREFERENTIALGOODSREQUEST
DESCRIPTOR.message_types_by_name['BuyPreferentialGoodsResponse'] = _BUYPREFERENTIALGOODSRESPONSE
DESCRIPTOR.enum_types_by_name['ProsperityErrorCodeEnum'] = _PROSPERITYERRORCODEENUM
DESCRIPTOR.enum_types_by_name['ProsperityModuleMsgSubCommand'] = _PROSPERITYMODULEMSGSUBCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProsperityInfoResponse = _reflection.GeneratedProtocolMessageType('ProsperityInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROSPERITYINFORESPONSE,
  '__module__' : 'ProsperityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ProsperityInfoResponse)
  })
_sym_db.RegisterMessage(ProsperityInfoResponse)

LevelUpGiftRequest = _reflection.GeneratedProtocolMessageType('LevelUpGiftRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEVELUPGIFTREQUEST,
  '__module__' : 'ProsperityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.LevelUpGiftRequest)
  })
_sym_db.RegisterMessage(LevelUpGiftRequest)

LevelUpGiftResponse = _reflection.GeneratedProtocolMessageType('LevelUpGiftResponse', (_message.Message,), {
  'DESCRIPTOR' : _LEVELUPGIFTRESPONSE,
  '__module__' : 'ProsperityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.LevelUpGiftResponse)
  })
_sym_db.RegisterMessage(LevelUpGiftResponse)

RankListRequest = _reflection.GeneratedProtocolMessageType('RankListRequest', (_message.Message,), {
  'DESCRIPTOR' : _RANKLISTREQUEST,
  '__module__' : 'ProsperityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.RankListRequest)
  })
_sym_db.RegisterMessage(RankListRequest)

RankInfoMsg = _reflection.GeneratedProtocolMessageType('RankInfoMsg', (_message.Message,), {
  'DESCRIPTOR' : _RANKINFOMSG,
  '__module__' : 'ProsperityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.RankInfoMsg)
  })
_sym_db.RegisterMessage(RankInfoMsg)

RankListResponse = _reflection.GeneratedProtocolMessageType('RankListResponse', (_message.Message,), {
  'DESCRIPTOR' : _RANKLISTRESPONSE,
  '__module__' : 'ProsperityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.RankListResponse)
  })
_sym_db.RegisterMessage(RankListResponse)

BuyPreferentialGoodsRequest = _reflection.GeneratedProtocolMessageType('BuyPreferentialGoodsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUYPREFERENTIALGOODSREQUEST,
  '__module__' : 'ProsperityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.BuyPreferentialGoodsRequest)
  })
_sym_db.RegisterMessage(BuyPreferentialGoodsRequest)

BuyPreferentialGoodsResponse = _reflection.GeneratedProtocolMessageType('BuyPreferentialGoodsResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUYPREFERENTIALGOODSRESPONSE,
  '__module__' : 'ProsperityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.BuyPreferentialGoodsResponse)
  })
_sym_db.RegisterMessage(BuyPreferentialGoodsResponse)


# @@protoc_insertion_point(module_scope)
