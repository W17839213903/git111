# import requests
# import re
# class Baisi():
#     # def __init__(self,head):
#     #     self.head=head
#     def qingqiu(self,page):
#         url = 'http://www.doutula.com/article/list/?page={}'.format(page)
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#         response = requests.get(url=url,headers=head)
#         html = response.content.decode('UTF-8')
#         print(html)
#         return html
#     def guolv(self,html):
#         patt = re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')
#         items = patt.findall(html)
#         # for i in items:
#             # print(i)
#         return items
#     def save(self,items):
#         qq = 0
#         for i in items:
#             print(i)
#             head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#             aaa = requests.get(url=i,headers=head)
#             html1 = aaa.content.decode('UTF-8')
#             patt1 = re.compile('onerror="this.src=(.*?)">',re.S)
#             items1 = patt1.findall(html1)
#             for i in items1:
#                 f.write(i)
#                 qq+=1
# a=Baisi()
# a.qingqiu(1)
# b=a.guolv(aa)
# a.save(b)

import requests
# import os
import re
class Doutu():
    def qingqiu(self,page):
        url = 'http://www.doutula.com/article/list/?page={}'.format(page)
        head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6776.400 QQBrowser/10.3.2601.400'}
        qingqiu = requests.get(url = url,headers = head)
        html = qingqiu.content.decode('UTF-8')
        return html
    def guolv(self,html):
        url = re.compile(r'http://www.doutula.com/article/detail/(.*?)"class="list-group-item random_list')
        head1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6776.400 QQBrowser/10.3.2601.400'}
        taotu = requests.get(url = url,headers = head1)
        html1 = qingqiu.content.decode('UTF-8')
        print(html1)
a=Doutu()
b=a.qingqiu(1)
a.guolv(b)