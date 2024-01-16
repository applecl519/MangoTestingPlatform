# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-10-25 17:40
# @Author : 毛鹏
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_ui.models import UiEleResult
from PyAutoTest.auto_test.auto_user.views.project import ProjectSerializers
from PyAutoTest.auto_test.auto_user.views.project_module import ProjectModuleSerializers
from PyAutoTest.auto_test.auto_user.views.user import UserSerializers
from PyAutoTest.tools.view_utils.model_crud import ModelCRUD
from PyAutoTest.tools.view_utils.response_data import ResponseData


class UiEleResultSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = UiEleResult
        fields = '__all__'


class UiEleResultSerializersC(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    project = ProjectSerializers(read_only=True)
    module_name = ProjectModuleSerializers(read_only=True)
    case_people = UserSerializers(read_only=True)

    class Meta:
        model = UiEleResult
        fields = '__all__'


class UiEleResultCRUD(ModelCRUD):
    model = UiEleResult
    queryset = UiEleResult.objects.all()
    serializer_class = UiEleResultSerializersC
    serializer = UiEleResultSerializers


class UiEleResultViews(ViewSet):
    model = UiEleResult
    serializer_class = UiEleResultSerializers

    @action(methods=['get'], detail=False)
    def get_ele_result(self, request: Request):
        ele_result = UiEleResult.objects.filter(test_suite_id=request.query_params.get('test_suite_id'),
                                                page_step_id=request.query_params.get('page_step_id'),
                                                case_id=request.query_params.get('case_id'))
        return ResponseData.success('获取元素结果成功', self.serializer_class(instance=ele_result, many=True).data)
