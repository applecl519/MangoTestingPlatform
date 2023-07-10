# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 邮箱通知封装
# @Time   : 2022-11-04 22:05
# @Author : 毛鹏
import json
import logging
import smtplib
from email.mime.text import MIMEText

from PyAutoTest.auto_test.auto_system.models import NoticeConfig
from PyAutoTest.utils.other_utils.native_ip import get_host_ip

logger = logging.getLogger('system')


class SendEmail:
    """ 发送邮箱 """

    def __init__(self, notice_obj: NoticeConfig):
        self.team = notice_obj.team.id
        config = json.loads(notice_obj.config)
        self.send_user = config['send_user']
        self.send_list = config['send_list']
        self.email_host = config['email_host']
        self.stamp_key = config['stamp_key']

    def send_main(self, case_id) -> None:
        """
        发送邮件
        :return:
        """
        send_list = self.send_list.split(',')  # 发送多个人，用,隔开就可以
        content = f"""
        各位同事, 大家好:
            自动化用例执行完成，执行结果如下:
            用例运行总数: {case_id} 个
            通过用例个数: {99} 个
            失败用例个数: {0} 个
            异常用例个数: {0} 个
            跳过用例个数: {0} 个
            成  功   率: {99} %


        **********************************
        芒果自动化平台地址：https://{get_host_ip()}:5173/index
        详细情况可前往芒果自动化平台查看，非相关负责人员可忽略此消息。谢谢！
        """
        try:
            self.send_mail(send_list, f'{self.team}接口自动化报告', content)
            logger.info(f"邮件发送成功{self.team},{self.send_user},{self.send_list},{self.stamp_key},"
                        f"{self.email_host}")
        except BaseException as e:
            logger.error(f"邮件发送失败，失败原因：{e},发送信息如下："
                         f"用例id：{case_id},"
                         f"项目名称：{self.team},"
                         f"发送用户：{self.send_user},"
                         f"发送列表：{self.send_list},"
                         f"登录key：{self.stamp_key},"
                         f"电子邮件主机：{self.email_host}")

    def send_mail(self, user_list: list, sub: str, content: str, ) -> None:
        """

        @param user_list: 发件人邮箱
        @param sub:
        @param content: 发送内容
        @return:
        """
        user = f"MangoAutoTestServer <{self.send_user}>"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')  # MIMEText设置发送的内容
        message['Subject'] = sub  # 邮件的主题
        message['From'] = user  # 设置发送人 设置自己的邮箱
        message['To'] = ";".join(user_list)  # 设置收件人 to是收件人，可以是列表
        server = smtplib.SMTP()
        server.connect(self.email_host)
        server.login(self.send_user, self.stamp_key)  # 登录qq邮箱
        server.sendmail(user, user_list, message.as_string())  #
        server.close()

    def error_mail(self, error_message: str) -> None:
        """
        执行异常邮件通知
        @param error_message: 报错信息
        @return:
        """
        send_list = self.send_list.split(',')  # 多个邮箱发送，config文件中直接添加  '806029174@qq.com'
        content = f"自动化测试执行完毕，程序中发现异常，请悉知。报错信息如下：\n{error_message}"
        self.send_mail(send_list, f'{self.team}接口自动化执行异常通知', content)


if __name__ == '__main__':
    # project = "Zshop"
    # send_user = '729164035@qq.com'
    # send_list = "maopeng@zalldigital.com,729164035@qq.com"
    # email_host = 'smtp.qq.com'
    # stamp_key = 'lqfzvjbpfcwtbecg'
    # case_id = [0, 1, 2]
    # SendEmail().send_main(case_id=case_id)
    # SendEmail.notice_data()
    pass