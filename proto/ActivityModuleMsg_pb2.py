# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActivityModuleMsg.proto
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
  name='ActivityModuleMsg.proto',
  package='com.common.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x41\x63tivityModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"\xe3\x01\n\x07RankMsg\x12\x10\n\x08playerId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x03 \x01(\t\x12\r\n\x05\x66rame\x18\x04 \x01(\t\x12\r\n\x05level\x18\x05 \x01(\x05\x12\r\n\x05score\x18\x06 \x01(\x05\x12\r\n\x05index\x18\x07 \x01(\x05\x12\x11\n\tlastIndex\x18\x08 \x01(\x05\x12\x13\n\x0brewardstate\x18\t \x01(\x05\x12\x0e\n\x06teamId\x18\n \x01(\t\x12\x10\n\x08teamname\x18\x0b \x01(\t\x12\x10\n\x08teamicon\x18\x0c \x01(\t\x12\x10\n\x08vipLevel\x18\r \x01(\x05\"o\n\x0bRankListMsg\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12)\n\x08ranklist\x18\x02 \x03(\x0b\x32\x17.com.common.msg.RankMsg\x12\'\n\x06myrank\x18\x03 \x01(\x0b\x32\x17.com.common.msg.RankMsg\"\x86\x01\n\x0b\x41\x63tivityMsg\x12\x12\n\nactivityId\x18\x01 \x01(\t\x12\x11\n\tstartTime\x18\x02 \x01(\x03\x12\x0f\n\x07\x65ndTime\x18\x03 \x01(\x03\x12\x13\n\x0bprewarmTime\x18\x04 \x01(\x03\x12\x15\n\rlastEnterTime\x18\x05 \x01(\x03\x12\x13\n\x0brankEndTime\x18\x06 \x01(\x03\"Y\n\x0e\x45ndActivityMsg\x12\x12\n\nactivityId\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x13\n\x0brewardState\x18\x03 \x01(\x05\x12\x10\n\x08\x65valuate\x18\x04 \x01(\x05\"Z\n\rRankRewardMsg\x12\x10\n\x08ranktype\x18\x01 \x01(\x05\x12\r\n\x05index\x18\x02 \x01(\x05\x12(\n\x07rewards\x18\x03 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"4\n\x0fHistoryScoreMsg\x12\x12\n\nactivityId\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\"\x15\n\x13\x41\x63tivityListRequest\"\xb3\x01\n\x14\x41\x63tivityListResponse\x12/\n\nactivities\x18\x01 \x03(\x0b\x32\x1b.com.common.msg.ActivityMsg\x12\x33\n\x0ewarmActivities\x18\x02 \x03(\x0b\x32\x1b.com.common.msg.ActivityMsg\x12\x35\n\rendActivities\x18\x03 \x03(\x0b\x32\x1e.com.common.msg.EndActivityMsg\"2\n\x1c\x41\x63tivityCountdownOverRequest\x12\x12\n\nactivityId\x18\x01 \x01(\t\"\x1f\n\x1d\x41\x63tivityCountdownOverResponse\")\n\x13\x41\x63tivityRankRequest\x12\x12\n\nactivityId\x18\x01 \x01(\t\"t\n\x14\x41\x63tivityRankResponse\x12*\n\x05ranks\x18\x01 \x03(\x0b\x32\x1b.com.common.msg.RankListMsg\x12\x30\n\x07history\x18\x02 \x03(\x0b\x32\x1f.com.common.msg.HistoryScoreMsg*\xa1\x01\n\x1b\x41\x63tivityModuleMsgSubCommand\x12\'\n\"ACTIVITYMODULEMSG_SUB_ACTIVITYLIST\x10\xe1]\x12\x30\n+ACTIVITYMODULEMSG_SUB_ACTIVITYCOUNTDOWNOVER\x10\xe2]\x12\'\n\"ACTIVITYMODULEMSG_SUB_ACTIVITYRANK\x10\xe3]'
  ,
  dependencies=[ItemModuleMsg__pb2.DESCRIPTOR,])

