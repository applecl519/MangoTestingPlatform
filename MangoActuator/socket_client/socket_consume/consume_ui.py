# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 
# @Time   : 2023/5/10 11:43
# @Author : 毛鹏
from concurrent.futures import ThreadPoolExecutor

from auto_ui.test_runner.debug_case_run import CaseDistribution
from auto_ui.test_runner.group_case_run import GroupCaseRun


class ConsumeUI:
    th = ThreadPoolExecutor(10)

    @staticmethod
    def debug_case(data: dict):
        CaseDistribution().debug_case_distribution(data)

    @classmethod
    def web_group_case(cls, data: dict):
        def run():
            GroupCaseRun.group_case_decompose(data)

        cls.th.submit(run)