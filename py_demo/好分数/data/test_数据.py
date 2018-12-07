#!/usr/bin/env python
#! -*- coding:utf-8 -*-

import xlrd
def denglu():
    shuju = []
    f = xlrd.open_workbook(r'C:\Users\bigbaby\Desktop\inpit.xls')
    sheet = f.sheets()[0]
    aa = sheet.nrows
    for i in range(1, aa):
        bb = sheet.row_values(i)
        shuju.append(bb)
    # print(shuju)
    return shuju