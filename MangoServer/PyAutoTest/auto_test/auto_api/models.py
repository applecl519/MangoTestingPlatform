from django.db import models

from PyAutoTest.auto_test.auto_system.models import ProjectProduct, ProductModule
from PyAutoTest.auto_test.auto_user.models import User
from PyAutoTest.exceptions import ToolsError

"""
     1.python manage.py makemigrations
     2.python manage.py migrate
"""


class ApiInfo(models.Model):
    """api用例表"""
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    project_product = models.ForeignKey(to=ProjectProduct, to_field="id", on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(to=ProductModule, to_field="id", on_delete=models.SET_NULL, null=True)

    # 0和空等于录制，1等于本期接口，2是调试完成
    type = models.SmallIntegerField(verbose_name='接口的类型', default=1)
    name = models.CharField(verbose_name="接口名称", max_length=1024)
    url = models.CharField(verbose_name="请求url", max_length=1024)
    method = models.SmallIntegerField(verbose_name="请求方法")
    header = models.JSONField(verbose_name="请求头", max_length=2048, null=True)
    params = models.JSONField(verbose_name="参数", null=True)
    data = models.JSONField(verbose_name="data", null=True)
    json = models.JSONField(verbose_name="json", null=True)
    file = models.JSONField(verbose_name="file", null=True)
    # 0失败， 1是成功
    status = models.SmallIntegerField(verbose_name="状态", default=2)
    front_custom = models.JSONField(verbose_name="前置自定义", null=True)

    class Meta:
        db_table = 'api_info'
        ordering = ['-id']

    def delete(self, *args, **kwargs):
        if ApiCaseDetailed.objects.filter(api_info=self).exists():
            raise ToolsError(300, "有关联数据，请先删除绑定的用例步骤详情后再删除！")
        super().delete(*args, **kwargs)


class ApiCase(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    project_product = models.ForeignKey(to=ProjectProduct, to_field="id", on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(to=ProductModule, to_field="id", on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name="测试用例名称", max_length=64)
    case_flow = models.TextField(verbose_name="步骤顺序", null=True)
    case_people = models.ForeignKey(to=User, to_field="id", verbose_name='用例责任人', on_delete=models.SET_NULL,
                                    null=True)
    # 0失败，1成功，2警告
    status = models.SmallIntegerField(verbose_name="状态", default=2)
    level = models.SmallIntegerField(verbose_name="用例级别")
    front_custom = models.JSONField(verbose_name="前置自定义", null=True)
    front_sql = models.JSONField(verbose_name="前置sql", null=True)
    front_headers = models.TextField(verbose_name="前置请求头", null=True)
    posterior_sql = models.JSONField(verbose_name="后置sql", null=True)

    class Meta:
        db_table = 'api_case'
        ordering = ['-id']

    def delete(self, *args, **kwargs):
        if ApiCaseDetailed.objects.filter(case=self).exists():
            raise ToolsError(300, "有关联数据，请先删除绑定的用例步骤详情后再删除！")
        super().delete(*args, **kwargs)


class ApiCaseDetailed(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    case = models.ForeignKey(to=ApiCase, to_field="id", on_delete=models.SET_NULL, null=True)
    api_info = models.ForeignKey(to=ApiInfo, to_field="id", on_delete=models.SET_NULL, null=True)
    case_sort = models.IntegerField(verbose_name="用例排序", null=True)
    # 请求
    url = models.CharField(verbose_name="请求url", max_length=1024, null=True)
    header = models.TextField(verbose_name="请求头", max_length=2048, null=True)
    params = models.JSONField(verbose_name="参数", null=True)
    data = models.JSONField(verbose_name="data", null=True)
    json = models.JSONField(verbose_name="json", null=True)
    file = models.JSONField(verbose_name="file", null=True)
    # 前置-目前只支持sql
    front_sql = models.JSONField(verbose_name="前置sql", null=True)
    # 断言
    ass_sql = models.JSONField(verbose_name="sql断言", null=True)
    ass_response_whole = models.JSONField(verbose_name="响应全匹配断言", null=True)
    ass_response_value = models.JSONField(verbose_name="响应值断言", null=True)
    # 后置
    posterior_sql = models.JSONField(verbose_name="后置sql", null=True)
    posterior_response = models.JSONField(verbose_name="后置响应处理", null=True)
    posterior_sleep = models.CharField(verbose_name="步骤顺序", max_length=64, null=True)
    status = models.SmallIntegerField(verbose_name="状态", default=2)
    result_data = models.JSONField(verbose_name="最近一次执行结果", null=True)

    class Meta:
        db_table = 'api_case_detailed'


class ApiPublic(models.Model):
    """api公共"""
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    project_product = models.ForeignKey(to=ProjectProduct, to_field="id", on_delete=models.SET_NULL, null=True)
    # 0等于自定义，1等于sql，2等于登录，3等于header
    type = models.SmallIntegerField(verbose_name="自定义变量类型")
    client = models.SmallIntegerField(verbose_name="什么端")
    name = models.CharField(verbose_name="名称", max_length=64)
    key = models.CharField(verbose_name="键", max_length=128)
    value = models.CharField(verbose_name="值", max_length=2048)
    status = models.SmallIntegerField(verbose_name="状态", default=0)

    class Meta:
        db_table = 'api_public'
        ordering = ['-id']
