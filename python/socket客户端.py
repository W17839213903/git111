# tcp
#客户端
import socket
#创建socket   封装协议
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务器     接收到的参数是元祖
soc.connect(('192.168.0.47',3000))
aaa = 'how are you'
soc.send(aaa.encode('utf-8'))
#接收响应
mag = soc.recv(1024)
print(mag.decode('utf-8'))




# #客户端
# import socket
# #创建socket   封装协议
# soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #连接服务器     接收到的参数是元祖
# a = (('192.168.0.109',3000))
# aaa = '你好吗?'
# soc.sendto(aaa.encode('utf-8'),a)
# #接收响应
# c = soc.recv(1024)
# print(c.decode('utf-8'))