import requests
import re
import json
class Zhilian():
    def qingqiu(self,page):
        url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize={}'.format(page)
        response = requests.get(url = url)
        html = response.content.decode('utf-8')
        print(html)
        return html
    def guolv(self,html):
        html1 = json.loads(html)
        print(html1)
        a=html1["data"]
        print(a)
zhilian = Zhilian()
aa=zhilian.qingqiu(120)
zhilian.guolv(aa)
# zhilian.erci(shuju)