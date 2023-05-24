# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023/5/10 11:34
# @Author : 毛鹏
from utils.decorator.singleton import singleton
from utils.socket_client.socket_consume.consume_ui import ConsumeUI


@singleton
class ConsumeDistribute(ConsumeUI):

    async def start_up(self, func, *args, **kwargs):
        await getattr(self, func)(*args, **kwargs)