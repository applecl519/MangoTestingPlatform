# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-10-12 18:14
# @Author : 毛鹏
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_user.models import ProjectModule
from PyAutoTest.auto_test.auto_user.views.project import ProjectSerializers
from PyAutoTest.tools.response_data import ResponseData
from PyAutoTest.tools.view_utils.model_crud import ModelCRUD


class ProjectModuleSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = ProjectModule
        fields = '__all__'


class ProjectModuleSerializersC(serializers.ModelSerializer):
    project = ProjectSerializers(read_only=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = ProjectModule
        fields = '__all__'


class ProjectModuleCRUD(ModelCRUD):
    model = ProjectModule
    queryset = ProjectModule.objects.all()
    serializer_class = ProjectModuleSerializersC
    # post专用序列化器
    serializer = ProjectModuleSerializers


class ProjectModuleViews(ViewSet):
    model = ProjectModule
    serializer_class = ProjectModuleSerializers

    @action(methods=['GET'], detail=False)
    def get_module_name_all(self, request: Request):
        res = self.model.objects.values_list('id', 'name').filter(project=request.query_params.get('project_id'))
        data = [{'key': _id, 'title': name} for _id, name in res]
        return ResponseData.success('获取数据成功', data)
