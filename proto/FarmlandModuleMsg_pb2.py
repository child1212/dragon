# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FarmlandModuleMsg.proto
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
  name='FarmlandModuleMsg.proto',
  package='com.common.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x46\x61rmlandModuleMsg.proto\x12\x0e\x63om.common.msg\x1a\x13ItemModuleMsg.proto\"A\n\x0b\x46\x61rmlandMsg\x12\x0f\n\x07plantId\x18\x01 \x02(\t\x12\x11\n\tstartTime\x18\x02 \x01(\x03\x12\x0e\n\x06\x63ropId\x18\x03 \x01(\t\"I\n\x13OpenFarmlandRequest\x12\x0f\n\x07sceneId\x18\x01 \x02(\t\x12\x0f\n\x07plantId\x18\x02 \x02(\t\x12\x10\n\x08plantIds\x18\x03 \x03(\t\"\x16\n\x14OpenFarmlandResponse\"S\n\x0cPlantCropMsg\x12\x0f\n\x07sceneId\x18\x01 \x02(\t\x12\x0f\n\x07plantId\x18\x02 \x02(\t\x12\x0e\n\x06\x63ropId\x18\x03 \x02(\t\x12\x11\n\tstartTime\x18\x04 \x02(\x03\"D\n\x10PlantCropRequest\x12\x30\n\nplantCrops\x18\x01 \x03(\x0b\x32\x1c.com.common.msg.PlantCropMsg\";\n\x11PlantCropResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"2\n\x0eReceiveCropMsg\x12\x0f\n\x07sceneId\x18\x01 \x02(\t\x12\x0f\n\x07plantId\x18\x02 \x02(\t\"J\n\x12ReceiveCropRequest\x12\x34\n\x0creceiveCrops\x18\x01 \x03(\x0b\x32\x1e.com.common.msg.ReceiveCropMsg\"=\n\x13ReceiveCropResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg\"5\n\x11\x41\x63\x63\x65lerateGrowMsg\x12\x0f\n\x07sceneId\x18\x01 \x02(\t\x12\x0f\n\x07plantId\x18\x02 \x02(\t\"S\n\x15\x41\x63\x63\x65lerateGrowRequest\x12:\n\x0f\x61\x63\x63\x65lerateGrows\x18\x01 \x03(\x0b\x32!.com.common.msg.AccelerateGrowMsg\"@\n\x16\x41\x63\x63\x65lerateGrowResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.com.common.msg.ItemMsg*\xc3\x01\n\x1b\x46\x61rmlandModuleMsgSubCommand\x12(\n\"FARMLANDMODULEMSG_SUB_OPENFARMLAND\x10\xb9\xc6\x01\x12%\n\x1f\x46\x41RMLANDMODULEMSG_SUB_PLANTCROP\x10\xba\xc6\x01\x12\'\n!FARMLANDMODULEMSG_SUB_RECEIVECROP\x10\xbb\xc6\x01\x12*\n$FARMLANDMODULEMSG_SUB_ACCELERATEGROW\x10\xbc\xc6\x01'
  ,
  dependencies=[ItemModuleMsg__pb2.DESCRIPTOR,])

_FARMLANDMODULEMSGSUBCOMMAND = _descriptor.EnumDescriptor(
  name='FarmlandModuleMsgSubCommand',
  full_name='com.common.msg.FarmlandModuleMsgSubCommand',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FARMLANDMODULEMSG_SUB_OPENFARMLAND', index=0, number=25401,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FARMLANDMODULEMSG_SUB_PLANTCROP', index=1, number=25402,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FARMLANDMODULEMSG_SUB_RECEIVECROP', index=2, number=25403,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FARMLANDMODULEMSG_SUB_ACCELERATEGROW', index=3, number=25404,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=844,
  serialized_end=1039,
)
_sym_db.RegisterEnumDescriptor(_FARMLANDMODULEMSGSUBCOMMAND)

FarmlandModuleMsgSubCommand = enum_type_wrapper.EnumTypeWrapper(_FARMLANDMODULEMSGSUBCOMMAND)
FARMLANDMODULEMSG_SUB_OPENFARMLAND = 25401
FARMLANDMODULEMSG_SUB_PLANTCROP = 25402
FARMLANDMODULEMSG_SUB_RECEIVECROP = 25403
FARMLANDMODULEMSG_SUB_ACCELERATEGROW = 25404



_FARMLANDMSG = _descriptor.Descriptor(
  name='FarmlandMsg',
  full_name='com.common.msg.FarmlandMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='plantId', full_name='com.common.msg.FarmlandMsg.plantId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='com.common.msg.FarmlandMsg.startTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cropId', full_name='com.common.msg.FarmlandMsg.cropId', index=2,
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
  serialized_start=64,
  serialized_end=129,
)


