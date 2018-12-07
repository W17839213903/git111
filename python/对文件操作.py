# 对文件操作  open( ) 函数
# 格式 open('文件名','权限','编码方式')
# a="""rewr
# ewqrweqr
# ewrew
# """
# f = open(r'C:\Users\王大保\Desktop\a.txt','a',encoding='utf-8')
# f.write(a)
# f.close()
# 文件名：如果路径不加路径，表示在当前目录下的文件。
# 如果此目录有这个文件，就操作这个文件。没有这个文件就创建文件。
# 如果要加路径的话，已经要把斜杠变成双斜杠，表示不转义。
# 或者在引号前加上r，有人表示不转义
# 权限 :  w (写)  r(读)  a(追加)
# w（write) 可写  但是会把原内容覆盖
# r(read,)  读取 读取结果是一个字符串
# r(raedlines) 读取 读取结果是一个列表
# f = open('a.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         f.write('{}*{}={}\t'.format(j,i,i*j))
#     f.write('\n')
# f.close()
#
#
#
# f = open(r'C:\Users\bigbaby\Desktop\a.jpg','rb')
# dd=f.read()
# f.close()
#
# w=open('a.jpg','ab')
# w.write(dd)
# w.close()
#
#
#
# with open('a.txt','a',encoding='utf-8') as b:
#     f=b.write(a)
# with open('a.txt','r',encoding='utf-8') as b:
#     f=b.readlines()
#     a=len(f)
# for i in f:
#     if i=='\n':
#         a=a-1
#     elif i[0] == '#':
#         a=a-1
# print(a)

# with open('day1.py','r',encoding='utf-8') as b:
#     f=b.readlines()
#     for i in range(len(f)-1):
#         print(i)
#         if f[i]=='\n' or f[i].startswith('#'):
#             f.remove(f[i])
# # print(len(f))
# try:
#     a='wee'
#     print(a+1)
# except NameError and TypeError:
#     print('hello')
# a=123
# raise TypeError('哈哈哈，就让你报错')
# print(123+1)
# s=0
# for i in range(1,10):
#     if i==10:
#         raise TypeError('哈哈哈，就让你报错')
#         s+=i
#         print(s)
# print(s)
# import random
#连接数据库的库  pymysql
#
# import day2
# day2.jiujiu()


# import time
# a=input('>')
# b=a.split( )
# if b[0][2] and b[0][3]==0 and int(b[0]) % 400 == 0:
#     print('{}是闰年'.format(a))
# elif b[0][2] and b[0][3] != 0 and int(b[0])%4==0:
#     print('{}是闰年'.format(a))
# else:
#     print('{}是平年'.format(a))
# c=(time.strptime('{}'.format(a),'%Y %m %d'))
# print('今天是周{}'.format(c[-3]+1))
# print('今天是一年中的第{}'.format(c[-2]))



# with open('a.txt','w',encoding='utf-8') as f:
#     for i in range(1,10):
#         for j in range(1,i+1):
#             f.write('{}*{}={}'.format(j,i,i*j)+' ')
#         f.write('\n')


# import os
# # for i in range(10):
# #     os.chdir(r'D:\123')
# #     os.mkdir('{}'.format(i))
# #     for j in range(10):  # 下面的路径改成目前文件的所在路径
# #         with open(r'D:\123\{}\{}.txt'.format(i,j),'w',encoding='utf-8') as f:
# #             f.write('123')
# #         os.remove(r'D:\123\{}\{}.txt'.format(i,j))
# #     os.rmdir('{}'.format(i))
# # print('over')

# with open(r'C:\Users\bigbaby\Desktop\b.jpg','rb') as f:
#     b=f.read()
# with open('a.jpg','wb') as t:
#     t.write(b)

# def wenjian(b):
#     with open('{}'.format(b),'r',encoding='utf-8') as b:
#         f=b.readlines()
#         print(f)
#         a=len(f)
#     for i in f:
#         if i=='\n':
#             a=a-1
#         elif i[0] == '#':
#             a=a-1
#     print(a)
# wenjian('a.txt')


import time
# print(time.time())   #时间戳
# print(time.localtime())  #本地时间  显示结果为元组  默认显示当前时间
# print(time.strftime('%Y %m %d %H-%M-%S %W',time.localtime(2142135412)))   #将时间戳格式化为现在时间
print(time.strptime('2008 08 08','%Y %m %d'))   #将现在时间格式化为元组
# a = (2005,12,31,23,21,23,21,54,23)
# print(time.mktime(a))     #将元祖时间格式化为时间戳
# time.sleep(3)
# print(123)     #休眠3秒钟