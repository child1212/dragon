# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ReflowModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15ReflowModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"\x13\n\x11ReflowInfoRequest\"D\n\x0cLoginInfoMsg\x12\x1b\n\x13lastLoginRewardTime\x18\x01 \x01(\x03\x12\x17\n\x0floginAwardTimes\x18\x02 \x01(\x05\"7\n\x0eTimeOrderTimes\x12\x16\n\x0estartTimestamp\x18\x01 \x01(\x03\x12\r\n\x05times\x18\x02 \x01(\x05\"M\n\x13TimeOrderWelfareMsg\x12\x36\n\x0etimeOrderInfos\x18\x01 \x03(\x0b\x32\x1e.com.common.msg.TimeOrderTimes\"5\n\x10SkinProduceOrder\x12\x0f\n\x07quality\x18\x01 \x01(\x05\x12\x10\n\x08\x65ndTimes\x18\x02 \x01(\x03\"R\n\x13SkinProduceOrderMsg\x12;\n\x11skinProduceOrders\x18\x01 \x03(\x0b\x32 .com.common.msg.SkinProduceOrder\"R\n\x0eWelfareInfoMsg\x12\r\n\x05wType\x18\x01 \x01(\x05\x12\x0f\n\x07msgBody\x18\x02 \x01(\x0c\x12\x11\n\tcdEndTime\x18\x03 \x01(\x03\x12\r\n\x05times\x18\x04 \x01(\x03\"7\n\nGrowthTask\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x0e\n\x06\x61wards\x18\x03 \x03(\x05\"\xca\x02\n\rReflowInfoMsg\x12\x0f\n\x07\x65ndTime\x18\x01 \x01(\x03\x12\r\n\x05rType\x18\x02 \x01(\x05\x12/\n\tloginInfo\x18\x03 \x01(\x0b\x32\x1c.com.common.msg.LoginInfoMsg\x12\x33\n\x0bwelfareInfo\x18\x04 \x01(\x0b\x32\x1e.com.common.msg.WelfareInfoMsg\x12;\n\x13historyWelfareInfos\x18\x05 \x01(\x0b\x32\x1e.com.common.msg.WelfareInfoMsg\x12/\n\x0bgrowthTasks\x18\x06 \x03(\x0b\x32\x1a.com.common.msg.GrowthTask\x12\x0b\n\x03tip\x18\x07 \x01(\x05\x12\x14\n\x0cneedEndAward\x18\x08 \x01(\x05\x12\x12\n\nplayerType\x18\t \x01(\x05\x12\x0e\n\x06giftId\x18\n \x01(\t\"J\n\x12ReflowInfoResponse\x12\x34\n\rreflowInfoMsg\x18\x01 \x01(\x0b\x32\x1d.com.common.msg.ReflowInfoMsg\"\x1c\n\x1aTakeReflowEndRewardRequest\"{\n\x1bTakeReflowEndRewardResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12\x34\n\rreflowInfoMsg\x18\x02 \x01(\x0b\x32\x1d.com.common.msg.ReflowInfoMsg\"\x18\n\x16TakeLoginRewardRequest\"\'\n\x17TakeLoginRewardResponse\x12\x0c\n\x04time\x18\x01 \x01(\x03\"3\n\x15TakeTaskRewardRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06tIndex\x18\x02 \x01(\x05\"\x18\n\x16TakeTaskRewardResponse\"\x17\n\x15RefreshWelfareRequest\"P\n\x16RefreshWelfareResponse\x12\x36\n\x0ewelfareInfoMsg\x18\x01 \x01(\x0b\x32\x1e.com.common.msg.WelfareInfoMsg\"\'\n\x15TakeGiftRewardRequest\x12\x0e\n\x06giftId\x18\x01 \x01(\t\"\x18\n\x16TakeGiftRewardResponse*\x99\x02\n\x19ReflowModuleMsgSubCommand\x12$\n\x1eREFLOWMODULEMSG_SUB_REFLOWINFO\x10\x9d\xe0\x01\x12-\n\'REFLOWMODULEMSG_SUB_TAKEREFLOWENDREWARD\x10\x9e\xe0\x01\x12)\n#REFLOWMODULEMSG_SUB_TAKELOGINREWARD\x10\x9f\xe0\x01\x12(\n\"REFLOWMODULEMSG_SUB_TAKETASKREWARD\x10\xa0\xe0\x01\x12(\n\"REFLOWMODULEMSG_SUB_REFRESHWELFARE\x10\xa1\xe0\x01\x12(\n\"REFLOWMODULEMSG_SUB_TAKEGIFTREWARD\x10\xa2\xe0\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ReflowModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_REFLOWMODULEMSGSUBCOMMAND']._serialized_start=1454
  _globals['_REFLOWMODULEMSGSUBCOMMAND']._serialized_end=1735
  _globals['_REFLOWINFOREQUEST']._serialized_start=62
  _globals['_REFLOWINFOREQUEST']._serialized_end=81
  _globals['_LOGININFOMSG']._serialized_start=83
  _globals['_LOGININFOMSG']._serialized_end=151
  _globals['_TIMEORDERTIMES']._serialized_start=153
  _globals['_TIMEORDERTIMES']._serialized_end=208
  _globals['_TIMEORDERWELFAREMSG']._serialized_start=210
  _globals['_TIMEORDERWELFAREMSG']._serialized_end=287
  _globals['_SKINPRODUCEORDER']._serialized_start=289
  _globals['_SKINPRODUCEORDER']._serialized_end=342
  _globals['_SKINPRODUCEORDERMSG']._serialized_start=344
  _globals['_SKINPRODUCEORDERMSG']._serialized_end=426
  _globals['_WELFAREINFOMSG']._serialized_start=428
  _globals['_WELFAREINFOMSG']._serialized_end=510
  _globals['_GROWTHTASK']._serialized_start=512
  _globals['_GROWTHTASK']._serialized_end=567
  _globals['_REFLOWINFOMSG']._serialized_start=570
  _globals['_REFLOWINFOMSG']._serialized_end=900
  _globals['_REFLOWINFORESPONSE']._serialized_start=902
  _globals['_REFLOWINFORESPONSE']._serialized_end=976
  _globals['_TAKEREFLOWENDREWARDREQUEST']._serialized_start=978
  _globals['_TAKEREFLOWENDREWARDREQUEST']._serialized_end=1006
  _globals['_TAKEREFLOWENDREWARDRESPONSE']._serialized_start=1008
  _globals['_TAKEREFLOWENDREWARDRESPONSE']._serialized_end=1131
  _globals['_TAKELOGINREWARDREQUEST']._serialized_start=1133
  _globals['_TAKELOGINREWARDREQUEST']._serialized_end=1157
  _globals['_TAKELOGINREWARDRESPONSE']._serialized_start=1159
  _globals['_TAKELOGINREWARDRESPONSE']._serialized_end=1198
  _globals['_TAKETASKREWARDREQUEST']._serialized_start=1200
  _globals['_TAKETASKREWARDREQUEST']._serialized_end=1251
  _globals['_TAKETASKREWARDRESPONSE']._serialized_start=1253
  _globals['_TAKETASKREWARDRESPONSE']._serialized_end=1277
  _globals['_REFRESHWELFAREREQUEST']._serialized_start=1279
  _globals['_REFRESHWELFAREREQUEST']._serialized_end=1302
  _globals['_REFRESHWELFARERESPONSE']._serialized_start=1304
  _globals['_REFRESHWELFARERESPONSE']._serialized_end=1384
  _globals['_TAKEGIFTREWARDREQUEST']._serialized_start=1386
  _globals['_TAKEGIFTREWARDREQUEST']._serialized_end=1425
  _globals['_TAKEGIFTREWARDRESPONSE']._serialized_start=1427
  _globals['_TAKEGIFTREWARDRESPONSE']._serialized_end=1451
# @@protoc_insertion_point(module_scope)
