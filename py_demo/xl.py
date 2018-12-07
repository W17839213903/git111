# import xlrd
# f=xlrd.open_workbook('text1.xls')     #打开一个文件
# #两种获取标签页的内容  1.通过所引来获取    2.通过标签页来获取
# sheet=f.nsheets       #获取有多少个标签页
# sheet=f.sheets()[0]     #索引获取标签页
# print(f.sheet_names())   #获取所有标签页的名称
#
# sheet = f.sheet_by_name('python操作excel')    #括号中填写操作的标签
# a=sheet.nrows             #获取文件中有多少行
# for i in range(a):
#     print(sheet.row_values(i))  #获取第几行的内容  第一行从0开始
# print(sheet.ncols)   #获取有多少列
# print(sheet.col_values(2))   #获取第几列内容  第一列从0开始
# print(sheet.cell(0,0).value)    #读取某个单元格的内容

# excel表格的追加

# xlutils智能操作复制的文件
# f=xlrd.open_workbook('text1.xls')、
#复制文件
# new_f = copy(f)
#操作复制的文件、
# sheet = new_f.get_sheet(0)
# sheet.write(5,5,'哈哈哈哈')  #写入
# new_f.save('text1.xls')
# for i in range(50,70):
#     for j in range(0,3):
#         if j==0:
#             sheet.write(i,j,'大猪蹄子')
#         elif j==1:
#             sheet.write(i,j,'18')
#         else:
#             sheet.write(i,j,'软测18班')
# new_f.save('textl.xls')




# import paramiko
#创建一个ssh客户端
# ssh123 = paramiko.SSHClient()
#把将要连接的主机添加到 known_hosts 文件中
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #免验证

# ssh123.connect(hostname='192.168.0.161',
#                port=22,
#                username='root',
#                password='123456')
#执行命令  产生3个结果
# aa,bb,cc = ssh123.exec_command('ls -al')       #只能输入有结果的命令
#第一个变量;执行的命令，输入
#第二个变量：命令的结果，输出
#第三个变量：命令的报错
# print(bb.read().decode())    #打印结果要添加.decode  不然结果就是字节码
# ssh123.close()          #断开连接

#
# 无限输入  像xshell一样
# while True:
#     import paramiko
#     ssh123 = paramiko.SSHClient()
#     ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh123.connect(hostname='192.168.0.161',
#                    port=22,
#                    username='root',
#                    password='123456')
#     a=input('输入命令')
#     aa,bb,cc=ssh123.exec_command(a)
#     if a=='exit':
#         ssh123.close()
#         break
#     else:
#         print(bb.read().decode())
#         print(cc.read().decode())


#创建一个传输通道  #接收的只能是元组
# ssh123 = paramiko.Transport(('192.168.0.161',22))
# ssh123.connect(username='root',password='123456')/
# 传输文件使用 sftp 协议   创建一个sftp 实例
# sftp = paramiko.SFTPClient.from_transport(ssh123)

#get 是从linux下载文件到本地
# sftp.get('anaconda-ks.cfg','./aaa.cfg')

#put 是从本地上传到Linux上
# sftp.put('./a.txt','./aaa1')


import unittest
import requests
from 框架.report import HTMLTestRunnertest
import time
import xlrd
class 学校(unittest.TestCase):
    def tes_数据(self):
        shuju = []              #创建一个空列表  用来接收表格数据
        f = xlrd.open_workbook('text.xls')    #打开存储数据的表格
        sheet = f.sheets()[0]      #索引获取标签页
        num = sheet.nrows          #统计多少行
        for i in range(1,num):
            aaa= sheet.row_values(i)     #循环获取没行内容
            shuju.append(aaa)        #把获取的内容添加到空列表中
        return shuju               #把所的数据用return 返还到变量
    def tess(self,a):
        url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
        canshu = {"filterInput":"{}".format(a)}
        headers = {'Cookie':"yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
        response = requests.get(url=url,headers=headers,params=canshu)
        aaaa = response.json()
        return aaaa
    def test_1(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[0][0])     #使用数据中的第一个变量的参数
        self.assertEqual(html['code'],shuju[0][1])    #使用数据中第一个变量的第一个预期结果
        self.assertIn(len(html['data']),range(int(shuju[0][2])))   #使用数据中第一个变量的第二个预期结果
    def test_2(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[1][0])    #使用数据中的第二个变量的参数
        self.assertEqual(html['code'],shuju[1][1])     #使用数据中第二个变量的第一个预期结果
        self.assertEqual(len(html['data']),int(shuju[1][2]))    #使用数据中第二个变量的第二个预期结果
    def test_3(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[2][0])     #使用数据中的第三个变量的参数
        self.assertEqual(html['code'],shuju[2][1])    #使用数据中第三个变量的第一个预期结果
        self.assertEqual(len(html['data']),int(shuju[2][2]))  #使用数据中第三个变量的第二个预期结果
    def test_4(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[3][0])    #使用数据中的第四个变量的参数
        self.assertEqual(html['code'],shuju[3][1])   #使用数据中第四个变量的第一个预期结果

suit =  unittest.TestSuite()
#添加测试用例  将测试用例添加到测试套件中
# suit.addTest(学校('test_1'))
# suit.addTest(学校('test_2'))
suit.addTest(unittest.makeSuite(学校))
now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
f = open('666.html','wb')
runner = HTMLTestRunnertest.HTMLTestRunner(tester='王大保',
                                           description='测试结果如下',
                                           title='好分数测试报告',
                                           stream=f)
runner.run(suit)
f.close()
