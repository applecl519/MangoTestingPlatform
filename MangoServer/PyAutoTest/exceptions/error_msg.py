# @Project: 芒果测试平台
# @Description: 错误消息统一管理
# @Time   : 2024-02-01 10:00
# @Author : 毛鹏
ERROR_MSG_0000 = (300, '内部服务异常，请联系管理员查看')
ERROR_MSG_0001 = (301, '系统代理出错，请检查系统代理')
ERROR_MSG_0002 = (302, '请求发生未知异常，请检查接口数据后再联系管理员查看')
ERROR_MSG_0003 = (303, '公共参数中登录，只允许返回为JSON格式的接口使用，或有其他错误，如有代理')
ERROR_MSG_0004 = (304, '全匹配断言失败，请检查响应结果')
ERROR_MSG_0005 = (305, '响应jsonpath断言失败，请检查jsonpath语法或提取的数据')
ERROR_MSG_0006 = (306, 'sql断言失败，请检查sql语句或查询结果')
ERROR_MSG_0007 = (307, '响应数据语法错误，返回的数据非json格式，请检查服务是否正常！')
ERROR_MSG_0008 = (308, '用例是空，请先配置用例')
ERROR_MSG_0009 = (309, 'mysql中无：{}库')
ERROR_MSG_0010 = (310, '数据清除不支持查询数据操作')
ERROR_MSG_0011 = (311, 'jsonpath表达式错误，表达式：{}')
ERROR_MSG_0012 = (312, '邮件接收人未填写或格式不可转换成JSON')
ERROR_MSG_0013 = (313, '手机号码必须是字符串类型')
ERROR_MSG_0014 = (314, '手机号码列表必须是list类型')
ERROR_MSG_0015 = (315, '随机字符串函数只支持传入int类型数字')
ERROR_MSG_0016 = (316, '邮件发送失败，请检查邮件配置是否正确')
ERROR_MSG_0017 = (317, '请检查email_host是否正确，导致无法连接发送错误')
ERROR_MSG_0018 = (318, '企业微信消息发送失败，请检查webhook地址是否正确可调用')
ERROR_MSG_0019 = (319, '企业微信「文本类型」消息发送失败')
ERROR_MSG_0020 = (320, '企业微信「file类型」消息发送失败')
ERROR_MSG_0021 = (321, '该项目未配置mysql，但是开启了数据库操作')
ERROR_MSG_0022 = (322, 'Mysql配置错误，请先在数据库中检查mysql配置是否正确')
ERROR_MSG_0023 = (323, '请检查mysql配置或确保该地址在服务器中可以被连接')
ERROR_MSG_0024 = (324, 'sql语句为空')
ERROR_MSG_0025 = (325, 'sql语法错误，sql:{}')
ERROR_MSG_0026 = (326, 'web端不提供该方法，您已经成功了，请直接开始使用该方法进行测试，文件名称：{}')
ERROR_MSG_0027 = (327, '缓存中无法获取到：{}的值')
ERROR_MSG_0028 = (328, '发送任务失败，请确保{}已连接{}')
ERROR_MSG_0029 = (329, '设备配置没有配置或者状态未开启，请先到前端自动化-设备配置中添加配置~')
ERROR_MSG_0030 = (330, '查询数据库结果为空错误，请联系管理查看错误问题')
ERROR_MSG_0031 = (331, '缓存的key未填写，请先到系统管理->系统设置中填写邮箱配置')
ERROR_MSG_0032 = (332, '该项目未配置mysql，请先开启mysql后再执行用例')
ERROR_MSG_0033 = (333, '公共参数sql在数据库中查询不到结果，sql：{}')
ERROR_MSG_0034 = (334, '用例前置sql在数据库中查询不到结果，sql：{}')
ERROR_MSG_0035 = (335, '公共参数的sql_key不是列表')
ERROR_MSG_0036 = (336, '用例前置的sql_key不是列表')
ERROR_MSG_0037 = (337, '请求超时，请检查请求域名的服务器是否正常')
ERROR_MSG_0038 = (338, '您的缓存信息未从执行器同步过来，请点击执行的：发送缓存数据 按钮')
ERROR_MSG_0039 = (339, '值的类型错误，请检查值是否符合json语法或者响应')
ERROR_MSG_0040 = (340, '现在还不支持PC桌面客户端和IOS的测试~')
ERROR_MSG_0041 = (341, 'sql断言时，查询的sql结果是空')
ERROR_MSG_0042 = (342, 'miniIO账号或密码不正确')
ERROR_MSG_0043 = (343, 'miniIO的IP或端口不正确')
ERROR_MSG_0044 = (344, 'miniIO提供的储存桶名称不正确')
ERROR_MSG_0045 = (345, '需要上传的文件路径不正确')
ERROR_MSG_0046 = (346, '您需要执行的用例没有对应的测试环境')
ERROR_MSG_0047 = (347, '方法不存在，请检查输入的方法名称是否正确')
ERROR_MSG_0048 = (348, '用户邮箱是空，请先给用户设置邮箱之后，再使用')
ERROR_MSG_0049 = (349, '你的测试项目有重复的测试环境，请检查数据，重复的部署环境和产品和自动化类型只允许存在一个')
ERROR_MSG_0050 = (350, '定时任务中用户昵称查询结果为空，请先清除异常用户后再测试')
ERROR_MSG_0055 = (352, '你开启的ui配置是空的，请删除后重新创建')
ERROR_MSG_0056 = (356, '一个测试环境现在不支持配置2个数据库，删除一个再进行尝试')
