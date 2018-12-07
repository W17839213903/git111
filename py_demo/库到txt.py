# import  pymysql
# abc=pymysql.connect(host='192.168.0.184',
#                 port=3306,
#                 user='root',
#                 password='123456',
#                 charset='utf8')
# aaa=abc.cursor()
# aaa.execute('show databases;')
# print(aaa.fetchall())
# aaa.execute('use shujuku;')
# aaa.execute('select * from biao1;')
# aa=aaa.fetchall()
# aaa.execute('desc biao1')
# bb=aaa.fetchall()
#
# with open('a.txt','a',encoding='utf-8') as f:
#     for i in range(len(bb)):
#         if i == len(bb) - 1:
#             f.write(bb[i][0])
#         else:
#             f.write(bb[i][0]+',')
#     for j in aa:
#         f.write("{}","{}","{}".format(j[0],j[1],j[2])+'\n')
#
# # import xlrt
# f=xlrt.open_workboot('text,xls')
# new_f=copy(f)
# sheet=new_f

