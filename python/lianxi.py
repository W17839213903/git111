#list(列表)   srt(字符串)  float(浮点数)  tuple(元组)  dict(字典)  int(整数)  bool(布尔值)
#none(空值)   set(集合)

#第一个内置函数type(变量名)  产看数据类型
# a=89
# print(type(a))
# a='wuldss'
# print(type(a))


# a=input('<<<<')
# b=a.split()
# b.sort()
# print(b)
# a=input('<<<<')
# b=a.split()
# b.sort()
# a1=int(b[0])
# a2=int(b[1])
# a3=int(b[2])
# if a1+a2>a3:
#     if a1**2+a2**2==a3**2:
#         print('直角三角形')
#     elif a1**2+a2**2<a3**2:
#         print('钝角三角形')
#     elif a1**2+a2**2>a3**2:
#         print('锐角三角形')
# else:
#     print('不能组成三角形')

# a={12,345,123,23,34,'ewrw',213,'reaafs'}
# # a.add(5798)
# b=a.pop()
# a.remove(123)
# # print(b)
# print(a)
# a = 12
# for i in range(2,a,3):
#     print(i)
#！/usr/bin/env prthon
# a=0
# for i in range(2,101):
#      for j in range(2,i):
#           if i % j==0 :
#               break
#      else:
#           a=a+i
# print(a)

# def quchong(*arge):
#     b=[]
#     for i in arge:
#         if i not in b:
#             b.append(i)
#     print(b)
#
# quchong(9,2,9,0,4,5,3,4,7,8,9,0,4,3,1,5,2)



# a=123
# def aaa():
#     global a
#     a=999
#     print(a)
#     return a
# print(a)
# aaa()
# print(a)


# def aaa():
#     a=0
#     for i in range(2,100):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             a=a+i
#     return a
#
# print(aaa())
# print(aaa()+1)



# aa = lambda x,y:x+y
# bb = lambda x,y:x-y
# cc = lambda x,y:x*y
# dd = lambda x,y:x//y
# a=input('>>>')
# if '+' in a:
#     a=a.split('+')
#     print(aa(int(a[0]),int(a[1])))
# if '-' in a:
#     a = a.split('-')
#     print(bb(int(a[0]),int(a[1])))
# if '*' in a:
#     a = a.split('*')
#     print(cc(int(a[0]),int(a[1])))
# if '//' in a:
#     a = a.split('//')
#     print(dd(int(a[0]),int(a[1])))


# a=[]
# for i in range(10):
#     if i > 5:
#         a.append(i)
# b=[(x-2) for x in range(10) if x > 5]
# print(a)
# print(b)

#
# a=(31,214,5,23,5213)
# print(min(a))
# a=100
# print(int(0b1010))

# for i in range(1,1000):
#     a=0
#     for j in range(1,i):
#         if i%j==0:
#             a=a+j
#     if a==i:
#         print(i)
# 选择法排序
# a=input('>>>>')
# b=a.split()
# c=len(b)
# for i in range(0,c):
#     for j in range(i+1,c):
#         if int(b[i])>int(b[j]):
#             b[i],b[j]=b[j],b[i]
#             print(b[0::])
# print(b[0::])




#冒泡排序
# a=input('>>>>')
# b=a.split()
# c=len(b)
# for i in range(0,c):
#     for j in range(i+1):
#         if int(b[i])>int(b[j]):
#             b[i],b[j]=b[j],b[i]
#             # print(b)
# print(b[::-1])


# 1000以内一个数的因数之和加起来等于本身的
# for i in range(1,1000):
#     a=0
#     for j in range(1,i):
#         if i%j==0:
#             a+=j
#     if i==a :
#         print(i)
# a=[23,12,43,25,1,29]
# b=a.copy()
# b.sort()
# c=b.index(b[0])
# d=b.index(b[-1])
# a[c],a[0]=a[0],a[c]
# a[d],a[-1]=a[-1],a[d]
# print(a)
#


#打印第一大和第二大的数
# a=[5000,3,51000,51000,51000,5000]
# a.sort()
# d=a.count(a[-1])
# f=a.count(a[-d-1])
# for i in range(0,d):
#     print(a[-1])
# for i in range(0,f):
#     print(a[-d-1])

#向左移动一位，不改变列表结构
# a=[1,5,6,3,8,2]
# b=len(a)
# for i in range(b-1):
#     a[i],a[i-1]=a[i-1],a[i]
# print(a)

# a=[21,23,12,14]
# b=len(a)
# for i in range(b):
#     for j in range()


# import random
# a=random.randrange(1,21)
# while True:
#     b=int(input('<<<'))
#     if b==a:
#         print('ok')
#         break
#     elif b>a:
#         print('大了')
#     elif b<a:
#         print('小了')

# for i in range(1,1001):
#     a=0
#     for j in range(1,i):
#         if i%j==0:
#             a=a+j
#     if a==i:
#         print(i)


# a=input('>>>>')
# b=len(a)//2
# for i in range(b):
#     if a[i]  != a[-i-1]:
#         print('no')
#         break
# else:
#         print('yes')

# a=[1,2,3,4,5]
# b=len(a)
# for i in range(b-1):
#     a[i],a[i-1]=a[i-1],a[i]
# print(a)


# a=input('>>>')
# b=a.split()
# c=[]
# for i in b:
#     for j in b:
#         for h in b:
#             if (i != j) and (i != h) and (j != h):
#                 print(i,j,h)
#                 c.append(int(i)*100+int(j)*10+int(h))
# print(c)

# a=[1,2,3,7,8,9]
# b=int(input('>>>'))
# a.append(b)
# c=len(a)
# for i in range(0,c):
#     for j in range(i+1):
#         if int(a[i])>int(a[j]):
#             a[i],a[j]=a[j],a[i]
# print(a[::-1])

# while True:
#     a=input('>>>>')
#     if a=='exit':
#         break
#     b=a.split()
#     c=len(b)
#     for i,j in enumerate(b):
#         b[i]=int(j)
#     print(sum(b)/c)
#     for h in b:
#         if h < sum(b)/c:
#             print(w)
# a=input('>>>')
# b=a.split()
# c=b.index(max(b))
# d=b.index(min(b))
# b[c],b[-1]=b[-1],b[c]
# b[d],b[0]=b[0],b[d]
# print(b)

# a=input('请输入一组数字')
# f=a.split(',')
# for i,j in enumerate(f):
#     f[i]=int(j)
# b=f.index(max(f))
# c=f.index(min(f))
# f[c],f[0]=f[0],f[c]
# f[b],f[-1]=f[-1],f[b]
# print(f)
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L = [sum(i) for i in zip([0]+L, L+[0])]
#


import requests
class Qiushi(object):
    def qingqiu(self):
        url = 'http://www.qiushibaike.com/text/page/1'
        qingqiu1 = requests.get(url=url)
        html = qingqiu1.content.decode('utf-8')
        return html
    def guolv(self):
        pass
qiushi = Qiushi()
qiushi.qingqiu()