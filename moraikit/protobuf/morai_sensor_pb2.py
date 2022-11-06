# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: morai_sensor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import morai_type_pb2 as morai__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12morai_sensor.proto\x12\rmorai_sim_api\x1a\x10morai_type.proto\"\xa6\x01\n\rSensorSetting\x12\x11\n\tunique_id\x18\x01 \x01(\t\x12.\n\x0bsensor_type\x18\x02 \x01(\x0e\x32\x19.morai_sim_api.SensorType\x12(\n\x08position\x18\x03 \x01(\x0b\x32\x16.morai_sim_api.Vector3\x12(\n\x08rotation\x18\x04 \x01(\x0b\x32\x16.morai_sim_api.Vector3\"C\n\x11SensorSettingList\x12.\n\x08req_list\x18\x01 \x03(\x0b\x32\x1c.morai_sim_api.SensorSetting\"4\n\x0cRemoveSensor\x12\x11\n\tunique_id\x18\x01 \x01(\t\x12\x11\n\tsensor_id\x18\x02 \x01(\t\"A\n\x10RemoveSensorList\x12-\n\x08req_list\x18\x01 \x03(\x0b\x32\x1b.morai_sim_api.RemoveSensor\"G\n\x0eSensorResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x11\n\ttarget_id\x18\x02 \x01(\t\x12\x11\n\tsensor_id\x18\x03 \x01(\t\"E\n\x12SensorResponseList\x12/\n\x08res_list\x18\x01 \x03(\x0b\x32\x1d.morai_sim_api.SensorResponse\"J\n\x11GTCylinderSetting\x12\x10\n\x08segments\x18\x01 \x01(\x05\x12\x14\n\x0cvertical_fov\x18\x02 \x01(\x02\x12\r\n\x05range\x18\x03 \x01(\x02\"\x89\x01\n\rGTConeSetting\x12\x10\n\x08segments\x18\x01 \x01(\x05\x12\x14\n\x0cvertical_fov\x18\x02 \x01(\x02\x12\x16\n\x0ehorizontal_fov\x18\x03 \x01(\x02\x12\x11\n\trange_min\x18\x04 \x01(\x02\x12\x11\n\trange_max\x18\x05 \x01(\x02\x12\x12\n\nresolution\x18\x07 \x01(\x05\"\xf4\x01\n\x0fGTSensorSetting\x12.\n\nshape_type\x18\x01 \x01(\x0e\x32\x1a.morai_sim_api.GTShapeType\x12:\n\x10\x63ylinder_setting\x18\x02 \x01(\x0b\x32 .morai_sim_api.GTCylinderSetting\x12\x32\n\x0c\x63one_setting\x18\x03 \x01(\x0b\x32\x1c.morai_sim_api.GTConeSetting\x12.\n\x06\x66ilter\x18\x04 \x03(\x0e\x32\x1e.morai_sim_api.ObstacleObjType\x12\x11\n\tmax_count\x18\x05 \x01(\x05\"\x83\x01\n\x14SetGroundTruthSensor\x12\x11\n\tunique_id\x18\x01 \x01(\t\x12\x11\n\tsensor_id\x18\x02 \x01(\t\x12\x32\n\ngt_setting\x18\x03 \x01(\x0b\x32\x1e.morai_sim_api.GTSensorSetting\x12\x11\n\tviz_range\x18\x04 \x01(\x08\"Q\n\x18SetGroundTruthSensorList\x12\x35\n\x08req_list\x18\x01 \x03(\x0b\x32#.morai_sim_api.SetGroundTruthSensor\"4\n\x0cTargetSensor\x12\x11\n\tunique_id\x18\x01 \x01(\t\x12\x11\n\tsensor_id\x18\x02 \x01(\t\"A\n\x10TargetSensorList\x12-\n\x08req_list\x18\x01 \x03(\x0b\x32\x1b.morai_sim_api.TargetSensor\"\xf6\x01\n\x0cObjectStatus\x12\x11\n\tunique_id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07heading\x18\x04 \x01(\x01\x12(\n\x08position\x18\x05 \x01(\x0b\x32\x16.morai_sim_api.Vector3\x12,\n\x0c\x61\x63\x63\x65leration\x18\x06 \x01(\x0b\x32\x16.morai_sim_api.Vector3\x12(\n\x08velocity\x18\x07 \x01(\x0b\x32\x16.morai_sim_api.Vector3\x12$\n\x04size\x18\x08 \x01(\x0b\x32\x16.morai_sim_api.Vector3\"I\n\x0bGroundTruth\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12)\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x1b.morai_sim_api.ObjectStatus\"?\n\x0fGroundTruthList\x12,\n\x08res_list\x18\x01 \x03(\x0b\x32\x1a.morai_sim_api.GroundTruth\"V\n\nSaveSensor\x12\x1b\n\x13is_custom_file_name\x18\x01 \x01(\x08\x12\x19\n\x11\x63ustrom_file_name\x18\x02 \x01(\t\x12\x10\n\x08\x66ile_dir\x18\x03 \x01(\t*\xfb\x01\n\nSensorType\x12\x14\n\x10SENSOR_TYPE_NONE\x10\x00\x12\x16\n\x12SENSOR_TYPE_CAMERA\x10\x01\x12\x17\n\x13SENSOR_TYPE_LIDAR3D\x10\x02\x12\x17\n\x13SENSOR_TYPE_LIDAR2D\x10\x03\x12\x13\n\x0fSENSOR_TYPE_GPS\x10\x04\x12\x13\n\x0fSENSOR_TYPE_IMU\x10\x05\x12\x15\n\x11SENSOR_TYPE_RADAR\x10\x06\x12\x1a\n\x16SENSOR_TYPE_ULTRASONIC\x10\x07\x12\x1b\n\x17SENSOR_TYPE_GROUNDTRUTH\x10\x08\x12\x13\n\x0fSENSOR_TYPE_END\x10\t*]\n\x0bGTShapeType\x12\x12\n\x0eGT_SHAPE_BEGIN\x10\x00\x12\x15\n\x11GT_SHAPE_Cylinder\x10\x01\x12\x11\n\rGT_SHAPE_Cone\x10\x02\x12\x10\n\x0cGT_SHAPE_END\x10\x03*\xb8\x03\n\x0fObstacleObjType\x12\x14\n\x10OBSTACL_OBJ_NONE\x10\x00\x12\x17\n\x13OBSTACL_OBJ_VEHICLE\x10\x01\x12\x1a\n\x16OBSTACL_OBJ_PEDESTRIAN\x10\x02\x12\x1a\n\x16OBSTACL_OBJ_EGOVEHICLE\x10\x03\x12\x18\n\x14OBSTACL_OBJ_OBSTACLE\x10\x04\x12\x1a\n\x16OBSTACL_OBJ_SPAWNPOINT\x10\x05\x12\x1c\n\x18OBSTACL_OBJ_MOVINGOBJECT\x10\x06\x12\x1d\n\x19OBSTACL_OBJ_EXTRAOBSTACLE\x10\x07\x12\x1f\n\x1bOBSTACL_OBJ_SSAFYSPAWNPOINT\x10\x08\x12 \n\x1cOBSTACL_OBJ_DESTINATIONPOINT\x10\t\x12\x1d\n\x19OBSTACL_OBJ_STOPOVERPOINT\x10\n\x12\x1d\n\x19OBSTACL_OBJ_PEDSPAWNPOINT\x10\x0b\x12\x1a\n\x16OBSTACL_OBJ_SHADEDAREA\x10\x0c\x12\x19\n\x15OBSTACL_OBJ_MAPOBJECT\x10\r\x12\x13\n\x0fOBSTACL_OBJ_MAX\x10\x0e\x32\xf7\x03\n\x0bMoraiSensor\x12R\n\tAddSensor\x12 .morai_sim_api.SensorSettingList\x1a!.morai_sim_api.SensorResponseList\"\x00\x12T\n\x0cRemoveSensor\x12\x1f.morai_sim_api.RemoveSensorList\x1a!.morai_sim_api.SensorResponseList\"\x00\x12X\n\x14SetGroundTruthSensor\x12\'.morai_sim_api.SetGroundTruthSensorList\x1a\x15.morai_sim_api.Result\"\x00\x12W\n\x12GetGroundTruthData\x12\x1f.morai_sim_api.TargetSensorList\x1a\x1e.morai_sim_api.GroundTruthList\"\x00\x12\x44\n\x0eSaveSensorData\x12\x19.morai_sim_api.SaveSensor\x1a\x15.morai_sim_api.Result\"\x00\x12\x45\n\x0eLoadSensorFile\x12\x1a.morai_sim_api.StringValue\x1a\x15.morai_sim_api.Result\"\x00\x42&H\x01\xaa\x02!CoreLib.Grpc.Protobuf.MoraiSimAPIb\x06proto3')

