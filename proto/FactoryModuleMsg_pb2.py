# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FactoryModuleMsg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemModuleMsg_pb2 as ItemModuleMsg__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='FactoryModuleMsg.proto',
  package='com.common.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x46\x61\x63toryModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"1\n\x10ProduceRecordMsg\x12\x0e\n\x06itemId\x18\x01 \x02(\t\x12\r\n\x05times\x18\x02 \x02(\x05\"\x92\x01\n\nFactoryMsg\x12\x11\n\tfactoryId\x18\x01 \x02(\t\x12\x13\n\x0bopenSlotCnt\x18\x02 \x02(\x05\x12\x11\n\tstartTime\x18\x03 \x02(\x03\x12\x0f\n\x07itemIds\x18\x04 \x03(\t\x12\x38\n\x0eproduceRecords\x18\x05 \x03(\x0b\x32 .com.common.msg.ProduceRecordMsg\"7\n\x11\x46\x61\x63toryProduceMsg\x12\x11\n\tfactoryId\x18\x01 \x02(\t\x12\x0f\n\x07itemIds\x18\x04 \x03(\t\"$\n\x0fOpenSlotRequest\x12\x11\n\tfactoryId\x18\x01 \x02(\t\"@\n\x10OpenSlotResponse\x12,\n\x08\x66\x61\x63torys\x18\x01 \x03(\x0b\x32\x1a.com.common.msg.FactoryMsg\"=\n\x18\x41\x64\x64\x46\x61\x63toryProduceRequest\x12\x11\n\tfactoryId\x18\x01 \x02(\t\x12\x0e\n\x06itemId\x18\x02 \x02(\t\"q\n\x19\x41\x64\x64\x46\x61\x63toryProduceResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12,\n\x08\x66\x61\x63torys\x18\x02 \x03(\x0b\x32\x1a.com.common.msg.FactoryMsg\"S\n\x1cReceiveFactoryProduceRequest\x12\x33\n\x08produces\x18\x01 \x03(\x0b\x32!.com.common.msg.FactoryProduceMsg\"u\n\x1dReceiveFactoryProduceResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12,\n\x08\x66\x61\x63torys\x18\x02 \x03(\x0b\x32\x1a.com.common.msg.FactoryMsg\"I\n\x18\x41\x63\x63\x65lerateProduceRequest\x12\x11\n\tfactoryId\x18\x01 \x02(\t\x12\r\n\x05price\x18\x02 \x02(\x05\x12\x0b\n\x03\x61\x64s\x18\x03 \x01(\x08\"q\n\x19\x41\x63\x63\x65lerateProduceResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12,\n\x08\x66\x61\x63torys\x18\x02 \x03(\x0b\x32\x1a.com.common.msg.FactoryMsg\"\x1d\n\x1b\x46\x61\x63toryCenterUpLevelRequest\"F\n\x1c\x46\x61\x63toryCenterUpLevelResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"[\n\x1fUseItemAccelerateProduceRequest\x12\x11\n\tfactoryId\x18\x01 \x02(\t\x12%\n\x04item\x18\x02 \x01(\x0b\x32\x17.com.common.msg.ItemMsg\"x\n UseItemAccelerateProduceResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\x12,\n\x08\x66\x61\x63torys\x18\x02 \x03(\x0b\x32\x1a.com.common.msg.FactoryMsg\"5\n\x1aUseDesignitemUnlockRequest\x12\x17\n\x0fitemTemplateIds\x18\x01 \x03(\t\"\x1d\n\x1bUseDesignitemUnlockResponse*\xe5\x02\n\x1a\x46\x61\x63toryModuleMsgSubCommand\x12#\n\x1d\x46\x41\x43TORYMODULEMSG_SUB_OPENSLOT\x10\x8d\xc4\x01\x12,\n&FACTORYMODULEMSG_SUB_ADDFACTORYPRODUCE\x10\x8e\xc4\x01\x12\x30\n*FACTORYMODULEMSG_SUB_RECEIVEFACTORYPRODUCE\x10\x8f\xc4\x01\x12,\n&FACTORYMODULEMSG_SUB_ACCELERATEPRODUCE\x10\x90\xc4\x01\x12/\n)FACTORYMODULEMSG_SUB_FACTORYCENTERUPLEVEL\x10\x91\xc4\x01\x12\x33\n-FACTORYMODULEMSG_SUB_USEITEMACCELERATEPRODUCE\x10\x92\xc4\x01\x12.\n(FACTORYMODULEMSG_SUB_USEDESIGNITEMUNLOCK\x10\x93\xc4\x01'
  ,
  dependencies=[ItemModuleMsg__pb2.DESCRIPTOR,])

