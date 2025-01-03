from threading import Thread

import atexit
import time
from django.apps import AppConfig

from PyAutoTest.auto_test.auto_api.service.api_call.case_flow import CaseFlow


class AutoApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PyAutoTest.auto_test.auto_api'

    def ready(self):
        def run():
            time.sleep(5)
            self.test_case_consumption()

        task = Thread(target=run)
        task.start()
        atexit.register(self.shutdown)

    def test_case_consumption(self):
        self.case_flow = CaseFlow()
        self.consumer_thread_instance = Thread(target=self.case_flow.process_tasks)
        self.consumer_thread_instance.start()

    def shutdown(self):
        print('Shutting down...')
        self.case_flow.stop()
        self.consumer_thread_instance.join()
    #
    # def start_consumer(self):
    #     time.sleep(5)
    #     # 在主线程中获取事件循环并启动任务
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #     loop.run_until_complete(self.test_case_consumption(loop))
    #
    # async def test_case_consumption(self, loop):
    #     CaseFlow.loop = loop
    #     await CaseFlow.process_tasks()