_SENSORTYPE = DESCRIPTOR.enum_types_by_name['SensorType']
SensorType = enum_type_wrapper.EnumTypeWrapper(_SENSORTYPE)
_GTSHAPETYPE = DESCRIPTOR.enum_types_by_name['GTShapeType']
GTShapeType = enum_type_wrapper.EnumTypeWrapper(_GTSHAPETYPE)
_OBSTACLEOBJTYPE = DESCRIPTOR.enum_types_by_name['ObstacleObjType']
ObstacleObjType = enum_type_wrapper.EnumTypeWrapper(_OBSTACLEOBJTYPE)
SENSOR_TYPE_NONE = 0
SENSOR_TYPE_CAMERA = 1
SENSOR_TYPE_LIDAR3D = 2
SENSOR_TYPE_LIDAR2D = 3
SENSOR_TYPE_GPS = 4
SENSOR_TYPE_IMU = 5
SENSOR_TYPE_RADAR = 6
SENSOR_TYPE_ULTRASONIC = 7
SENSOR_TYPE_GROUNDTRUTH = 8
SENSOR_TYPE_END = 9
GT_SHAPE_BEGIN = 0
GT_SHAPE_Cylinder = 1
GT_SHAPE_Cone = 2
GT_SHAPE_END = 3
OBSTACL_OBJ_NONE = 0
OBSTACL_OBJ_VEHICLE = 1
OBSTACL_OBJ_PEDESTRIAN = 2
OBSTACL_OBJ_EGOVEHICLE = 3
OBSTACL_OBJ_OBSTACLE = 4
OBSTACL_OBJ_SPAWNPOINT = 5
OBSTACL_OBJ_MOVINGOBJECT = 6
OBSTACL_OBJ_EXTRAOBSTACLE = 7
OBSTACL_OBJ_SSAFYSPAWNPOINT = 8
OBSTACL_OBJ_DESTINATIONPOINT = 9
OBSTACL_OBJ_STOPOVERPOINT = 10
OBSTACL_OBJ_PEDSPAWNPOINT = 11
OBSTACL_OBJ_SHADEDAREA = 12
OBSTACL_OBJ_MAPOBJECT = 13
OBSTACL_OBJ_MAX = 14


