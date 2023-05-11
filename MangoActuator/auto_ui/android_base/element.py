from uiautomator2 import UiObject

from auto_ui.android_base.android_base import AndroidBase, ElementNotFoundError, ElementNotDisappearError
from utils.logs.log_control import ERROR, INFO


class UiautomatorElementOperation(AndroidBase):
    """元素操作类"""

    def click(self, element: UiObject):
        """单击"""
        element.click()

    def double_click(self, element: UiObject):
        """双击"""
        element.center()

    def click_coord(self, x, y):
        """单击坐标"""
        self.android.click(x, y)

    def double_click_coord(self, x, y):
        """双击坐标"""
        self.android.double_click(x, y)

    def long_click_coord(self, element: UiObject, time_):
        """长按元素"""
        element.long_click(duration=time_)

    def input_text(self, element: UiObject, text):
        """输入"""
        element.set_text(text)

    def clear_text(self, element: UiObject):
        """清空输入框"""
        element.clear_text()

    # def scroll_to_ele(self, element: UiObject, direction):
    #     """滑动到元素出现"""
    #     if "xpath" in element:
    #         XPath(self.android).scroll_to(element, direction)
    #     elif direction == "up":
    #         self.android(scrollable=True).forward.to(element)
    #     elif direction == "down":
    #         self.android(scrollable=True).backward.to(element)
    #     elif direction == "left":
    #         self.android(scrollable=True).horiz.forward.to(element)
    #     else:
    #         self.android(scrollable=True).horiz.backward.to(element)

    def pinch_in(self, element: UiObject):
        """缩小"""
        element.pinch_in()

    def pinch_out(self, element: UiObject):
        """放大"""
        element.pinch_out()

    def wait(self, element: UiObject, time_):
        """等待元素出现"""
        try:
            if element.wait(timeout=time_):
                INFO.logger.info("成功等待元素出现")
            else:
                ERROR.logger.error("等待元素出现失败 元素不存在")
                raise ElementNotFoundError("element not exists")
        except ElementNotFoundError as e:
            ERROR.logger.error(f"元素可能不存在，元素：{element}，报错信息：{e}")
            return False
        except Exception as e:
            ERROR.logger.error(f"无法等待元素出现，元素：{element}，报错信息：{e}")
            return False

    def wait_gone(self, element: UiObject, time_):
        """等待元素消失"""
        try:
            res = element.wait_gone(timeout=time_)
            if res:
                INFO.logger.info("成功等待元素消失")
            else:
                ERROR.logger.error("等待元素消失失败 元素仍存在")
                raise ElementNotDisappearError("element exists")
        except ElementNotDisappearError as e:
            ERROR.logger.error(f"元素可能无法消失，元素：{element}，报错信息：{e}")
            return False
        except Exception as e:
            ERROR.logger.error(f"无法等待元素消失，元素：{element}，报错信息：{e}")
            return False

    def drag_to_ele(self, start_element: UiObject, end_element: UiObject):
        """拖动A元素到达B元素上"""
        try:
            start_element.drag_to(end_element)
            INFO.logger.info("成功拖动到元素")
        except Exception as e:
            ERROR.logger.error(f"无法拖动到元素，拖拽元素：{start_element}，到达元素：{end_element}，报错信息：{e}")
            return False

    def drag_to_coord(self, element: UiObject, x, y):
        """拖动元素到坐标上"""
        element.drag_to(x, y)

    def swipe_ele(self, element: UiObject, direction):
        """元素内滑动"""
        element.swipe(direction)

    def get_ele_text(self, element: UiObject):
        """提取元素文本"""
        return element.get_text()

    def get_ele_center(self, element: UiObject):
        """提取元素位置"""
        x, y = element.center()
        return x, y

    def get_ele_x(self, element: UiObject):
        """提取元素X Y坐标"""
        x, y = element.center()
        return x, y
