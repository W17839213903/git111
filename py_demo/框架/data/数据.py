#！/usr/bin/env python
#! -*- coding:utf-8 -*-

import xlrd
def duqu():
    shuju = []
    f = xlrd.open_workbook(r'D:\Python.py\py_demo\框架\data\text.xls')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1, num):
        aaa = sheet.row_values(i)
        shuju.append(aaa)
    return shuju