_FACTORYMODULEMSGSUBCOMMAND = _descriptor.EnumDescriptor(
  name='FactoryModuleMsgSubCommand',
  full_name='com.common.msg.FactoryModuleMsgSubCommand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FACTORYMODULEMSG_SUB_OPENSLOT', index=0, number=25101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FACTORYMODULEMSG_SUB_ADDFACTORYPRODUCE', index=1, number=25102,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FACTORYMODULEMSG_SUB_RECEIVEFACTORYPRODUCE', index=2, number=25103,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FACTORYMODULEMSG_SUB_ACCELERATEPRODUCE', index=3, number=25104,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FACTORYMODULEMSG_SUB_FACTORYCENTERUPLEVEL', index=4, number=25105,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FACTORYMODULEMSG_SUB_USEITEMACCELERATEPRODUCE', index=5, number=25106,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FACTORYMODULEMSG_SUB_USEDESIGNITEMUNLOCK', index=6, number=25107,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1401,
  serialized_end=1758,
)
_sym_db.RegisterEnumDescriptor(_FACTORYMODULEMSGSUBCOMMAND)

FactoryModuleMsgSubCommand = enum_type_wrapper.EnumTypeWrapper(_FACTORYMODULEMSGSUBCOMMAND)
FACTORYMODULEMSG_SUB_OPENSLOT = 25101
FACTORYMODULEMSG_SUB_ADDFACTORYPRODUCE = 25102
FACTORYMODULEMSG_SUB_RECEIVEFACTORYPRODUCE = 25103
FACTORYMODULEMSG_SUB_ACCELERATEPRODUCE = 25104
FACTORYMODULEMSG_SUB_FACTORYCENTERUPLEVEL = 25105
FACTORYMODULEMSG_SUB_USEITEMACCELERATEPRODUCE = 25106
FACTORYMODULEMSG_SUB_USEDESIGNITEMUNLOCK = 25107



_PRODUCERECORDMSG = _descriptor.Descriptor(
  name='ProduceRecordMsg',
  full_name='com.common.msg.ProduceRecordMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='itemId', full_name='com.common.msg.ProduceRecordMsg.itemId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='times', full_name='com.common.msg.ProduceRecordMsg.times', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=63,
  serialized_end=112,
)


_FACTORYMSG = _descriptor.Descriptor(
  name='FactoryMsg',
  full_name='com.common.msg.FactoryMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='factoryId', full_name='com.common.msg.FactoryMsg.factoryId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='openSlotCnt', full_name='com.common.msg.FactoryMsg.openSlotCnt', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='com.common.msg.FactoryMsg.startTime', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemIds', full_name='com.common.msg.FactoryMsg.itemIds', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='produceRecords', full_name='com.common.msg.FactoryMsg.produceRecords', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=115,
  serialized_end=261,
)


_FACTORYPRODUCEMSG = _descriptor.Descriptor(
  name='FactoryProduceMsg',
  full_name='com.common.msg.FactoryProduceMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='factoryId', full_name='com.common.msg.FactoryProduceMsg.factoryId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemIds', full_name='com.common.msg.FactoryProduceMsg.itemIds', index=1,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=263,
  serialized_end=318,
)


_OPENSLOTREQUEST = _descriptor.Descriptor(
  name='OpenSlotRequest',
  full_name='com.common.msg.OpenSlotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='factoryId', full_name='com.common.msg.OpenSlotRequest.factoryId', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=320,
  serialized_end=356,
)


_OPENSLOTRESPONSE = _descriptor.Descriptor(
  name='OpenSlotResponse',
  full_name='com.common.msg.OpenSlotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='factorys', full_name='com.common.msg.OpenSlotResponse.factorys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=358,
  serialized_end=422,
)


_ADDFACTORYPRODUCEREQUEST = _descriptor.Descriptor(
  name='AddFactoryProduceRequest',
  full_name='com.common.msg.AddFactoryProduceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='factoryId', full_name='com.common.msg.AddFactoryProduceRequest.factoryId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemId', full_name='com.common.msg.AddFactoryProduceRequest.itemId', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=424,
  serialized_end=485,
)


