# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023/3/23 11:29
# @Author : 毛鹏
from typing import Optional

from playwright.async_api import Locator

from auto_ui.ui_tools.base_model import CaseResult, ElementModel
from auto_ui.web_base import WebDevice
from utils.enum_class.socket_client_ui import ElementExp
from utils.logs.log_control import ERROR
from utils.nuw_logs import NewLog
from utils.test_data_cache import DataCleaning


class WebRun(WebDevice):

    def __init__(self):
        super().__init__()
        self.ele_opt_res = CaseResult()
        self.element: Optional[ElementModel] = None

    async def open_url(self, url: str, case_id):
        """
        记录用例名称，并且打开url
        @param url: url
        @param case_id:
        @return:
        """

        await self.w_wait_for_timeout(1)
        await self.w_goto(url)
        self.ele_opt_res.test_obj_id = url

    async def ele_main(self) -> dict and bool:
        """
        将数据设为变量，并对这个元素进行操作
        @return: 返回是否操作成功
        """

        async def element_exception_handling(e):
            ERROR.logger.error(f'元素操作失败，请检查内容\n'
                               f'报错信息：{e}\n'
                               f'元素对象：{self.element.dict()}\n')
            path = rf'{NewLog.get_log_screenshot()}\{self.element.ele_name_a + DataCleaning.get_deta_hms()}.jpg'
            self.ele_opt_res.picture_path = await self.w_screenshot(path)
            return False

        try:
            if self.element.ope_value:
                self.element.ope_value.locating = await self.__find_ele()
                self.element.ope_value.input_value = await self.__input_value()
                await self.action_element()
                return True
            else:
                await element_exception_handling('ope_value没有值，请检查用例步骤中的元素操作值')
        except Exception as e:
            await element_exception_handling(e)

    async def action_element(self) -> None:
        """
            处理元素的一些事件，包括点击，输入，移动
        @return:
        """
        await getattr(self, self.element.ope_type)(**self.element.ope_value.dict())
        if self.element.ele_sleep:
            await self.w_wait_for_timeout(self.element.ele_sleep)

    async def __find_ele(self) -> Locator:
        """
        基于playwright的元素查找
        @return:
        """
        # 这里要处理iframe
        if self.element.ele_loc:
            # 处理元素并查找
            match self.element.ele_exp:
                case ElementExp.XPATH.value:
                    ele = self.page.locator(f'xpath={self.element.ele_loc}')
                case ElementExp.PLACEHOLDER.value:
                    ele = self.page.get_by_placeholder(self.element.ele_loc)
                case ElementExp.TEXT.value:
                    ele = self.page.get_by_text(self.element.ele_loc, exact=True)
                case ElementExp.CSS.value:
                    ele = self.page.locator(f'css={self.element.ele_loc}')
                case ElementExp.ID.value:
                    ele = self.page.locator(f'id={self.element.ele_loc}')
                case _:
                    ERROR.logger.error(f'没有更多元素定位方式，{self.element.ele_loc}')
                    ele = None
            # 获取元素的文本或元素下标进行断言
            if not ele:
                ERROR.logger.error(f'元素操作失败，请检查内容\n'
                                   f'元素对象：{self.element.dict()}\n')
                await self.w_screenshot(self.element.ele_name_a)
                self.ele_opt_res.existence = await ele.count()
            self.ele_opt_res.existence = await ele.count()
            return ele.nth(0 if self.element.ele_sub is None else self.element.ele_sub)
        else:
            self.ele_opt_res.existence = 0
            ERROR.logger.error(f'元素为空，无法定位，请检查元素表达式是否为空！元素对象：{self.element.dict()}')

    async def __input_value(self):
        """
        输入依赖解决
        @return:
        """
        return DataCleaning.case_input_data(self, self.element.ope_value.input_value,
                                            self.element.ope_value_key)
