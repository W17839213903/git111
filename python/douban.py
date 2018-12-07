import requests
import re
import xlwt
import xlrd
from xlutils.copy import copy
class Douban:
    def qingqiu(self,page):
        url = 'https://book.douban.com/top250?start={}'.format(page)
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        aaa = requests.get(url=url,headers=head)
        html = aaa.text
        return html

    def guolv(self,html):
        shuming1 = []
        jianjie1 = []
        patt = re.compile(r'<table width="100%">(,*?)</table>',re.S)
        items = patt.findall(html)
        for i in items:
            shuming = re.findall(r'title="(.*?)"',re.S,i)
            jianjie = re.findall(r' <span class="inq">(.*?)</span>',i)
            if len(jianjie) == 0:
                jianjie.append('没有')
            shuming1.append(shuming[0])
            jianjie1.append(jianjie[0])
        print(shuming1,jianjie1)
        return shuming1,jianjie1
    def save(self,shuju):
        f = xlwt.Workbook(encoding='utf-8')
        sheet=f.add_sheet('sheet1')
        sheet.write()



        f.save('test.xls')

dou = Douban()
a=dou.qingqiu(25)
b=dou.guolv(a)
print(b)
























# import requests
# import re
# import xlwt
# import xlrd
# import xlutils
#
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
#
# class Douban:
#
#     def qingqiu(self,page):
#         url = 'https://movie.douban.com/top250?start=50&filter='.format(page)
#         res=requests.get(url=url,headers=head)
#         a=res.content.decode('utf-8')
#         return a
#
#     def guolv(self,a):
#         patt = re.compile('<img width="100" alt="(.*?)" src="https://img')
#         items =patt.findall(a)
#         return items
#
#     def guolv2(self,a):
#         patt = re.compile('<span class="inq">(.*?)</span>')
#         items =patt.findall(a)
#         return items
#
# aaa=1
# dou=Douban()
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('sheet1')
# sheet.write(0, 0, '电影名')
# sheet.write(0, 1, '简介')
# for i in range(0, 250, 25):
#     a=dou.qingqiu(i)
#     b=dou.guolv(a)
#     for j in b:
#         sheet.write(aaa, 0, '{}'.format(j))
#         aaa+=1
# f.save('test2.xls')
# aaa=1
# from xlutils.copy import copy
# f = xlrd.open_workbook('test2.xls')
# new_f=copy(f)
# sheet2=new_f.get_sheet(0)
# for i in range(0, 250, 25):
#     a=dou.qingqiu(i)
#     b=dou.guolv2(a)
#     for j in b:
#         sheet2.write(aaa, 1, '{}'.format(j))
#         aaa+=1
# new_f.save('test2.xls')