_SENSORSETTING = DESCRIPTOR.message_types_by_name['SensorSetting']
_SENSORSETTINGLIST = DESCRIPTOR.message_types_by_name['SensorSettingList']
_REMOVESENSOR = DESCRIPTOR.message_types_by_name['RemoveSensor']
_REMOVESENSORLIST = DESCRIPTOR.message_types_by_name['RemoveSensorList']
_SENSORRESPONSE = DESCRIPTOR.message_types_by_name['SensorResponse']
_SENSORRESPONSELIST = DESCRIPTOR.message_types_by_name['SensorResponseList']
_GTCYLINDERSETTING = DESCRIPTOR.message_types_by_name['GTCylinderSetting']
_GTCONESETTING = DESCRIPTOR.message_types_by_name['GTConeSetting']
_GTSENSORSETTING = DESCRIPTOR.message_types_by_name['GTSensorSetting']
_SETGROUNDTRUTHSENSOR = DESCRIPTOR.message_types_by_name['SetGroundTruthSensor']
_SETGROUNDTRUTHSENSORLIST = DESCRIPTOR.message_types_by_name['SetGroundTruthSensorList']
_TARGETSENSOR = DESCRIPTOR.message_types_by_name['TargetSensor']
_TARGETSENSORLIST = DESCRIPTOR.message_types_by_name['TargetSensorList']
_OBJECTSTATUS = DESCRIPTOR.message_types_by_name['ObjectStatus']
_GROUNDTRUTH = DESCRIPTOR.message_types_by_name['GroundTruth']
_GROUNDTRUTHLIST = DESCRIPTOR.message_types_by_name['GroundTruthList']
_SAVESENSOR = DESCRIPTOR.message_types_by_name['SaveSensor']
SensorSetting = _reflection.GeneratedProtocolMessageType('SensorSetting', (_message.Message,), {
  'DESCRIPTOR' : _SENSORSETTING,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.SensorSetting)
  })
