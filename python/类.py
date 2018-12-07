class Python():
    def zhishu(self,a,b):
        s=0
        for i in range(a,b):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                s+=i
        print(s)


    def huiwen(self,a):
        b=len(a)//2
        for i in range(b):
            if a[i] != a[-i-1]:
                print('no')
                break
        else:
            print('yes')

    def zuida(self,a):
        b=a.copy()
        b.sort()
        c=a.index(b[0])
        d=a.index(b[-1])
        a[d],a[0]=a[0],a[d]
        a[c],a[-1]=a[-1],a[c]
        print(a)

    def shiliu(self,a):
        b=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        c=''
        while True:
            a1=a%16
            a=a//16
            c=c+b[a1]
            if a == 0:
                break
        print(c[::-1])

    def jiujiu(self,a,b):
        for i in range(a,b):
            for j in range(1,i+1):
                print('{}*{}={}'.format(j,i,i*j),end='\t')
            print()
a=Python()
a.shiliu(200)
a.huiwen('qweewq')
a.zhishu(100,1000)
a.jiujiu(2,7)


#!/usr/bin/env python
# -*- coding:utf -* -*-
p=0
alll=0
s=0
all=int(input('请输入总资产'))
goods = [
    {'name': '电脑', 'price': 1999},
    {'name': '鼠标', 'price': 10},
    {'name': '游艇', 'price': 20},
    {'name': '美女', 'price': 998}
        ]
for i,j in enumerate(goods):
    print(i+1,j['name'],j['price'])
    yugou=[]
    ygjg=[]
    ygsp=[]

print('已进入购物车，按exit退出购物车')
while True:
    b=input('请输入商品号')
    if b=='exit':
        print('已退出购物车')
        break
    elif int(b)==0 or int(b) > 4:
        print('对不起，没有这个商品编号，请重新输入')
        continue
    ygsp.append(goods[int(b)-1]['name'])
    ygjg.append(goods[int(b)-1]['price'])
print('你要买的商品{}'.format(ygsp))
print('你要买的商品单价{}'.format(ygjg))
for i in ygjg:
    p+=i
print('你要买的商品总价{}'.format(p))
while True:
    if all < p:
        print('是否删除购物车商品，删除输入yes,不删除输入no。')
        break
yn = input('是否删除购物车商品')
if yn=='no':
    cz = int(input('你要充值多钱'))
    alll = alll + cz + all
    if alll<p:
        print('余额不足，1请充值')
        cz = int(input('你要充值多钱'))
        alll = alll + cz + all
    else:
        print('商品已购买，谢谢惠顾')
if yn=='yes':
    shanchu = int(input('要删除的商品编号'))
    print(shanchu)
if shanchu==b:
    ygsp.remove(goods[shanchu-1]['name'])
    ygjg.remove(goods[shanchu-1]['price'])
print(ygsp)
print(ygjg)
print('你现在要买的商品{}'.format(ygsp))
print('你现在要买的商品单价{}'.format(ygjg))
for j3 in ygjg:
    s += int(j3)
print('你现在要买的商品总价{}'.format(s))
while True:
    if alll<p:
        print('余额不足，1请充值')
        break
    cz = int(input('你要充值多钱'))
    alll = alll + cz + all
else:
    print('商品已购买，谢谢惠顾')