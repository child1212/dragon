# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LuckyCardModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18LuckyCardModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"\x16\n\x14LuckyCardInfoRequest\"P\n\x12LuckyCardResultMsg\x12\x10\n\x08position\x18\x01 \x01(\x05\x12(\n\x07rewards\x18\x02 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"x\n\x10LuckyCardInfoMsg\x12\x11\n\tstartTime\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12\r\n\x05times\x18\x03 \x01(\x05\x12\x33\n\x07results\x18\x04 \x03(\x0b\x32\".com.common.msg.LuckyCardResultMsg\"S\n\x15LuckyCardInfoResponse\x12:\n\x10luckyCardInfoMsg\x18\x01 \x01(\x0b\x32 .com.common.msg.LuckyCardInfoMsg\"\x17\n\x15LuckyCardStartRequest\"\x18\n\x16LuckyCardStartResponse\"(\n\x14LuckyCardFlipRequest\x12\x10\n\x08position\x18\x01 \x01(\x05\"V\n\x15LuckyCardFlipResponse\x12(\n\x07rewards\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12\x13\n\x0b\x66inalReward\x18\x02 \x01(\x08*\xa3\x01\n\x1cLuckyCardModuleMsgSubCommand\x12*\n$LUCKYCARDMODULEMSG_SUB_LUCKYCARDINFO\x10\xe5\xe1\x01\x12+\n%LUCKYCARDMODULEMSG_SUB_LUCKYCARDSTART\x10\xe6\xe1\x01\x12*\n$LUCKYCARDMODULEMSG_SUB_LUCKYCARDFLIP\x10\xe7\xe1\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'LuckyCardModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_LUCKYCARDMODULEMSGSUBCOMMAND']._serialized_start=560
  _globals['_LUCKYCARDMODULEMSGSUBCOMMAND']._serialized_end=723
  _globals['_LUCKYCARDINFOREQUEST']._serialized_start=65
  _globals['_LUCKYCARDINFOREQUEST']._serialized_end=87
  _globals['_LUCKYCARDRESULTMSG']._serialized_start=89
  _globals['_LUCKYCARDRESULTMSG']._serialized_end=169
  _globals['_LUCKYCARDINFOMSG']._serialized_start=171
  _globals['_LUCKYCARDINFOMSG']._serialized_end=291
  _globals['_LUCKYCARDINFORESPONSE']._serialized_start=293
  _globals['_LUCKYCARDINFORESPONSE']._serialized_end=376
  _globals['_LUCKYCARDSTARTREQUEST']._serialized_start=378
  _globals['_LUCKYCARDSTARTREQUEST']._serialized_end=401
  _globals['_LUCKYCARDSTARTRESPONSE']._serialized_start=403
  _globals['_LUCKYCARDSTARTRESPONSE']._serialized_end=427
  _globals['_LUCKYCARDFLIPREQUEST']._serialized_start=429
  _globals['_LUCKYCARDFLIPREQUEST']._serialized_end=469
  _globals['_LUCKYCARDFLIPRESPONSE']._serialized_start=471
  _globals['_LUCKYCARDFLIPRESPONSE']._serialized_end=557
# @@protoc_insertion_point(module_scope)
