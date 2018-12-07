import pymysql
abc = pymysql.connect(host='192.168.0.179',
                      port=3306,
                      user='root',
                      password='123456',
                      charset='utf8')
aaa = abc.cursor() #创建游标
aaa.execute('use shujuu')    #使用数据库
# aaa.execute('create table stu1(姓名 char(255),年龄 int,班级 char(255));')   #创建表格
list1=['小李',0,'软件测试19班']           # 空列表  为下边添加表内容使用
for i in range(1,31):                    #循环添加30
    aaa.execute('insert into stu1 values("{}",{},"{}");'.format(list1[0],list1[1]+i,list1[2]))  #往表里添加内容
    abc.commit()     #更新表数据
aaa.execute('select * from stu1;')    #查看表中内容
aa=aaa.fetchall()         #将结果赋予aa
aaa.execute('desc stu1;')   #查看表头
bb=aaa.fetchall()            #将结果赋予bb
with open('a.txt','w',encoding='utf-8') as f:     #创建一个新文件 给予写的权限
    for i in range(len(bb)):       #循环表头  如果是最后一个就直接添加进文件  否则在添加文件的同时添加一个空格
        if i == len(bb)-1:
            f.write(bb[i][0])
        else:
            f.write(bb[i][0]+' ')
    for j in aa:      #循环表里内容  依次添加到文件中
        f.write('\n'+'{},{},{}'.format(j[0],j[1],j[2]))