# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2024-11-25 15:04
# @Author : 毛鹏
from django.db import connection

from PyAutoTest.auto_test.auto_system.models import TestSuite, TestSuiteDetails
from PyAutoTest.auto_test.auto_system.service.notic_tools import NoticeMain
from PyAutoTest.enums.tools_enum import TaskEnum, StatusEnum, ClientTypeEnum
from PyAutoTest.models.socket_model import SocketDataModel
from PyAutoTest.models.system_model import TestSuiteDetailsResultModel
from PyAutoTest.tools.decorator.retry import orm_retry


class UpdateTestSuite:
    @classmethod
    @orm_retry('update_case')
    def update_test_suite(cls, test_suite_id: int, status: int):
        connection.ensure_connection()
        test_suite = TestSuite.objects.get(id=test_suite_id)
        test_suite.status = status
        test_suite.save()

    @classmethod
    @orm_retry('update_test_suite')
    def update_test_suite_details(cls, data: TestSuiteDetailsResultModel):
        connection.ensure_connection()
        test_suite_detail = TestSuiteDetails.objects.get(id=data.id)
        test_suite_detail.result_data = data.result_data.model_dump()
        test_suite_detail.status = data.status
        test_suite_detail.error_message = data.error_message
        test_suite_detail.save()
        test_suite_detail_list = TestSuiteDetails.objects.filter(test_suite=data.test_suite,
                                                                 status__in=[TaskEnum.STAY_BEGIN.value,
                                                                             TaskEnum.PROCEED.value])
        if not test_suite_detail_list.exists():
            test_suite = TestSuiteDetails.objects.filter(test_suite=data.test_suite, status=StatusEnum.FAIL.value)
            if not test_suite.exists():
                cls.update_test_suite(data.test_suite, StatusEnum.SUCCESS.value)
            else:
                cls.update_test_suite(data.test_suite, StatusEnum.FAIL.value)
            cls.send_test_result(data.test_suite, data.error_message)

    @classmethod
    @orm_retry('send_test_result')
    def send_test_result(cls, test_suite_id: int, msg):
        connection.ensure_connection()
        test_suite = TestSuite.objects.get(id=test_suite_id)
        if test_suite.is_notice == StatusEnum.SUCCESS.value:
            NoticeMain.notice_main(test_suite.test_env, test_suite_id)
        from PyAutoTest.auto_test.auto_system.consumers import ChatConsumer
        ChatConsumer.active_send(SocketDataModel(
            code=200 if test_suite.status else 300,
            msg=msg,
            user=test_suite.user.username,
            is_notice=ClientTypeEnum.WEB.value,
        ))
