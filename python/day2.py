#基础语句
#判断语句   循环语句   异常处理语句  上下文管理语句

#判断语句
# a = 45
# if a > 40:
#     print('hello')
# else:
#     print(123)
a='d'

print(b)
# a = input('请输入成绩')
# a = int(a)
# if a >= 90:
#     print('优秀')
# elif a >= 80:
#     print('良好')
# elif a >= 70:
#     print('及格')
# elif a >=0:
#     print('废物')

# a = input('请输入字符串')
# if a.startswith('a'):
#     if a.endswith('c'):
#      print('hello world')
# elif a.endswith('c'):
#        print('hello')
# else
#     print('world')
# else:
#        print(123)


# a=input('<<<<')
# if a.startswith('a'):
#     if a.endswith('c'):
#         print('hello world')
#     else:
#         print('hello')
# elif a.endswith('c'):
#     print('world')
# else:
#     print(123)


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






#循环语句  for  while
#for 语句  格式：
#注意：1、没有do和done
#      2、冒号和缩进
# for 变量名 in 范围 ：
#     执行语句
#     执行语句
    # 执行语句
#     。。。



# a = 0
# for i in range(1,101):
#     a+=i
# print(a)

# print(sum(range(101)))

# a={'name':123,'age':123,'sex':123}
# # for i,j in a.items():
# #     print(i,j)

# a=0
# b=0
# for i in range(1,100,2):
#     a=a+i
# for j in range(2,100,2):
#     b=b+j
# print(a-b)
# a=['123','wqe','ewqr',[1,2,3]]
# for i,j in enumerate(a[1]):
#     print(i,j)

# a=['电脑','计算机','MP3']
# for i,j in enumerate(a):
#     i+=1
#     print(i,j)
# b=input('<<')
# b=int(b)
# print(a[b-1])

# b = 0
# for a in range(1,100):
#     if a % 2 == 0:
#         b = b - a
#     else:
#         b = b + a
# print(b)

# import random
# a=random.randrange(1,10)
# c.inp

#
# for i in range(3):
#     for j in range(2):
#         for k in range(2):
#             print(123)
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         # if j <= i:
#         print("{}*{}={}".format(j,i,i*j),end='\t')
#         # else:
#     print()
#             # break


# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}".format(j,i,i*j),end='\t')
#     print()
# a=0
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         a=a+i
# print(a)


# import random
# a=random.randrange(1,10)
# for b in range(1,4):
#     b = int(input('<<'))
#     if b == a:
#        print('正确')
#        break
#     elif b < a:
#        print("小了")
#     elif b > a:
#        print("大了")
# else:
#     print('笨蛋')


# for i in range()

# a=int(input('<<<'))
# b=1
# c=0
# for i in range(1,a+1):
#     if i<a+1:
#         b=b*i
#         c=c+b
# print(c)
#!/usr/bin/env prthon
# a=['电脑','计算机','MP3']
# for i,j in enumerate(a):
#     print(i+1,j)
# b=int(input('商品编号'))
# print(a[b-1])

# a=input('<<<')
# b=a.split()
# b.sort()
# a1=b.index(max(b))
# a2=int(b[1])
# a3=int(b[2])
# if a1+a2>a3:
#     if a1**2+a2**2==a3**2:
#         print('直角三角形')
#     elif a1**2+a2**2<a3**2:
#         print('钝角三角形')
#     else:
#         print('锐角三角形')
# else:
#     print('不能组成三角形')

#!/usr/bin/env prthon
# -*- coding:utf -8 -*-
# import random
# a=random.randrange(1,10)
# for i in range(1,4):
#     b=int(input('<<<'))
#     c=3-i
#     if a==b:
#         print('正确')
#         break
#     elif a>b:
#         print('小了')
#         print('你还有{}次机会'.format(c))
#     elif a<b:
#         print('大了')
#         print('你还有{}次机会'.format(c))
# else:
#     print('笨蛋')

#
# a=[1,2,33,45,12,3,12,21,3]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#         b.sort()
# print(b)




# a=1
# c=0
# while a < 101:
#     c=c+a
#     a+=1
# print(c)
# a=0
# for i in range(1,101):
#     a=a+i
# print(a)
#!/usr/bin/env prthon
#-*- coding:utf -8 -*-
# import random
# a=random.randrange(1,20)
# print(a)
# while True:
#     b = int(input('<<'))
#     if b == a:
#        print('苹果电脑一台')
#        break
#     elif b == a-1:
#        print("苹果手机一部")
#        break
#     elif b == a-2:
#        print("56寸大电视一台")
#        break
#     else:
#         print('谢谢惠顾')
#         break
# else:
# #     print('笨蛋')

# while True:
#     while True:
#         for i in range(1,10):
#             if i == 9:
#                 break
#             else:
#                 print(i)
#         break
#     break
# a=1
# while a < 10:
#     b=1
#     while b <=a:
#         print('{}*{} ={}'.format(b,a,a*b),end='\t')
#         b+=1
#     print()
# a+=1

# a=0
# while a < 3:
#     print('hello')
#     break
# else:
#     print('123')
# a=[1,2,3,32,12,43]
# print(sum(a)/6)




#
# while True:
#     a=input('请输入一组数字')
#     if a=='exit':
#         break
#     b=a.split()
#     c=len(b)
#     for i,j in enumerate(b):
#         b[i]=int(j)
#     k=sum(b)/c
#     print(k)
#     for z in b:
#         if z < k:
#             print(z)

