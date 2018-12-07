#!/usr/bin/env python
# -*- coding:utf -* -*-
alll=0
s=0
all=int(input('请输入总资产'))
# def goods():
goods = [
    {'name': '电脑', 'price': 1999},
    {'name': '鼠标', 'price': 10},
    {'name': '游艇', 'price': 20},
    {'name': '美女', 'price': 998}
        ]
for i,j in enumerate(goods):
    print(i+1,j)
# goods()
def xuan():
    num=0
    yumai=[]
    print('已进入购物车，按exit退出购物车')
    while True:
        b=input('请输入商品号')
        if b=='exit':
            print('已退出购物车')
            break
        elif int(b) == 0 or int(b) > 4:
            print('对不起，输入错误，请重新输入')
            continue
        else:
            yumai.append(goods[int(b)-1])
    print(yumai)
    for i,j in enumerate(yumai):
        num+=j['price']
    print('你要买的商品总价{}'.format(num))
    return num
num=xuan()
def shanchu():
    sc=input('请输入你要删除的商品编号')

def chongzhi():
    if all < num:
        print('余额不足，请充值')
    else:
        print('')

        print('商品已购买，谢谢惠顾。')
yn = input('是否删除')
if yn=='no':
    cz = int(input('你要充值多钱'))  alll = alll + cz + all
    if alll<num:
        print('余额不足，1请充值')

    else:
        print('商品已购买，谢谢惠顾')
# if yn=='yes':
#     shanchu = int(input('要删除的商品编号'))
#     print(shanchu)
# if shanchu==b:
#     ygsp.remove(goods[shanchu-1]['name'])
#     ygjg.remove(goods[shanchu-1]['price'])
# print(ygsp)
# print(ygjg)
# print('你现在要买的商品{}'.format(ygsp))
# print('你现在要买的商品单价{}'.format(ygjg))
# for j3 in ygjg:
#     s += int(j3)
# print('你现在要买的商品总价{}'.format(s))
# while True:
#     if alll<p:
#         print('余额不足，1请充值')
#         break
#     cz = int(input('你要充值多钱'))
#     alll = alll + cz + all
# else:
#     print('商品已购买，谢谢惠顾')