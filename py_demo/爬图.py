#百思不得姐
import requests
import re
class Baisi():
    def qingqiu(self):  ###请求获取html
        url123='http://www.budejie.com/pic/1'###URL
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
        response = requests.get(url=url123,headers=head)##发送请求
        html=response.content.decode('UTF-8')###把响应解析为html  字节码的格式
        return html
    def guolv(self,html):###过滤获得图片的URL
        patt = re.compile(r'"http://mpic.spriteapp.cn(.*?)1.jpg"')#过滤URL的条件
        items = patt.findall(html)##过滤后的内容
        return items
    def save(self,items):
        for j,i in enumerate(items):
            i = i.replace('"','')
            i = 'https://mpic.spriteapp.cn' + i + '1.jpg'
            print(i)
        #保存图片
            tupian = requests.get(i,verify=False)##发送请求
            res1 = tupian.content##获取图片，解析为二进制
            with open('{}.jpg'.format(j),'wb') as f:
                f.write(res1)
baisi = Baisi()
aaa = baisi.qingqiu()
bbb = baisi.guolv(aaa)
baisi.save(bbb)

