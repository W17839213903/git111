# os 模块
# 作用：Python与操作系统之间的交互
import os

# a = os.popen('ping 8.8.8.8')     #执行
# print(a.read())
#

#获取当前位置
# print(os.getc wd())


# 切换目录
# os.chdir(r'D:\123')  #两个斜杠或者路径前边加r  是为了让转义字符不转义
# print(os.getcwd())

# 创建目录
# os.mkdir(r'D:\123\王大保啊')  #如果不加路径 就在当前目录下创建
# os.makedirs(r'aaa\bbb\ccc')   #创建递归目录

#删除递归目录
# os.removedirs(r'aaa')
#删除一个空目录
# os.rmdir(r'D:\123\王大保啊')
#删除文件
# os.remove('a.txt')

#获取当前目录下的所有文件
# print(os.listdir(r'D:\软件'))

#更改文件名
# os.rename('图形1.py','图形.py')

#将文件名和路径隔开
#注意  分割的是字符串  与有无此文件或路径无关
# print(os.path.split(r'D:\12\6666.py'))

#将文件后缀名和文件路径分开
# print(os.path.splitext(r'D:\12\6666.py'))

#过滤出 .py 的文件
# for i in os.listdir():
#     if os.path.splitext(i)[-1] == '.py':
#         print(i)

# print(os.path.isfile('__pycache__'))        #判断是否为普通文件
# print(os.path.isdir('__pycache__'))         #判断是否为目录文件
# print(os.path.islink('__pycache__'))        #判断是否为链接文件
#
# for i in os.listdir():
#     if os.path.isdir(i):
#         print(i)

#统计某目录下有多少普通文件 有多少目录
# def wenjian(a):
#     os.chdir(a)
#     s=0
#     s1=0
#     for i in os.listdir():
#         if os.path.isdir(i):
#             s+=1
#         else:
#             s1+=1
#     print('目录文件有{}个'.format(s))
#     print('普通文件有{}个'.format(s1))
# wenjian(r'D:\软件')

# a = [i for i in os.listdir() if os.path.isfile(i)]
# b = [y for y in os.listdir() if os.path.isdir(y)]
# print(len(a),len(b))

# xlwt 需要下载的模块 作用：给Excel表格写入数据
# xlrd 需要下载的模块 作用：读取Excel表格中的数据
# xlutils 需要下载的模块 作用：给Excel表格中追加数据
# import xlwt
#打开一个空白文件
# f = xlwt.Workbook(encoding='utf-8')
#添加一个标签页,括号中写标签页的名称
# sheet = f.add_sheet('python操作excel')
#写入数据；
# sheet.write(0,0,'姓名')
#第一个数字代表有多少行。第一行从0开始
#第二个数字代表有多少列。第一列从0开始
#第三个字符串代表写入的内容


#給Excel表格批量添加30条数据  #####################
# import xlwt
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python操作excel')
# sheet.write(0,0,'姓名')
# sheet.write(0,1,'年龄')
# sheet.write(0,2,'班级')
# for i in range(1,31):
#         sheet.write(i,0,'小明啊')
#         sheet.write(i,1, 18)
#         sheet.write(i,2,'一班')
#         # continue
# f.save('text1.xls')

import xlwt
f = xlwt.Workbook(encoding='utf-8')
sheet = f.add_sheet('python操作excel')
sheet.write(0,0,'姓名')
sheet.write(0,1,'年龄')
sheet.write(0,2,'班级')
a = ['小米',18,'一班']
for i in range(1,31):
    for j in range(3):
        sheet.write(i,j,a[j])
f.save('text1.xls')