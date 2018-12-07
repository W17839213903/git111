import time
import HTMLTestRunnertest
import re
import unittest
from 框架.test.test_学校 import 学校
class Test_run():
    def run_多个(self,aa):
        suit = unittest.TestSuite()
        for i in aa:
            discover = unittest.defaultTestLoader.discover(r'..\test',pattern='{}.py'.format(i.strip()))
            suit.addTest(discover)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open(r'D:\Python.py\py_demo\框架\report\abcd1.html','wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='王大保',
                                                   description='测试结果如下',
                                                   title='好分数测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()
    def run_all(self,aa):
        suit = unittest.TestSuite()
        disvover = unittest.defaultTestLoader.discover(r'..\test',pattern='*.py')
        suit.addTest(disvover)
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open(r'D:\Python.py\py_demo\框架\report\abcd2.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='王大保',
                                                   description='测试结果如下',
                                                   title='好分数测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()

if __name__ == '__main__':

    run = Test_run()
    # run.run_all()

    with open(r'D:\Python.py\py_demo\框架\data\run.txt','r') as f:
        aa = f.readlines()
        if 'all' in aa:
            run.run_all(aa)
        else:
            run.run_多个(aa)