# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023/5/10 11:34
# @Author : 毛鹏

from socket_client.socket_consume.consume_ui import ConsumeUI


class ConsumeDistribute(ConsumeUI):

    # @staticmethod
    def start_up(self, func, *args, **kwargs):
        getattr(self, func)(*args, **kwargs)