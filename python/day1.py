#!/bin/env python
# -*- coding:utf-8 -*-




#a = 'asAD '
#b = a.capitalize()   将字符串中的大写变小写，小写变大写。
#a=' sadf '
#b=a.lstrip()         #去除字符串中左边的空格
#b=a.rstrip()         # 去掉字符串中右边的空格
#b=a.strip()          #去掉字符串中两边的空格
#print(b)
#print(a)
#'sadsfFsRTsdsf'
#b=a.replace('s','123')    #替换 ：将前一个字符替换为后一个字符
# b=a.replace('s','123',3)   #1代表从左往右替换的个数
# print(b)
# a='sadsaf'
# b=a.startswith("f")     #判断字符串是否以括号中的元素开头；
#b=a.endswith('a')        #判断字符串是否以括号中的字符结尾；
# print(b)
# a='hello {},我今年{}岁'    #{}占位符
# # b=a.format('小红',23)      #format 填充占位符，格式化字符串。
# # print(b)
# a='hello %s ,我今年 %d 岁'    #{}占位符
# b=a%('小红',23)
# print(b)
# a='abcd'
# b=','.join(a)  #以指定的字符串作为分隔符，将a中所有元素组成一个新的字符串。
# print()
#
#
#以指定字符串为分隔符，将a中所有元素分割成一个列表。




# a='abc'
# b='-'.join(a)
# print(b)
# a='123'
# b=a.split(',')
# print(b)
# a='fdgasdg'
# b=a.'startswith('s')
# print(b)
#
# a='hello {},我今年{}岁'
# b=a.format('小平',23)
# print(b)
#a='hello %s ,我今年 %d 岁'





#list（列表）：一组数组的集合（等同于shell数组）
#一中括号为标识，以逗号隔开 [元素1,元素2,元素3,]
#作用：用来存储数据的
#特点：1.可变的 2支持索引  3.支持切片
#a=[2,'qwe',2,5]
#a.append(10)     #将括号里的元素添加到列表中   只能添加一个
#print(a)         #默认添加到最后
# print(a[-3][2])   #多层数据
#冒号代表所有的数据  单独一个数字表示取值的下标号
#print(a[1:3])    #切片和字符串一样   切片只取集合的某一段或者某一个
# b=["qw",'ewr','ewr','try']
# a=[13,23,34,56,b]
# a[4].insert(2,'abc')   #第一个参数是下表位置，第二个参数是添加的元素
# # #a.remove(13)          #删除里边某个元素
# # a.pop(0)               #删除下标所在元素
# print(a)
# b=[23,2,4,'wqe']
# a=[2,'wee',2,2,2,2,21,3,b]
# a.remove(2)
# print(a)
# c=a[4].index(23)               #获取某元素的下标值
# c=a.count(2)                     #统计某元素在列表中一共有多少个
# d=len(a)
# print(c)
# print(d)
#第二个python内置函数 len()  统某数据类型中有多少个元素
##c=['a','A']
# a.reverse()  #反转列表
# b.reverse()
#b.sort(reverse=True)      #排序   默认是升序  必须处于同一数据类型  列表不能排序
#b.reverse()
#a.clear()                #清空列表
# import copy
# b = [23, 2, 4, 5, 7]
# b.clear()
# print(b)
# a = [2, 21, 3, b]
# f=a.copy()   #复制列表  前复制：只能复制第一层的数据
# f=copy.deepcopy(a)   #复制列表  深复制：完完全全的复制一遍
# a.append(100)
# a[3].append(100)
# print(a)
# print(f)
# a=[1,2,3,5,6]
# b=[2,'wer',4,3]
# a.extend(b)    #将b里边所有的元素更新到a里边去 （就是把b里的元素添加到a里边去）
# print(a)
# print(b)



#tuple（元组）  一组数据的集合，用来存储数据的
#一小括号为标识，以逗号隔开
#特点：1，不可变得。  2、支持索引。   3、支持切片

a = (123,345,23,'1234')  #只有一个元素时必须加逗号
#print(type(a))
# a.count(23)      #计算元素在元组中有多少个
# a.index(23)       #获取某元素的下标位置
c=a.count(23)
d=a.index(23)
print(c,d)


