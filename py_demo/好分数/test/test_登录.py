#!/usr/bin/env python
#! -*- conding:utf-8 -*-

import unittest
import time
from 好分数.config.好分数_接口 import 好分数
from 好分数.data.test_数据 import denglu
class 测试(unittest.TestCase):
    aaa = 好分数.登录()
    def test_1(self):
        html = self.tes_学校(self.shuju[0][0])
        self.assertEqual(html['code'], int(self.shuju[0][1]))
        self.assertIn(len(html['data']), range(int(self.shuju[0][2])))

    def test_2(self):
        html = self.tes_学校(self.shuju[1][0])
        self.assertEqual(html['code'], int(self.shuju[1][1]))
        self.assertEqual(len(html['data']), int(self.shuju[1][2]))

    def test_3(self):
        html = self.tes_学校(self.shuju[2][0])
        self.assertEqual(html['code'], int(self.shuju[2][1]))
        self.assertEqual(len(html['data']), int(self.shuju[2][2]))

    def test_4(self):
        html = self.tes_学校(self.shuju[3][0])
        self.assertEqual(html['code'], int(self.shuju[3][1]))
        self.assertEqual(len(html['data']), int(self.shuju[3][2]))