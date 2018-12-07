#！/usr/bin/env python
#! -*- coding:utf-8 -*-

import xlrd

class 读取():
    def 读取_token(self):

        f = xlrd.open_workbook(r'D:\Python.py\py_demo\电商\data\电商.xls')
        sheet = f.sheets()[0]
        aa = sheet.col_values(4)
        return aa

    def 读取_登录(self):
        denglu=[]
        f = xlrd.open_workbook(r'D:\Python.py\py_demo\电商\data\电商.xls')
        sheet = f.sheets()[0]
        aa = sheet.col_values(2)
        bb = sheet.col_values(3)
        # print(aa,bb)
        return aa,bb

    def 读取_注册(self):
        denglu = []
        f = xlrd.open_workbook(r'D:\Python.py\py_demo\电商\data\电商.xls')
        sheet = f.sheets()[0]
        cc = sheet.col_values(0)
        dd = sheet.col_values(1)
        return cc,dd

