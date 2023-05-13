# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-03-25 18:54
# @Author : 毛鹏
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_ui.models import UiConfig
from PyAutoTest.auto_test.auto_user.views.user import UserSerializersC
from PyAutoTest.utils.view_utils.model_crud import ModelCRUD


class UiConfigSerializers(serializers.ModelSerializer):
    user_id = UserSerializersC(read_only=True)

    class Meta:
        model = UiConfig
        fields = '__all__'


class UiConfigSerializersC(serializers.ModelSerializer):
    class Meta:
        model = UiConfig
        fields = '__all__'


class UiConfigCRUD(ModelCRUD):
    model = UiConfig
    queryset = UiConfig.objects.all()
    serializer_class = UiConfigSerializers
    serializer = UiConfigSerializersC


class UiConfigViews(ViewSet):

    @action(methods=['GET'], detail=False)
    def test(self, request):
        pass
