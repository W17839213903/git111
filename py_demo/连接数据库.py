import pymysql
#连接数据库   先在虚拟技术授权  在刷新权限   然后在刷新防火墙规则
# grant all privileges on *.* to '用户名'@'%' identified by 密码
# fiush privileges      刷新权限
#iptables -F    刷新防火墙规则
abc=pymysql.connect(host='192.168.0.184',
                port=3306,
                user='root',
                password='123456',
                charset='utf8')
#创建游标
aaa = abc.cursor()
aaa.execute('show databases;')          #执行sql语句
print(aaa.fetchall())                    #读取上一句sql语句的结果
aaa.execute('use test1;')
aaa.execute('show tables;')
print(aaa.fetchmany())                   #只读取自定义的结果，不写默认读取一个，如果数字大于所有的结果，就全部读取。
# print(aaa.fetchall())                    #和fetchmany()连用时  fetchall 读取剩下的所有结果
print(aaa.fetchone())
print(aaa.fetchone())                      #每次读取一个结果 本身有迭代功能
print(aaa.fetchone())
print(aaa.fetchone())
aaa.execute('use zuoye;')
aaa.execute('select * from stu1;')
aa=aaa.fetchall()
aaa.execute('desc stu1;')
bb=aaa.fetchall()
with open('a.txt','w',encoding='utf-8') as f:
    for i in range(len(bb)):
        if i == len(bb)-1:
            f.write(bb[i][0])
        else:
            f.write(bb[i][0]+',')
    for j in aa:
        f.write('\n'+'{},{},{}'.format(j[0],j[1],j[2]))