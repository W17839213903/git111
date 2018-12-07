#!/usr/bin/env python
#! -*- encoding -*-

import unittest
from 测试包.config.学校_接口 import 学校_查询
from 测试包.data.test_数据 import duqu

class 学校(unittest.TestCase):

    tes_学校 = 学校_查询().学校_快查
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