_ADDFACTORYPRODUCERESPONSE = _descriptor.Descriptor(
  name='AddFactoryProduceResponse',
  full_name='com.common.msg.AddFactoryProduceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='com.common.msg.AddFactoryProduceResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factorys', full_name='com.common.msg.AddFactoryProduceResponse.factorys', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=487,
  serialized_end=600,
)


_RECEIVEFACTORYPRODUCEREQUEST = _descriptor.Descriptor(
  name='ReceiveFactoryProduceRequest',
  full_name='com.common.msg.ReceiveFactoryProduceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='produces', full_name='com.common.msg.ReceiveFactoryProduceRequest.produces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=602,
  serialized_end=685,
)


_RECEIVEFACTORYPRODUCERESPONSE = _descriptor.Descriptor(
  name='ReceiveFactoryProduceResponse',
  full_name='com.common.msg.ReceiveFactoryProduceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='com.common.msg.ReceiveFactoryProduceResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factorys', full_name='com.common.msg.ReceiveFactoryProduceResponse.factorys', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=687,
  serialized_end=804,
)


_ACCELERATEPRODUCEREQUEST = _descriptor.Descriptor(
  name='AccelerateProduceRequest',
  full_name='com.common.msg.AccelerateProduceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='factoryId', full_name='com.common.msg.AccelerateProduceRequest.factoryId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='com.common.msg.AccelerateProduceRequest.price', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ads', full_name='com.common.msg.AccelerateProduceRequest.ads', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=806,
  serialized_end=879,
)


_ACCELERATEPRODUCERESPONSE = _descriptor.Descriptor(
  name='AccelerateProduceResponse',
  full_name='com.common.msg.AccelerateProduceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='com.common.msg.AccelerateProduceResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factorys', full_name='com.common.msg.AccelerateProduceResponse.factorys', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=881,
  serialized_end=994,
)


_FACTORYCENTERUPLEVELREQUEST = _descriptor.Descriptor(
  name='FactoryCenterUpLevelRequest',
  full_name='com.common.msg.FactoryCenterUpLevelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=996,
  serialized_end=1025,
)


_FACTORYCENTERUPLEVELRESPONSE = _descriptor.Descriptor(
  name='FactoryCenterUpLevelResponse',
  full_name='com.common.msg.FactoryCenterUpLevelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='com.common.msg.FactoryCenterUpLevelResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1027,
  serialized_end=1097,
)


_USEITEMACCELERATEPRODUCEREQUEST = _descriptor.Descriptor(
  name='UseItemAccelerateProduceRequest',
  full_name='com.common.msg.UseItemAccelerateProduceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='factoryId', full_name='com.common.msg.UseItemAccelerateProduceRequest.factoryId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item', full_name='com.common.msg.UseItemAccelerateProduceRequest.item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1099,
  serialized_end=1190,
)


_USEITEMACCELERATEPRODUCERESPONSE = _descriptor.Descriptor(
  name='UseItemAccelerateProduceResponse',
  full_name='com.common.msg.UseItemAccelerateProduceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='com.common.msg.UseItemAccelerateProduceResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factorys', full_name='com.common.msg.UseItemAccelerateProduceResponse.factorys', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1192,
  serialized_end=1312,
)


_USEDESIGNITEMUNLOCKREQUEST = _descriptor.Descriptor(
  name='UseDesignitemUnlockRequest',
  full_name='com.common.msg.UseDesignitemUnlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='itemTemplateIds', full_name='com.common.msg.UseDesignitemUnlockRequest.itemTemplateIds', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1314,
  serialized_end=1367,
)


_USEDESIGNITEMUNLOCKRESPONSE = _descriptor.Descriptor(
  name='UseDesignitemUnlockResponse',
  full_name='com.common.msg.UseDesignitemUnlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1369,
  serialized_end=1398,
)

