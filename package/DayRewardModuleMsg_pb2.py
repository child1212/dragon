# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DayRewardModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DayRewardModuleMsg.proto',
  package='com.common.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x44\x61yRewardModuleMsg.proto\x12\x0e\x63om.common.msg\"$\n\x14\x44\x61yRewardInfoRequest\x12\x0c\n\x04\x66lag\x18\x01 \x02(\x08\"\x88\x01\n\x15\x44\x61yRewardInfoResponse\x12\x1c\n\x14\x63ontinueEnterGameNum\x18\x01 \x02(\x05\x12\x10\n\x08\x62\x61tchNum\x18\x02 \x02(\x05\x12\x12\n\nisRewarded\x18\x03 \x02(\x08\x12\x14\n\x0crdBuildingId\x18\x04 \x02(\t\x12\x15\n\risAdsRewarded\x18\x05 \x01(\x08\"4\n\x13GetDayRewardRequest\x12\x0c\n\x04\x66lag\x18\x01 \x02(\x08\x12\x0f\n\x07\x61\x64sFlag\x18\x02 \x01(\x08\"\\\n\x14GetDayRewardResponse\x12\x10\n\x08\x62\x61tchNum\x18\x01 \x02(\x05\x12\x1c\n\x14\x63ontinueEnterGameNum\x18\x02 \x02(\x05\x12\x14\n\x0crdBuildingId\x18\x03 \x01(\t*s\n\x1c\x44\x61yRewardModuleMsgSubCommand\x12)\n$DAYREWARDMODULEMSG_SUB_DAYREWARDINFO\x10\xa9\x46\x12(\n#DAYREWARDMODULEMSG_SUB_GETDAYREWARD\x10\xaa\x46'
)

_DAYREWARDMODULEMSGSUBCOMMAND = _descriptor.EnumDescriptor(
  name='DayRewardModuleMsgSubCommand',
  full_name='com.common.msg.DayRewardModuleMsgSubCommand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DAYREWARDMODULEMSG_SUB_DAYREWARDINFO', index=0, number=9001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DAYREWARDMODULEMSG_SUB_GETDAYREWARD', index=1, number=9002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=369,
  serialized_end=484,
)
_sym_db.RegisterEnumDescriptor(_DAYREWARDMODULEMSGSUBCOMMAND)

DayRewardModuleMsgSubCommand = enum_type_wrapper.EnumTypeWrapper(_DAYREWARDMODULEMSGSUBCOMMAND)
DAYREWARDMODULEMSG_SUB_DAYREWARDINFO = 9001
DAYREWARDMODULEMSG_SUB_GETDAYREWARD = 9002



_DAYREWARDINFOREQUEST = _descriptor.Descriptor(
  name='DayRewardInfoRequest',
  full_name='com.common.msg.DayRewardInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='com.common.msg.DayRewardInfoRequest.flag', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=80,
)


_DAYREWARDINFORESPONSE = _descriptor.Descriptor(
  name='DayRewardInfoResponse',
  full_name='com.common.msg.DayRewardInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='continueEnterGameNum', full_name='com.common.msg.DayRewardInfoResponse.continueEnterGameNum', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='com.common.msg.DayRewardInfoResponse.batchNum', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isRewarded', full_name='com.common.msg.DayRewardInfoResponse.isRewarded', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rdBuildingId', full_name='com.common.msg.DayRewardInfoResponse.rdBuildingId', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isAdsRewarded', full_name='com.common.msg.DayRewardInfoResponse.isAdsRewarded', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=219,
)


_GETDAYREWARDREQUEST = _descriptor.Descriptor(
  name='GetDayRewardRequest',
  full_name='com.common.msg.GetDayRewardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='com.common.msg.GetDayRewardRequest.flag', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adsFlag', full_name='com.common.msg.GetDayRewardRequest.adsFlag', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=221,
  serialized_end=273,
)


_GETDAYREWARDRESPONSE = _descriptor.Descriptor(
  name='GetDayRewardResponse',
  full_name='com.common.msg.GetDayRewardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='com.common.msg.GetDayRewardResponse.batchNum', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='continueEnterGameNum', full_name='com.common.msg.GetDayRewardResponse.continueEnterGameNum', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rdBuildingId', full_name='com.common.msg.GetDayRewardResponse.rdBuildingId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=367,
)

DESCRIPTOR.message_types_by_name['DayRewardInfoRequest'] = _DAYREWARDINFOREQUEST
DESCRIPTOR.message_types_by_name['DayRewardInfoResponse'] = _DAYREWARDINFORESPONSE
DESCRIPTOR.message_types_by_name['GetDayRewardRequest'] = _GETDAYREWARDREQUEST
DESCRIPTOR.message_types_by_name['GetDayRewardResponse'] = _GETDAYREWARDRESPONSE
DESCRIPTOR.enum_types_by_name['DayRewardModuleMsgSubCommand'] = _DAYREWARDMODULEMSGSUBCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DayRewardInfoRequest = _reflection.GeneratedProtocolMessageType('DayRewardInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAYREWARDINFOREQUEST,
  '__module__' : 'DayRewardModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.DayRewardInfoRequest)
  })
_sym_db.RegisterMessage(DayRewardInfoRequest)

DayRewardInfoResponse = _reflection.GeneratedProtocolMessageType('DayRewardInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAYREWARDINFORESPONSE,
  '__module__' : 'DayRewardModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.DayRewardInfoResponse)
  })
_sym_db.RegisterMessage(DayRewardInfoResponse)

GetDayRewardRequest = _reflection.GeneratedProtocolMessageType('GetDayRewardRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDAYREWARDREQUEST,
  '__module__' : 'DayRewardModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.GetDayRewardRequest)
  })
_sym_db.RegisterMessage(GetDayRewardRequest)

GetDayRewardResponse = _reflection.GeneratedProtocolMessageType('GetDayRewardResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDAYREWARDRESPONSE,
  '__module__' : 'DayRewardModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.GetDayRewardResponse)
  })
_sym_db.RegisterMessage(GetDayRewardResponse)


# @@protoc_insertion_point(module_scope)
