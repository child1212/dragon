# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DragonBubbleModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x44ragonBubbleModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"<\n\tBubbleMsg\x12\x10\n\x08\x62ubbleId\x18\x01 \x01(\x03\x12\x0e\n\x06itemId\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\"\xc6\x01\n\x0f\x44ragonBubbleMsg\x12\x11\n\tstartTime\x18\x01 \x01(\x03\x12\x12\n\ntodayTimes\x18\x02 \x01(\x05\x12\x18\n\x10singleTotalTimes\x18\x03 \x01(\x05\x12\x13\n\x0bsingleTimes\x18\x04 \x01(\x05\x12*\n\x07\x62ubbles\x18\x05 \x03(\x0b\x32\x19.com.common.msg.BubbleMsg\x12\x0f\n\x07\x64ragons\x18\x06 \x03(\x03\x12\x11\n\tresetTime\x18\x07 \x01(\x03\x12\r\n\x05level\x18\x08 \x01(\x05\"\x0f\n\rCreateRequest\"G\n\x0e\x43reateResponse\x12\x35\n\x0c\x64ragonBubble\x18\x01 \x01(\x0b\x32\x1f.com.common.msg.DragonBubbleMsg\"\x13\n\x11SupplementRequest\"K\n\x12SupplementResponse\x12\x35\n\x0c\x64ragonBubble\x18\x01 \x01(\x0b\x32\x1f.com.common.msg.DragonBubbleMsg\"!\n\rRewardRequest\x12\x10\n\x08\x62ubbleId\x18\x01 \x01(\x03\"G\n\x0eRewardResponse\x12\x35\n\x0c\x64ragonBubble\x18\x01 \x01(\x0b\x32\x1f.com.common.msg.DragonBubbleMsg*\x9d\x01\n\x1f\x44ragonBubbleModuleMsgSubCommand\x12&\n DRAGONBUBBLEMODULEMSG_SUB_CREATE\x10\xe9\xcf\x01\x12*\n$DRAGONBUBBLEMODULEMSG_SUB_SUPPLEMENT\x10\xea\xcf\x01\x12&\n DRAGONBUBBLEMODULEMSG_SUB_REWARD\x10\xeb\xcf\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DragonBubbleModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DRAGONBUBBLEMODULEMSGSUBCOMMAND']._serialized_start=628
  _globals['_DRAGONBUBBLEMODULEMSGSUBCOMMAND']._serialized_end=785
  _globals['_BUBBLEMSG']._serialized_start=68
  _globals['_BUBBLEMSG']._serialized_end=128
  _globals['_DRAGONBUBBLEMSG']._serialized_start=131
  _globals['_DRAGONBUBBLEMSG']._serialized_end=329
  _globals['_CREATEREQUEST']._serialized_start=331
  _globals['_CREATEREQUEST']._serialized_end=346
  _globals['_CREATERESPONSE']._serialized_start=348
  _globals['_CREATERESPONSE']._serialized_end=419
  _globals['_SUPPLEMENTREQUEST']._serialized_start=421
  _globals['_SUPPLEMENTREQUEST']._serialized_end=440
  _globals['_SUPPLEMENTRESPONSE']._serialized_start=442
  _globals['_SUPPLEMENTRESPONSE']._serialized_end=517
  _globals['_REWARDREQUEST']._serialized_start=519
  _globals['_REWARDREQUEST']._serialized_end=552
  _globals['_REWARDRESPONSE']._serialized_start=554
  _globals['_REWARDRESPONSE']._serialized_end=625
# @@protoc_insertion_point(module_scope)
