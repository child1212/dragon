# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SkinProduceModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aSkinProduceModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"=\n\x0eSkinProduceMsg\x12\r\n\x05tplId\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\r\n\x05state\x18\x03 \x01(\x05\"{\n\x13SkinProduceOrderMsg\x12\x0f\n\x07quality\x18\x01 \x01(\x05\x12\x11\n\tstartTime\x18\x02 \x01(\x03\x12\x11\n\tskinTplId\x18\x03 \x01(\t\x12-\n\x0c\x65xtraRewards\x18\x04 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"\x14\n\x12ProduceInfoRequest\"\xbc\x01\n\x13ProduceInfoResponse\x12\x30\n\x08produces\x18\x01 \x03(\x0b\x32\x1e.com.common.msg.SkinProduceMsg\x12:\n\rproduceOrders\x18\x02 \x03(\x0b\x32#.com.common.msg.SkinProduceOrderMsg\x12\x1b\n\x13\x63umulativeStartTime\x18\x03 \x01(\x03\x12\x1a\n\x12\x63umulativeOrderCnt\x18\x04 \x01(\x05\"\x1e\n\rUnlockRequest\x12\r\n\x05tplId\x18\x01 \x01(\t\"\x10\n\x0eUnlockResponse\")\n\x18ProduceDragonSkinRequest\x12\r\n\x05tplId\x18\x01 \x01(\t\"\xca\x01\n\x19ProduceDragonSkinResponse\x12\x0c\n\x04succ\x18\x01 \x01(\x08\x12.\n\x07newSkin\x18\x02 \x01(\x0b\x32\x1d.com.common.msg.DragonSkinMsg\x12&\n\x05items\x18\x03 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12/\n\x07produce\x18\x04 \x01(\x0b\x32\x1e.com.common.msg.SkinProduceMsg\x12\x16\n\x0e\x63onsumeSkinIds\x18\x05 \x03(\x03\"/\n\x14UseDesignItemRequest\x12\x17\n\x0fitemTemplateIds\x18\x01 \x03(\t\"\x17\n\x15UseDesignItemResponse\"B\n\x18UseDragonSkinItemRequest\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"I\n\x19UseDragonSkinItemResponse\x12,\n\x05skins\x18\x01 \x03(\x0b\x32\x1d.com.common.msg.DragonSkinMsg\")\n\x17\x44\x65leteDragonSkinRequest\x12\x0e\n\x06skinId\x18\x01 \x01(\x03\"P\n\x18\x44\x65leteDragonSkinResponse\x12\x34\n\x08\x63reature\x18\x01 \x01(\x0b\x32\".com.common.msg.MagicalCreatureMsg\"\x18\n\x16OpenSkinProduceRequest\"\x19\n\x17OpenSkinProduceResponse\"3\n\x19\x45xchangeDesignItemRequest\x12\x16\n\x0eitemTemplateId\x18\x01 \x01(\t\"\x1c\n\x1a\x45xchangeDesignItemResponse\"F\n\x1dProduceDragonSkinOrderRequest\x12\x0f\n\x07quality\x18\x01 \x01(\x05\x12\x14\n\x0cresultSkinId\x18\x02 \x01(\t\"O\n\x1eProduceDragonSkinOrderResponse\x12-\n\x0c\x65xtraRewards\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"]\n DragonSkinOrderAccelerateRequest\x12\x0f\n\x07quality\x18\x01 \x01(\x05\x12(\n\x07\x63onsume\x18\x02 \x02(\x0b\x32\x17.com.common.msg.ItemMsg\"#\n!DragonSkinOrderAccelerateResponse\"6\n#ProduceDragonSkinOrderRewardRequest\x12\x0f\n\x07quality\x18\x01 \x01(\x05\"\x9a\x01\n$ProduceDragonSkinOrderRewardResponse\x12.\n\x07newSkin\x18\x01 \x01(\x0b\x32\x1d.com.common.msg.DragonSkinMsg\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12\x1a\n\x12\x63umulativeOrderCnt\x18\x03 \x01(\x05\".\n\x19OrderProgressStartRequest\x12\x11\n\tstartTime\x18\x01 \x02(\x03\"\x1c\n\x1aOrderProgressStartResponse\"n\n\"ProduceDragonSkinOrderStartRequest\x12\x0f\n\x07quality\x18\x01 \x01(\x05\x12\x16\n\x0e\x63onsumeSkinIds\x18\x02 \x03(\x03\x12\x12\n\nuseWelfare\x18\x03 \x01(\x08\x12\x0b\n\x03\x61\x64s\x18\x04 \x01(\x08\"%\n#ProduceDragonSkinOrderStartResponse*\xb6\x05\n\x1eSkinProduceModuleMsgSubCommand\x12*\n$SKINPRODUCEMODULEMSG_SUB_PRODUCEINFO\x10\xcd\xd0\x01\x12%\n\x1fSKINPRODUCEMODULEMSG_SUB_UNLOCK\x10\xce\xd0\x01\x12\x30\n*SKINPRODUCEMODULEMSG_SUB_PRODUCEDRAGONSKIN\x10\xcf\xd0\x01\x12,\n&SKINPRODUCEMODULEMSG_SUB_USEDESIGNITEM\x10\xd0\xd0\x01\x12\x30\n*SKINPRODUCEMODULEMSG_SUB_USEDRAGONSKINITEM\x10\xd1\xd0\x01\x12/\n)SKINPRODUCEMODULEMSG_SUB_DELETEDRAGONSKIN\x10\xd2\xd0\x01\x12.\n(SKINPRODUCEMODULEMSG_SUB_OPENSKINPRODUCE\x10\xd3\xd0\x01\x12\x31\n+SKINPRODUCEMODULEMSG_SUB_EXCHANGEDESIGNITEM\x10\xd4\xd0\x01\x12\x35\n/SKINPRODUCEMODULEMSG_SUB_PRODUCEDRAGONSKINORDER\x10\xd5\xd0\x01\x12\x38\n2SKINPRODUCEMODULEMSG_SUB_DRAGONSKINORDERACCELERATE\x10\xd6\xd0\x01\x12;\n5SKINPRODUCEMODULEMSG_SUB_PRODUCEDRAGONSKINORDERREWARD\x10\xd7\xd0\x01\x12\x31\n+SKINPRODUCEMODULEMSG_SUB_ORDERPROGRESSSTART\x10\xd8\xd0\x01\x12:\n4SKINPRODUCEMODULEMSG_SUB_PRODUCEDRAGONSKINORDERSTART\x10\xd9\xd0\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SkinProduceModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SKINPRODUCEMODULEMSGSUBCOMMAND']._serialized_start=1972
  _globals['_SKINPRODUCEMODULEMSGSUBCOMMAND']._serialized_end=2666
  _globals['_SKINPRODUCEMSG']._serialized_start=67
  _globals['_SKINPRODUCEMSG']._serialized_end=128
  _globals['_SKINPRODUCEORDERMSG']._serialized_start=130
  _globals['_SKINPRODUCEORDERMSG']._serialized_end=253
  _globals['_PRODUCEINFOREQUEST']._serialized_start=255
  _globals['_PRODUCEINFOREQUEST']._serialized_end=275
  _globals['_PRODUCEINFORESPONSE']._serialized_start=278
  _globals['_PRODUCEINFORESPONSE']._serialized_end=466
  _globals['_UNLOCKREQUEST']._serialized_start=468
  _globals['_UNLOCKREQUEST']._serialized_end=498
  _globals['_UNLOCKRESPONSE']._serialized_start=500
  _globals['_UNLOCKRESPONSE']._serialized_end=516
  _globals['_PRODUCEDRAGONSKINREQUEST']._serialized_start=518
  _globals['_PRODUCEDRAGONSKINREQUEST']._serialized_end=559
  _globals['_PRODUCEDRAGONSKINRESPONSE']._serialized_start=562
  _globals['_PRODUCEDRAGONSKINRESPONSE']._serialized_end=764
  _globals['_USEDESIGNITEMREQUEST']._serialized_start=766
  _globals['_USEDESIGNITEMREQUEST']._serialized_end=813
  _globals['_USEDESIGNITEMRESPONSE']._serialized_start=815
  _globals['_USEDESIGNITEMRESPONSE']._serialized_end=838
  _globals['_USEDRAGONSKINITEMREQUEST']._serialized_start=840
  _globals['_USEDRAGONSKINITEMREQUEST']._serialized_end=906
  _globals['_USEDRAGONSKINITEMRESPONSE']._serialized_start=908
  _globals['_USEDRAGONSKINITEMRESPONSE']._serialized_end=981
  _globals['_DELETEDRAGONSKINREQUEST']._serialized_start=983
  _globals['_DELETEDRAGONSKINREQUEST']._serialized_end=1024
  _globals['_DELETEDRAGONSKINRESPONSE']._serialized_start=1026
  _globals['_DELETEDRAGONSKINRESPONSE']._serialized_end=1106
  _globals['_OPENSKINPRODUCEREQUEST']._serialized_start=1108
  _globals['_OPENSKINPRODUCEREQUEST']._serialized_end=1132
  _globals['_OPENSKINPRODUCERESPONSE']._serialized_start=1134
  _globals['_OPENSKINPRODUCERESPONSE']._serialized_end=1159
  _globals['_EXCHANGEDESIGNITEMREQUEST']._serialized_start=1161
  _globals['_EXCHANGEDESIGNITEMREQUEST']._serialized_end=1212
  _globals['_EXCHANGEDESIGNITEMRESPONSE']._serialized_start=1214
  _globals['_EXCHANGEDESIGNITEMRESPONSE']._serialized_end=1242
  _globals['_PRODUCEDRAGONSKINORDERREQUEST']._serialized_start=1244
  _globals['_PRODUCEDRAGONSKINORDERREQUEST']._serialized_end=1314
  _globals['_PRODUCEDRAGONSKINORDERRESPONSE']._serialized_start=1316
  _globals['_PRODUCEDRAGONSKINORDERRESPONSE']._serialized_end=1395
  _globals['_DRAGONSKINORDERACCELERATEREQUEST']._serialized_start=1397
  _globals['_DRAGONSKINORDERACCELERATEREQUEST']._serialized_end=1490
  _globals['_DRAGONSKINORDERACCELERATERESPONSE']._serialized_start=1492
  _globals['_DRAGONSKINORDERACCELERATERESPONSE']._serialized_end=1527
  _globals['_PRODUCEDRAGONSKINORDERREWARDREQUEST']._serialized_start=1529
  _globals['_PRODUCEDRAGONSKINORDERREWARDREQUEST']._serialized_end=1583
  _globals['_PRODUCEDRAGONSKINORDERREWARDRESPONSE']._serialized_start=1586
  _globals['_PRODUCEDRAGONSKINORDERREWARDRESPONSE']._serialized_end=1740
  _globals['_ORDERPROGRESSSTARTREQUEST']._serialized_start=1742
  _globals['_ORDERPROGRESSSTARTREQUEST']._serialized_end=1788
  _globals['_ORDERPROGRESSSTARTRESPONSE']._serialized_start=1790
  _globals['_ORDERPROGRESSSTARTRESPONSE']._serialized_end=1818
  _globals['_PRODUCEDRAGONSKINORDERSTARTREQUEST']._serialized_start=1820
  _globals['_PRODUCEDRAGONSKINORDERSTARTREQUEST']._serialized_end=1930
  _globals['_PRODUCEDRAGONSKINORDERSTARTRESPONSE']._serialized_start=1932
  _globals['_PRODUCEDRAGONSKINORDERSTARTRESPONSE']._serialized_end=1969
# @@protoc_insertion_point(module_scope)
