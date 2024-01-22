# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description: 项目表
# @Time   : 2023-03-03 12:21
# @Author : 毛鹏
import logging

from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_user.service.files_crud import FilesCRUD
from PyAutoTest.enums.tools_enum import StatusEnum
from PyAutoTest.tools.view_utils.model_crud import ModelCRUD
from PyAutoTest.tools.view_utils.response_data import ResponseData
from ..models import Project

logger = logging.getLogger('user')


class ProjectSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'  # 全部进行序列化


class ProjectCRUD(ModelCRUD):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    serializer = ProjectSerializers

    def post(self, request: Request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            FilesCRUD(serializer.data.get('id')).add_project()
            return ResponseData.success('新增一条记录成功', serializer.data)
        else:
            logger.error(f'执行保存时报错，请检查！数据：{request.data}, 报错信息：{str(serializer.errors)}')
            return ResponseData.fail(str(serializer.errors))

    def delete(self, request: Request):
        if '[' in request.query_params.get('id'):
            for i in eval(request.query_params.get('id')):
                self.model.objects.get(pk=i).delete()
                FilesCRUD(i).delete_project()
        else:
            # 一条删
            self.model.objects.get(id=request.query_params.get('id')).delete()
            self.asynchronous_callback(request)
            FilesCRUD(request.query_params.get('id')).delete_project()
        return ResponseData.success('删除项目成功', )


class ProjectViews(ViewSet):
    model = Project
    serializer_class = ProjectSerializers

    @action(methods=['get'], detail=False)
    def get_all_items(self, request: Request):
        items = Project.objects.filter(status=StatusEnum.SUCCESS.value)
        data = [{'title': i.name, 'key': i.pk} for i in items]
        return ResponseData.success('获取所有项目名称成功', data)
