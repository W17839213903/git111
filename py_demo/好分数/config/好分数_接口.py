#!/usr/bin/env python
#! -*- encoding:utf-8  -*-

import unittest
from 好分数.data.test_数据 import denglu
import requests
class 好分数(unittest.TestCase):
    shuju = denglu()
    def 登录(self):
        for i in self.shuju:
            url = "http://testsupport-be.haofenshu.com/v1/accounts/session"
            payload = "account={}&password={}&undefined=".format(i[0],int(i[1]))
            headers = {
                'Content-Type': "application/x-www-form-urlencoded",
                'cache-control': "no-cache",
                'Postman-Token': "2aadfd21-6016-4365-83dd-126c02de9e56"
            }
            response = requests.request("POST", url, data=payload, headers=headers)

            html = response.json()
            # print(html)
        return html
# a=好分数()
# a.登录()