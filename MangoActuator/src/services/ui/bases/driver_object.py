# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description:
# @Time   : 2024-04-24 10:43
# @Author : 毛鹏

from src.services.ui.bases.android.new_android import NewAndroid
from src.services.ui.bases.web.new_browser import NewBrowser


class DriverObject(NewBrowser, NewAndroid):
    pass
