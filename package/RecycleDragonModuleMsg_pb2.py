# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RecycleDragonModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cRecycleDragonModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"1\n\x0cRecycleCount\x12\x12\n\ndragonType\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\"N\n\x10\x43umulativeReward\x12\x10\n\x08rewardId\x18\x01 \x01(\x05\x12(\n\x07rewards\x18\x02 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"\x1a\n\x18RecycleDragonInfoRequest\"\xbd\x02\n\x19RecycleDragonInfoResponse\x12\x11\n\tstartTime\x18\x01 \x01(\x03\x12\x13\n\x0b\x64ragonTypes\x18\x02 \x03(\x05\x12\x1a\n\x12\x63umulativeRewardId\x18\x03 \x01(\x05\x12\x17\n\x0f\x63umulativeScore\x18\x04 \x01(\x05\x12\x33\n\rrecycleCounts\x18\x05 \x03(\x0b\x32\x1c.com.common.msg.RecycleCount\x12;\n\x11\x63umulativeRewards\x18\x06 \x03(\x0b\x32 .com.common.msg.CumulativeReward\x12\x39\n\x18unclaimedTransferRewards\x18\x07 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12\x16\n\x0eunclaimedScore\x18\x08 \x01(\x05\"/\n\x18RecycleDragonOpenRequest\x12\x13\n\x0b\x64ragonTypes\x18\x01 \x03(\x05\"X\n\x19RecycleDragonOpenResponse\x12;\n\x11\x63umulativeRewards\x18\x01 \x03(\x0b\x32 .com.common.msg.CumulativeReward\"D\n\x1aRecycleDragonCreateRequest\x12\x11\n\tstartTime\x18\x01 \x01(\x03\x12\x13\n\x0b\x64ragonTypes\x18\x02 \x03(\x05\"\x1d\n\x1bRecycleDragonCreateResponse\"D\n\x1aRecycleDragonDeleteRequest\x12\x11\n\tstartTime\x18\x01 \x01(\x03\x12\x13\n\x0b\x64ragonTypes\x18\x02 \x03(\x05\"\x1d\n\x1bRecycleDragonDeleteResponse\"T\n\x1aRecycleDragonSkipCdRequest\x12)\n\x08\x63ostItem\x18\x01 \x01(\x0b\x32\x17.com.common.msg.ItemMsg\x12\x0b\n\x03\x61\x64s\x18\x02 \x01(\x08\"\x1d\n\x1bRecycleDragonSkipCdResponse\"Z\n\x1cRecycleDragonTransferRequest\x12\x12\n\ncreatureId\x18\x01 \x03(\x03\x12\x11\n\tstartTime\x18\x02 \x01(\x03\x12\x13\n\x0b\x64ragonTypes\x18\x03 \x03(\x05\"S\n\x1dRecycleDragonTransferResponse\x12\x32\n\x06others\x18\x01 \x03(\x0b\x32\".com.common.msg.MagicalCreatureMsg\"$\n\"RecycleDragonTransferRewardRequest\"Y\n#RecycleDragonTransferRewardResponse\x12\x32\n\x11\x63ontributeRewards\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"&\n$RecycleDragonCumulativeRewardRequest\"\xcc\x01\n%RecycleDragonCumulativeRewardResponse\x12\x31\n\x07rewards\x18\x01 \x03(\x0b\x32 .com.common.msg.CumulativeReward\x12\x1a\n\x12\x63umulativeRewardId\x18\x02 \x01(\x05\x12\x17\n\x0f\x63umulativeScore\x18\x03 \x01(\x05\x12;\n\x11\x63umulativeRewards\x18\x04 \x03(\x0b\x32 .com.common.msg.CumulativeReward*\xe2\x03\n RecycleDragonModuleMsgSubCommand\x12\x32\n,RECYCLEDRAGONMODULEMSG_SUB_RECYCLEDRAGONINFO\x10\xfd\xd9\x01\x12\x32\n,RECYCLEDRAGONMODULEMSG_SUB_RECYCLEDRAGONOPEN\x10\xfe\xd9\x01\x12\x34\n.RECYCLEDRAGONMODULEMSG_SUB_RECYCLEDRAGONCREATE\x10\xff\xd9\x01\x12\x34\n.RECYCLEDRAGONMODULEMSG_SUB_RECYCLEDRAGONDELETE\x10\x80\xda\x01\x12\x34\n.RECYCLEDRAGONMODULEMSG_SUB_RECYCLEDRAGONSKIPCD\x10\x81\xda\x01\x12\x36\n0RECYCLEDRAGONMODULEMSG_SUB_RECYCLEDRAGONTRANSFER\x10\x83\xda\x01\x12<\n6RECYCLEDRAGONMODULEMSG_SUB_RECYCLEDRAGONTRANSFERREWARD\x10\x84\xda\x01\x12>\n8RECYCLEDRAGONMODULEMSG_SUB_RECYCLEDRAGONCUMULATIVEREWARD\x10\x85\xda\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RecycleDragonModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_RECYCLEDRAGONMODULEMSGSUBCOMMAND']._serialized_start=1560
  _globals['_RECYCLEDRAGONMODULEMSGSUBCOMMAND']._serialized_end=2042
  _globals['_RECYCLECOUNT']._serialized_start=69
  _globals['_RECYCLECOUNT']._serialized_end=118
  _globals['_CUMULATIVEREWARD']._serialized_start=120
  _globals['_CUMULATIVEREWARD']._serialized_end=198
  _globals['_RECYCLEDRAGONINFOREQUEST']._serialized_start=200
  _globals['_RECYCLEDRAGONINFOREQUEST']._serialized_end=226
  _globals['_RECYCLEDRAGONINFORESPONSE']._serialized_start=229
  _globals['_RECYCLEDRAGONINFORESPONSE']._serialized_end=546
  _globals['_RECYCLEDRAGONOPENREQUEST']._serialized_start=548
  _globals['_RECYCLEDRAGONOPENREQUEST']._serialized_end=595
  _globals['_RECYCLEDRAGONOPENRESPONSE']._serialized_start=597
  _globals['_RECYCLEDRAGONOPENRESPONSE']._serialized_end=685
  _globals['_RECYCLEDRAGONCREATEREQUEST']._serialized_start=687
  _globals['_RECYCLEDRAGONCREATEREQUEST']._serialized_end=755
  _globals['_RECYCLEDRAGONCREATERESPONSE']._serialized_start=757
  _globals['_RECYCLEDRAGONCREATERESPONSE']._serialized_end=786
  _globals['_RECYCLEDRAGONDELETEREQUEST']._serialized_start=788
  _globals['_RECYCLEDRAGONDELETEREQUEST']._serialized_end=856
  _globals['_RECYCLEDRAGONDELETERESPONSE']._serialized_start=858
  _globals['_RECYCLEDRAGONDELETERESPONSE']._serialized_end=887
  _globals['_RECYCLEDRAGONSKIPCDREQUEST']._serialized_start=889
  _globals['_RECYCLEDRAGONSKIPCDREQUEST']._serialized_end=973
  _globals['_RECYCLEDRAGONSKIPCDRESPONSE']._serialized_start=975
  _globals['_RECYCLEDRAGONSKIPCDRESPONSE']._serialized_end=1004
  _globals['_RECYCLEDRAGONTRANSFERREQUEST']._serialized_start=1006
  _globals['_RECYCLEDRAGONTRANSFERREQUEST']._serialized_end=1096
  _globals['_RECYCLEDRAGONTRANSFERRESPONSE']._serialized_start=1098
  _globals['_RECYCLEDRAGONTRANSFERRESPONSE']._serialized_end=1181
  _globals['_RECYCLEDRAGONTRANSFERREWARDREQUEST']._serialized_start=1183
  _globals['_RECYCLEDRAGONTRANSFERREWARDREQUEST']._serialized_end=1219
  _globals['_RECYCLEDRAGONTRANSFERREWARDRESPONSE']._serialized_start=1221
  _globals['_RECYCLEDRAGONTRANSFERREWARDRESPONSE']._serialized_end=1310
  _globals['_RECYCLEDRAGONCUMULATIVEREWARDREQUEST']._serialized_start=1312
  _globals['_RECYCLEDRAGONCUMULATIVEREWARDREQUEST']._serialized_end=1350
  _globals['_RECYCLEDRAGONCUMULATIVEREWARDRESPONSE']._serialized_start=1353
  _globals['_RECYCLEDRAGONCUMULATIVEREWARDRESPONSE']._serialized_end=1557
# @@protoc_insertion_point(module_scope)