#dict(字典) 存储数据的，数据格式 ： key=value
#以键值对的方式存储书据
#以大括号为表识，以逗号隔开。
#特点：1、可变的。  2、无序的。   3、不支持索引
#字典中的键(key)
#必须是唯一的
# a = {'name':'小明','age':20,'sex':'男'}
# b = {'wer':12}# print(c)
# a.update(b)  #将字典中b的所有元素更新到a中。
# print(a)
# a['six']=666  #添加
# a.pop('name')   #删除key所在的键值对
# a.popitem()      #默认删除最后一个
# b=a.keys()       #获取所有的key
# c=a.values()     #获取所有的值
# b=a.items()       #获取所有的键值对
# print(b)
# print(c)
#a = {'name': '小明', 'age': 20, 'sex': '男'}
#b = {'wer': 12}
# a['name'] = '123'     #更改键的值


#set(集合) 一组数据的集合  ，储存数据的，
#一大括号来标识得，以逗号分开  {1,2,34,32,43}
#特点：1、不重复的   2、无序的   3、不支持索引  4、可变的
#a={12,345,12,23,34}
#a.add('ewerewt')    #添加一个元素，但是不能添加列表  能添加元组
#a.pop()              #默认删除最后一个
#a.remove(12)    #删除括号中的元素
#print(a)

# a={1,2,3,4}
# b={21,3,4,55}


# a.update(b)
# # 并集  |      并集 &
# print(a|b)
# print(a&b)
# print(a)
# print(b)
# a = input('>>>>')
# a = int(a)
# print(type(a))
#import copy
# b = ['wqe','ewr','ret']
# a = [2,'qwe',3,2,5,b]
# a.append(10)
# f = a.copy()
# print(f)
# # b.append(100)
# print(a)
# print(b)


#a = [12,2,31,87,1,92]
# a.append(10)
# print(a)
# a.insert(1,'shazi')
# print(a)
#a.remove(1)
#a.pop(2)
#f = a.index(3)
#f = a.count(1)
#a.reverse()
#a.sort()
#a.sort(reverse=True)
#print(a)

# a = [1,2,3,4,5]
# # #a.clear()
# # b=[3,5,6,7,8]
# # a.extend(b)
# # print(a)
# a=[12,24,21,34,12,21]
# a=set(a)
# a=list(a)
# #a.sort()
# a.sort(reverse=True)
# print(a)


#运算符
#不需要命令
#算术运算符 +(加) -(减) *(乘) /(除)  **(幂) //(整除)
# a='dfg'>'abc'
# print(a)
#比较运算符   >    <   ==  !=  >=  <=
#成员运算符   in（在）  和   not  in（不在）
# a=[1.234,34,23,4]
# print(1 in a)
#逻辑运算符  与（and） 或（or）  非（not）

#赋值运算符 +=  -=  *=  /=  **=  //=

# a=3+4
# # a+=5
# # a-=4
# # a*=3
# # print(a)


# a=[9,23,12,43,9,34,23]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# for j in range(len(b)):
#     for k in range(i+1,len(b)):
#         if b[i] > b[i+1]:
#             b[i],b[i+1]=b[i+1],b[i]
# print(b)

# a='q,w,e,r,t,y'
# b=a.split(',')
# print(b)
# a=input('>>')
# b=a.split(',')
# print(b)
# a='qwe'
# b='_'.join(a)
# print(b)

# a=[1,2,3]
# b=[]
# a.append('wqe')
# a.remove(3)
# a.pop(2)
# a.insert(3,'qwweqr')
# b=a.index(2)
# b=a.count(2)
# a.sort()
# a.sort(reverse=True)
# a.clear()
# import copy
# b=copy.deepcopy(a)
# print(b)
# b.extend(a)
# a.reverse()
# print(a)




# a=(123,456,23,1234)
# a.index(23)
# print(b)

# diet(字典)   存储数据的   数据格式  key=value
# 以键值对的方式存储数据
# 亿大括号标识  小括号隔开
# 特点 可变的  无序的 不支持索引
# 字典中的key必须是唯一的

#
# a.update(b)   #将b中的所有元素更先到a中
# a['qaz']='qwer'   #添加键值对到a中
# a.pop('age')     #删除key所在的键值对
# a.popitem()       #默认删除最后一 个    因为无序   所以随机删除
# b=a.keys()    #获取所有的的key
# b = a.values()   #获取所有的值
# b = a.items()    #获取所有的键值对
# a['name'] = '66666'   #更改键的值
# print(a)0


# # set(集合)
# a={1,2,3,4,5,6,67}
# a.add((123,1,2,3,4))   #添加元素到集合中
# a.pop()       #删除元素  默认最后一个
# a.remove(2)   #删除括号中元素
# print(a)
