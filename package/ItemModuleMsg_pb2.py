# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ItemModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13ItemModuleMsg.proto\x12\x0e\x63om.common.msg\"A\n\x07ItemMsg\x12\x16\n\x0eitemTemplateId\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x0f\n\x07\x63\x64Times\x18\x03 \x03(\x03\"\x1f\n\x0fItemListRequest\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x05\":\n\x10ItemListResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"I\n\x10ItemChangeNotify\x12\x0e\n\x06isAdds\x18\x01 \x03(\x08\x12%\n\x04msgs\x18\x02 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"=\n\x0eSubItemRequest\x12\x17\n\x0fitemTemplateIds\x18\x01 \x03(\t\x12\x12\n\nitemCounts\x18\x02 \x03(\x05\"$\n\x0fSubItemResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\"4\n\x0e\x44ragonSkillMsg\x12\x0f\n\x07skillId\x18\x01 \x01(\t\x12\x11\n\tskillTime\x18\x02 \x01(\x03\"j\n\rDragonSkinMsg\x12\x0e\n\x06skinId\x18\x01 \x01(\x03\x12\r\n\x05tplId\x18\x02 \x01(\t\x12\x12\n\ncreatureId\x18\x03 \x01(\x03\x12\x13\n\x0b\x65nergyLimit\x18\x04 \x01(\x05\x12\x11\n\tequipTime\x18\x05 \x01(\x03\"\x8e\x04\n\x12MagicalCreatureMsg\x12\x12\n\ncreatureId\x18\x01 \x02(\x03\x12\x12\n\ntemplateId\x18\x02 \x02(\t\x12\x18\n\x10physicalStrength\x18\x03 \x01(\x05\x12\x1f\n\x17getPhysicalStrengthTime\x18\x04 \x01(\x03\x12\x10\n\x08nestType\x18\x05 \x01(\x05\x12#\n\x1blastCollectHangUpRewardTime\x18\x06 \x01(\x03\x12\x18\n\x10repletionEndTime\x18\x07 \x01(\x03\x12\x11\n\trewardCnt\x18\x08 \x01(\x05\x12\x17\n\x0f\x66irstRewardTime\x18\t \x01(\x03\x12\x0f\n\x07\x65xplore\x18\n \x01(\x08\x12.\n\x06skills\x18\x0b \x03(\x0b\x32\x1e.com.common.msg.DragonSkillMsg\x12!\n\x19lastCrownHangUpRewardTime\x18\x0c \x01(\x03\x12,\n\x05skins\x18\r \x03(\x0b\x32\x1d.com.common.msg.DragonSkinMsg\x12\x13\n\x0bmazeEndTime\x18\x0e \x01(\x03\x12\x1c\n\x14todayHangUpRewardCnt\x18\x0f \x01(\x05\x12\x1c\n\x14totalHangUpRewardCnt\x18\x10 \x01(\x05\x12\x1b\n\x13maxPhysicalStrength\x18\x11 \x01(\x05\x12\x18\n\x10inTeamCommission\x18\x12 \x01(\x08\"j\n\x0eUseItemRequest\x12\x16\n\x0eitemTemplateId\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\r\n\x05param\x18\x03 \x01(\t\x12\x11\n\tlevelType\x18\x04 \x01(\x05\x12\x0f\n\x07useType\x18\x05 \x01(\x05\"\xe2\x01\n\x0fUseItemResponse\x12\x16\n\x0eitemTemplateId\x18\x01 \x01(\t\x12\x10\n\x08\x65ntityId\x18\x02 \x01(\t\x12\x12\n\ncreatureId\x18\x03 \x01(\x03\x12&\n\x05items\x18\x04 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12\x35\n\tcreatures\x18\x05 \x03(\x0b\x32\".com.common.msg.MagicalCreatureMsg\x12\x32\n\x06others\x18\x06 \x03(\x0b\x32\".com.common.msg.MagicalCreatureMsg\"n\n\x13\x45xchangeItemRequest\x12\x16\n\x0eitemTemplateId\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\r\n\x05isUse\x18\x03 \x01(\x08\x12\x11\n\tlevelType\x18\x04 \x01(\x05\x12\x0e\n\x06source\x18\x05 \x01(\x05\"\x16\n\x14\x45xchangeItemResponse\"\'\n\x10\x46indItemsRequest\x12\x13\n\x0btemplateIds\x18\x01 \x03(\t\">\n\x11\x46indItemsResponse\x12)\n\x08itemMsgs\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"!\n\x13\x43ollectItemsRequest\x12\n\n\x02id\x18\x01 \x02(\t\"\x16\n\x14\x43ollectItemsResponse\"K\n\x17SupplementEnergyRequest\x12\x0c\n\x04mark\x18\x01 \x02(\x05\x12\x10\n\x08\x64iamonds\x18\x02 \x02(\x05\x12\x10\n\x08\x65nergies\x18\x03 \x02(\x05\"L\n\x18SupplementEnergyResponse\x12\x0c\n\x04mark\x18\x01 \x02(\x05\x12\x10\n\x08\x64iamonds\x18\x02 \x02(\x05\x12\x10\n\x08\x65nergies\x18\x03 \x02(\x05\"G\n\x0eSupplementItem\x12\x16\n\x0eitemTemplateId\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x0e\n\x06source\x18\x03 \x01(\x05\"F\n\x15SupplementItemRequest\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.com.common.msg.SupplementItem\"\x18\n\x16SupplementItemResponse\"\x14\n\x12ReplaceItemRequest\"\x15\n\x13ReplaceItemResponse\"\'\n\x14\x44\x65\x63omposeItemRequest\x12\x0f\n\x07itemIds\x18\x01 \x03(\t\"\x17\n\x15\x44\x65\x63omposeItemResponse*\xa3\x03\n\x17ItemModuleMsgSubCommand\x12\x1f\n\x1aITEMMODULEMSG_SUB_ITEMLIST\x10\xd1\x0f\x12\x1e\n\x19ITEMMODULEMSG_SUB_USEITEM\x10\xd2\x0f\x12\x1e\n\x19ITEMMODULEMSG_SUB_SUBITEM\x10\xd3\x0f\x12!\n\x1cITEMMODULEMSG_SUB_ITEMCHANGE\x10\xd4\x0f\x12#\n\x1eITEMMODULEMSG_SUB_EXCHANGEITEM\x10\xd5\x0f\x12 \n\x1bITEMMODULEMSG_SUB_FINDITEMS\x10\xd7\x0f\x12#\n\x1eITEMMODULEMSG_SUB_COLLECTITEMS\x10\xd8\x0f\x12\'\n\"ITEMMODULEMSG_SUB_SUPPLEMENTENERGY\x10\xd9\x0f\x12%\n ITEMMODULEMSG_SUB_SUPPLEMENTITEM\x10\xda\x0f\x12\"\n\x1dITEMMODULEMSG_SUB_REPLACEITEM\x10\xdb\x0f\x12$\n\x1fITEMMODULEMSG_SUB_DECOMPOSEITEM\x10\xdc\x0f')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ItemModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ITEMMODULEMSGSUBCOMMAND']._serialized_start=2141
  _globals['_ITEMMODULEMSGSUBCOMMAND']._serialized_end=2560
  _globals['_ITEMMSG']._serialized_start=39
  _globals['_ITEMMSG']._serialized_end=104
  _globals['_ITEMLISTREQUEST']._serialized_start=106
  _globals['_ITEMLISTREQUEST']._serialized_end=137
  _globals['_ITEMLISTRESPONSE']._serialized_start=139
  _globals['_ITEMLISTRESPONSE']._serialized_end=197
  _globals['_ITEMCHANGENOTIFY']._serialized_start=199
  _globals['_ITEMCHANGENOTIFY']._serialized_end=272
  _globals['_SUBITEMREQUEST']._serialized_start=274
  _globals['_SUBITEMREQUEST']._serialized_end=335
  _globals['_SUBITEMRESPONSE']._serialized_start=337
  _globals['_SUBITEMRESPONSE']._serialized_end=373
  _globals['_DRAGONSKILLMSG']._serialized_start=375
  _globals['_DRAGONSKILLMSG']._serialized_end=427
  _globals['_DRAGONSKINMSG']._serialized_start=429
  _globals['_DRAGONSKINMSG']._serialized_end=535
  _globals['_MAGICALCREATUREMSG']._serialized_start=538
  _globals['_MAGICALCREATUREMSG']._serialized_end=1064
  _globals['_USEITEMREQUEST']._serialized_start=1066
  _globals['_USEITEMREQUEST']._serialized_end=1172
  _globals['_USEITEMRESPONSE']._serialized_start=1175
  _globals['_USEITEMRESPONSE']._serialized_end=1401
  _globals['_EXCHANGEITEMREQUEST']._serialized_start=1403
  _globals['_EXCHANGEITEMREQUEST']._serialized_end=1513
  _globals['_EXCHANGEITEMRESPONSE']._serialized_start=1515
  _globals['_EXCHANGEITEMRESPONSE']._serialized_end=1537
  _globals['_FINDITEMSREQUEST']._serialized_start=1539
  _globals['_FINDITEMSREQUEST']._serialized_end=1578
  _globals['_FINDITEMSRESPONSE']._serialized_start=1580
  _globals['_FINDITEMSRESPONSE']._serialized_end=1642
  _globals['_COLLECTITEMSREQUEST']._serialized_start=1644
  _globals['_COLLECTITEMSREQUEST']._serialized_end=1677
  _globals['_COLLECTITEMSRESPONSE']._serialized_start=1679
  _globals['_COLLECTITEMSRESPONSE']._serialized_end=1701
  _globals['_SUPPLEMENTENERGYREQUEST']._serialized_start=1703
  _globals['_SUPPLEMENTENERGYREQUEST']._serialized_end=1778
  _globals['_SUPPLEMENTENERGYRESPONSE']._serialized_start=1780
  _globals['_SUPPLEMENTENERGYRESPONSE']._serialized_end=1856
  _globals['_SUPPLEMENTITEM']._serialized_start=1858
  _globals['_SUPPLEMENTITEM']._serialized_end=1929
  _globals['_SUPPLEMENTITEMREQUEST']._serialized_start=1931
  _globals['_SUPPLEMENTITEMREQUEST']._serialized_end=2001
  _globals['_SUPPLEMENTITEMRESPONSE']._serialized_start=2003
  _globals['_SUPPLEMENTITEMRESPONSE']._serialized_end=2027
  _globals['_REPLACEITEMREQUEST']._serialized_start=2029
  _globals['_REPLACEITEMREQUEST']._serialized_end=2049
  _globals['_REPLACEITEMRESPONSE']._serialized_start=2051
  _globals['_REPLACEITEMRESPONSE']._serialized_end=2072
  _globals['_DECOMPOSEITEMREQUEST']._serialized_start=2074
  _globals['_DECOMPOSEITEMREQUEST']._serialized_end=2113
  _globals['_DECOMPOSEITEMRESPONSE']._serialized_start=2115
  _globals['_DECOMPOSEITEMRESPONSE']._serialized_end=2138
# @@protoc_insertion_point(module_scope)
