# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CutVegetableModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x43utVegetableModuleMsg.proto\x12\x0e\x63om.common.msg\"/\n\x0fOpenGameRequest\x12\r\n\x05\x61\x63tId\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\t\"\x12\n\x10OpenGameResponse\"A\n\x10\x43loseGameRequest\x12\r\n\x05\x61\x63tId\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\x12\x0f\n\x07levelId\x18\x03 \x01(\t\"9\n\x11\x43loseGameResponse\x12\x12\n\nawardLevel\x18\x01 \x01(\x05\x12\x10\n\x08\x65xchange\x18\x02 \x01(\x05\"!\n\x10GameInfosRequest\x12\r\n\x05\x61\x63tId\x18\x01 \x01(\t\"Z\n\x11GameInfosResponse\x12\x10\n\x08\x65nergies\x18\x01 \x01(\x05\x12\x0e\n\x06scores\x18\x02 \x01(\x05\x12\x12\n\nawardLevel\x18\x03 \x01(\x05\x12\x0f\n\x07levelId\x18\x04 \x01(\t*\xa1\x01\n\x1f\x43utVegetableModuleMsgSubCommand\x12(\n\"CUTVEGETABLEMODULEMSG_SUB_OPENGAME\x10\xad\xe3\x01\x12)\n#CUTVEGETABLEMODULEMSG_SUB_CLOSEGAME\x10\xae\xe3\x01\x12)\n#CUTVEGETABLEMODULEMSG_SUB_GAMEINFOS\x10\xaf\xe3\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CutVegetableModuleMsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CUTVEGETABLEMODULEMSGSUBCOMMAND']._serialized_start=370
  _globals['_CUTVEGETABLEMODULEMSGSUBCOMMAND']._serialized_end=531
  _globals['_OPENGAMEREQUEST']._serialized_start=47
  _globals['_OPENGAMEREQUEST']._serialized_end=94
  _globals['_OPENGAMERESPONSE']._serialized_start=96
  _globals['_OPENGAMERESPONSE']._serialized_end=114
  _globals['_CLOSEGAMEREQUEST']._serialized_start=116
  _globals['_CLOSEGAMEREQUEST']._serialized_end=181
  _globals['_CLOSEGAMERESPONSE']._serialized_start=183
  _globals['_CLOSEGAMERESPONSE']._serialized_end=240
  _globals['_GAMEINFOSREQUEST']._serialized_start=242
  _globals['_GAMEINFOSREQUEST']._serialized_end=275
  _globals['_GAMEINFOSRESPONSE']._serialized_start=277
  _globals['_GAMEINFOSRESPONSE']._serialized_end=367
# @@protoc_insertion_point(module_scope)
