# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MiningModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15MiningModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"}\n\x13MiningCommissionMsg\x12\x14\n\x0c\x63ommissionId\x18\x01 \x01(\x03\x12\r\n\x05tplId\x18\x02 \x01(\t\x12\x11\n\tstartTime\x18\x03 \x01(\x03\x12\x11\n\tcreatures\x18\x04 \x03(\x03\x12\x1b\n\x13\x63reatureTemplateIds\x18\x05 \x03(\t\"B\n\rMiningBossMsg\x12\x0e\n\x06\x62ossId\x18\x01 \x02(\t\x12\x0e\n\x06\x65nergy\x18\x02 \x02(\x05\x12\x11\n\tstartTime\x18\x03 \x01(\x03\"2\n\x0eMiningEventMsg\x12\x11\n\teventType\x18\x01 \x02(\x05\x12\r\n\x05tplId\x18\x02 \x02(\t\"\xc2\x01\n\rMiningGridMsg\x12\x0b\n\x03pos\x18\x01 \x02(\x05\x12\x0e\n\x06\x64igCnt\x18\x02 \x02(\x05\x12\x0f\n\x07\x63leared\x18\x03 \x02(\x08\x12\'\n\x06reward\x18\x04 \x01(\x0b\x32\x17.com.common.msg.ItemMsg\x12-\n\x05\x65vent\x18\x05 \x01(\x0b\x32\x1e.com.common.msg.MiningEventMsg\x12+\n\x04\x62oss\x18\x06 \x01(\x0b\x32\x1d.com.common.msg.MiningBossMsg\"O\n\x0eMiningFloorMsg\x12\x0f\n\x07\x66loorId\x18\x01 \x02(\t\x12,\n\x05grids\x18\x02 \x03(\x0b\x32\x1d.com.common.msg.MiningGridMsg\"\x13\n\x11MiningInfoRequest\"\xad\x02\n\x12MiningInfoResponse\x12\r\n\x05group\x18\x01 \x03(\x05\x12.\n\x06\x66loors\x18\x02 \x03(\x0b\x32\x1e.com.common.msg.MiningFloorMsg\x12\x38\n\x0b\x63ommissions\x18\x03 \x03(\x0b\x32#.com.common.msg.MiningCommissionMsg\x12\x10\n\x08groupCnt\x18\x04 \x01(\x05\x12\x17\n\x0fnextRefreshTime\x18\x05 \x01(\x03\x12\x1a\n\x12lastRewardDigFloor\x18\x06 \x01(\x05\x12\x18\n\x10\x64igFloorRewardId\x18\x07 \x01(\x05\x12\x11\n\tdayReward\x18\x08 \x01(\x08\x12\x12\n\nrewardType\x18\t \x01(\x05\x12\x16\n\x0e\x63hangeTypeTime\x18\n \x01(\x03\"$\n\x13MiningCreateRequest\x12\r\n\x05group\x18\x01 \x02(\x05\"F\n\x14MiningCreateResponse\x12.\n\x06\x66loors\x18\x01 \x03(\x0b\x32\x1e.com.common.msg.MiningFloorMsg\"*\n\nDigGridMsg\x12\x0f\n\x07\x66loorId\x18\x01 \x01(\t\x12\x0b\n\x03pos\x18\x02 \x01(\x05\"S\n\x10MiningDigRequest\x12\x11\n\tdigItemId\x18\x01 \x01(\t\x12,\n\x08\x64igGrids\x18\x02 \x03(\x0b\x32\x1a.com.common.msg.DigGridMsg\"M\n\x11MiningDigResponse\x12\x38\n\x0b\x63ommissions\x18\x01 \x03(\x0b\x32#.com.common.msg.MiningCommissionMsg\"?\n\x10MiningBoxRequest\x12+\n\x07\x64igGrid\x18\x01 \x02(\x0b\x32\x1a.com.common.msg.DigGridMsg\"=\n\x11MiningBoxResponse\x12(\n\x07rewards\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"m\n\x13MiningBossPKRequest\x12\x0f\n\x07\x66loorId\x18\x01 \x02(\t\x12\x0b\n\x03pos\x18\x02 \x02(\x05\x12\x11\n\tcreatures\x18\x03 \x03(\x03\x12\x10\n\x08maxFloor\x18\x04 \x01(\x05\x12\x13\n\x0b\x64iamondPass\x18\x05 \x01(\x08\"Z\n\x14MiningBossPKResponse\x12\x0b\n\x03win\x18\x01 \x02(\x08\x12\x35\n\tcreatures\x18\x02 \x03(\x0b\x32\".com.common.msg.MagicalCreatureMsg\"B\n\x17MiningCommissionRequest\x12\x14\n\x0c\x63ommissionId\x18\x01 \x01(\x03\x12\x11\n\tcreatures\x18\x02 \x03(\x03\"\x1a\n\x18MiningCommissionResponse\"5\n\x1dMiningCommissionRewardRequest\x12\x14\n\x0c\x63ommissionId\x18\x01 \x01(\x03\" \n\x1eMiningCommissionRewardResponse\"3\n\x1fMiningWeekDigFloorRewardRequest\x12\x10\n\x08maxFloor\x18\x01 \x01(\x05\"\"\n MiningWeekDigFloorRewardResponse\"*\n\x16MiningWeekResetRequest\x12\x10\n\x08maxFloor\x18\x01 \x01(\x05\"2\n\x17MiningWeekResetResponse\x12\x17\n\x0fnextRefreshTime\x18\x01 \x01(\x03\"6\n\x16MiningBossStartRequest\x12\x0f\n\x07\x66loorId\x18\x01 \x02(\t\x12\x0b\n\x03pos\x18\x02 \x02(\x05\"\x19\n\x17MiningBossStartResponse\"8\n\x18MiningBossRefreshRequest\x12\x0f\n\x07\x66loorId\x18\x01 \x02(\t\x12\x0b\n\x03pos\x18\x02 \x02(\x05\"H\n\x19MiningBossRefreshResponse\x12+\n\x04\x62oss\x18\x01 \x02(\x0b\x32\x1d.com.common.msg.MiningBossMsg\"3\n\x1dMiningChangeRewardTypeRequest\x12\x12\n\nrewardType\x18\x01 \x01(\x05\"P\n\x1eMiningChangeRewardTypeResponse\x12.\n\x06\x66loors\x18\x02 \x03(\x0b\x32\x1e.com.common.msg.MiningFloorMsg\"7\n\x16MiningDayRewardRequest\x12\x10\n\x08maxFloor\x18\x01 \x01(\x05\x12\x0b\n\x03\x61\x64s\x18\x02 \x01(\x08\"\x19\n\x17MiningDayRewardResponse*\xcd\x04\n\x19MiningModuleMsgSubCommand\x12$\n\x1eMININGMODULEMSG_SUB_MININGINFO\x10\xc9\xe2\x01\x12&\n MININGMODULEMSG_SUB_MININGCREATE\x10\xca\xe2\x01\x12#\n\x1dMININGMODULEMSG_SUB_MININGDIG\x10\xcb\xe2\x01\x12#\n\x1dMININGMODULEMSG_SUB_MININGBOX\x10\xcc\xe2\x01\x12&\n MININGMODULEMSG_SUB_MININGBOSSPK\x10\xcd\xe2\x01\x12*\n$MININGMODULEMSG_SUB_MININGCOMMISSION\x10\xce\xe2\x01\x12\x30\n*MININGMODULEMSG_SUB_MININGCOMMISSIONREWARD\x10\xcf\xe2\x01\x12\x32\n,MININGMODULEMSG_SUB_MININGWEEKDIGFLOORREWARD\x10\xd0\xe2\x01\x12)\n#MININGMODULEMSG_SUB_MININGWEEKRESET\x10\xd1\xe2\x01\x12)\n#MININGMODULEMSG_SUB_MININGBOSSSTART\x10\xd2\xe2\x01\x12+\n%MININGMODULEMSG_SUB_MININGBOSSREFRESH\x10\xd3\xe2\x01\x12\x30\n*MININGMODULEMSG_SUB_MININGCHANGEREWARDTYPE\x10\xd4\xe2\x01\x12)\n#MININGMODULEMSG_SUB_MININGDAYREWARD\x10\xd5\xe2\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MiningModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_MININGMODULEMSGSUBCOMMAND']._serialized_start=2366
  _globals['_MININGMODULEMSGSUBCOMMAND']._serialized_end=2955
  _globals['_MININGCOMMISSIONMSG']._serialized_start=62
  _globals['_MININGCOMMISSIONMSG']._serialized_end=187
  _globals['_MININGBOSSMSG']._serialized_start=189
  _globals['_MININGBOSSMSG']._serialized_end=255
  _globals['_MININGEVENTMSG']._serialized_start=257
  _globals['_MININGEVENTMSG']._serialized_end=307
  _globals['_MININGGRIDMSG']._serialized_start=310
  _globals['_MININGGRIDMSG']._serialized_end=504
  _globals['_MININGFLOORMSG']._serialized_start=506
  _globals['_MININGFLOORMSG']._serialized_end=585
  _globals['_MININGINFOREQUEST']._serialized_start=587
  _globals['_MININGINFOREQUEST']._serialized_end=606
  _globals['_MININGINFORESPONSE']._serialized_start=609
  _globals['_MININGINFORESPONSE']._serialized_end=910
  _globals['_MININGCREATEREQUEST']._serialized_start=912
  _globals['_MININGCREATEREQUEST']._serialized_end=948
  _globals['_MININGCREATERESPONSE']._serialized_start=950
  _globals['_MININGCREATERESPONSE']._serialized_end=1020
  _globals['_DIGGRIDMSG']._serialized_start=1022
  _globals['_DIGGRIDMSG']._serialized_end=1064
  _globals['_MININGDIGREQUEST']._serialized_start=1066
  _globals['_MININGDIGREQUEST']._serialized_end=1149
  _globals['_MININGDIGRESPONSE']._serialized_start=1151
  _globals['_MININGDIGRESPONSE']._serialized_end=1228
  _globals['_MININGBOXREQUEST']._serialized_start=1230
  _globals['_MININGBOXREQUEST']._serialized_end=1293
  _globals['_MININGBOXRESPONSE']._serialized_start=1295
  _globals['_MININGBOXRESPONSE']._serialized_end=1356
  _globals['_MININGBOSSPKREQUEST']._serialized_start=1358
  _globals['_MININGBOSSPKREQUEST']._serialized_end=1467
  _globals['_MININGBOSSPKRESPONSE']._serialized_start=1469
  _globals['_MININGBOSSPKRESPONSE']._serialized_end=1559
  _globals['_MININGCOMMISSIONREQUEST']._serialized_start=1561
  _globals['_MININGCOMMISSIONREQUEST']._serialized_end=1627
  _globals['_MININGCOMMISSIONRESPONSE']._serialized_start=1629
  _globals['_MININGCOMMISSIONRESPONSE']._serialized_end=1655
  _globals['_MININGCOMMISSIONREWARDREQUEST']._serialized_start=1657
  _globals['_MININGCOMMISSIONREWARDREQUEST']._serialized_end=1710
  _globals['_MININGCOMMISSIONREWARDRESPONSE']._serialized_start=1712
  _globals['_MININGCOMMISSIONREWARDRESPONSE']._serialized_end=1744
  _globals['_MININGWEEKDIGFLOORREWARDREQUEST']._serialized_start=1746
  _globals['_MININGWEEKDIGFLOORREWARDREQUEST']._serialized_end=1797
  _globals['_MININGWEEKDIGFLOORREWARDRESPONSE']._serialized_start=1799
  _globals['_MININGWEEKDIGFLOORREWARDRESPONSE']._serialized_end=1833
  _globals['_MININGWEEKRESETREQUEST']._serialized_start=1835
  _globals['_MININGWEEKRESETREQUEST']._serialized_end=1877
  _globals['_MININGWEEKRESETRESPONSE']._serialized_start=1879
  _globals['_MININGWEEKRESETRESPONSE']._serialized_end=1929
  _globals['_MININGBOSSSTARTREQUEST']._serialized_start=1931
  _globals['_MININGBOSSSTARTREQUEST']._serialized_end=1985
  _globals['_MININGBOSSSTARTRESPONSE']._serialized_start=1987
  _globals['_MININGBOSSSTARTRESPONSE']._serialized_end=2012
  _globals['_MININGBOSSREFRESHREQUEST']._serialized_start=2014
  _globals['_MININGBOSSREFRESHREQUEST']._serialized_end=2070
  _globals['_MININGBOSSREFRESHRESPONSE']._serialized_start=2072
  _globals['_MININGBOSSREFRESHRESPONSE']._serialized_end=2144
  _globals['_MININGCHANGEREWARDTYPEREQUEST']._serialized_start=2146
  _globals['_MININGCHANGEREWARDTYPEREQUEST']._serialized_end=2197
  _globals['_MININGCHANGEREWARDTYPERESPONSE']._serialized_start=2199
  _globals['_MININGCHANGEREWARDTYPERESPONSE']._serialized_end=2279
  _globals['_MININGDAYREWARDREQUEST']._serialized_start=2281
  _globals['_MININGDAYREWARDREQUEST']._serialized_end=2336
  _globals['_MININGDAYREWARDRESPONSE']._serialized_start=2338
  _globals['_MININGDAYREWARDRESPONSE']._serialized_end=2363
# @@protoc_insertion_point(module_scope)
