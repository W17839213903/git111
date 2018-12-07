# requests  #第三方库需要下载
# 爬虫： 又叫网络蜘蛛
#模仿刘浏览器  根据自己规定的规则批量下载网络中的资源

# 正则表达式： 匹配文件中的内容

#可以模仿浏览器的模块  urllb, urllib3, requests
#匹配内容的模块  re, bs4, xpath

import requests
import re
# 爬虫分类 1.聚焦爬虫（只爬去某个网站的资源）  2.搜索爬虫（爬取整个网络的资源）
#面向对象代码  爬虫第一步：分析网址的变化
#                第二步： html文件，过滤并下载想要的文件
#                第三部：保存  保存的权限和格式
class Qiushi(object):
    def qingqiu(self,page):
        url ='https://www.qiushibaike.com/text/page/{}/'.format(page)
        #发送请求
        response = requests.get(url=url)
        #读取结果的方式   1义字符串的方式读取 2以字节码的方式读取
        # print(response.text)   #  字符串
        html=response.content.decode('utf-8')   #字节码
        return html
    def guolv(self,abc):
        shuju=[]
        patt = re.compile(r'<div class="p">(.*?)</div>', re.S)
        items = patt.findall(abc)
        for i in items:
            i=i.replace('<span>','')
            i=i.replace('</span>','')
            i=i.replace('<br/>','')
            i=i.strip()
            shuju.append(i)
        return shuju
    def save(self,shuju):
        with open('c.txt','a',encoding='utf-8') as f:
            for i in shuju:
                f.write(i+'\n')
qiushi = Qiushi()
jieguo=qiushi.qingqiu(2)
shuju=qiushi.guolv(jieguo)
qiushi.save(shuju)