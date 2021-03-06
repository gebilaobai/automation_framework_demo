# coding=utf-8
import HTMLTestRunnerCN
import os
import time
import unittest


# 设置报告文件存储路径
report_path = os.path.dirname(os.path.abspath('.')) + '\\test_report\\'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = file(HtmlFile, 'wb')


suite = unittest.TestLoader().discover("testsuits")

if __name__ == '__main__':

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=u"XX项目测试报告",
                                             description=u"用例测试情况", tester='baiy')
    # 开始执行测试套件
    runner.run(suite)
