# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActiveEggModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x41\x63tiveEggModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"\x16\n\x14\x41\x63tiveEggInfoRequest\"a\n\x0c\x41\x63tiveEggMsg\x12\r\n\x05\x65ggId\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0b\n\x03\x63ur\x18\x04 \x01(\x05\x12\x0b\n\x03max\x18\x05 \x01(\x05\x12\n\n\x02\x63\x64\x18\x06 \x01(\x03\"]\n\x15\x41\x63tiveEggInfoResponse\x12*\n\x04\x65ggs\x18\x01 \x03(\x0b\x32\x1c.com.common.msg.ActiveEggMsg\x12\x18\n\x10\x63umulativeEnergy\x18\x02 \x01(\x05\";\n\x19\x41\x63tiveEggDiamondCDRequest\x12\r\n\x05\x65ggId\x18\x01 \x01(\x05\x12\x0f\n\x07\x64iamond\x18\x02 \x01(\x05\"g\n\x1a\x41\x63tiveEggDiamondCDResponse\x12\x0f\n\x07retCode\x18\x01 \x01(\x05\x12*\n\x04\x65ggs\x18\x02 \x03(\x0b\x32\x1c.com.common.msg.ActiveEggMsg\x12\x0c\n\x04\x63ost\x18\x03 \x01(\x05\"&\n\x14\x41\x63tiveEggOpenRequest\x12\x0e\n\x06\x65ggIds\x18\x01 \x03(\x05\"m\n\x15\x41\x63tiveEggOpenResponse\x12(\n\x07rewards\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12*\n\x04\x65ggs\x18\x02 \x03(\x0b\x32\x1c.com.common.msg.ActiveEggMsg\"\x1c\n\x1a\x41\x63tiveEggSystemInfoRequest\"h\n\x1b\x41\x63tiveEggSystemInfoResponse\x12\x30\n\nsystemEggs\x18\x01 \x03(\x0b\x32\x1c.com.common.msg.ActiveEggMsg\x12\x17\n\x0freceivedSystems\x18\x02 \x03(\t\"1\n\x1d\x41\x63tiveEggSystemReceiveRequest\x12\x10\n\x08systemId\x18\x01 \x01(\t\"R\n\x1e\x41\x63tiveEggSystemReceiveResponse\x12\x30\n\nsystemEggs\x18\x01 \x03(\x0b\x32\x1c.com.common.msg.ActiveEggMsg\",\n\x1a\x41\x63tiveEggSystemOpenRequest\x12\x0e\n\x06\x65ggIds\x18\x01 \x03(\x05\"D\n\tEggReward\x12\r\n\x05\x65ggId\x18\x01 \x01(\x05\x12(\n\x07rewards\x18\x02 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"L\n\x1b\x41\x63tiveEggSystemOpenResponse\x12-\n\neggRewards\x18\x01 \x03(\x0b\x32\x19.com.common.msg.EggReward*\xc0\x02\n\x1c\x41\x63tiveEggModuleMsgSubCommand\x12*\n$ACTIVEEGGMODULEMSG_SUB_ACTIVEEGGINFO\x10\xd9\xcc\x01\x12/\n)ACTIVEEGGMODULEMSG_SUB_ACTIVEEGGDIAMONDCD\x10\xda\xcc\x01\x12*\n$ACTIVEEGGMODULEMSG_SUB_ACTIVEEGGOPEN\x10\xdb\xcc\x01\x12\x30\n*ACTIVEEGGMODULEMSG_SUB_ACTIVEEGGSYSTEMINFO\x10\xdc\xcc\x01\x12\x33\n-ACTIVEEGGMODULEMSG_SUB_ACTIVEEGGSYSTEMRECEIVE\x10\xdd\xcc\x01\x12\x30\n*ACTIVEEGGMODULEMSG_SUB_ACTIVEEGGSYSTEMOPEN\x10\xde\xcc\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ActiveEggModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ACTIVEEGGMODULEMSGSUBCOMMAND']._serialized_start=1066
  _globals['_ACTIVEEGGMODULEMSGSUBCOMMAND']._serialized_end=1386
  _globals['_ACTIVEEGGINFOREQUEST']._serialized_start=65
  _globals['_ACTIVEEGGINFOREQUEST']._serialized_end=87
  _globals['_ACTIVEEGGMSG']._serialized_start=89
  _globals['_ACTIVEEGGMSG']._serialized_end=186
  _globals['_ACTIVEEGGINFORESPONSE']._serialized_start=188
  _globals['_ACTIVEEGGINFORESPONSE']._serialized_end=281
  _globals['_ACTIVEEGGDIAMONDCDREQUEST']._serialized_start=283
  _globals['_ACTIVEEGGDIAMONDCDREQUEST']._serialized_end=342
  _globals['_ACTIVEEGGDIAMONDCDRESPONSE']._serialized_start=344
  _globals['_ACTIVEEGGDIAMONDCDRESPONSE']._serialized_end=447
  _globals['_ACTIVEEGGOPENREQUEST']._serialized_start=449
  _globals['_ACTIVEEGGOPENREQUEST']._serialized_end=487
  _globals['_ACTIVEEGGOPENRESPONSE']._serialized_start=489
  _globals['_ACTIVEEGGOPENRESPONSE']._serialized_end=598
  _globals['_ACTIVEEGGSYSTEMINFOREQUEST']._serialized_start=600
  _globals['_ACTIVEEGGSYSTEMINFOREQUEST']._serialized_end=628
  _globals['_ACTIVEEGGSYSTEMINFORESPONSE']._serialized_start=630
  _globals['_ACTIVEEGGSYSTEMINFORESPONSE']._serialized_end=734
  _globals['_ACTIVEEGGSYSTEMRECEIVEREQUEST']._serialized_start=736
  _globals['_ACTIVEEGGSYSTEMRECEIVEREQUEST']._serialized_end=785
  _globals['_ACTIVEEGGSYSTEMRECEIVERESPONSE']._serialized_start=787
  _globals['_ACTIVEEGGSYSTEMRECEIVERESPONSE']._serialized_end=869
  _globals['_ACTIVEEGGSYSTEMOPENREQUEST']._serialized_start=871
  _globals['_ACTIVEEGGSYSTEMOPENREQUEST']._serialized_end=915
  _globals['_EGGREWARD']._serialized_start=917
  _globals['_EGGREWARD']._serialized_end=985
  _globals['_ACTIVEEGGSYSTEMOPENRESPONSE']._serialized_start=987
  _globals['_ACTIVEEGGSYSTEMOPENRESPONSE']._serialized_end=1063
# @@protoc_insertion_point(module_scope)
