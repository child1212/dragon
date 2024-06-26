# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActivityMonopolyModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2
import ActivityModuleMsg_pb2 as ActivityModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x41\x63tivityMonopolyModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\x1a\x17\x41\x63tivityModuleMsg.proto\")\n\x13MonopolyInfoRequest\x12\x12\n\nactivityId\x18\x01 \x01(\t\"\xce\x01\n\x14MonopolyInfoResponse\x12\x0f\n\x07levelId\x18\x01 \x01(\x05\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12\x15\n\rfloorRewardId\x18\x03 \x01(\x05\x12\x15\n\rtodayFloorCnt\x18\x04 \x01(\x05\x12\x13\n\x0btaskLevelId\x18\x05 \x01(\x05\x12\x11\n\ttaskIndex\x18\x06 \x01(\x05\x12\x11\n\ttaskState\x18\x07 \x01(\x05\x12\x14\n\x0crecoverHpCnt\x18\x08 \x01(\x05\"\x19\n\x17MonopolyRollDiceRequest\"\x1a\n\x18MonopolyRollDiceResponse\"c\n\x1aMonopolyLevelFinishRequest\x12\x0f\n\x07levelId\x18\x01 \x01(\x05\x12\x0c\n\x04succ\x18\x02 \x01(\x08\x12&\n\x05items\x18\x03 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"\x1d\n\x1bMonopolyLevelFinishResponse\"X\n\x1dMonopolyLevelPropsItemRequest\x12\x0f\n\x07levelId\x18\x01 \x01(\x05\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\" \n\x1eMonopolyLevelPropsItemResponse\"\x1c\n\x1aMonopolyFloorRewardRequest\"\\\n\x1bMonopolyFloorRewardResponse\x12\x15\n\rfloorRewardId\x18\x01 \x01(\x05\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"\x1a\n\x18MonopolyQuickPassRequest\"C\n\x19MonopolyQuickPassResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"\x1a\n\x18MonopolyRecoverHpRequest\"\x1b\n\x19MonopolyRecoverHpResponse*\xa9\x03\n#ActivityMonopolyModuleMsgSubCommand\x12\x30\n*ACTIVITYMONOPOLYMODULEMSG_SUB_MONOPOLYINFO\x10\xcd\xe9\x01\x12\x34\n.ACTIVITYMONOPOLYMODULEMSG_SUB_MONOPOLYROLLDICE\x10\xce\xe9\x01\x12\x37\n1ACTIVITYMONOPOLYMODULEMSG_SUB_MONOPOLYLEVELFINISH\x10\xcf\xe9\x01\x12:\n4ACTIVITYMONOPOLYMODULEMSG_SUB_MONOPOLYLEVELPROPSITEM\x10\xd0\xe9\x01\x12\x37\n1ACTIVITYMONOPOLYMODULEMSG_SUB_MONOPOLYFLOORREWARD\x10\xd1\xe9\x01\x12\x35\n/ACTIVITYMONOPOLYMODULEMSG_SUB_MONOPOLYQUICKPASS\x10\xd2\xe9\x01\x12\x35\n/ACTIVITYMONOPOLYMODULEMSG_SUB_MONOPOLYRECOVERHP\x10\xd3\xe9\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ActivityMonopolyModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ACTIVITYMONOPOLYMODULEMSGSUBCOMMAND']._serialized_start=939
  _globals['_ACTIVITYMONOPOLYMODULEMSGSUBCOMMAND']._serialized_end=1364
  _globals['_MONOPOLYINFOREQUEST']._serialized_start=97
  _globals['_MONOPOLYINFOREQUEST']._serialized_end=138
  _globals['_MONOPOLYINFORESPONSE']._serialized_start=141
  _globals['_MONOPOLYINFORESPONSE']._serialized_end=347
  _globals['_MONOPOLYROLLDICEREQUEST']._serialized_start=349
  _globals['_MONOPOLYROLLDICEREQUEST']._serialized_end=374
  _globals['_MONOPOLYROLLDICERESPONSE']._serialized_start=376
  _globals['_MONOPOLYROLLDICERESPONSE']._serialized_end=402
  _globals['_MONOPOLYLEVELFINISHREQUEST']._serialized_start=404
  _globals['_MONOPOLYLEVELFINISHREQUEST']._serialized_end=503
  _globals['_MONOPOLYLEVELFINISHRESPONSE']._serialized_start=505
  _globals['_MONOPOLYLEVELFINISHRESPONSE']._serialized_end=534
  _globals['_MONOPOLYLEVELPROPSITEMREQUEST']._serialized_start=536
  _globals['_MONOPOLYLEVELPROPSITEMREQUEST']._serialized_end=624
  _globals['_MONOPOLYLEVELPROPSITEMRESPONSE']._serialized_start=626
  _globals['_MONOPOLYLEVELPROPSITEMRESPONSE']._serialized_end=658
  _globals['_MONOPOLYFLOORREWARDREQUEST']._serialized_start=660
  _globals['_MONOPOLYFLOORREWARDREQUEST']._serialized_end=688
  _globals['_MONOPOLYFLOORREWARDRESPONSE']._serialized_start=690
  _globals['_MONOPOLYFLOORREWARDRESPONSE']._serialized_end=782
  _globals['_MONOPOLYQUICKPASSREQUEST']._serialized_start=784
  _globals['_MONOPOLYQUICKPASSREQUEST']._serialized_end=810
  _globals['_MONOPOLYQUICKPASSRESPONSE']._serialized_start=812
  _globals['_MONOPOLYQUICKPASSRESPONSE']._serialized_end=879
  _globals['_MONOPOLYRECOVERHPREQUEST']._serialized_start=881
  _globals['_MONOPOLYRECOVERHPREQUEST']._serialized_end=907
  _globals['_MONOPOLYRECOVERHPRESPONSE']._serialized_start=909
  _globals['_MONOPOLYRECOVERHPRESPONSE']._serialized_end=936
# @@protoc_insertion_point(module_scope)
