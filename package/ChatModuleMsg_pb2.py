# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ChatModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x43hatModuleMsg.proto\x12\x0e\x63om.common.msg\"\x88\x01\n\x08\x43hatInfo\x12\x0b\n\x03pid\x18\x01 \x02(\t\x12\r\n\x05pname\x18\x02 \x02(\t\x12\x0c\n\x04head\x18\x03 \x02(\t\x12\r\n\x05\x66rame\x18\x04 \x02(\t\x12\r\n\x05title\x18\x05 \x02(\t\x12\x11\n\ttimeStamp\x18\x06 \x02(\x03\x12\x0f\n\x07\x63ontent\x18\x07 \x02(\t\x12\x10\n\x08vipLevel\x18\x08 \x01(\x05\"Z\n\x0bRedEnvelope\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0e\n\x06itemid\x18\x02 \x01(\t\x12\x11\n\ttimeStamp\x18\x03 \x01(\x03\x12\x0b\n\x03pid\x18\x04 \x01(\t\x12\r\n\x05pname\x18\x05 \x01(\t\"n\n\x11RedEnvelopeRecord\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0b\n\x03pid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06itemId\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x05\x12\x11\n\ttimeStamp\x18\x06 \x01(\x03\",\n\x0bSpecialInfo\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0f\n\x07msgBody\x18\x02 \x01(\x0c\"F\n\x0b\x43hatRequest\x12\x0b\n\x03\x63id\x18\x01 \x02(\t\x12*\n\x08\x63hatInfo\x18\x02 \x01(\x0b\x32\x18.com.common.msg.ChatInfo\"!\n\x0c\x43hatResponse\x12\x11\n\ttimeStamp\x18\x01 \x02(\x03\"1\n\x0f\x43hatListRequest\x12\x0b\n\x03\x63id\x18\x01 \x02(\t\x12\x11\n\ttimeStamp\x18\x02 \x02(\x03\"r\n\x10\x43hatListResponse\x12+\n\tchatInfos\x18\x01 \x03(\x0b\x32\x18.com.common.msg.ChatInfo\x12\x31\n\x0cspecialInfos\x18\x02 \x03(\x0b\x32\x1b.com.common.msg.SpecialInfo*Y\n\x17\x43hatModuleMsgSubCommand\x12\x1c\n\x16\x43HATMODULEMSG_SUB_CHAT\x10\xa5\xd5\x01\x12 \n\x1a\x43HATMODULEMSG_SUB_CHATLIST\x10\xa6\xd5\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ChatModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CHATMODULEMSGSUBCOMMAND']._serialized_start=702
  _globals['_CHATMODULEMSGSUBCOMMAND']._serialized_end=791
  _globals['_CHATINFO']._serialized_start=40
  _globals['_CHATINFO']._serialized_end=176
  _globals['_REDENVELOPE']._serialized_start=178
  _globals['_REDENVELOPE']._serialized_end=268
  _globals['_REDENVELOPERECORD']._serialized_start=270
  _globals['_REDENVELOPERECORD']._serialized_end=380
  _globals['_SPECIALINFO']._serialized_start=382
  _globals['_SPECIALINFO']._serialized_end=426
  _globals['_CHATREQUEST']._serialized_start=428
  _globals['_CHATREQUEST']._serialized_end=498
  _globals['_CHATRESPONSE']._serialized_start=500
  _globals['_CHATRESPONSE']._serialized_end=533
  _globals['_CHATLISTREQUEST']._serialized_start=535
  _globals['_CHATLISTREQUEST']._serialized_end=584
  _globals['_CHATLISTRESPONSE']._serialized_start=586
  _globals['_CHATLISTRESPONSE']._serialized_end=700
# @@protoc_insertion_point(module_scope)
