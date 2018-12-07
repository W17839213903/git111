import smtplib
import email.mime.text
import email.mime.multipart

sender='m15037109541@163.com'
recver= ['m15037109541@163.com',
          '15837806865@163.com',
          'zhang15660600605@163.com',
          'xcz201807@163.com']
server='smtp.163.com'
passwd='WDB123'
message = email.mime.multipart.MIMEMultipart()
message['from'] = sender
message['to'] = recver
message['subject'] = 'python lenrn'
text = """      
送你个小姐姐"""
text = email.mime.text.MIMEText(text)
message.attach(text)

att2 = email.mime.text.MIMEText(open('a.jpg','rb').read(),'base64','utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2['Content-Disposition'] = 'attachment;filename="a.jpg"'
att3 = email.mime.text.MIMEText(open('aaa.cfg','rb').read(),'base64','utf-8')
att3["Content-Type"] = 'application/octet-stream'
att3['Content-Disposition'] = 'attachment;filename="aaa.cfg"'
message.attach(att3)

smtp123 = smtplib.SMTP_SSL(server,465)

smtp123.login(sender,passwd)
smtp123.sendmail(sender,recver,message.as_string())
smtp123.close()