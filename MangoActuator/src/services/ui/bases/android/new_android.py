# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2024-05-23 15:05
# @Author : 毛鹏

from typing import Optional

import uiautomator2 as us
from adbutils import AdbTimeout

from src.exceptions import *
from src.models.ui_model import EquipmentModel

"""
python -m uiautomator2 init
python -m weditor

"""


class NewAndroid:

    def __init__(self, android_config: EquipmentModel = None):
        self.config = android_config
        self.info: Optional[dict | None] = None
        self.example_dict = []

    def new_android(self):
        if self.config is None:
            raise UiError(*ERROR_MSG_0042)
        android = us.connect(self.config.and_equipment)
        self.example_dict.append({
            'config': self.config,
            'info': self.info,
            'android': android
        })
        self.info = android.info
        try:
            msg = f"设备启动成功！产品名称：{self.info.get('productName')}"
        except RuntimeError:
            raise UiError(*ERROR_MSG_0045, value=(self.config.equipment,))
        except (AdbTimeout, TimeoutError):
            raise UiError(*ERROR_MSG_0047, value=(self.config.equipment,))
        else:
            android.implicitly_wait(10)
            return android

    def close_android(self):
        pass
