# class Gouwuche():
#     goods = [
#         {"name":"电脑","price":1999},
#         {"name":"鼠标","price":10},
#         {"name":"游艇","price":20},
#         {"name":"美女","price":998}
#         ]
#     gouwuche = []
#     def __init__(self,zichan):
#         self.zichan = zichan
#     def goumai(self,zichan):
#         zongjia=0
#         for i in self.gouwuche:
#             for j in self.goods:
#                 if i == j['name']:
#                     zongjia+=j['price']
#         if self.zichan < zongjia:
#             print('你的余额不足，选择你接下来的操作')
#             c = input('请输入充值或者删除')
#             if c =='充值':
#                 self.充值()
#             else:
#                 self.删除()
#         else:
#             self.zichan = self.zichan - zongjia
#             print('购买成功，显示余额{}'.format(self.zichan))
#     def 充值(self):
#         a = int(input('请输入充值金额'))
#         self.zichan += a
#         print(self.zichan)
#     def 删除(self):
#         b = input('请輸入刪除的物品')
#         self.gouwuche.remove(b)
#         self.goumai(self.zichan)
#     def chaoshi(self):
#         for i,j in enumerate(self.goods):
#             print(i+1,j['name'],j['price'])
#         gouwche = []
#         while True:
#             xuhao = input('请输入商品序号，输入exit退出')
#             if xuhao == 'exit':
#                 break
#             else:
#                 self.gouwuche.append(self.goods[int(xuhao)-1]['name'])
#         self.goumai(self.zichan)
# zichan = int(input('>>'))
# gou = Gouwuche(zichan)
# gou.chaoshi()
# gou.goumai(zichan)
