import pymysql
abc = pymysql.connect(host='192.168.0.20',
                      port=3306,
                      user='root',
                      password='123456',
                      charset='utf8')
aaa = abc.cursor()
aaa.execute('use shujuu')
with open('a.txt','r', encoding = 'utf-8') as f:
    a=f.readlines()
for i in a:
    print(i)
    b=i.split(',')
    aaa.execute('insert into stu1 values("{}",{},"{}");'.format(b[0],b[1],b[2]))
aaa.execute('select * from stu1;')
print(aaa.fetchall())


23

# import xlrd
# import pymys
# abc = pymysql.connect(host='192.168.0.26',
#                       port=3306,
#                       user='root',
#                       password='123456')
# with open('b.txt','r',encoding='utf-8') as f:
#     aa=f.readlines()
# youbiao = abc.cursor()
# youbiao.execute('create database shujuu;')
# youbiao.execute('use shujuu;')
# for i in aa:
#     bb=i.split(' ')
#     print(bb[0],bb[1],bb[2])
# # for j in range(len(aa)):
# #     if j == 0:
# #        youbiao.execute('create table aaa({} char(255),{} float,{} char(255));'.format(bb[0],bb[1],bb[2]))
# #
# #     else:
# youbiao.execute('insert into aaa values ("{}","{}","{}")'.format(bb[0],bb[1],bb[2]))



import xlrd
import pymysql
abc = pymysql.connect(host='192.168.0.57',
                      port=3306,
                      user='root',
                      password='123456',charset='utf8')
youbiao = abc.cursor()
# youbiao.execute('create database shujuu1;')
youbiao.execute('use test;')
with open('b.txt','r',encoding='utf-8') as f:
    aa=f.readline()
    bb=aa.split(' ')
    youbiao.execute('create table biao_6({} char(10),{} float,{} char(10));'.format(bb[0], bb[1], bb[2]))
    aa=f.read().split('\n')
    for j in aa:
        bb=j.split(' ')
        youbiao.execute('insert into biao_6 values("{}","{}","{}")'.format(bb[0],bb[1],bb[2]))
abc.commit()
