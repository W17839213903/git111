# import smtplib    #发送邮件的协议
# import email.mime.text   #处理发送的内容
# import email.mime.multipart  #处理邮件的表头
#
# sender='WDB17839213903@163.com'        #发送者
# recver=  'doungln@163.com'
#         # '1454952416@qq.com']        #接收者
# server='smtp.163.com'                #服务器地址
# passwd='WDB123'                     #授权码
# #创建一个空邮件
# message = email.mime.multipart.MIMEMultipart()
# message['from'] = sender   #发件人
# message['to'] = recver  ##收件人
# message['subject'] = 'python lenrn'  #主题
# text = """
# 送你个小姐姐"""  #正文
# text = email.mime.text.MIMEText(text)     #处理文本信息
# message.attach(text)   #蒋处理后的信息添加到邮件里
#
# #添加附件： 处理方式 ：一二进制的方式读取文件
# att2 = email.mime.text.MIMEText(open('a.jpg','rb').read(),'base64','utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2['Content-Disposition'] = 'attachment;filename="a.jpg"'
# message.attach(att2)
# #定义服务器和端口
# smtp123 = smtplib.SMTP_SSL(server,465)
#
# #登录服务器
# smtp123.login(sender,passwd)
# #发送文件
# smtp123.sendmail(sender,recver,message.as_string())
# #断开连接
# smtp123.close()






#时间模块
import time
# print(time.time())              ##时间戳  代表从1970年到现在所经过的秒数
# print(time.localtime())        #本地时间  显示结果是一个元组  默认显示1是当前时间
# print(time.localtime())


#  格式化成现在的时间
# print(time.strftime('%Y %m %d %H-%M-%S %w',time.localtime(32535187199)))


# print(time.strptime('1970 12 12','%Y %m %d'))    #将现在时间格式化为元组


#将元组时间格式化为时间戳
# a=(time.strptime('1970 12 12','%Y %m %d'))
# b=(3000,12,31,23,59,59,32,21,32)
# print(time.mktime(b))

#休眠
# print(time.sleep(5))
# print(12323213)


a=input('请输入年月日')
b=a.split()
if b[0][3]==0 and b[0][4]==0 and int(b[0])//400 :
    print('{}是闰年'.format(a))
if b[0][3]==0 and int(b[0])//4:
        print('{}是闰年'.format(a))
else:
    print('{}是平年'.format(a))
c=(time.strptime('{}'.format(a),'%Y %m %d'))
print('今天是周{}'.format(c[-3]+1))
print('今天是一年中的第{}天'.format(c[-2]))