_sym_db.RegisterMessage(SensorSetting)

SensorSettingList = _reflection.GeneratedProtocolMessageType('SensorSettingList', (_message.Message,), {
  'DESCRIPTOR' : _SENSORSETTINGLIST,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.SensorSettingList)
  })
_sym_db.RegisterMessage(SensorSettingList)

RemoveSensor = _reflection.GeneratedProtocolMessageType('RemoveSensor', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESENSOR,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.RemoveSensor)
  })
_sym_db.RegisterMessage(RemoveSensor)

RemoveSensorList = _reflection.GeneratedProtocolMessageType('RemoveSensorList', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESENSORLIST,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.RemoveSensorList)
  })
_sym_db.RegisterMessage(RemoveSensorList)

SensorResponse = _reflection.GeneratedProtocolMessageType('SensorResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENSORRESPONSE,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.SensorResponse)
  })
_sym_db.RegisterMessage(SensorResponse)

SensorResponseList = _reflection.GeneratedProtocolMessageType('SensorResponseList', (_message.Message,), {
  'DESCRIPTOR' : _SENSORRESPONSELIST,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.SensorResponseList)
  })
_sym_db.RegisterMessage(SensorResponseList)

GTCylinderSetting = _reflection.GeneratedProtocolMessageType('GTCylinderSetting', (_message.Message,), {
  'DESCRIPTOR' : _GTCYLINDERSETTING,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.GTCylinderSetting)
  })
_sym_db.RegisterMessage(GTCylinderSetting)

GTConeSetting = _reflection.GeneratedProtocolMessageType('GTConeSetting', (_message.Message,), {
  'DESCRIPTOR' : _GTCONESETTING,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.GTConeSetting)
  })
_sym_db.RegisterMessage(GTConeSetting)

GTSensorSetting = _reflection.GeneratedProtocolMessageType('GTSensorSetting', (_message.Message,), {
  'DESCRIPTOR' : _GTSENSORSETTING,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.GTSensorSetting)
  })
_sym_db.RegisterMessage(GTSensorSetting)

SetGroundTruthSensor = _reflection.GeneratedProtocolMessageType('SetGroundTruthSensor', (_message.Message,), {
  'DESCRIPTOR' : _SETGROUNDTRUTHSENSOR,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.SetGroundTruthSensor)
  })
_sym_db.RegisterMessage(SetGroundTruthSensor)

SetGroundTruthSensorList = _reflection.GeneratedProtocolMessageType('SetGroundTruthSensorList', (_message.Message,), {
  'DESCRIPTOR' : _SETGROUNDTRUTHSENSORLIST,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.SetGroundTruthSensorList)
  })
_sym_db.RegisterMessage(SetGroundTruthSensorList)

TargetSensor = _reflection.GeneratedProtocolMessageType('TargetSensor', (_message.Message,), {
  'DESCRIPTOR' : _TARGETSENSOR,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.TargetSensor)
  })
