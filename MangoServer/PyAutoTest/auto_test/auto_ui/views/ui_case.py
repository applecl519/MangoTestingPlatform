# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description: 
# @Time   : 2023-03-25 18:53
# @Author : 毛鹏
from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_ui.models import UiCase
from PyAutoTest.auto_test.auto_ui.service.ui_test_run import UiTestRun
from PyAutoTest.auto_test.auto_user.views.project import ProjectSerializers
from PyAutoTest.auto_test.auto_user.views.project_module import ProjectModuleSerializers
from PyAutoTest.auto_test.auto_user.views.user import UserSerializers
from PyAutoTest.enums.tools_enum import StatusEnum, ClientNameEnum
from PyAutoTest.exceptions import MangoServerError
from PyAutoTest.tools.view.model_crud import ModelCRUD
from PyAutoTest.tools.view.response_data import ResponseData
from PyAutoTest.tools.view.response_msg import *


class UiCaseSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = UiCase
        fields = '__all__'


class UiCaseSerializersC(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    project = ProjectSerializers(read_only=True)
    module_name = ProjectModuleSerializers(read_only=True)
    case_people = UserSerializers(read_only=True)

    class Meta:
        model = UiCase
        fields = '__all__'

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'project',
            'module_name',
            'case_people')
        return queryset


class UiCaseCRUD(ModelCRUD):
    model = UiCase
    queryset = UiCase.objects.all()
    serializer_class = UiCaseSerializersC
    serializer = UiCaseSerializers


class UiCaseViews(ViewSet):
    model = UiCase
    serializer_class = UiCaseSerializers

    @action(methods=['get'], detail=False)
    def ui_case_run(self, request: Request):
        """
        执行单个用例组
        @param request:
        @return:
        """
        try:
            case_json = UiTestRun(request.user['id'], request.GET.get("testing_environment")).case(
                case_id=int(request.GET.get("case_id")))
        except MangoServerError as error:
            return ResponseData.fail((error.code, error.msg))
        return ResponseData.success(RESPONSE_MSG_0074, case_json.dict(), value=(ClientNameEnum.DRIVER.value,))

    @action(methods=['get'], detail=False)
    def ui_batch_run(self, request: Request):
        """
        批量执行多个用例组
        @param request:
        @return:
        """
        try:
            case_json = UiTestRun(request.user['id'], request.GET.get("testing_environment")).case_batch(
                case_id_list=eval(request.GET.get("case_id_list")))
        except MangoServerError as error:
            return ResponseData.fail((error.code, error.msg))
        return ResponseData.success(RESPONSE_MSG_0074, case_json, value=(ClientNameEnum.DRIVER.value,))

    @action(methods=['POST'], detail=False)
    def cody_case(self, request: Request):
        from PyAutoTest.auto_test.auto_ui.views.ui_case_steps_detailed import UiCaseStepsDetailedSerializers
        from PyAutoTest.auto_test.auto_ui.views.ui_case_steps_detailed import UiCaseStepsDetailed
        case_id = request.data.get('case_id')
        case_obj = UiCase.objects.get(id=case_id)
        case_obj = model_to_dict(case_obj)
        case_id = case_obj['id']
        case_obj['name'] = '(副本)' + case_obj['name']
        case_obj['status'] = StatusEnum.FAIL.value
        del case_obj['id']
        serializer = self.serializer_class(data=case_obj)
        if serializer.is_valid():
            serializer.save()
            ui_case_steps_detailed_obj = UiCaseStepsDetailed.objects.filter(case=case_id)
            for i in ui_case_steps_detailed_obj:
                case_steps_detailed = model_to_dict(i)
                del case_steps_detailed['id']
                case_steps_detailed['case'] = serializer.data['id']
                ui_case_steps_serializer = UiCaseStepsDetailedSerializers(data=case_steps_detailed)
                if ui_case_steps_serializer.is_valid():
                    ui_case_steps_serializer.save()
                else:
                    return ResponseData.fail(RESPONSE_MSG_0075, ui_case_steps_serializer.errors)
            return ResponseData.success(RESPONSE_MSG_0073, serializer.data)
        else:
            return ResponseData.fail(RESPONSE_MSG_0075, serializer.errors)
