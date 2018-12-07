#！/usr/bin/env python
#! -*- coding:utf-8 -*-

import requests
from 电商.data import test_数据
class 电商_接口():

    def 电商_注册(self):
        shuju = test_数据.读取_token()
        canshu = test_数据.读取_注册()
        for i in shuju:
            url = 'http://www.zhaoapi.cn/user/reg'
            headers = {"token":'{}'.format(i)}
        for j in canshu:
            response = requests.get(url=url,headers=headers,params=j)
            aaaa = response.json()

        print(aaaa)
        # return aaaa
bb = 电商_接口()
bb.电商_注册()