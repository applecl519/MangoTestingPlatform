# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2023-02-16 20:58
# @Author : 毛鹏

from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_system.models import Database
from PyAutoTest.auto_test.auto_user.views.project_product import ProjectProductSerializersC
from PyAutoTest.enums.tools_enum import StatusEnum
from PyAutoTest.tools.decorator.error_response import error_response
from PyAutoTest.tools.view.model_crud import ModelCRUD
from PyAutoTest.tools.view.response_data import ResponseData
from PyAutoTest.tools.view.response_msg import *


class DatabaseSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Database
        fields = '__all__'


class DatabaseSerializersC(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    project_product = ProjectProductSerializersC(read_only=True)

    class Meta:
        model = Database
        fields = '__all__'

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'project_product',
        )
        return queryset


class DatabaseCRUD(ModelCRUD):
    model = Database
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializersC
    serializer = DatabaseSerializers


class DatabaseViews(ViewSet):
    model = Database
    serializer_class = DatabaseSerializers

    @action(methods=['put'], detail=False)
    @error_response('system')
    def put_status(self, request: Request):
        """
        修改启停用
        :param request:
        :return:
        """
        if request.data.get('status') == StatusEnum.SUCCESS.value:
            obj = self.model.objects.filter(environment=request.data.get('environment')).values('status')
            if any(item['status'] == 1 for item in obj):
                # if self.model.objects \
                #         .filter(project_id=obj.project_id, type=obj.type, status=StatusEnum.SUCCESS.value) \
                #         and request.data.get('status') == StatusEnum.SUCCESS.value:
                return ResponseData.fail(RESPONSE_MSG_0119, )
        obj = self.model.objects.get(id=request.data.get('id'))
        obj.status = request.data.get('status')
        obj.save()
        return ResponseData.success(RESPONSE_MSG_0047, )