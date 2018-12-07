import requests
import re
import xlrd
class Qingqiu():
    def qingqiu(self,page):
        url='https://book.douban.com/top250?start={}'.format(page)
        aaa=requests.get(url=url)
        html = aaa.content.decode('utf-8')
        # print(html)
        return html
    def guolv(self,html):
        shuju=[]
        shuju1=[]
        patt1=re.compile('&#34; title=(.*?)</a>',re.S)
        patt=re.compile('<span class="inq">(.*?)</span>',re.S)
        htmlll=patt1.findall()
        htmll=patt.findall(abc)
        print(htmll)
        for i in htmlll:
            for j in htmll:
                i = i.strip()
                j = j.strip()
                shuju.append(i)
                shuju1.append(j)
        print(shuju,shuju1)
        return shuju,shuju1
    def save(self,shuju):
        f=xlrd.open_workbook('text.xls')
        sheet=f.sheet_by_name('python操作excel')
        for i in shuju:
                b=len(i)
                print(i)
                for j in range(b):
                    f.write(j,0,i[0])
                    f.write(j,0,i[1])
qiushi=Qingqiu()
jieguo=qiushi.qingqiu(0)
shuju=qiushi.guolv(jieguo)
qiushi.save(shuju)
###错的