#
#
#
#打印平均值以及比平均值小的，exit时推出
# while True:
#     a=input('>>>')
#     if a=='exit':
#         break
#     b=a.split()
#     c=len(b)
#     for i,j in enumerate(b):
#         b[i]=int(j)
#     print(sum(b)/c)
#     for w in b:
#         if w < sum(b)/c:
#             print(w)



#
# a=[1,1,1,5,5,3,4,2,3,7,0,9,6,5]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#         b.sort()
# print(b)

#水仙花数
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)

# 字符串变整数 不用int
# a=input('<<<')
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             s+=h*10**i
# print(s)
# print(type(s))
#十进制转十六进制
# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b=int(input('<<<<'))
# f=''
# while True:
#     c=b%16
#     b=b//16
#     f+=a[c]
#     if b==0:
#         break
# print(f[::-1])
# 判断是否为回文字符串
# a='qwerrewq'
# b=len(a)//2
# for i in range(b):
#     if a[i] != a[-i-1]:
#         print('no')
#         break
# else:
#     print('yes')
#
# a='qwer2132rewq'
# b=a[::-1]
# if b==a:
#     print('yes')
# else:
#     print('no')
# a=input('aaaa')
# b=len(a)
# i=0
# while i < b:
#     if a[i] != a[-i-1]:
#         print('no')
#         break
#     i+=1
# else:
#     print('yes')
# 不动列表，把最大的放前边  最小的放后边
# a=[223,432,213,645,2321]
# b=a.index(max(a))
# c=a.index(min(a))
# a[b],a[0]=a[0],a[b]
# a[c],a[-1]=a[-1],a[c]
# print(a)
#
# a=[12,32,11,43,23,67]
# b=a.copy()
# b.sort()
# c=a.index(b[0])
# d=a.index(b[-1])
# a[d],a[0]=a[0],a[d]
# a[c],a[-1]=a[-1],a[c]
# print(a)
# a=[12,23,13,34]
# b=len(a)
# for i in range(b-1):
#     i=a.index(min(a))
#     for j in range(i+1,b):
#         if a[j]<a[i]:
#             j=a.index(min(a))
#             print(a)

# def jiujiu(a=1,x=10):
#     for i in range(a,x):
#         for j in range(1,i+1):
#             print("{}*{}={}".format(j,i,i*j),end='\t')
#         print()
# print(__name__)
# if __name__=='__main__':
#     jiujiu(8)
#     print('hello')
# jiujiu()



# def aaa(**ae):
#     print(ae)
# aaa(name=123,wqe=123)


# a=input('<<<')
# b=a[::-1]
# sum=0
# for i,j in enumerate(b):
#     for h in range(0,10):
#         if str(h)==j:
#             sum=sum+h*10**i
# print(sum)
# print(type(sum))

# a=input('>>>')
# # b=len(a)//2
# # for i in range(b):
# #     if a[i] != a[-i-1]:
# #         print('NO')
# #         break
# # else:
# #     print('YES')


# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b=int(input('<<<'))
# f=''
# while True:
#     c=b%16
#     b=b//16
#     f=f+a[c]
#     if b==0:
#         break
# print(f[::-1])

# a=[3,5,1,2,9,8]
# b=a.copy()
# b.sort()
# c=a.index(b[0])
# d=a.index(b[-1])
# a[d],a[0]=a[0],a[d]
# a[c],a[-1]=a[-1],a[c]
# print(a)
# aa = lambda x,y:x+y
# bb = lambda x,y:x-y
# cc = lambda x,y:x*y
# dd = lambda x,y:x/y
# a=input('>>>')
# if '+' in a:
#     a=a.split('+')
#     print(a)
#     print(aa(int(a[0]),int(int(a[2]))
# if '-' in a:
#     a = a.split('-')
#     print(bb(int(a[0]),int(int(a[2]))
# if '*' in a:
#     a = a.split('*')
#     print(cc(int(a[0]),int(int(a[2]))
# if '//' in a:
#     a = a.split('//')
#     print(dd(int(a[0]),int(int(a[2]))
# bb=lambda i,j:i+j
# aa=lambda i,j:i*j
# cc=lambda i,j:i-j
# dd=lambda i,j:i/j
# a=input('请输入两个数')
# if '+' in a:
#     a = a.split('+')
#     print(bb(int(a[0]), int(a[1])))
# if '-' in a:
#     a = a.split('-')
#     print(cc(int(a[0]), int(a[1])))
# if '*' in a:
#     a = a.split('*')
#     print(aa(int(a[0]), int(a[1]))) res=requests.get(url=url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,html):
#         patt=re.compile('<img src="(.*?)"/></a>')
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#         items=patt.findall(html)
#         print(items)
#         for j,i in enumerate(items):
#             new_url=i
#             respons=requests.get(url=new_url,headers=head)
#             tu=respons.content
#         with open('c.jpg'.format(j),'wb') as f:
#             f.write(tu)
#
# douban=douban()
# a=douban.wangzhi()
# douban.guolv(a)
# if '/' in a:
#     a = a.split('/')
#     print(dd(int(a[0]), int(a[1])))

import requests
import re
class douban():
    def wangzhi(self):
        url='https://book.douban.com/latest?icn=index-latestbook-all'
        head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