_OPENFARMLANDREQUEST = _descriptor.Descriptor(
  name='OpenFarmlandRequest',
  full_name='com.common.msg.OpenFarmlandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sceneId', full_name='com.common.msg.OpenFarmlandRequest.sceneId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plantId', full_name='com.common.msg.OpenFarmlandRequest.plantId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plantIds', full_name='com.common.msg.OpenFarmlandRequest.plantIds', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=131,
  serialized_end=204,
)


_OPENFARMLANDRESPONSE = _descriptor.Descriptor(
  name='OpenFarmlandResponse',
  full_name='com.common.msg.OpenFarmlandResponse',
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
  serialized_start=206,
  serialized_end=228,
)


_PLANTCROPMSG = _descriptor.Descriptor(
  name='PlantCropMsg',
  full_name='com.common.msg.PlantCropMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sceneId', full_name='com.common.msg.PlantCropMsg.sceneId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plantId', full_name='com.common.msg.PlantCropMsg.plantId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cropId', full_name='com.common.msg.PlantCropMsg.cropId', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='com.common.msg.PlantCropMsg.startTime', index=3,
      number=4, type=3, cpp_type=2, label=2,
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
  serialized_start=230,
  serialized_end=313,
)


_PLANTCROPREQUEST = _descriptor.Descriptor(
  name='PlantCropRequest',
  full_name='com.common.msg.PlantCropRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='plantCrops', full_name='com.common.msg.PlantCropRequest.plantCrops', index=0,
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
  serialized_start=315,
  serialized_end=383,
)


_PLANTCROPRESPONSE = _descriptor.Descriptor(
  name='PlantCropResponse',
  full_name='com.common.msg.PlantCropResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='com.common.msg.PlantCropResponse.items', index=0,
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
  serialized_start=385,
  serialized_end=444,
)


_RECEIVECROPMSG = _descriptor.Descriptor(
  name='ReceiveCropMsg',
  full_name='com.common.msg.ReceiveCropMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sceneId', full_name='com.common.msg.ReceiveCropMsg.sceneId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plantId', full_name='com.common.msg.ReceiveCropMsg.plantId', index=1,
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
  serialized_start=446,
  serialized_end=496,
)


_RECEIVECROPREQUEST = _descriptor.Descriptor(
  name='ReceiveCropRequest',
  full_name='com.common.msg.ReceiveCropRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='receiveCrops', full_name='com.common.msg.ReceiveCropRequest.receiveCrops', index=0,
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
  serialized_start=498,
  serialized_end=572,
)


_RECEIVECROPRESPONSE = _descriptor.Descriptor(
  name='ReceiveCropResponse',
  full_name='com.common.msg.ReceiveCropResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='com.common.msg.ReceiveCropResponse.items', index=0,
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
  serialized_start=574,
  serialized_end=635,
)


_ACCELERATEGROWMSG = _descriptor.Descriptor(
  name='AccelerateGrowMsg',
  full_name='com.common.msg.AccelerateGrowMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sceneId', full_name='com.common.msg.AccelerateGrowMsg.sceneId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plantId', full_name='com.common.msg.AccelerateGrowMsg.plantId', index=1,
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
  serialized_start=637,
  serialized_end=690,
)


_ACCELERATEGROWREQUEST = _descriptor.Descriptor(
  name='AccelerateGrowRequest',
  full_name='com.common.msg.AccelerateGrowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accelerateGrows', full_name='com.common.msg.AccelerateGrowRequest.accelerateGrows', index=0,
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
  serialized_start=692,
  serialized_end=775,
)


_ACCELERATEGROWRESPONSE = _descriptor.Descriptor(
  name='AccelerateGrowResponse',
  full_name='com.common.msg.AccelerateGrowResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='com.common.msg.AccelerateGrowResponse.items', index=0,
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
  serialized_start=777,
  serialized_end=841,
)

