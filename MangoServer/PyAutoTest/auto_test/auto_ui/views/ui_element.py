# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description:
# @Time   : 2023-01-15 22:06
# @Author : 毛鹏
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_ui.models import UiElement
from PyAutoTest.auto_test.auto_ui.views.ui_page import UiPageSerializers
from PyAutoTest.auto_test.auto_user.views.project import ProjectSerializers
from PyAutoTest.enum_class.ui_enum import ElementExp
from PyAutoTest.utils.view_utils.model_crud import ModelCRUD
from PyAutoTest.utils.view_utils.view_tools import enum_list


class UiElementSerializers(serializers.ModelSerializer):
    team = ProjectSerializers()
    page = UiPageSerializers()

    class Meta:
        model = UiElement
        fields = '__all__'


class UiElementSerializersC(serializers.ModelSerializer):
    class Meta:
        model = UiElement
        fields = '__all__'  # 全部进行序列化


class UiElementCRUD(ModelCRUD):
    model = UiElement
    queryset = UiElement.objects.all()
    serializer_class = UiElementSerializers
    serializer = UiElementSerializersC

    def get(self, request):
        try:
            books = self.model.objects.filter(page_id=request.query_params.get('page_id')).order_by('id')
            return Response({
                "code": 200,
                "msg": "获取数据成功~",
                "data": self.get_serializer_class()(instance=books, many=True).data,
                'totalSize': len(books)
            })
        except:
            return Response({
                'code': 300,
                'msg': '您查询的数据不存在~',
                'data': ''
            })


class UiElementViews(ViewSet):

    @action(methods=['get'], detail=False)
    def get_ele_name(self, request):
        """
        获取
        :param request:
        :return:
        """
        res = UiElement.objects.filter(page=request.query_params.get('name')).values_list('id', 'name')
        data = [{'key': _id, 'title': name} for _id, name in res]
        return Response({
            'code': 200,
            'msg': '获取数据成功~',
            'data': data
        })

    @action(methods=['get'], detail=False)
    def get_exp_type(self, request):
        """
        获取操作类型
        :param request:
        :return:
        """
        return Response({
            'code': 200,
            'msg': '获取数据成功~',
            'data': enum_list(ElementExp)
        })
