# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import morai_actor_pb2 as morai__actor__pb2
import morai_type_pb2 as morai__type__pb2


class MoraiActorStub(object):
    """Actor 관련 서비스
    차량, 보행자, 장애물
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetEgo = channel.unary_unary(
                '/morai_sim_api.MoraiActor/SetEgo',
                request_serializer=morai__actor__pb2.EgoCtrlCmd.SerializeToString,
                response_deserializer=morai__type__pb2.Result.FromString,
                )
        self.SpawnActor = channel.unary_unary(
                '/morai_sim_api.MoraiActor/SpawnActor',
                request_serializer=morai__actor__pb2.SpawnActorParams.SerializeToString,
                response_deserializer=morai__actor__pb2.ActorResponses.FromString,
                )
        self.GetActorStateStream = channel.unary_stream(
                '/morai_sim_api.MoraiActor/GetActorStateStream',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=morai__actor__pb2.ActorStates.FromString,
                )
        self.GetActorState = channel.unary_unary(
                '/morai_sim_api.MoraiActor/GetActorState',
                request_serializer=morai__actor__pb2.ActorInfo.SerializeToString,
                response_deserializer=morai__actor__pb2.ActorState.FromString,
                )
        self.GetActorNetworkSetting = channel.unary_unary(
                '/morai_sim_api.MoraiActor/GetActorNetworkSetting',
                request_serializer=morai__actor__pb2.ActorInfo.SerializeToString,
                response_deserializer=morai__actor__pb2.NetworkProtocolSetting.FromString,
                )
        self.DestroyActor = channel.unary_unary(
                '/morai_sim_api.MoraiActor/DestroyActor',
                request_serializer=morai__actor__pb2.ActorInfo.SerializeToString,
                response_deserializer=morai__type__pb2.Result.FromString,
                )
        self.DestroyAllActors = channel.unary_unary(
                '/morai_sim_api.MoraiActor/DestroyAllActors',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=morai__type__pb2.Result.FromString,
                )
        self.WalkerControl = channel.unary_unary(
                '/morai_sim_api.MoraiActor/WalkerControl',
                request_serializer=morai__actor__pb2.WalkerCtrlCmd.SerializeToString,
                response_deserializer=morai__type__pb2.Result.FromString,
                )
        self.VehicleControl = channel.unary_unary(
                '/morai_sim_api.MoraiActor/VehicleControl',
                request_serializer=morai__actor__pb2.VehicleCtrlCmd.SerializeToString,
                response_deserializer=morai__type__pb2.Result.FromString,
                )
        self.SetVehicleRoute = channel.unary_unary(
                '/morai_sim_api.MoraiActor/SetVehicleRoute',
                request_serializer=morai__actor__pb2.VehicleRoute.SerializeToString,
                response_deserializer=morai__type__pb2.Result.FromString,
                )
        self.SetVehicleDestination = channel.unary_unary(
                '/morai_sim_api.MoraiActor/SetVehicleDestination',
                request_serializer=morai__actor__pb2.VehicleDestination.SerializeToString,
                response_deserializer=morai__type__pb2.Result.FromString,
                )
        self.SetActorProperty = channel.unary_unary(
                '/morai_sim_api.MoraiActor/SetActorProperty',
                request_serializer=morai__actor__pb2.ActorProperty.SerializeToString,
                response_deserializer=morai__type__pb2.Result.FromString,
                )
        self.GetTrafficLightInfoByLink = channel.unary_unary(
                '/morai_sim_api.MoraiActor/GetTrafficLightInfoByLink',
                request_serializer=morai__type__pb2.LinkInfo.SerializeToString,
                response_deserializer=morai__actor__pb2.TLInfo.FromString,
                )
        self.GetTrafficLightInfoByUid = channel.unary_unary(
                '/morai_sim_api.MoraiActor/GetTrafficLightInfoByUid',
                request_serializer=morai__type__pb2.StringValue.SerializeToString,
                response_deserializer=morai__actor__pb2.TLInfo.FromString,
                )
        self.GetIntscnTLInfo = channel.unary_unary(
                '/morai_sim_api.MoraiActor/GetIntscnTLInfo',
                request_serializer=morai__type__pb2.StringValue.SerializeToString,
                response_deserializer=morai__actor__pb2.TLInfoList.FromString,
                )
        self.SetTrafficLightState = channel.unary_unary(
                '/morai_sim_api.MoraiActor/SetTrafficLightState',
                request_serializer=morai__actor__pb2.TLStateParamList.SerializeToString,
                response_deserializer=morai__actor__pb2.ActorResponses.FromString,
                )
        self.SetIntersectionState = channel.unary_unary(
                '/morai_sim_api.MoraiActor/SetIntersectionState',
                request_serializer=morai__actor__pb2.IntscnStateParamList.SerializeToString,
                response_deserializer=morai__actor__pb2.ActorResponses.FromString,
                )
        self.SetIntersectionSchedule = channel.unary_unary(
                '/morai_sim_api.MoraiActor/SetIntersectionSchedule',
                request_serializer=morai__actor__pb2.IntscnScheduleParamList.SerializeToString,
                response_deserializer=morai__actor__pb2.ActorResponses.FromString,
                )
        self.SetDisturbance = channel.unary_unary(
                '/morai_sim_api.MoraiActor/SetDisturbance',
                request_serializer=morai__actor__pb2.DisturbanceVehicleList.SerializeToString,
                response_deserializer=morai__actor__pb2.ActorResponses.FromString,
                )
        self.CreateSpawnPoint = channel.unary_unary(
                '/morai_sim_api.MoraiActor/CreateSpawnPoint',
                request_serializer=morai__actor__pb2.CreateSpawnPointList.SerializeToString,
                response_deserializer=morai__actor__pb2.ActorResponses.FromString,
                )
        self.EnableSpawnPoint = channel.unary_unary(
                '/morai_sim_api.MoraiActor/EnableSpawnPoint',
                request_serializer=morai__actor__pb2.EnableSpawnPointList.SerializeToString,
                response_deserializer=morai__actor__pb2.ActorResponses.FromString,
                )
        self.SetSpawnPoint = channel.unary_unary(
                '/morai_sim_api.MoraiActor/SetSpawnPoint',
                request_serializer=morai__actor__pb2.SetSpawnPointList.SerializeToString,
                response_deserializer=morai__actor__pb2.ActorResponses.FromString,
                )
        self.GetVehicleSpec = channel.unary_unary(
                '/morai_sim_api.MoraiActor/GetVehicleSpec',
                request_serializer=morai__actor__pb2.VehicleSpecParam.SerializeToString,
                response_deserializer=morai__actor__pb2.VehicleSpec.FromString,
                )


class MoraiActorServicer(object):
    """Actor 관련 서비스
    차량, 보행자, 장애물
    """

    def SetEgo(self, request, context):
        """Ego 설정
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SpawnActor(self, request, context):
        """Actor 생성
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActorStateStream(self, request, context):
        """Actor 상태 조회
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActorState(self, request, context):
        """Actor 상태 조회
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActorNetworkSetting(self, request, context):
        """Network 설정 조회
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroyActor(self, request, context):
        """선택한 Actor 제거
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroyAllActors(self, request, context):
        """모든 Actor 제거
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WalkerControl(self, request, context):
        """Walker 제어
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VehicleControl(self, request, context):
        """차량 제어
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetVehicleRoute(self, request, context):
        """차량 경로 설정 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetVehicleDestination(self, request, context):
        """차량 목적지 설정
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetActorProperty(self, request, context):
        """Actor 속성 설정
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrafficLightInfoByLink(self, request, context):
        """Link ID, TL ID, IntscnID 통해 해당 위치의 Traffic Light id, state 획득
        매개 변수 : Link ID, TL ID, IntscnID
        리턴 : 성공/실패(bool), Traffic Light ID, Traffic Light state(color)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrafficLightInfoByUid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIntscnTLInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTrafficLightState(self, request, context):
        """신호등의 state(light color) 변경
        매개 변수 : list of (tl ID, tl color, (bool)isImpulse : 1회성 세팅 or 세팅 유지)
        리턴 : List of (성공/실패, tl ID, tl ID)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetIntersectionState(self, request, context):
        """교차로 state 변경
        매개 변수 : list of (intersection ID, state index)
        리턴 : List of (성공/실패, tl ID, tl ID)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetIntersectionSchedule(self, request, context):
        """기능 : 교차로 schedule 변경
        매개 변수 : list of (intersection ID, list of 차량 신호등 state, list of yellow duration, list of 보행자 신호등 state)
        리턴 : List of (성공/실패, tl ID, tl ID)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDisturbance(self, request, context):
        """비정상적 차량 주행(ex. 졸음운전) 설정
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSpawnPoint(self, request, context):
        """Spawn Point 생성
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableSpawnPoint(self, request, context):
        """Spawn Point Enable/Disable
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSpawnPoint(self, request, context):
        """Set Spawn Point
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVehicleSpec(self, request, context):
        """차량 제원 정보 획득
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MoraiActorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetEgo': grpc.unary_unary_rpc_method_handler(
                    servicer.SetEgo,
                    request_deserializer=morai__actor__pb2.EgoCtrlCmd.FromString,
                    response_serializer=morai__type__pb2.Result.SerializeToString,
            ),
            'SpawnActor': grpc.unary_unary_rpc_method_handler(
                    servicer.SpawnActor,
                    request_deserializer=morai__actor__pb2.SpawnActorParams.FromString,
                    response_serializer=morai__actor__pb2.ActorResponses.SerializeToString,
            ),
            'GetActorStateStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetActorStateStream,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=morai__actor__pb2.ActorStates.SerializeToString,
            ),
            'GetActorState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActorState,
                    request_deserializer=morai__actor__pb2.ActorInfo.FromString,
                    response_serializer=morai__actor__pb2.ActorState.SerializeToString,
            ),
            'GetActorNetworkSetting': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActorNetworkSetting,
                    request_deserializer=morai__actor__pb2.ActorInfo.FromString,
                    response_serializer=morai__actor__pb2.NetworkProtocolSetting.SerializeToString,
            ),
            'DestroyActor': grpc.unary_unary_rpc_method_handler(
                    servicer.DestroyActor,
                    request_deserializer=morai__actor__pb2.ActorInfo.FromString,
                    response_serializer=morai__type__pb2.Result.SerializeToString,
            ),
            'DestroyAllActors': grpc.unary_unary_rpc_method_handler(
                    servicer.DestroyAllActors,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=morai__type__pb2.Result.SerializeToString,
            ),
            'WalkerControl': grpc.unary_unary_rpc_method_handler(
                    servicer.WalkerControl,
                    request_deserializer=morai__actor__pb2.WalkerCtrlCmd.FromString,
                    response_serializer=morai__type__pb2.Result.SerializeToString,
            ),
            'VehicleControl': grpc.unary_unary_rpc_method_handler(
                    servicer.VehicleControl,
                    request_deserializer=morai__actor__pb2.VehicleCtrlCmd.FromString,
                    response_serializer=morai__type__pb2.Result.SerializeToString,
            ),
            'SetVehicleRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.SetVehicleRoute,
                    request_deserializer=morai__actor__pb2.VehicleRoute.FromString,
                    response_serializer=morai__type__pb2.Result.SerializeToString,
            ),
            'SetVehicleDestination': grpc.unary_unary_rpc_method_handler(
                    servicer.SetVehicleDestination,
                    request_deserializer=morai__actor__pb2.VehicleDestination.FromString,
                    response_serializer=morai__type__pb2.Result.SerializeToString,
            ),
            'SetActorProperty': grpc.unary_unary_rpc_method_handler(
                    servicer.SetActorProperty,
                    request_deserializer=morai__actor__pb2.ActorProperty.FromString,
                    response_serializer=morai__type__pb2.Result.SerializeToString,
            ),
            'GetTrafficLightInfoByLink': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrafficLightInfoByLink,
                    request_deserializer=morai__type__pb2.LinkInfo.FromString,
                    response_serializer=morai__actor__pb2.TLInfo.SerializeToString,
            ),
            'GetTrafficLightInfoByUid': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrafficLightInfoByUid,
                    request_deserializer=morai__type__pb2.StringValue.FromString,
                    response_serializer=morai__actor__pb2.TLInfo.SerializeToString,
            ),
            'GetIntscnTLInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIntscnTLInfo,
                    request_deserializer=morai__type__pb2.StringValue.FromString,
                    response_serializer=morai__actor__pb2.TLInfoList.SerializeToString,
            ),
            'SetTrafficLightState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTrafficLightState,
                    request_deserializer=morai__actor__pb2.TLStateParamList.FromString,
                    response_serializer=morai__actor__pb2.ActorResponses.SerializeToString,
            ),
            'SetIntersectionState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetIntersectionState,
                    request_deserializer=morai__actor__pb2.IntscnStateParamList.FromString,
                    response_serializer=morai__actor__pb2.ActorResponses.SerializeToString,
            ),
            'SetIntersectionSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.SetIntersectionSchedule,
                    request_deserializer=morai__actor__pb2.IntscnScheduleParamList.FromString,
                    response_serializer=morai__actor__pb2.ActorResponses.SerializeToString,
            ),
            'SetDisturbance': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDisturbance,
                    request_deserializer=morai__actor__pb2.DisturbanceVehicleList.FromString,
                    response_serializer=morai__actor__pb2.ActorResponses.SerializeToString,
            ),
            'CreateSpawnPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSpawnPoint,
                    request_deserializer=morai__actor__pb2.CreateSpawnPointList.FromString,
                    response_serializer=morai__actor__pb2.ActorResponses.SerializeToString,
            ),
            'EnableSpawnPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableSpawnPoint,
                    request_deserializer=morai__actor__pb2.EnableSpawnPointList.FromString,
                    response_serializer=morai__actor__pb2.ActorResponses.SerializeToString,
            ),
            'SetSpawnPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSpawnPoint,
                    request_deserializer=morai__actor__pb2.SetSpawnPointList.FromString,
                    response_serializer=morai__actor__pb2.ActorResponses.SerializeToString,
            ),
            'GetVehicleSpec': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVehicleSpec,
                    request_deserializer=morai__actor__pb2.VehicleSpecParam.FromString,
                    response_serializer=morai__actor__pb2.VehicleSpec.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'morai_sim_api.MoraiActor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MoraiActor(object):
    """Actor 관련 서비스
    차량, 보행자, 장애물
    """

    @staticmethod
    def SetEgo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/SetEgo',
            morai__actor__pb2.EgoCtrlCmd.SerializeToString,
            morai__type__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SpawnActor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/SpawnActor',
            morai__actor__pb2.SpawnActorParams.SerializeToString,
            morai__actor__pb2.ActorResponses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActorStateStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/morai_sim_api.MoraiActor/GetActorStateStream',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            morai__actor__pb2.ActorStates.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActorState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/GetActorState',
            morai__actor__pb2.ActorInfo.SerializeToString,
            morai__actor__pb2.ActorState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActorNetworkSetting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/GetActorNetworkSetting',
            morai__actor__pb2.ActorInfo.SerializeToString,
            morai__actor__pb2.NetworkProtocolSetting.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DestroyActor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/DestroyActor',
            morai__actor__pb2.ActorInfo.SerializeToString,
            morai__type__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DestroyAllActors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/DestroyAllActors',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            morai__type__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WalkerControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/WalkerControl',
            morai__actor__pb2.WalkerCtrlCmd.SerializeToString,
            morai__type__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VehicleControl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/VehicleControl',
            morai__actor__pb2.VehicleCtrlCmd.SerializeToString,
            morai__type__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetVehicleRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/SetVehicleRoute',
            morai__actor__pb2.VehicleRoute.SerializeToString,
            morai__type__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetVehicleDestination(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/SetVehicleDestination',
            morai__actor__pb2.VehicleDestination.SerializeToString,
            morai__type__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetActorProperty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/SetActorProperty',
            morai__actor__pb2.ActorProperty.SerializeToString,
            morai__type__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrafficLightInfoByLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/GetTrafficLightInfoByLink',
            morai__type__pb2.LinkInfo.SerializeToString,
            morai__actor__pb2.TLInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrafficLightInfoByUid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/GetTrafficLightInfoByUid',
            morai__type__pb2.StringValue.SerializeToString,
            morai__actor__pb2.TLInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIntscnTLInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/GetIntscnTLInfo',
            morai__type__pb2.StringValue.SerializeToString,
            morai__actor__pb2.TLInfoList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetTrafficLightState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/SetTrafficLightState',
            morai__actor__pb2.TLStateParamList.SerializeToString,
            morai__actor__pb2.ActorResponses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetIntersectionState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/SetIntersectionState',
            morai__actor__pb2.IntscnStateParamList.SerializeToString,
            morai__actor__pb2.ActorResponses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetIntersectionSchedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/SetIntersectionSchedule',
            morai__actor__pb2.IntscnScheduleParamList.SerializeToString,
            morai__actor__pb2.ActorResponses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDisturbance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/SetDisturbance',
            morai__actor__pb2.DisturbanceVehicleList.SerializeToString,
            morai__actor__pb2.ActorResponses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSpawnPoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/CreateSpawnPoint',
            morai__actor__pb2.CreateSpawnPointList.SerializeToString,
            morai__actor__pb2.ActorResponses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableSpawnPoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/EnableSpawnPoint',
            morai__actor__pb2.EnableSpawnPointList.SerializeToString,
            morai__actor__pb2.ActorResponses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSpawnPoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/SetSpawnPoint',
            morai__actor__pb2.SetSpawnPointList.SerializeToString,
            morai__actor__pb2.ActorResponses.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVehicleSpec(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/morai_sim_api.MoraiActor/GetVehicleSpec',
            morai__actor__pb2.VehicleSpecParam.SerializeToString,
            morai__actor__pb2.VehicleSpec.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
