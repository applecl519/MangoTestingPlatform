# -*- coding: utf-8 -*-
# @Project: MangoServer
# @Description: 
# @Time   : 2023-01-15 10:56
# @Author : 毛鹏
import json
import logging

from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from PyAutoTest.auto_test.auto_ui.models import UiPageStepsDetailed, UiPageSteps
from PyAutoTest.auto_test.auto_ui.views.ui_element import UiElementSerializers
from PyAutoTest.auto_test.auto_ui.views.ui_page_steps import UiPageStepsSerializers
from PyAutoTest.enums.ui_enum import DriveTypeEnum
from PyAutoTest.tools.cache_utils.redis_base import RedisBase
from PyAutoTest.tools.view_utils.model_crud import ModelCRUD
from PyAutoTest.tools.view_utils.response_data import ResponseData
from PyAutoTest.tools.view_utils.response_msg import *

logger = logging.getLogger('ui')


class UiPageStepsDetailedSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = UiPageStepsDetailed
        fields = '__all__'


class UiPageStepsDetailedSerializersC(serializers.ModelSerializer):
    page_step = UiPageStepsSerializers(read_only=True)
    ele_name_a = UiElementSerializers(read_only=True)
    ele_name_b = UiElementSerializers(read_only=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = UiPageStepsDetailed
        fields = '__all__'


class UiPageStepsDetailedCRUD(ModelCRUD):
    """
        haha
    """
    model = UiPageStepsDetailed
    queryset = UiPageStepsDetailed.objects.all().order_by('step_sort')
    serializer_class = UiPageStepsDetailedSerializersC
    serializer = UiPageStepsDetailedSerializers

    def get(self, request: Request):
        page_step_id = request.GET.get('page_step_id')
        _id = request.GET.get('id')
        if page_step_id:
            books = self.model.objects.filter(page_step_id=page_step_id).order_by('step_sort')
        else:
            books = self.model.objects.filter(id=_id).order_by('step_sort')
        data = [self.serializer_class(i).data for i in books]
        return ResponseData.success(RESPONSE_MSG_0016, data)

    def callback(self, _id):
        """
        排序
        @param _id: 步骤id
        @return:
        """
        data = {'id': _id, 'run_flow': '', 'name': ''}
        run = self.model.objects.filter(page_step=_id).order_by('step_sort')
        for i in run:
            data['run_flow'] += '->'
            if i.ele_name_a:
                data['run_flow'] += i.ele_name_a.name
            else:
                data['run_flow'] += i.ope_type if i.ope_type else '无元素操作'
        data['name'] = run[0].page_step.name
        from PyAutoTest.auto_test.auto_ui.views.ui_page_steps import UiPageStepsCRUD
        ui_case = UiPageStepsCRUD()
        res = ui_case.serializer(instance=UiPageSteps.objects.get(pk=_id), data=data)
        if res.is_valid():
            res.save()
        else:
            logger.error(f'保存用例执行顺序报错！，报错结果：{str(res.errors)}')


class UiPageStepsDetailedView(ViewSet):
    model = UiPageStepsDetailed
    serializer_class = UiPageStepsDetailedSerializers

    @action(methods=['get'], detail=False)
    def get_ope_type(self, request: Request):
        page_type = request.query_params.get('page_type')
        redis = RedisBase('default')
        data = []
        if not page_type:
            data.append({
                'value': 'all',
                'label': '请选择操作端',
                'children': json.loads(redis.get('PlaywrightElementOperation'))
            })
            ui_auto = redis.get('UiautomatorApplication')
            if ui_auto:
                data.append({
                    'value': 'all',
                    'label': '请选择操作端',
                    'children': json.loads(ui_auto)
                })
            desktop = redis.get('DESKTOP_OPE')
            if desktop:
                data.append({
                    'value': 'all',
                    'label': '请选择操作端',
                    'children': json.loads(desktop)
                })
            ios = redis.get('IOS_OPE')
            if ios:
                data.append({
                    'value': 'all',
                    'label': '请选择操作端',
                    'children': json.loads(ios)
                })
            return ResponseData.success(RESPONSE_MSG_0017, data)
        if int(page_type) == DriveTypeEnum.WEB.value:
            data = json.loads(redis.get('PlaywrightElementOperation'))
        elif int(page_type) == DriveTypeEnum.ANDROID.value:
            data = json.loads(redis.get('UiautomatorApplication'))
        elif int(page_type) == DriveTypeEnum.DESKTOP.value:
            data = json.loads(redis.get('DESKTOP_OPE'))
        else:
            data = json.loads(redis.get('IOS_OPE'))
        return ResponseData.success(RESPONSE_MSG_0017, data)

    @action(methods=['get'], detail=False)
    def get_ass_type(self, request: Request):
        page_type = request.query_params.get('page_type')
        redis = RedisBase('default')
        if page_type:
            if int(page_type) == DriveTypeEnum.WEB.value:
                data = json.loads(redis.get('PlaywrightAssertion'))
            elif int(page_type) == DriveTypeEnum.ANDROID.value:
                data = json.loads(redis.get('UiautomatorAssertion'))
            elif int(page_type) == DriveTypeEnum.DESKTOP.value:
                data = json.loads(redis.get('DESKTOP_ASS'))
            else:
                data = json.loads(redis.get('IOS_ASS'))
            data.append({'value': 'PublicAssertion',
                         'label': '元素文本',
                         'children': json.loads(redis.get('PublicAssertion'))})
            data.append(json.loads(redis.get('SqlAssertion'))[0])
        else:
            data = json.loads(redis.get('PublicAssertion'))
        return ResponseData.success(RESPONSE_MSG_0018, data)

    @action(methods=['get'], detail=False)
    def get_ass_method(self, request: Request):
        """
        获取断言类型
        @param request:
        @return:
        """
        redis = RedisBase('default')
        data = redis.get('assertion')
        return ResponseData.success(RESPONSE_MSG_0019, json.loads(data))

    @action(methods=['put'], detail=False)
    def put_step_sort(self, request: Request):
        """
        修改排序
        @param request:
        @return:
        """
        page_step_id = None

        for i in request.data.get('step_sort_list'):
            obj = self.model.objects.get(id=i['id'])
            obj.step_sort = i['step_sort']
            page_step_id = obj.page_step.id
            obj.save()
        UiPageStepsDetailedCRUD().callback(page_step_id)
        return ResponseData.success(RESPONSE_MSG_0020, )
