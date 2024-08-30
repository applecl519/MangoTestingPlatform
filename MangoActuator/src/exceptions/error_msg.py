# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 错误消息统一管理
# @Time   : 2024-02-01 10:00
# @Author : 毛鹏
ERROR_MSG_0001 = (301, '连接错误，请检查IP，端口，账号，密码')
ERROR_MSG_0002 = (302, '缓存中无法获取到：{}的值')
ERROR_MSG_0003 = (303, 'jsonpath表达式错误，请检查表达式：{}')
ERROR_MSG_0004 = (304, '数据不可以被转换成json')
ERROR_MSG_0005 = (305, '响应jsonpath断言失败')
ERROR_MSG_0006 = (306, '随机字符串函数只支持传入int类型数字')
ERROR_MSG_0007 = (307, '找不到下载的目录，请检查logs中是否存在：upload_files，这个目录')
ERROR_MSG_0008 = (308, '浏览器类型不正确，请联系管理员检查')
ERROR_MSG_0009 = (309, '浏览器路径不正确，请重新设置，路径：{}')
ERROR_MSG_0010 = (310, '浏览器对象被关闭，请重试')
ERROR_MSG_0011 = (311, '操作元素:{} 超时，请检查元素可见但是是否可操作，或元素在iframe中，或调整定位方式')
ERROR_MSG_0012 = (312, '操作失败，请检查输入的值是否有空字符串，null或不满足传参的值')
ERROR_MSG_0013 = (
    313, '打开url时超时，分为2个问题：1.启用的浏览器过多，应当减少浏览器并发个数；2.自行查看为啥60秒还未打开：{}')
ERROR_MSG_0014 = (314, '元素的类型错误，请联系管理员进行排查问题')
ERROR_MSG_0015 = (315, '的类型错误，请联系管理员进行排查问题')
ERROR_MSG_0016 = (316, 'UI断言失败，请检查用例断言')
ERROR_MSG_0017 = (317, '断言失败，请检查用例断言')
ERROR_MSG_0018 = (318, '断言失败，断言输入值是：空字符串、null或不满足函数接受类型')
ERROR_MSG_0019 = (319, '配置了sql断言，但是并没有配置mysql的数据库配置，请检查！用例id：{}，步骤ID：{}')
ERROR_MSG_0020 = (320, '没有更多的断言方式，请检查是否选择了非该设备类型的元素定位方式')
ERROR_MSG_0021 = (321, '元素未找到，请检查断言前操作是否正常完成')
ERROR_MSG_0022 = (322, '页面无此元素，请检查传入的元素是否正确')
ERROR_MSG_0023 = (323, 'iframe中未找到此元素，请检查元素表达式是否是正确的')
ERROR_MSG_0024 = (324, '上传文件的元素必须要是input标签中的')
ERROR_MSG_0025 = (325, '用例步骤的数据取不到，请检查是否对步骤进行了修改，而用例未更新')
ERROR_MSG_0026 = (326, '文件不存在')
ERROR_MSG_0027 = (
    327,
    '您元素的操作内容中没有任何的数据，请检查：1.页面步骤详情中字段->元素操作值是否是空，是空可能是你删除了，也可能是执行器的操作选项没有同步需要点击执行器的同步发送缓存数据；2.元素表达式错误导致查询不到元素；')
ERROR_MSG_0028 = (328, '一个元素内只能包含一个需要被替换的内容')
ERROR_MSG_0029 = (329, '页面无元素：{} 表达式：{}')
ERROR_MSG_0030 = (330, '断言时没有找到元素')
ERROR_MSG_0031 = (331, '元素未找到准备进行断言获取元素文本类容异常，元素名称：{}，表达式：{}')
ERROR_MSG_0032 = (332, '元素：{} 的元素表达式定位的标签无法对应操作的类型，或其他操作异常')
ERROR_MSG_0033 = (333, 'mysql中无：{}库')
ERROR_MSG_0034 = (334, 'sql存在语法错误，sql：{}')
ERROR_MSG_0035 = (335, 'sql语句是空，或查询字段或条件字段不存在')

ERROR_MSG_0036 = (336, '公共参数sql在数据库中查询不到结果，sql：{}')
ERROR_MSG_0037 = (337, '用例前置sql在数据库中查询不到结果，sql：{}')
ERROR_MSG_0038 = (338, '公共参数的sql_key不是列表')
ERROR_MSG_0039 = (339, '用例前置的sql_key不是列表')
ERROR_MSG_0040 = (340, '截图失败')
ERROR_MSG_0041 = (341, '元素操作时失败，请检查元素类型，定位表达式和iframe是否填写正确')
ERROR_MSG_0042 = (342, '实例化对象错误，设备信息是空无法实例化，请联系管理员检查')
ERROR_MSG_0043 = (343, '元素可能不存在，元素：{}，报错信息：{}')
ERROR_MSG_0044 = (344, '元素可能无法消失，元素：{}，报错信息：{}')
ERROR_MSG_0045 = (345, '设备启动超时！请检查设备是否已成功连接电脑，设备号：{}')
ERROR_MSG_0046 = (346, '应用名称是空，请检查测试环境中的包名是否正确且有值')
ERROR_MSG_0047 = (
    347, '设备启动超时！请检查设备是否开启了：文件传输模式、开发者模式、usb调试，开启后请重新连接电脑，设备号：{}')
ERROR_MSG_0048 = (348, '选项发生错误，请在执行器点击发送缓存数据，然后重新修改步骤的操作！或联系管理员处理！')
ERROR_MSG_0049 = (349, 'url格式错误，请检查url或者是选择的测试环境不正确')
ERROR_MSG_0050 = (350, 'xpath定位未找到元素')
ERROR_MSG_0051 = (351, '请检查email_host是否正确，导致无法连接发送错误')
ERROR_MSG_0052 = (352, '元素：{} 进行断言时发生异常，请检查元素是否可以正常使用')
ERROR_MSG_0053 = (353, '该用例已经测试失败，在截图的时候发生未知异常！')
ERROR_MSG_0054 = (354, '浏览器已被关闭，可能是手动关闭，用例失败！')
ERROR_MSG_0055 = (355, '您的电脑未安装指定浏览器！')
ERROR_MSG_0056 = (356, '输入的参数类型不正确，请检查操作输入框的类型是否正确')
ERROR_MSG_0057 = (357, '必要配置未安装，在执行器的虚拟环境中安装：playwright install ffmpeg')
