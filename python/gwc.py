#!/usr/bin/env python
# -*- coding:utf -* -*-
a=int(input('请输入总资产'))
goods = [
    {'name': '电脑', 'price': 1999},
    {'name': '鼠标', 'price': 10},
    {'name': '游艇', 'price': 20},
    {'name': '美女', 'price': 998}
        ]
for i,j in enumerate(goods):
    print(i+1,j['name'],j['price'])
print('已进入购物车，按exit退出购物车')
# while True:
#     gouwuche = []
#     bh=input('请输入商品编号，按exit退出购物车')
#     if bh=='exit':
#         break
#     else:
#         gouwuche.append(goods[int(bh)-1]['name'])
# def goumia():
#     zongjia = 0
#     b=input('请输入商品名称')
#     for i in b:
#         for i in goods:
#             if i == j['name']:
#                 zongjia+=j['price']
#     if a < zongjia:
#         print('你的余额不足，充值还是删除购物车商品')
#         a=input('请输入充值或者删除')
#         if a == '充值':
#             pass
#
# for i in ygjg:
#     p+=i
# print('你要买的商品总价{}'.format(p))
# while True:
#     if all < p:
#         print('余额不足，请充值')
#         cz = int(input('你要充值多钱'))
#         alll = alll + cz + all
#         if all < p and alll < p:
#             print()
#         elif alll >= p:
#             print('商品已购买，谢谢惠顾')
#             break