_sym_db.RegisterMessage(TargetSensor)

TargetSensorList = _reflection.GeneratedProtocolMessageType('TargetSensorList', (_message.Message,), {
  'DESCRIPTOR' : _TARGETSENSORLIST,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.TargetSensorList)
  })
_sym_db.RegisterMessage(TargetSensorList)

ObjectStatus = _reflection.GeneratedProtocolMessageType('ObjectStatus', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTATUS,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.ObjectStatus)
  })
_sym_db.RegisterMessage(ObjectStatus)

GroundTruth = _reflection.GeneratedProtocolMessageType('GroundTruth', (_message.Message,), {
  'DESCRIPTOR' : _GROUNDTRUTH,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.GroundTruth)
  })
_sym_db.RegisterMessage(GroundTruth)

GroundTruthList = _reflection.GeneratedProtocolMessageType('GroundTruthList', (_message.Message,), {
  'DESCRIPTOR' : _GROUNDTRUTHLIST,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.GroundTruthList)
  })
_sym_db.RegisterMessage(GroundTruthList)

SaveSensor = _reflection.GeneratedProtocolMessageType('SaveSensor', (_message.Message,), {
  'DESCRIPTOR' : _SAVESENSOR,
  '__module__' : 'morai_sensor_pb2'
  # @@protoc_insertion_point(class_scope:morai_sim_api.SaveSensor)
  })
_sym_db.RegisterMessage(SaveSensor)

_MORAISENSOR = DESCRIPTOR.services_by_name['MoraiSensor']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\001\252\002!CoreLib.Grpc.Protobuf.MoraiSimAPI'
  _SENSORTYPE._serialized_start=1837
  _SENSORTYPE._serialized_end=2088
  _GTSHAPETYPE._serialized_start=2090
  _GTSHAPETYPE._serialized_end=2183
  _OBSTACLEOBJTYPE._serialized_start=2186
  _OBSTACLEOBJTYPE._serialized_end=2626
  _SENSORSETTING._serialized_start=56
  _SENSORSETTING._serialized_end=222
  _SENSORSETTINGLIST._serialized_start=224
  _SENSORSETTINGLIST._serialized_end=291
  _REMOVESENSOR._serialized_start=293
  _REMOVESENSOR._serialized_end=345
  _REMOVESENSORLIST._serialized_start=347
  _REMOVESENSORLIST._serialized_end=412
  _SENSORRESPONSE._serialized_start=414
  _SENSORRESPONSE._serialized_end=485
  _SENSORRESPONSELIST._serialized_start=487
  _SENSORRESPONSELIST._serialized_end=556
  _GTCYLINDERSETTING._serialized_start=558
  _GTCYLINDERSETTING._serialized_end=632
  _GTCONESETTING._serialized_start=635
  _GTCONESETTING._serialized_end=772
  _GTSENSORSETTING._serialized_start=775
  _GTSENSORSETTING._serialized_end=1019
  _SETGROUNDTRUTHSENSOR._serialized_start=1022
  _SETGROUNDTRUTHSENSOR._serialized_end=1153
  _SETGROUNDTRUTHSENSORLIST._serialized_start=1155
  _SETGROUNDTRUTHSENSORLIST._serialized_end=1236
  _TARGETSENSOR._serialized_start=1238
  _TARGETSENSOR._serialized_end=1290
  _TARGETSENSORLIST._serialized_start=1292
  _TARGETSENSORLIST._serialized_end=1357
  _OBJECTSTATUS._serialized_start=1360
  _OBJECTSTATUS._serialized_end=1606
  _GROUNDTRUTH._serialized_start=1608
  _GROUNDTRUTH._serialized_end=1681
  _GROUNDTRUTHLIST._serialized_start=1683
  _GROUNDTRUTHLIST._serialized_end=1746
  _SAVESENSOR._serialized_start=1748
  _SAVESENSOR._serialized_end=1834
  _MORAISENSOR._serialized_start=2629
  _MORAISENSOR._serialized_end=3132
# @@protoc_insertion_point(module_scope)
