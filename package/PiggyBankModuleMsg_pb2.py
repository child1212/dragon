# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PiggyBankModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18PiggyBankModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"d\n\x10PiggyBankInfoMsg\x12\x0e\n\x06\x62\x61nkId\x18\x01 \x01(\t\x12\x11\n\tstartTime\x18\x02 \x01(\x03\x12\x0e\n\x06\x65nergy\x18\x03 \x01(\x05\x12\x0e\n\x06\x62ought\x18\x04 \x01(\x08\x12\r\n\x05group\x18\x05 \x01(\t\"\'\n\x15PiggyBankStartRequest\x12\x0e\n\x06\x62\x61nkId\x18\x01 \x02(\t\"\x18\n\x16PiggyBankStartResponse\"\x1a\n\x18PiggyBankUpdateIdRequest\"\x1b\n\x19PiggyBankUpdateIdResponse*{\n\x1cPiggyBankModuleMsgSubCommand\x12+\n%PIGGYBANKMODULEMSG_SUB_PIGGYBANKSTART\x10\xd1\xd7\x01\x12.\n(PIGGYBANKMODULEMSG_SUB_PIGGYBANKUPDATEID\x10\xd2\xd7\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PiggyBankModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_PIGGYBANKMODULEMSGSUBCOMMAND']._serialized_start=291
  _globals['_PIGGYBANKMODULEMSGSUBCOMMAND']._serialized_end=414
  _globals['_PIGGYBANKINFOMSG']._serialized_start=65
  _globals['_PIGGYBANKINFOMSG']._serialized_end=165
  _globals['_PIGGYBANKSTARTREQUEST']._serialized_start=167
  _globals['_PIGGYBANKSTARTREQUEST']._serialized_end=206
  _globals['_PIGGYBANKSTARTRESPONSE']._serialized_start=208
  _globals['_PIGGYBANKSTARTRESPONSE']._serialized_end=232
  _globals['_PIGGYBANKUPDATEIDREQUEST']._serialized_start=234
  _globals['_PIGGYBANKUPDATEIDREQUEST']._serialized_end=260
  _globals['_PIGGYBANKUPDATEIDRESPONSE']._serialized_start=262
  _globals['_PIGGYBANKUPDATEIDRESPONSE']._serialized_end=289
# @@protoc_insertion_point(module_scope)