_ACTIVITYMODULEMSGSUBCOMMAND = _descriptor.EnumDescriptor(
  name='ActivityModuleMsgSubCommand',
  full_name='com.common.msg.ActivityModuleMsgSubCommand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVITYMODULEMSG_SUB_ACTIVITYLIST', index=0, number=12001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVITYMODULEMSG_SUB_ACTIVITYCOUNTDOWNOVER', index=1, number=12002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVITYMODULEMSG_SUB_ACTIVITYRANK', index=2, number=12003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1233,
  serialized_end=1394,
)
_sym_db.RegisterEnumDescriptor(_ACTIVITYMODULEMSGSUBCOMMAND)

ActivityModuleMsgSubCommand = enum_type_wrapper.EnumTypeWrapper(_ACTIVITYMODULEMSGSUBCOMMAND)
ACTIVITYMODULEMSG_SUB_ACTIVITYLIST = 12001
ACTIVITYMODULEMSG_SUB_ACTIVITYCOUNTDOWNOVER = 12002
ACTIVITYMODULEMSG_SUB_ACTIVITYRANK = 12003



_RANKMSG = _descriptor.Descriptor(
  name='RankMsg',
  full_name='com.common.msg.RankMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerId', full_name='com.common.msg.RankMsg.playerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.common.msg.RankMsg.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='com.common.msg.RankMsg.avatar', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame', full_name='com.common.msg.RankMsg.frame', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='com.common.msg.RankMsg.level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='com.common.msg.RankMsg.score', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='com.common.msg.RankMsg.index', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastIndex', full_name='com.common.msg.RankMsg.lastIndex', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rewardstate', full_name='com.common.msg.RankMsg.rewardstate', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teamId', full_name='com.common.msg.RankMsg.teamId', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teamname', full_name='com.common.msg.RankMsg.teamname', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teamicon', full_name='com.common.msg.RankMsg.teamicon', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vipLevel', full_name='com.common.msg.RankMsg.vipLevel', index=12,
      number=13, type=5, cpp_type=1, label=1,
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
  serialized_start=65,
  serialized_end=292,
)


_RANKLISTMSG = _descriptor.Descriptor(
  name='RankListMsg',
  full_name='com.common.msg.RankListMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='com.common.msg.RankListMsg.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ranklist', full_name='com.common.msg.RankListMsg.ranklist', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='myrank', full_name='com.common.msg.RankListMsg.myrank', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=294,
  serialized_end=405,
)


_ACTIVITYMSG = _descriptor.Descriptor(
  name='ActivityMsg',
  full_name='com.common.msg.ActivityMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='com.common.msg.ActivityMsg.activityId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='com.common.msg.ActivityMsg.startTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='com.common.msg.ActivityMsg.endTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prewarmTime', full_name='com.common.msg.ActivityMsg.prewarmTime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastEnterTime', full_name='com.common.msg.ActivityMsg.lastEnterTime', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rankEndTime', full_name='com.common.msg.ActivityMsg.rankEndTime', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  serialized_start=408,
  serialized_end=542,
)


_ENDACTIVITYMSG = _descriptor.Descriptor(
  name='EndActivityMsg',
  full_name='com.common.msg.EndActivityMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='com.common.msg.EndActivityMsg.activityId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='com.common.msg.EndActivityMsg.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rewardState', full_name='com.common.msg.EndActivityMsg.rewardState', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evaluate', full_name='com.common.msg.EndActivityMsg.evaluate', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=544,
  serialized_end=633,
)


_RANKREWARDMSG = _descriptor.Descriptor(
  name='RankRewardMsg',
  full_name='com.common.msg.RankRewardMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ranktype', full_name='com.common.msg.RankRewardMsg.ranktype', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='com.common.msg.RankRewardMsg.index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='com.common.msg.RankRewardMsg.rewards', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=635,
  serialized_end=725,
)


