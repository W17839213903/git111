#！/usr/bin/env python
#! -*- coding:utf-8 -*-
import unittest
from 框架.config.学校_接口 import 学校
from 框架.data.数据 import duqu
class 考试(unittest.TestCase):

    tes_学校 = 学校.学校_快查
    shuju = duqu()

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