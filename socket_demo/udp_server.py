#! /usr/bin/env python
# -*- coding:utf-8 -*-
# udp_server.py

import socket

HOST = ' '  # localhost:本机， ip值，空：任意主机都可以访问
PORT = 8888
ADDR = (HOST, PORT)
BUFFSIZE=1024

# 新建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定ip和端口
sock.bind(ADDR)

# 发送和接收数据
while True:
    try:
        print('UDP SERVER START...')
        data, addr = sock.recvfrom(BUFFSIZE)
        print('test.....')
        print('get:', data.decode()) # bytes -> str
        sock.sendto(data, addr)
    except Exception as e:
        print(e)

# 关闭socket
sock.close()