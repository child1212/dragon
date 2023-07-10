# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GlobalProgressModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dGlobalProgressModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"\x1b\n\x19GlobalProgressInfoRequest\"X\n\x0eSpecialProduct\x12(\n\x07product\x18\x01 \x01(\x0b\x32\x17.com.common.msg.ItemMsg\x12\x0e\n\x06shopId\x18\x02 \x01(\t\x12\x0c\n\x04rate\x18\x03 \x01(\x05\"\xcc\x01\n\x08TaskInfo\x12%\n\x04need\x18\x01 \x01(\x0b\x32\x17.com.common.msg.ItemMsg\x12&\n\x05\x61ward\x18\x02 \x01(\x0b\x32\x17.com.common.msg.ItemMsg\x12\x11\n\tfinishNum\x18\x03 \x01(\x05\x12\x0f\n\x07\x61warded\x18\x04 \x01(\x08\x12/\n\x07product\x18\x05 \x01(\x0b\x32\x1e.com.common.msg.SpecialProduct\x12\x0e\n\x06number\x18\x06 \x01(\x05\x12\x0c\n\x04turn\x18\x07 \x01(\x05\"\x8b\x01\n\x1aGlobalProgressInfoResponse\x12+\n\ttaskInfos\x18\x01 \x03(\x0b\x32\x18.com.common.msg.TaskInfo\x12*\n\x08taskInfo\x18\x02 \x01(\x0b\x32\x18.com.common.msg.TaskInfo\x12\x14\n\x0c\x65ndTimeStamp\x18\x03 \x01(\x03\".\n\x0eTaskComposeKey\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x0c\n\x04turn\x18\x02 \x01(\x05\"@\n\x10TakeAwardRequest\x12,\n\x04keys\x18\x01 \x03(\x0b\x32\x1e.com.common.msg.TaskComposeKey\"\x88\x02\n\x11TakeAwardResponse\x12/\n\x07\x61warded\x18\x01 \x03(\x0b\x32\x1e.com.common.msg.TaskComposeKey\x12\x33\n\x0bnotFinished\x18\x02 \x03(\x0b\x32\x1e.com.common.msg.TaskComposeKey\x12\x19\n\x11notFinishedNowNum\x18\x03 \x03(\x05\x12\x30\n\x08notFound\x18\x04 \x03(\x0b\x32\x1e.com.common.msg.TaskComposeKey\x12*\n\x08taskInfo\x18\x05 \x01(\x0b\x32\x18.com.common.msg.TaskInfo\x12\x14\n\x0c\x65ndTimeStamp\x18\x06 \x01(\x03\"F\n\x16\x44\x65lSpecialAwardRequest\x12,\n\x04keys\x18\x01 \x03(\x0b\x32\x1e.com.common.msg.TaskComposeKey\"\x19\n\x17\x44\x65lSpecialAwardResponse\"\x18\n\x16RefreshTaskInfoRequest\"[\n\x17RefreshTaskInfoResponse\x12*\n\x08taskInfo\x18\x01 \x01(\x0b\x32\x18.com.common.msg.TaskInfo\x12\x14\n\x0c\x65ndTimeStamp\x18\x02 \x01(\x03\"\x1e\n\x1cGlobalProgressInfoV33Request\"\x92\x01\n\x1dGlobalProgressInfoV33Response\x12*\n\x08taskInfo\x18\x01 \x01(\x0b\x32\x18.com.common.msg.TaskInfo\x12\x14\n\x0c\x65ndTimeStamp\x18\x02 \x01(\x03\x12\x15\n\rdayTriggerNum\x18\x03 \x01(\x05\x12\x18\n\x10\x64\x61yStatisticsNum\x18\x04 \x01(\x05\"\x17\n\x15TriggerTaskV33Request\"Z\n\x16TriggerTaskV33Response\x12*\n\x08taskInfo\x18\x01 \x01(\x0b\x32\x18.com.common.msg.TaskInfo\x12\x14\n\x0c\x65ndTimeStamp\x18\x02 \x01(\x03*\xd7\x02\n!GlobalProgressModuleMsgSubCommand\x12\x34\n.GLOBALPROGRESSMODULEMSG_SUB_GLOBALPROGRESSINFO\x10\xd5\xe8\x01\x12+\n%GLOBALPROGRESSMODULEMSG_SUB_TAKEAWARD\x10\xd6\xe8\x01\x12\x31\n+GLOBALPROGRESSMODULEMSG_SUB_DELSPECIALAWARD\x10\xd7\xe8\x01\x12\x31\n+GLOBALPROGRESSMODULEMSG_SUB_REFRESHTASKINFO\x10\xd8\xe8\x01\x12\x37\n1GLOBALPROGRESSMODULEMSG_SUB_GLOBALPROGRESSINFOV33\x10\xd9\xe8\x01\x12\x30\n*GLOBALPROGRESSMODULEMSG_SUB_TRIGGERTASKV33\x10\xda\xe8\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GlobalProgressModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_GLOBALPROGRESSMODULEMSGSUBCOMMAND']._serialized_start=1436
  _globals['_GLOBALPROGRESSMODULEMSGSUBCOMMAND']._serialized_end=1779
  _globals['_GLOBALPROGRESSINFOREQUEST']._serialized_start=70
  _globals['_GLOBALPROGRESSINFOREQUEST']._serialized_end=97
  _globals['_SPECIALPRODUCT']._serialized_start=99
  _globals['_SPECIALPRODUCT']._serialized_end=187
  _globals['_TASKINFO']._serialized_start=190
  _globals['_TASKINFO']._serialized_end=394
  _globals['_GLOBALPROGRESSINFORESPONSE']._serialized_start=397
  _globals['_GLOBALPROGRESSINFORESPONSE']._serialized_end=536
  _globals['_TASKCOMPOSEKEY']._serialized_start=538
  _globals['_TASKCOMPOSEKEY']._serialized_end=584
  _globals['_TAKEAWARDREQUEST']._serialized_start=586
  _globals['_TAKEAWARDREQUEST']._serialized_end=650
  _globals['_TAKEAWARDRESPONSE']._serialized_start=653
  _globals['_TAKEAWARDRESPONSE']._serialized_end=917
  _globals['_DELSPECIALAWARDREQUEST']._serialized_start=919
  _globals['_DELSPECIALAWARDREQUEST']._serialized_end=989
  _globals['_DELSPECIALAWARDRESPONSE']._serialized_start=991
  _globals['_DELSPECIALAWARDRESPONSE']._serialized_end=1016
  _globals['_REFRESHTASKINFOREQUEST']._serialized_start=1018
  _globals['_REFRESHTASKINFOREQUEST']._serialized_end=1042
  _globals['_REFRESHTASKINFORESPONSE']._serialized_start=1044
  _globals['_REFRESHTASKINFORESPONSE']._serialized_end=1135
  _globals['_GLOBALPROGRESSINFOV33REQUEST']._serialized_start=1137
  _globals['_GLOBALPROGRESSINFOV33REQUEST']._serialized_end=1167
  _globals['_GLOBALPROGRESSINFOV33RESPONSE']._serialized_start=1170
  _globals['_GLOBALPROGRESSINFOV33RESPONSE']._serialized_end=1316
  _globals['_TRIGGERTASKV33REQUEST']._serialized_start=1318
  _globals['_TRIGGERTASKV33REQUEST']._serialized_end=1341
  _globals['_TRIGGERTASKV33RESPONSE']._serialized_start=1343
  _globals['_TRIGGERTASKV33RESPONSE']._serialized_end=1433
# @@protoc_insertion_point(module_scope)