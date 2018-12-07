# 面向对象： 将函数进行分类和封装，使开发更高效
#不用面向对象：做某件事
            #将大象放进冰箱
            # 1、开冰箱门
            # 2、放大象
            # 3、关门                  一直需要自己做
#用面向对象是： 先雇一个人
#               多了个对象
#               有对象去做
#               1、开冰箱门
#               2、放大象
#               3、关门                这个过程有雇的人做，不需要自己在动手做了
#只关注输入和输出

#在Python上通过类来实现某个对象的功能
#定义一个类：      class   函数（）：
                        # def  （函数名）
                        # def  （函数名）
                        # def  （函数名）
# class  Shuzi():                 #为了和函数名区分， 类名首字母一般为大写
#     def jiujiu(self):
#         print('hello')
#
#     def zhishu(self):
#         print('12')
#
#     def yinshu(self):
#         print(666)

#类的基本元素： 属性   方法
#对象 ： 是类的实例化

# Shuzi().jiujiu()
# Shuzi().yinshu()

# a=Shuzi()
# a.jiujiu()
# a.yinshu()
# a就是类的实例化
# object
#实例化 ： 1、自定义实例化：方便在类的外部去调用
         # 2、内置实例化(self):方便在类的外部去调用

#继承 ： 一个新的类拥有旧的类的所有方法
# class Shuzi():                  #(父类）
#     def __jiecheng(self,a):
#         b=1
#         c=0
#         for i in range(1,a+1):
#                 b=b*i
#                 c=c+b
#         print(c)
#         return c
#     def zhishu(self,a):
#         d=self.__jiecheng()
#         s=0
#         for i in range(2,a+1):
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 s+=i
#         return s
#
# class  aa():                                      #(子类)
#     def aaa(self):                                  #(空语句)
#         print(123)
# # aa=aa()
# # print(aa.jiecheng())
# # object
# # 多继承 ： 一个新的类拥有多个旧的类的方法
# #如果继承的多个类中有相同的方法，使用的是最左边的方法
# class bb(Shuzi,aa):
#     def aaa(self):                      #会覆盖之前的 aaa  方法
#         s=0
#         for i in range(101):
#             s+=i
#         print(s)
# bb=bb()
# print(bb.zhishu(6))
# class Shuzi():
#     name='小刚'
#     nianji=10
#     def __init__(self,a,b):
#         self.name=a
#         self.nianji=b
#     def aa(self):
#         print('hello,%s,今年%d年级'%(self.name,self.nianji))
#     def bb(self):
#         print('hello,%s,今年12岁'%(self.name))
# aa=Shuzi('旺仔牛奶',8)
# aa.aa()
# aa.bb()
# aa=Shuzi('汪汪汪',9)
# aa.aa()
# bb.__jiecheng()


# class Shuzi():
#     name='小刚'
#     nianji=10
#     def __init__(self,a,b):
#         self.name=a
#         self.nianji=b
#     def aa(self):
#         print('hello,%s,今年%d年级'%(self.name,self.nianji))
#     def bb(self):
#         print('hello,%s,今年12岁'%(self.name))
# aa=Shuzi('旺仔牛奶',8)
# aa.aa()
# aa.bb()
# aa=Shuzi('汪汪汪',9)
# aa.aa()

# class Python():
#     def zhishu(self,a,b):
#         s=0
#         for i in range(a,b):
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 s+=i
#         return s
#
#
#     def huiwen(self,a):
#         b=len(a)//2
#         for i in range(b):
#             if a[i] != a[-i-1]:
#                 print('no')
#                 break
#         else:
#             print('yes')
#
#     def quchong(self,a):
#         b=a.copy()
#         b.sort()
#         c=a.index(b[0])
#         d=a.index(b[-1])
#         a[d],a[0]=a[0],a[d]
#         a[c],a[-1]=a[-1],a[c]
#         print(a)
# aa=Python()
# aa.quchong([5,1,2,3,4])

import pymysql
#连接数据库   先在虚拟技术授权  在刷新权限   然后在刷新防火墙规则
# grant all privileges on *.* to '用户名'@'%' identified by 密码
# fiush privileges      刷新权限
#iptables -F    刷新防火墙规则
abc=pymysql.connect(host='192.168.0.184',
                port=3306,
                user='root',
                password='123456',
                charset='utf8')
#创建游标
aaa = abc.cursor()            #
aaa.execute('show databases;')          #执行sql语句
print(aaa.fetchall())                    #读取上一句sql语句的结果
aaa.execute('use test1;')
aaa.execute('show tables;')
print(aaa.fetchmany())                   #只读取自定义的结果，不写默认读取一个，如果数字大于所有的结果，就全部读取。
# print(aaa.fetchall())                    #和fetchmany()连用时  fetchall 读取剩下的所有结果
print(aaa.fetchone())
print(aaa.fetchone())                      #每次读取一个结果 本身有迭代功能
print(aaa.fetchone())
print(aaa.fetchone())
aaa.execute('create database shuju;')
#aaa = abc.cursor()
aaa.execute('use shuju;')
aaa.execute('create table biao1(name char(255),age int,banji char(255));')
q = ['消耗',1,'19class']
for i in range(30):
    aaa.execute('insert into biao1 values("{}",{},"{}");'.format(q[0],q[1]+i,q[2]))
    abc.commit()
aaa.execute('select * from biao1;')

for i in aaa.fetchall():
    print(i)

