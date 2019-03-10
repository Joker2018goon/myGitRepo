#! /usr/bin/env python
# -*- coding:utf-8 -*-
# tcp_server.py

import socket

HOST = ''
PORT = 8888
ADDR = (HOST, PORT)
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(ADDR)

# 监听连接的个数
sock.listen(1)

print('启动tcp服务')

# 发送和接收数据
while True:
    # 等待连接
    conn, addr = sock.accept()
    print('成功连接：',addr)
    while True:
        data=conn.recv(BUFFSIZE)
        print('收到数据：',data.decode('utf-8'))
        if data:
            conn.sendall(data)
        else:
            print(f'没收到{addr}的数据')
            break
    
    conn.close()

# 关闭socket
sock.close()