# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: InviteFriendsModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cInviteFriendsModuleMsg.proto\x12\x0e\x63om.common.msg\"\x1a\n\x18InviteFriendsInfoRequest\"d\n\x19InviteFriendsInfoResponse\x12\x1c\n\x14waitRewardFriendsNum\x18\x01 \x01(\x05\x12\x16\n\x0e\x61wardSuccIndex\x18\x02 \x01(\x05\x12\x11\n\tinviteNum\x18\x03 \x01(\x05\"\x18\n\x16TakeInviteAwardRequest\"^\n\x17TakeInviteAwardResponse\x12\x18\n\x10rewardFriendsNum\x18\x01 \x01(\x05\x12\x16\n\x0e\x61wardSuccIndex\x18\x02 \x01(\x05\x12\x11\n\tinviteNum\x18\x03 \x01(\x05*\x88\x01\n InviteFriendsModuleMsgSubCommand\x12\x32\n,INVITEFRIENDSMODULEMSG_SUB_INVITEFRIENDSINFO\x10\xa9\xdc\x01\x12\x30\n*INVITEFRIENDSMODULEMSG_SUB_TAKEINVITEAWARD\x10\xaa\xdc\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'InviteFriendsModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_INVITEFRIENDSMODULEMSGSUBCOMMAND']._serialized_start=301
  _globals['_INVITEFRIENDSMODULEMSGSUBCOMMAND']._serialized_end=437
  _globals['_INVITEFRIENDSINFOREQUEST']._serialized_start=48
  _globals['_INVITEFRIENDSINFOREQUEST']._serialized_end=74
  _globals['_INVITEFRIENDSINFORESPONSE']._serialized_start=76
  _globals['_INVITEFRIENDSINFORESPONSE']._serialized_end=176
  _globals['_TAKEINVITEAWARDREQUEST']._serialized_start=178
  _globals['_TAKEINVITEAWARDREQUEST']._serialized_end=202
  _globals['_TAKEINVITEAWARDRESPONSE']._serialized_start=204
  _globals['_TAKEINVITEAWARDRESPONSE']._serialized_end=298
# @@protoc_insertion_point(module_scope)
