# -*- coding:utf-8 -*-
# udp_client.py

import socket

HOST='10.51.4.188'
PORT=8888
ADDR=(HOST,PORT)
BUFFSIZE=1024

# 新建socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定ip和端口
sock.bind(ADDR)

# 发送和接收数据
while True:
    try:
        data=input('>>')
        if not data:
            break
        print('发送信息：',data)
        sock.sendto(data.encode(),ADDR)
        recv_data,addr=sock.recvfrom(BUFFSIZE)
        print('收到的数据：',recv_data.decode())
    except Exception as e:
        print(e)

# 关闭socket
sock.close()