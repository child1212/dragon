# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GatewayModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16GatewayModuleMsg.proto\x12\x0f\x63om.framwork.sx\"s\n\rMessageStruct\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05msgId\x18\x02 \x01(\x05\x12\x0f\n\x07msgBody\x18\x03 \x01(\x0c\x12\x0f\n\x07genTime\x18\x04 \x01(\x03\x12\x12\n\nsequenceId\x18\x05 \x01(\x03\x12\x0f\n\x07version\x18\x06 \x01(\t\"k\n\x15GatewayPackageRequest\x12\x10\n\x08senderId\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\x03\x12-\n\x05\x62odys\x18\x03 \x03(\x0b\x32\x1e.com.framwork.sx.MessageStruct\"V\n\x16GatewayPackageResponse\x12-\n\x05\x62odys\x18\x01 \x03(\x0b\x32\x1e.com.framwork.sx.MessageStruct\x12\r\n\x05\x66lags\x18\x02 \x03(\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GatewayModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_MESSAGESTRUCT']._serialized_start=43
  _globals['_MESSAGESTRUCT']._serialized_end=158
  _globals['_GATEWAYPACKAGEREQUEST']._serialized_start=160
  _globals['_GATEWAYPACKAGEREQUEST']._serialized_end=267
  _globals['_GATEWAYPACKAGERESPONSE']._serialized_start=269
  _globals['_GATEWAYPACKAGERESPONSE']._serialized_end=355
# @@protoc_insertion_point(module_scope)
