# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023-04-25 22:33
# @Author : 毛鹏

from auto_ui.web_base.playwright_obj.playwright_base import PlaywrightBase


class PlaywrightOperationBrowser(PlaywrightBase):
    """浏览器操作类"""

    async def wait_for_timeout(self, sleep: int):
        await self.page.wait_for_timeout(sleep)

    async def goto(self, url: str):
        """
        打开url
        @param url: 打开的指定url
        @return:
        """
        await self.page.goto(url, timeout=50000)

    async def screenshot(self, path: str, full_page=True):
        """整个页面截图"""
        await self.page.screenshot(path=path, full_page=full_page)

    async def ele_screenshot(self, selector: str, path: str):
        """元素截图"""
        await self.page.locator(selector).screenshot(path=path)
