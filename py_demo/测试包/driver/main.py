#!/usr/bin/env python
#! -*- encoding -*-

# import time
# import HTMLTestRunnertest
# import unittest
# from 测试包.test.test_学校 import 学校
#
# class Test_run():
#     def run_多个(self):
#         suit = unittest.TestSuite()     #生成一个测试套件  添加一个测试套件
#         suit.addTest(unittest.makeSuite(学校))
#         now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
#         f = open(r'D:\Python.py\py_demo\测试包\report\abc1.html','wb')
#         runner = HTMLTestRunnertest.HTMLTestRunner(tester='王大保',
#                                                    description='测试结果如下',
#                                                    title='好分数测试报告',
#                                                    stream=f)
#         runner.run(suit)
#         f.close()
#
#     def run_all(self):
#         suit = unittest.TestSuite()
#         desvover = unittest.defaultTestLoader.discover(r'..\test',pattern='*.py')
#         suit.addTest(desvover)
#         now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
#         f = open(r'D:\Python.py\py_demo\测试包\report\abc2.html','wb')
#         runner = HTMLTestRunnertest.HTMLTestRunner(tester='王大保',
#                                                    description='测试结果如下',
#                                                    title='好分数测试报告',
#                                                    stream=f)
#         runner.run(suit)
#         f.close()
#
# if __name__ == '__main__':
#     run = Test_run()
#     run.run_all()




import time
import HTMLTestRunnertest
import unittest
import re

class Test_run():
    def run_多个(self,aa):
        suit = unittest.TestSuite()
        for i in aa:
            print(i)
            discover=unittest.defaultTestLoader.discover(r'..\test',pattern='{}.py'.format(i.strip()))
            suit.addTest(discover)
        now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
        f = open(r'D:\Python.py\py_demo\测试包\report\abc1.html','wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='王大保',
                                                   description='测试结果如下',
                                                   title='好分数测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()

    def run_all(self,aa):
        suit = unittest.TestSuite()
        desvover = unittest.defaultTestLoader.discover(r'..\test',pattern='test*.py')
        suit.addTest(desvover)
        now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
        f = open(r'D:\Python.py\py_demo\测试包\report\abc2.html','wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='王大保',
                                                   description='测试结果如下',
                                                   title='好分数测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()

if __name__ == '__main__':
    run = Test_run()
    with open(r'D:\Python.py\py_demo\测试包\data\run.txt','r') as f:
        aa=f.readlines()
        print(aa)
        if 'all' in aa:
            run.run_all(aa)
        else:
            run.run_多个(aa)