_FACTORYMSG.fields_by_name['produceRecords'].message_type = _PRODUCERECORDMSG
_OPENSLOTRESPONSE.fields_by_name['factorys'].message_type = _FACTORYMSG
_ADDFACTORYPRODUCERESPONSE.fields_by_name['items'].message_type = ItemModuleMsg__pb2._ITEMMSG
_ADDFACTORYPRODUCERESPONSE.fields_by_name['factorys'].message_type = _FACTORYMSG
_RECEIVEFACTORYPRODUCEREQUEST.fields_by_name['produces'].message_type = _FACTORYPRODUCEMSG
_RECEIVEFACTORYPRODUCERESPONSE.fields_by_name['items'].message_type = ItemModuleMsg__pb2._ITEMMSG
_RECEIVEFACTORYPRODUCERESPONSE.fields_by_name['factorys'].message_type = _FACTORYMSG
_ACCELERATEPRODUCERESPONSE.fields_by_name['items'].message_type = ItemModuleMsg__pb2._ITEMMSG
_ACCELERATEPRODUCERESPONSE.fields_by_name['factorys'].message_type = _FACTORYMSG
_FACTORYCENTERUPLEVELRESPONSE.fields_by_name['items'].message_type = ItemModuleMsg__pb2._ITEMMSG
_USEITEMACCELERATEPRODUCEREQUEST.fields_by_name['item'].message_type = ItemModuleMsg__pb2._ITEMMSG
_USEITEMACCELERATEPRODUCERESPONSE.fields_by_name['items'].message_type = ItemModuleMsg__pb2._ITEMMSG
_USEITEMACCELERATEPRODUCERESPONSE.fields_by_name['factorys'].message_type = _FACTORYMSG
DESCRIPTOR.message_types_by_name['ProduceRecordMsg'] = _PRODUCERECORDMSG
DESCRIPTOR.message_types_by_name['FactoryMsg'] = _FACTORYMSG
DESCRIPTOR.message_types_by_name['FactoryProduceMsg'] = _FACTORYPRODUCEMSG
DESCRIPTOR.message_types_by_name['OpenSlotRequest'] = _OPENSLOTREQUEST
DESCRIPTOR.message_types_by_name['OpenSlotResponse'] = _OPENSLOTRESPONSE
DESCRIPTOR.message_types_by_name['AddFactoryProduceRequest'] = _ADDFACTORYPRODUCEREQUEST
DESCRIPTOR.message_types_by_name['AddFactoryProduceResponse'] = _ADDFACTORYPRODUCERESPONSE
DESCRIPTOR.message_types_by_name['ReceiveFactoryProduceRequest'] = _RECEIVEFACTORYPRODUCEREQUEST
DESCRIPTOR.message_types_by_name['ReceiveFactoryProduceResponse'] = _RECEIVEFACTORYPRODUCERESPONSE
DESCRIPTOR.message_types_by_name['AccelerateProduceRequest'] = _ACCELERATEPRODUCEREQUEST
DESCRIPTOR.message_types_by_name['AccelerateProduceResponse'] = _ACCELERATEPRODUCERESPONSE
DESCRIPTOR.message_types_by_name['FactoryCenterUpLevelRequest'] = _FACTORYCENTERUPLEVELREQUEST
DESCRIPTOR.message_types_by_name['FactoryCenterUpLevelResponse'] = _FACTORYCENTERUPLEVELRESPONSE
DESCRIPTOR.message_types_by_name['UseItemAccelerateProduceRequest'] = _USEITEMACCELERATEPRODUCEREQUEST
DESCRIPTOR.message_types_by_name['UseItemAccelerateProduceResponse'] = _USEITEMACCELERATEPRODUCERESPONSE
DESCRIPTOR.message_types_by_name['UseDesignitemUnlockRequest'] = _USEDESIGNITEMUNLOCKREQUEST
DESCRIPTOR.message_types_by_name['UseDesignitemUnlockResponse'] = _USEDESIGNITEMUNLOCKRESPONSE
DESCRIPTOR.enum_types_by_name['FactoryModuleMsgSubCommand'] = _FACTORYMODULEMSGSUBCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProduceRecordMsg = _reflection.GeneratedProtocolMessageType('ProduceRecordMsg', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCERECORDMSG,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ProduceRecordMsg)
  })
_sym_db.RegisterMessage(ProduceRecordMsg)

FactoryMsg = _reflection.GeneratedProtocolMessageType('FactoryMsg', (_message.Message,), {
  'DESCRIPTOR' : _FACTORYMSG,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.FactoryMsg)
  })
_sym_db.RegisterMessage(FactoryMsg)

FactoryProduceMsg = _reflection.GeneratedProtocolMessageType('FactoryProduceMsg', (_message.Message,), {
  'DESCRIPTOR' : _FACTORYPRODUCEMSG,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.FactoryProduceMsg)
  })
