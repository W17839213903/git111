#！/usr/bin/env python
#! -*- coding:utf-8 -*-

import xlrd
def duqu():
    shuju=[]
    f=xlrd.open_workbook(r'D:\Python.py\py_demo\测试包\data\text.xls')
    sheet = f.sheets()[0]
    aa = sheet.nrows
    for i in range(1,aa):
        bb = sheet.row_values(i)
        shuju.append(bb)
    return shuju