_PLANTCROPREQUEST.fields_by_name['plantCrops'].message_type = _PLANTCROPMSG
_PLANTCROPRESPONSE.fields_by_name['items'].message_type = ItemModuleMsg__pb2._ITEMMSG
_RECEIVECROPREQUEST.fields_by_name['receiveCrops'].message_type = _RECEIVECROPMSG
_RECEIVECROPRESPONSE.fields_by_name['items'].message_type = ItemModuleMsg__pb2._ITEMMSG
_ACCELERATEGROWREQUEST.fields_by_name['accelerateGrows'].message_type = _ACCELERATEGROWMSG
_ACCELERATEGROWRESPONSE.fields_by_name['items'].message_type = ItemModuleMsg__pb2._ITEMMSG
DESCRIPTOR.message_types_by_name['FarmlandMsg'] = _FARMLANDMSG
DESCRIPTOR.message_types_by_name['OpenFarmlandRequest'] = _OPENFARMLANDREQUEST
DESCRIPTOR.message_types_by_name['OpenFarmlandResponse'] = _OPENFARMLANDRESPONSE
DESCRIPTOR.message_types_by_name['PlantCropMsg'] = _PLANTCROPMSG
DESCRIPTOR.message_types_by_name['PlantCropRequest'] = _PLANTCROPREQUEST
DESCRIPTOR.message_types_by_name['PlantCropResponse'] = _PLANTCROPRESPONSE
DESCRIPTOR.message_types_by_name['ReceiveCropMsg'] = _RECEIVECROPMSG
DESCRIPTOR.message_types_by_name['ReceiveCropRequest'] = _RECEIVECROPREQUEST
DESCRIPTOR.message_types_by_name['ReceiveCropResponse'] = _RECEIVECROPRESPONSE
DESCRIPTOR.message_types_by_name['AccelerateGrowMsg'] = _ACCELERATEGROWMSG
DESCRIPTOR.message_types_by_name['AccelerateGrowRequest'] = _ACCELERATEGROWREQUEST
DESCRIPTOR.message_types_by_name['AccelerateGrowResponse'] = _ACCELERATEGROWRESPONSE
DESCRIPTOR.enum_types_by_name['FarmlandModuleMsgSubCommand'] = _FARMLANDMODULEMSGSUBCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FarmlandMsg = _reflection.GeneratedProtocolMessageType('FarmlandMsg', (_message.Message,), {
  'DESCRIPTOR' : _FARMLANDMSG,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.FarmlandMsg)
  })
_sym_db.RegisterMessage(FarmlandMsg)

OpenFarmlandRequest = _reflection.GeneratedProtocolMessageType('OpenFarmlandRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENFARMLANDREQUEST,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.OpenFarmlandRequest)
  })
_sym_db.RegisterMessage(OpenFarmlandRequest)

OpenFarmlandResponse = _reflection.GeneratedProtocolMessageType('OpenFarmlandResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENFARMLANDRESPONSE,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.OpenFarmlandResponse)
  })
_sym_db.RegisterMessage(OpenFarmlandResponse)

PlantCropMsg = _reflection.GeneratedProtocolMessageType('PlantCropMsg', (_message.Message,), {
  'DESCRIPTOR' : _PLANTCROPMSG,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.PlantCropMsg)
  })
_sym_db.RegisterMessage(PlantCropMsg)

PlantCropRequest = _reflection.GeneratedProtocolMessageType('PlantCropRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLANTCROPREQUEST,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.PlantCropRequest)
  })
_sym_db.RegisterMessage(PlantCropRequest)

PlantCropResponse = _reflection.GeneratedProtocolMessageType('PlantCropResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLANTCROPRESPONSE,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.PlantCropResponse)
  })
_sym_db.RegisterMessage(PlantCropResponse)

ReceiveCropMsg = _reflection.GeneratedProtocolMessageType('ReceiveCropMsg', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVECROPMSG,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ReceiveCropMsg)
  })
_sym_db.RegisterMessage(ReceiveCropMsg)

ReceiveCropRequest = _reflection.GeneratedProtocolMessageType('ReceiveCropRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVECROPREQUEST,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ReceiveCropRequest)
  })
_sym_db.RegisterMessage(ReceiveCropRequest)

ReceiveCropResponse = _reflection.GeneratedProtocolMessageType('ReceiveCropResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVECROPRESPONSE,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.ReceiveCropResponse)
  })
_sym_db.RegisterMessage(ReceiveCropResponse)

AccelerateGrowMsg = _reflection.GeneratedProtocolMessageType('AccelerateGrowMsg', (_message.Message,), {
  'DESCRIPTOR' : _ACCELERATEGROWMSG,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AccelerateGrowMsg)
  })
_sym_db.RegisterMessage(AccelerateGrowMsg)

AccelerateGrowRequest = _reflection.GeneratedProtocolMessageType('AccelerateGrowRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCELERATEGROWREQUEST,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AccelerateGrowRequest)
  })
_sym_db.RegisterMessage(AccelerateGrowRequest)

AccelerateGrowResponse = _reflection.GeneratedProtocolMessageType('AccelerateGrowResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCELERATEGROWRESPONSE,
  '__module__' : 'FarmlandModuleMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.common.msg.AccelerateGrowResponse)
  })
_sym_db.RegisterMessage(AccelerateGrowResponse)


# @@protoc_insertion_point(module_scope)
