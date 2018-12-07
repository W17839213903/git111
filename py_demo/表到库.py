#excel表格到数据库


import xlrd
import pymysql
abc = pymysql.connect(host='192.168.0.57',
                      port=3306,
                      user='root',
                      password='123456')       #连接数据库
you = abc.cursor()                                #创建游标
you.execute('create database shuju;')           #创建库
you.execute('use shuju;')                       #使用库
f = xlrd.open_workbook('text1.xls')             #打开excel表格
sheet = f.nsheets                               #统计多少标签页
sheet = f.sheets()[0]                           #索引获取标签页名称
hang = sheet.nrows                              #获取多少行
lie = sheet.ncols                               #获取多少列
print(hang,lie)
for i in range(hang):                           #循环每行内容
    aa = sheet.row_values(i)
    if i == 0:
        you.execute('create table excel({} char(255),{} float,{} char(255));'.format(aa[0],aa[1],aa[2]))  #创建表
    else:
        you.execute('insert into excel values("{}", "{}", "{}" )'.format(aa[0],aa[1],aa[2]))       #添加数据