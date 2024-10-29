# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2024-07-15 17:48
# @Author : 毛鹏

import jwt
from django.conf import settings
from django.core.handlers.asgi import ASGIRequest
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from PyAutoTest.settings import IS_DELETE


class IsDeleteMiddleWare(MiddlewareMixin):

    def process_request(self, request: ASGIRequest):
        if not IS_DELETE:
            token = request.META.get('HTTP_AUTHORIZATION')
            if token:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
                if payload.get('username') not in ['admin', ]:
                    if request.method == 'DELETE':
                        return JsonResponse({
                            "code": 300,
                            "msg": "演示环境非管理员权限禁止删除，只能执行测试任务",
                            "data": None
                        }, status=200)
                    # elif request.method == 'POST':
                    #     return JsonResponse({
                    #         "code": 300,
                    #         "msg": "演示环境非管理员权限禁止新增，只能执行测试任务",
                    #         "data": None
                    #     }, status=200)
                    elif request.method == 'PUT' and payload.get('username') != 'wfq123456':
                        if request.path not in ['/user/environment',
                                                '/user/project/put',
                                                '/ui/config/put/status']:
                            return JsonResponse({
                                "code": 300,
                                "msg": "演示环境非管理员权限禁止修改，只能执行测试任务",
                                "data": None
                            }, status=200)

    def process_response(self, request, response):
        return response
