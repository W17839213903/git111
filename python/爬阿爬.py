import requests
import re
class Doutu():
    def qingqiu(self,x=3):    #请求
        for i in range(1,x):
            url = 'http://www.doutula.com/article/list/?page={}'.format(x)     #斗图啦网址
            head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
            aaa = requests.get(url=url,headers=head)
            html = aaa.content.decode('UTF-8')    #编码方式
        print(html)
        return html
    def guolv(self,html):
        patt = re.compile('http://www.doutula.com/article/detail/[0-9]{7}')
        items = patt.findall(html) 
        print(items)
        return items
    def save(self,items):
        num=0
        for i in items:
            head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
            bbb = requests.get(url=i,headers=head)
            html1 = bbb.content.decode('UTF-8')
            patt1 = re.compile('"this.src=(.*?)">')
            items1 = patt1.findall(html1)
        # print(items1)

            for i in items1:
                i = i.replace("'",'')
                tupian = requests.get(i)
                res1 = tupian.content
                with open(r'D:\aaa\{}.jpg'.format(num),'wb') as f:
                    f.write(res1)
                    num+=1
doutu = Doutu()
aa=doutu.qingqiu(7)
bb=doutu.guolv(aa)
doutu.save(bb)