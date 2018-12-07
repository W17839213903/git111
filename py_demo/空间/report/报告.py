import HTMLTestRunnertest
import unittest
import time

suit = unittest.TestSuite()
for i in :
    discover = unittest.defaultTestLoader.discover(r'..\test', pattern='{}.py'.format(i.strip()))
    suit.addTest(discover)
now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
f = open(r'D:\Python.py\py_demo\框架\report\abcd1.html', 'wb')
runner = HTMLTestRunnertest.HTMLTestRunner(tester='王大保',
                                           description='测试结果如下',
                                           title='好分数测试报告',
                                           stream=f)