_HISTORYSCOREMSG = _descriptor.Descriptor(
  name='HistoryScoreMsg',
  full_name='com.common.msg.HistoryScoreMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='com.common.msg.HistoryScoreMsg.activityId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='com.common.msg.HistoryScoreMsg.score', index=1,
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
  serialized_start=727,
  serialized_end=779,
)


_ACTIVITYLISTREQUEST = _descriptor.Descriptor(
  name='ActivityListRequest',
  full_name='com.common.msg.ActivityListRequest',
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
  serialized_start=781,
  serialized_end=802,
)


_ACTIVITYLISTRESPONSE = _descriptor.Descriptor(
  name='ActivityListResponse',
  full_name='com.common.msg.ActivityListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activities', full_name='com.common.msg.ActivityListResponse.activities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='warmActivities', full_name='com.common.msg.ActivityListResponse.warmActivities', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endActivities', full_name='com.common.msg.ActivityListResponse.endActivities', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=805,
  serialized_end=984,
)


_ACTIVITYCOUNTDOWNOVERREQUEST = _descriptor.Descriptor(
  name='ActivityCountdownOverRequest',
  full_name='com.common.msg.ActivityCountdownOverRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='com.common.msg.ActivityCountdownOverRequest.activityId', index=0,
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
  serialized_start=986,
  serialized_end=1036,
)


_ACTIVITYCOUNTDOWNOVERRESPONSE = _descriptor.Descriptor(
  name='ActivityCountdownOverResponse',
  full_name='com.common.msg.ActivityCountdownOverResponse',
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
  serialized_start=1038,
  serialized_end=1069,
)


_ACTIVITYRANKREQUEST = _descriptor.Descriptor(
  name='ActivityRankRequest',
  full_name='com.common.msg.ActivityRankRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='activityId', full_name='com.common.msg.ActivityRankRequest.activityId', index=0,
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
  serialized_start=1071,
  serialized_end=1112,
)


_ACTIVITYRANKRESPONSE = _descriptor.Descriptor(
  name='ActivityRankResponse',
  full_name='com.common.msg.ActivityRankResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ranks', full_name='com.common.msg.ActivityRankResponse.ranks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='history', full_name='com.common.msg.ActivityRankResponse.history', index=1,
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
  serialized_start=1114,
  serialized_end=1230,
)

_RANKLISTMSG.fields_by_name['ranklist'].message_type = _RANKMSG
_RANKLISTMSG.fields_by_name['myrank'].message_type = _RANKMSG
_RANKREWARDMSG.fields_by_name['rewards'].message_type = ItemModuleMsg__pb2._ITEMMSG
_ACTIVITYLISTRESPONSE.fields_by_name['activities'].message_type = _ACTIVITYMSG
_ACTIVITYLISTRESPONSE.fields_by_name['warmActivities'].message_type = _ACTIVITYMSG
_ACTIVITYLISTRESPONSE.fields_by_name['endActivities'].message_type = _ENDACTIVITYMSG
_ACTIVITYRANKRESPONSE.fields_by_name['ranks'].message_type = _RANKLISTMSG
_ACTIVITYRANKRESPONSE.fields_by_name['history'].message_type = _HISTORYSCOREMSG
DESCRIPTOR.message_types_by_name['RankMsg'] = _RANKMSG
DESCRIPTOR.message_types_by_name['RankListMsg'] = _RANKLISTMSG
DESCRIPTOR.message_types_by_name['ActivityMsg'] = _ACTIVITYMSG
DESCRIPTOR.message_types_by_name['EndActivityMsg'] = _ENDACTIVITYMSG
DESCRIPTOR.message_types_by_name['RankRewardMsg'] = _RANKREWARDMSG
DESCRIPTOR.message_types_by_name['HistoryScoreMsg'] = _HISTORYSCOREMSG
DESCRIPTOR.message_types_by_name['ActivityListRequest'] = _ACTIVITYLISTREQUEST
DESCRIPTOR.message_types_by_name['ActivityListResponse'] = _ACTIVITYLISTRESPONSE
DESCRIPTOR.message_types_by_name['ActivityCountdownOverRequest'] = _ACTIVITYCOUNTDOWNOVERREQUEST
DESCRIPTOR.message_types_by_name['ActivityCountdownOverResponse'] = _ACTIVITYCOUNTDOWNOVERRESPONSE
DESCRIPTOR.message_types_by_name['ActivityRankRequest'] = _ACTIVITYRANKREQUEST
DESCRIPTOR.message_types_by_name['ActivityRankResponse'] = _ACTIVITYRANKRESPONSE
DESCRIPTOR.enum_types_by_name['ActivityModuleMsgSubCommand'] = _ACTIVITYMODULEMSGSUBCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RankMsg = _reflection.GeneratedProtocolMessageType('RankMsg', (_message.Message,), {
  'DESCRIPTOR' : _RANKMSG,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.RankMsg)
  })
