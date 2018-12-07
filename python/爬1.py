#导入正则表达式模块   只能过滤字符串
import re      #re可以将字符串编译成Python能识别的
#
# a='qwe123qweqwe456qwe'
# #将要匹配的正则编译
# b=re.compile('qwe.*?qwe')
# d=re.compile('qwe')
# #到目的字符串中去查找
# c=b.findall(a)
# f=d.findall(a)
# print(c,f)

#贪婪模式和非贪婪模式
#贪婪模式：尽可能多的去匹配最后的字符串
#非贪婪模式： 尽可能少的去匹配最后的字符串
#带 ？ 的 是非贪婪   带 * 的 是贪婪    ？为第一优先级  以？为主
# .匹配任意一个字符   除了换行符
#re.S
# a="""qwe12
# 3qweqwe456qwe"""
# b=re.compile('qwe(.*?)qwe',re.S)
# c=b.findall(a)
# print(c)

#re.I
# a="""qwe123qweqwe456qwe"""
# b=re.compile('QWE(.*?)QWE',re.I)
# c=b.findall(a)
# print(c)

import requests
import re
# class Qingqiu():
#     def qingqiu(self,page):
#         url='http://www.17k.com/chapter/2899153/{}.html'.format(page)
#         aaa=requests.get(url=url)
#         html = aaa.content.decode('utf-8')
#         # print(html)6
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         patt=re.compile('<span class="ellipsis">(.*?)</a>',re.S)
#         htmll=patt.findall(abc)
#         print(htmll)
#         for i in htmll:
#             i = i.replace('<span>', '')
#             i = i.replace('</span>', '')
#             i = i.replace('&#12288;&#12288;','')
#             i = i.replace('<br /><br />', '\n')
#             i = i.strip()
#             shuju.append(i)
#         return shuju
#     def save(self,shuju):
#         with open('c.txt','a',encoding='utf-8') as f:
#             for i in shuju:
#                 print(i)
#                 f.write(i)
# qiushi=Qingqiu()
# jieguo=qiushi.qingqiu(35985504)
# shuju=qiushi.guolv(jieguo)
# qiushi.save(shuju)


import re
import pymysql
abc = pymysql.connect(host='192.168.0.30',
                      port = 3306,
                      user = 'root',
                      password = '123456')
aaa = abc.cursor()
aaa.execute('use test;')
aaa.execute('select * from stu;')
bbb = aaa.fetchall()
with open('a.txt','r',encoding='utf-8') as f:
    for i in bbb:
        b = re.compile(('.*'))
        print(b)
        # for j in range(len(bbb)):
        #     f.write(b)