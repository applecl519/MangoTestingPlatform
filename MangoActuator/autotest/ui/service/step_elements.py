# -*- coding: utf-8 -*-
# @Project: MangoActuator
# @Description: 
# @Time   : 2023/5/4 14:34
# @Author : 毛鹏
from urllib.parse import urlparse, urljoin

from playwright._impl._api_types import Error

from autotest.ui.base_tools import ElementMain
from enums.tools_enum import StatusEnum
from enums.ui_enum import DriveTypeEnum
from exceptions import MangoActuatorError
from exceptions.ui_exception import UiCacheDataIsNullError, BrowserObjectClosed
from models.socket_model.ui_model import PageStepsResultModel, PageStepsModel, WEBConfigModel
from service_conn.http_conn.http_api import HttpApi
from settings import settings
from tools import InitPath
from tools.data_processor import RandomTimeData
from tools.decorator.memory import async_memory
from tools.desktop.signal_send import SignalSend
from tools.log_collector import log
from tools.message.error_msg import ERROR_MSG_0025, ERROR_MSG_0010, ERROR_MSG_0053


class StepElements(ElementMain):
    page_step_model: PageStepsModel = None
    page_step_result_model: PageStepsResultModel = None

    async def steps_init(self, page_step_model: PageStepsModel):
        self.page_step_model = page_step_model
        self.page_step_result_model = PageStepsResultModel(
            test_suite_id=self.test_suite_id,
            case_id=self.case_id,
            case_step_details_id=self.page_step_model.case_step_details_id,
            page_step_id=page_step_model.id,
            page_step_name=page_step_model.name,
            status=StatusEnum.FAIL.value,
            element_result_list=[],
            error_message=None)

        self.page_step_id = page_step_model.id
        self.case_step_details_id = page_step_model.case_step_details_id
        if self.page_step_model.environment_config:
            self.set_mysql(self.page_step_model.environment_config)

    @async_memory
    async def steps_main(self) -> PageStepsResultModel:
        SignalSend.notice_signal_c(f'正在准备执行步骤：{self.page_step_model.name}')
        for element_model in self.page_step_model.element_list:
            element_data = None
            if not self.is_step:
                for _element_data in self.page_step_model.case_data:
                    if _element_data.page_step_details_id == element_model.id:
                        element_data = _element_data.page_step_details_data
                if element_data is None:
                    raise UiCacheDataIsNullError(*ERROR_MSG_0025)
            # 执行用例
            try:
                await self.element_setup(element_model, element_data, self.page_step_model.type)
                await self.element_main()
            except MangoActuatorError as error:
                await self.__error(error)
                return self.page_step_result_model
            except Error as error:
                if error.message == "Target page, context or browser has been closed":
                    await self.setup()
                    self.element_test_result.error_message = error.message
                    self.page_step_result_model.error_message = error.message
                    self.page_step_result_model.element_result_list.append(self.element_test_result)
                    raise BrowserObjectClosed(*ERROR_MSG_0010)
                else:
                    raise error
            else:
                self.page_step_result_model.element_result_list.append(self.element_test_result)
        self.page_step_result_model.status = StatusEnum.SUCCESS.value
        SignalSend.notice_signal_c(f'步骤：{self.page_step_model.name} 执行完成！')
        return self.page_step_result_model

    @async_memory
    async def driver_init(self):
        match self.page_step_model.type:
            case DriveTypeEnum.WEB.value:
                await self.web_init()
            case DriveTypeEnum.ANDROID.value:
                self.__android_init()
            case DriveTypeEnum.IOS.value:
                self.__ios_init()
            case DriveTypeEnum.DESKTOP.value:
                self.__desktop_init()
            case _:
                log.error('自动化类型不存在，请联系管理员检查！')

    async def web_init(self, data: WEBConfigModel | None = None):
        if self.page:
            return
        if data:
            self.driver_object.web_config = data
            self.context, self.page = await self.driver_object.new_web_page()
        else:
            self.driver_object.web_config = self.page_step_model.equipment_config
            self.context, self.page = await self.driver_object.new_web_page()
            test_object_value = urljoin(self.page_step_model.environment_config.test_object_value,
                                        self.page_step_model.url)
            try:
                if self.page and urlparse(self.url).netloc.lower() != urlparse(
                        test_object_value).netloc.lower() and not data:
                    await self.w_goto(test_object_value)
                    self.url = test_object_value
            except Error as error:
                if error.message == "Target page, context or browser has been closed":
                    await self.setup()
                    self.page_step_result_model.status = StatusEnum.FAIL.value
                    self.page_step_result_model.error_message = error.message
                    self.page_step_result_model.element_result_list.append(self.element_test_result)
                    raise BrowserObjectClosed(*ERROR_MSG_0010)

    def __android_init(self):
        package_name = self.page_step_model.environment_config.test_object_value
        if self.android is None:
            self.driver_object.android_config = self.page_step_model.equipment_config
            self.android = self.driver_object.new_android()
        if self.android and self.package_name != package_name:
            self.a_clear_app(package_name)
            self.a_start_app(package_name)
            self.package_name = package_name

    def __ios_init(self, ):
        pass

    def __desktop_init(self, ):
        pass

    async def __error(self, error: MangoActuatorError):
        log.warning(
            f"""
            元素操作失败->
            element_model：{self.element_model.model_dump() if self.element_model else self.element_model}
            element_test_result：{self.element_test_result.model_dump() if self.element_test_result else self.element_test_result}
            error：{error.msg}
            """
        )
        if self.element_test_result:
            file_name = f'失败截图-{self.element_model.name}{RandomTimeData.get_deta_hms()}.jpg'
            file_path = rf"{InitPath.failure_screenshot_file}/{file_name}"
            self.element_test_result.picture_path = f'files/{file_name}'
            self.page_step_result_model.element_result_list.append(self.element_test_result)
            self.element_test_result.error_message = error.msg
            SignalSend.notice_signal_c(f'''元素名称：{self.element_test_result.ele_name}
                                           元素表达式：{self.element_test_result.loc}
                                           操作类型：{self.element_test_result.ope_type}
                                           操作值：{self.element_test_result.ope_value}
                                           断言类型：{self.element_test_result.ass_type}
                                           断言值：{self.element_test_result.ass_value}
                                           元素个数：{self.element_test_result.ele_quantity}
                                           截图路径：{file_path}
                                           元素失败提示：{error.msg}''')
            await self.__error_screenshot(file_path, file_name)
        self.page_step_result_model.status = StatusEnum.FAIL.value
        self.page_step_result_model.error_message = error.msg

    async def __error_screenshot(self, file_path, file_name):
        match self.page_step_model.type:
            case DriveTypeEnum.WEB.value:
                try:
                    await self.w_screenshot(file_path)
                except Error as error:
                    if error.message == "Target page, context or browser has been closed" \
                            or "Target page, context or browser has been closed" in str(error):
                        await self.setup()
                        raise BrowserObjectClosed(*ERROR_MSG_0010)
                except AttributeError:
                    await self.setup()
                    raise BrowserObjectClosed(*ERROR_MSG_0010)
            case DriveTypeEnum.ANDROID.value:
                self.a_screenshot(file_path)
            case DriveTypeEnum.IOS.value:
                pass
            case DriveTypeEnum.DESKTOP.value:
                pass
            case _:
                log.error('自动化类型不存在，请联系管理员检查！')
        if not settings.IS_DEBUG:
            HttpApi().upload_file(self.project_product_id, file_path, file_name)