_sym_db.RegisterMessage(FactoryProduceMsg)

OpenSlotRequest = _reflection.GeneratedProtocolMessageType('OpenSlotRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENSLOTREQUEST,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.OpenSlotRequest)
  })
_sym_db.RegisterMessage(OpenSlotRequest)

OpenSlotResponse = _reflection.GeneratedProtocolMessageType('OpenSlotResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENSLOTRESPONSE,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.OpenSlotResponse)
  })
_sym_db.RegisterMessage(OpenSlotResponse)

AddFactoryProduceRequest = _reflection.GeneratedProtocolMessageType('AddFactoryProduceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDFACTORYPRODUCEREQUEST,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AddFactoryProduceRequest)
  })
_sym_db.RegisterMessage(AddFactoryProduceRequest)

AddFactoryProduceResponse = _reflection.GeneratedProtocolMessageType('AddFactoryProduceResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDFACTORYPRODUCERESPONSE,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AddFactoryProduceResponse)
  })
_sym_db.RegisterMessage(AddFactoryProduceResponse)

ReceiveFactoryProduceRequest = _reflection.GeneratedProtocolMessageType('ReceiveFactoryProduceRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEFACTORYPRODUCEREQUEST,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ReceiveFactoryProduceRequest)
  })
_sym_db.RegisterMessage(ReceiveFactoryProduceRequest)

ReceiveFactoryProduceResponse = _reflection.GeneratedProtocolMessageType('ReceiveFactoryProduceResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEFACTORYPRODUCERESPONSE,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ReceiveFactoryProduceResponse)
  })
_sym_db.RegisterMessage(ReceiveFactoryProduceResponse)

AccelerateProduceRequest = _reflection.GeneratedProtocolMessageType('AccelerateProduceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCELERATEPRODUCEREQUEST,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AccelerateProduceRequest)
  })
_sym_db.RegisterMessage(AccelerateProduceRequest)

AccelerateProduceResponse = _reflection.GeneratedProtocolMessageType('AccelerateProduceResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCELERATEPRODUCERESPONSE,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AccelerateProduceResponse)
  })
_sym_db.RegisterMessage(AccelerateProduceResponse)

FactoryCenterUpLevelRequest = _reflection.GeneratedProtocolMessageType('FactoryCenterUpLevelRequest', (_message.Message,), {
  'DESCRIPTOR' : _FACTORYCENTERUPLEVELREQUEST,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.FactoryCenterUpLevelRequest)
  })
_sym_db.RegisterMessage(FactoryCenterUpLevelRequest)

FactoryCenterUpLevelResponse = _reflection.GeneratedProtocolMessageType('FactoryCenterUpLevelResponse', (_message.Message,), {
  'DESCRIPTOR' : _FACTORYCENTERUPLEVELRESPONSE,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.FactoryCenterUpLevelResponse)
  })
_sym_db.RegisterMessage(FactoryCenterUpLevelResponse)

UseItemAccelerateProduceRequest = _reflection.GeneratedProtocolMessageType('UseItemAccelerateProduceRequest', (_message.Message,), {
  'DESCRIPTOR' : _USEITEMACCELERATEPRODUCEREQUEST,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.UseItemAccelerateProduceRequest)
  })
_sym_db.RegisterMessage(UseItemAccelerateProduceRequest)

UseItemAccelerateProduceResponse = _reflection.GeneratedProtocolMessageType('UseItemAccelerateProduceResponse', (_message.Message,), {
  'DESCRIPTOR' : _USEITEMACCELERATEPRODUCERESPONSE,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.UseItemAccelerateProduceResponse)
  })
_sym_db.RegisterMessage(UseItemAccelerateProduceResponse)

UseDesignitemUnlockRequest = _reflection.GeneratedProtocolMessageType('UseDesignitemUnlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _USEDESIGNITEMUNLOCKREQUEST,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.UseDesignitemUnlockRequest)
  })
_sym_db.RegisterMessage(UseDesignitemUnlockRequest)

UseDesignitemUnlockResponse = _reflection.GeneratedProtocolMessageType('UseDesignitemUnlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _USEDESIGNITEMUNLOCKRESPONSE,
  '__module__' : 'FactoryModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.UseDesignitemUnlockResponse)
  })
_sym_db.RegisterMessage(UseDesignitemUnlockResponse)


# @@protoc_insertion_point(module_scope)