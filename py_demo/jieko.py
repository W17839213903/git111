#接口测试 ：发送请求，验证响应是否符合需求的过程
#postman/jmeter
#requests 发送http请求    accert  断言处理

# import unittest
# import requests
# class 学校():
#     def test_学校(a):
#         url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
#         # a=input('>>')
#         canshu = {"filterInput":"{}".format(a)}
#         headers = {'Cookie':"yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
#         response = requests.get(url=url,headers=headers,params=canshu)
#         # html = response.content.decode('utf-8')
#         html = response.json()
#         assert html['code'] == 0

# class 学校(unittest.TestCase):
#     def setUp(self):           # 初始测试化环境 每次执行测试用例前执行 保证每一个用例都在相同的环境下执行
#         print(123)
#     def tearDown(self):        # 清理环境  每次用例执行完之后执行
#         print(456)
#     def test_1(self):          #每一个测试用例必须以test开头  执行顺序为ASCII码的优先顺序
#         print('a')
#     def test_2(self):
#         print('b')


# unittest.main()


# unittest.TestCase   :用来作用例管理，管理测试用例
# unittest.TestSuite   :测试套件：多个测试用例集合在一起
# unittest.TestLoader   :测试载入，将测试用例加载到测试套件中
# unittest.TestRunner   :执行测试用例


#
# class 好分数(unittest.TestCase):
#     def setUp(self):
#         aaa=["北京",123,'assad','!@#$']
#         for i in aaa:
#             canshu = {"filterInput": "{}".format(i)}
#             url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#             headers = {'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
#             response = requests.get(url=url, headers=headers, params=canshu)
#             html = response.json()
#             return html
#     def tearDown(self):
#         pass
#     def test_1(self,html):
#         self.canshu = {"filterInput": "北京"}
#         html["code"] == 0
#         html["msg"] == "学校快查成功"
#
#     def test_2(self,html):
#         self.canshu = {"filterInput": "上海"}
#         html["code"] == 0
#         html["msg"] == "学校快查成功"
#
#     def test_3(self,html):
#         self.canshu = {"filterInput": "123"}
#         html["code"] == 0
#         html["msg"] == "学校快查成功"
#
#     def test_4(self,html):
#         self.canshu = {"filterInput": "！@#"}
#         html["code"] == 0
#         html["msg"] == "学校快查成功"
#
#     def test_5(self,html):
#         self.canshu = {"filterInput": "abcd"}
#         html["code"] == 0
#         html["msg"] == "学校快查成功"
#
# unittest.main()

import unittest
import requests
from 框架.report import HTMLTestRunnertest
import time
import xlrd
class 学校(unittest.TestCase):
    def tes_数据(self):
        shuju = []
        f = xlrd.open_workbook('text.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(1,num):
            aaa= sheet.row_values(i)
            shuju.append(aaa)
        return shuju
    def tess(self,a):
        url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
        canshu = {"filterInput":"{}".format(a)}
        headers = {'Cookie':"yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
        response = requests.get(url=url,headers=headers,params=canshu)
        aaaa = response.json()
        return aaaa
    def test_1(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[0][0])    #使用数据中的第一个变量的参数
        self.assertEqual(html['code'],int(shuju[0][1]))    #使用数据中第一个变量的第一个预期结果
        self.assertIn(len(html['data']),range(int(shuju[0][2])))    #使用数据中第一个变量的第二个预期结果
    def test_2(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[1][0])     #使用数据中的第二个变量的参数
        self.assertEqual(html['code'],int(shuju[1][1]))    #使用数据中第二个变量的第一个预期结果
        self.assertEqual(len(html['data']),int(shuju[1][2]))     #使用数据中第二个变量的第二个预期结果
    def test_3(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[2][0])      #使用数据中的第三个变量的参数
        self.assertEqual(html['code'],int(shuju[2][1]))     #使用数据中第三个变量的第一个预期结果
        self.assertEqual(len(html['data']),int(shuju[2][2])) #使用数据中第三个变量的第二个预期结果
    def test_4(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[3][0])     #使用数据中的第四个变量的参数
        self.assertEqual(html['code'],int(shuju[3][1]))     #使用数据中第四个变量的第一个预期结果
        self.assertEqual(len(html['data']),int(shuju[3][2])) #使用数据中第四个变量的第二个预期结果

# if __name__ == '__main__':
#     unittest.main()



#生成一个测试套件  添加一个测试套件
suit =  unittest.TestSuite()
#添加测试用例  将测试用例添加到测试套件中
# suit.addTest(学校('test_1'))
# suit.addTest(学校('test_2'))
suit.addTest(unittest.makeSuite(学校))
now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
f = open('abc.html','wb')
runner = HTMLTestRunnertest.HTMLTestRunner(tester='王大保',
                                           description='测试结果如下',
                                           title='好分数测试报告',
                                           stream=f)
runner.run(suit)
f.close()

