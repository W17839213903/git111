# import  pymysql
# abc=pymysql.connect(host='192.168.0.184',
#                 port=3306,
#                 user='root',
#                 password='123456',
#                 charset='utf8')
# aaa=abc.cursor()
# aaa.execute('show databases;')
# # print(aaa.fetchall())
# aaa.execute('use shujuku;')
# aaa.execute('select * from biao1;')
# aa=aaa.fetchall()
# aaa.execute('desc biao1')
# bb=aaa.fetchall()
#
# with open('a.txt','a',encoding='utf-8') as f:
#     for i in range(len(bb)):
#         if i == len(bb) - 1:
#             f.write(bb[i][0])
#         else:
#             f.write(bb[i][0]+',')
#     for j in aa:
#         f.write('\n'+'{},{},{}'.format(j[0],j[1],j[2]))
# import pymysql
# abc =pymysql.connect(host = '192.168.0.184',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# aaa=abc.cursor()
# # aaa.execute('create database zuoye;')
# aaa.execute('use zuoye')
# # aaa.execute("create table stu1(姓名 char(255),年龄 int,班级 char(255));")
# list1 = ['小王',1,'软件测试19班']
# for i in range(30):
#     aaa.execute('insert into stu1 values("{}",{},"{}");'.format(list1[0],list1[1]+i,list1[2]))
#     abc.commit()
# aaa.execute('select * from stu1;')
# print(aaa.fetchall())
# aaa.execute('desc stu1;')
# print(aaa.fetchall())

#创建30条数据
# import pymysql
# abc = pymysql.connect(host = '192.168.0.36',
#                       port = 3306,
#                       user = 'root',
#                       password = '123456')
# you = abc.cursor()
# you.execute('show databases;')
# you.execute('use test;')
# you.execute('create table stu(姓名 char(255),年龄 float,班级 char(255));')
# you.execute('desc stu;')
# print(you.fetchall())
# for i in range(30):
#     a=['小米',20.0,'软测一班']
#     you.execute('insert into stu values("{}","{}","{}");'.format(a[0],a[1],a[2]))
# you.execute('select * from stu;')
# print(len(you.fetchall()))

# 库到txt
# import pymysql
# abc = pymysql.connect(host = '192.168.0.36',
#                       port = 3306,
#                       user = 'root',
#                       password = '123456')
# you = abc.cursor()
# you.execute('show databases;')
# you.execute('use test;')
# you.execute('desc stu;')
# biaotou = you.fetchall()
# you.execute('select * from stu;')
# shuju = you.fetchall()
# print(shuju)
# with open('a.txt','w',encoding='utf-8') as f:
#     for i in range(len(biaotou)):
#         if i == len(biaotou)-1:
#             f.write(biaotou[i][0]+'\n')
#         else:
#             f.write(biaotou[i][0]+' ')
#     for j in shuju:
#         f.write('\n'+'{} {} {}'.format(j[0],j[1],j[2]))


import pymysql
import xlwt
f = xlwt.Workbook()
sheet = f.add_sheet('caozuo数据')
abc = pymysql.connect(host = '192.168.0.36',
                      port = 3306,
                      user = 'root',
                      password = '123456')
you = abc.cursor()
you.execute('show databases;')
you.execute('use test;')
you.execute('desc stu;')
biaotou = you.fetchall()
you.execute('select * from stu;')
shuju = you.fetchall()
print(shuju[1])
print(shuju)
for i in range(len(shuju)):
    for j in range(len(biaotou)):
        if i == 0:
            sheet.write(i,j,biaotou[j][0])
        else:
            sheet.write(i,0,shuju[j][0])
            sheet.write(i,1,shuju[j][1])
            sheet.write(i,2,shuju[j][2])
f.save('huchuan.xls')

# import pymysql
# import xlwt
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('caozuo数据',)
# abc = pymysql.connect(host = '192.168.0.36',
#                       port = 3306,
#                       user = 'root',
#                       password = '123456')
# you = abc.cursor()
# you.execute('show databases;')
# you.execute('use test;')
# you.execute('desc stu;')
# biaotou = you.fetchall()
# biaotou1=[]
# m=1
# for i in biaotou:
#     sheet.write(0,m,'{}'.format(i[0]))
#     m+=1
# you.execute('select * from stu;')
# shuju = you.fetchall()
# k=1
# for i in shuju:
#     sheet.write(k,0,'{}'.format(i[0]))
#     sheet.write(k, 1, '{}'.format(i[0]))
#     sheet.write(k, 2, '{}'.format(i[0]))
#     k+=1
# f.save('huchuan.xls')