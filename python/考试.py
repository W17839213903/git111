import requests
import re
import json
class  Boss():
    def qingqiu(self):
        url = 'https://www.zhipin.com/job_detail/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88'
        heads={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"}
        qingqiu = requests.get(url=url,headers=heads)
        html = qingqiu.content.decode('utf-8')
        # print(html)
        return html
    def guolv(self,html):

        patt = re.compile('<div class="job-primary">.*?<div class="job-title">(.*?)</div>.*?<span class="red">(.*?)</span>.*?<em class="vline"></em>(.*?)<em class="vline"></em>(.*?)</p>.*?</li>',re.S)
        quanbu = patt.findall(html)
        print(quanbu)
        return quanbu

a=Boss()
b=a.qingqiu()
a.guolv(b)