_sym_db.RegisterMessage(RankMsg)

RankListMsg = _reflection.GeneratedProtocolMessageType('RankListMsg', (_message.Message,), {
  'DESCRIPTOR' : _RANKLISTMSG,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.RankListMsg)
  })
_sym_db.RegisterMessage(RankListMsg)

ActivityMsg = _reflection.GeneratedProtocolMessageType('ActivityMsg', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYMSG,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ActivityMsg)
  })
_sym_db.RegisterMessage(ActivityMsg)

EndActivityMsg = _reflection.GeneratedProtocolMessageType('EndActivityMsg', (_message.Message,), {
  'DESCRIPTOR' : _ENDACTIVITYMSG,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.EndActivityMsg)
  })
_sym_db.RegisterMessage(EndActivityMsg)

RankRewardMsg = _reflection.GeneratedProtocolMessageType('RankRewardMsg', (_message.Message,), {
  'DESCRIPTOR' : _RANKREWARDMSG,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.RankRewardMsg)
  })
_sym_db.RegisterMessage(RankRewardMsg)

HistoryScoreMsg = _reflection.GeneratedProtocolMessageType('HistoryScoreMsg', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYSCOREMSG,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.HistoryScoreMsg)
  })
_sym_db.RegisterMessage(HistoryScoreMsg)

ActivityListRequest = _reflection.GeneratedProtocolMessageType('ActivityListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYLISTREQUEST,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ActivityListRequest)
  })
_sym_db.RegisterMessage(ActivityListRequest)

ActivityListResponse = _reflection.GeneratedProtocolMessageType('ActivityListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYLISTRESPONSE,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ActivityListResponse)
  })
_sym_db.RegisterMessage(ActivityListResponse)

ActivityCountdownOverRequest = _reflection.GeneratedProtocolMessageType('ActivityCountdownOverRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYCOUNTDOWNOVERREQUEST,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ActivityCountdownOverRequest)
  })
_sym_db.RegisterMessage(ActivityCountdownOverRequest)

ActivityCountdownOverResponse = _reflection.GeneratedProtocolMessageType('ActivityCountdownOverResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYCOUNTDOWNOVERRESPONSE,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ActivityCountdownOverResponse)
  })
_sym_db.RegisterMessage(ActivityCountdownOverResponse)

ActivityRankRequest = _reflection.GeneratedProtocolMessageType('ActivityRankRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYRANKREQUEST,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ActivityRankRequest)
  })
_sym_db.RegisterMessage(ActivityRankRequest)

ActivityRankResponse = _reflection.GeneratedProtocolMessageType('ActivityRankResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYRANKRESPONSE,
  '__module__' : 'ActivityModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ActivityRankResponse)
  })
_sym_db.RegisterMessage(ActivityRankResponse)


# @@protoc_insertion_point(module_scope)