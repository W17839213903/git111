# server 端

import socket
# 创建socket    封装协议(第一个协议：ipv4协议，第二个协议：使用TCP的协议)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定ip和端口号    bind 接受的数据为元组
host = ('192.168.0.47',3000)
s.bind(host)
#监听   (数字)  表示最大等待数
s.listen(3)
while True:
    #接受请求
    a,b = s.accept()    #第一个结果a：是客户端的连接信息 第二个结果b：客户端的ip地址和端口号
    #接受数据
    msg = a.recv(1024)        #1024代表每次接受的最大字节数
    print(msg.decode('utf-8'))
    #发送响应0
    reg = 'welcome'
    a.send(reg.encode('utf-8'))