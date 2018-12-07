#数据库到表格

#
import xlrd
from xlutils.copy import copy
import pymysql
abc = pymysql.connect(host='192.168.0.57',
                      port=3306,
                      user='root',
                      password='123456')
you = abc.cursor()
you.execute('show databases;')
you.execute('use shuju;')
you.execute('show tables;')
you.execute('select * from excel;')
aa = you.fetchall()
you.execute('desc excel;')
bb = you.fetchall()
excel = xlrd.open_workbook('text.xls')
new_excel = copy(excel)
sheet = new_excel.get_sheet(0)
print(aa[0][0])
for i in range(len(aa)):
    for j in range(len(bb)):
        if i == 0:
            sheet.write(i,j,bb[j][0])
        else:
            sheet.write(i,0,aa[j][0])
            sheet.write(i,1,aa[j][1])
            sheet.write(i,2,aa[j][2])
new_excel.save('text.xls')


