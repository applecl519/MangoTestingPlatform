# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description: 
# @Time   : 2023-06-04 12:24
# @Author : 毛鹏
from PyAutoTest.auto_test.auto_api.models import ApiPublic, ApiCase
from PyAutoTest.auto_test.auto_system.consumers import ChatConsumer
from PyAutoTest.auto_test.auto_system.models import TestObject
from PyAutoTest.auto_test.auto_system.service.socket_link.actuator_api_enum import ApiEnum
from PyAutoTest.enums.tools_enum import ClientTypeEnum, StatusEnum
from PyAutoTest.models.socket_model import SocketDataModel, QueueModel
from PyAutoTest.models.socket_model.api_model import PublicModel, ApiCaseGroupModel, RequestModel
from PyAutoTest.settings import DRIVER


class RunApiSend:
    def __init__(self, username: str, test_obj: int = None):
        self.username = username
        if test_obj:
            self.host = TestObject.objects.get(id=int(test_obj)).value

    def public_args_data(self) -> list[PublicModel]:
        """
        处理公共数据
        """
        objects_filter = ApiPublic.objects.filter(status=StatusEnum.SUCCESS.value, type=0)
        public_args_list = []
        for obj in objects_filter:
            public_args_model = PublicModel(
                end=obj.end,
                public_type=obj.public_type,
                name=obj.name,
                key=obj.key,
                value=obj.value
            )
            public_args_list.append(public_args_model)
        self.__socket_send(public_args_list, ApiEnum.REFRESH_CACHE.value)
        return public_args_list

    def request_data(self, case_id: int, send: bool = False) -> RequestModel:
        """
        处理一个用力请求数据
        """
        case = ApiCase.objects.get(id=case_id)
        case_json = RequestModel(case_id=case.id,
                                 case_name=case.name,
                                 url=self.host + case.url,
                                 method=case.method,
                                 header=case.header,
                                 body_type=case.body_type,
                                 body=case.body)
        if self.username and send:
            self.__socket_send(case_json, ApiEnum.A_DEBUG_CASE.value)
            return case_json
        return case_json

    def batch_requests_data(self, case_list: list) -> list[RequestModel]:
        """
        批量请求
        """
        case_json = [self.request_data(i)[0] for i in case_list]
        self.__socket_send(case_json, ApiEnum.A_BATCH_CASE.value)
        return case_json

    def group_case_data(self, group_name, case_list: list) -> ApiCaseGroupModel:
        """
        用例组数据
        """
        case_json = ApiCaseGroupModel(
            group_name=group_name,
            case_group_list=[self.request_data(i)[0] for i in case_list])
        self.__socket_send(case_json, ApiEnum.A_GROUP_CASE.value)
        return case_json

    def __socket_send(self, case_json, func_name: str) -> None:
        """
        发送给第三方工具方法
        @param case_json: 需要发送的json数据
        @param func_name: 需要执行的函数
        @return:
        """
        data = QueueModel(func_name=func_name, func_args=case_json)
        ChatConsumer.active_send(SocketDataModel(
            code=200,
            msg=f'{DRIVER}：收到用例数据，准备开始执行自动化任务！',
            user=self.username,
            is_notice=ClientTypeEnum.ACTUATOR.value,
            data=data,
        ))
