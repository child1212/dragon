# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GashaponModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ActivityModuleMsg_pb2 as ActivityModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17GashaponModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x17\x41\x63tivityModuleMsg.proto\")\n\x13GashaponInfoRequest\x12\x12\n\nactivityId\x18\x01 \x02(\t\"9\n\x17GashaponRechargeRecords\x12\x0e\n\x06shopId\x18\x01 \x02(\t\x12\x0e\n\x06\x62uyCnt\x18\x02 \x02(\x05\"\x8b\x02\n\x14GashaponInfoResponse\x12\x31\n\x0cgashaponInfo\x18\x01 \x01(\x0b\x32\x1b.com.common.msg.ActivityMsg\x12\"\n\x1alastReceiveLoginTicketTime\x18\x02 \x01(\x03\x12\x1b\n\x13todayLevelTicketCnt\x18\x03 \x01(\x05\x12@\n\x0frechargeRecords\x18\x04 \x03(\x0b\x32\'.com.common.msg.GashaponRechargeRecords\x12\x11\n\ttoysTimes\x18\x05 \x01(\x05\x12\x19\n\x11rechargeToysTimes\x18\x06 \x01(\x05\x12\x0f\n\x07tickets\x18\x07 \x01(\x05\"?\n\x1aGashaponCapsuleToysRequest\x12\x12\n\nactivityId\x18\x01 \x02(\t\x12\r\n\x05index\x18\x02 \x02(\t\"K\n\x1bGashaponCapsuleToysResponse\x12\x11\n\ttoysTimes\x18\x01 \x02(\x05\x12\x19\n\x11rechargeToysTimes\x18\x02 \x02(\x05\"/\n\x19ReceiveLoginTicketRequest\x12\x12\n\nactivityId\x18\x01 \x02(\t\"\x1c\n\x1aReceiveLoginTicketResponse*\xa5\x01\n\x1bGashaponModuleMsgSubCommand\x12\'\n\"GASHAPONMODULEMSG_SUB_GASHAPONINFO\x10\x81_\x12.\n)GASHAPONMODULEMSG_SUB_GASHAPONCAPSULETOYS\x10\x82_\x12-\n(GASHAPONMODULEMSG_SUB_RECEIVELOGINTICKET\x10\x83_')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GashaponModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_GASHAPONMODULEMSGSUBCOMMAND']._serialized_start=662
  _globals['_GASHAPONMODULEMSGSUBCOMMAND']._serialized_end=827
  _globals['_GASHAPONINFOREQUEST']._serialized_start=68
  _globals['_GASHAPONINFOREQUEST']._serialized_end=109
  _globals['_GASHAPONRECHARGERECORDS']._serialized_start=111
  _globals['_GASHAPONRECHARGERECORDS']._serialized_end=168
  _globals['_GASHAPONINFORESPONSE']._serialized_start=171
  _globals['_GASHAPONINFORESPONSE']._serialized_end=438
  _globals['_GASHAPONCAPSULETOYSREQUEST']._serialized_start=440
  _globals['_GASHAPONCAPSULETOYSREQUEST']._serialized_end=503
  _globals['_GASHAPONCAPSULETOYSRESPONSE']._serialized_start=505
  _globals['_GASHAPONCAPSULETOYSRESPONSE']._serialized_end=580
  _globals['_RECEIVELOGINTICKETREQUEST']._serialized_start=582
  _globals['_RECEIVELOGINTICKETREQUEST']._serialized_end=629
  _globals['_RECEIVELOGINTICKETRESPONSE']._serialized_start=631
  _globals['_RECEIVELOGINTICKETRESPONSE']._serialized_end=659
# @@protoc_insertion_point(module_scope)
