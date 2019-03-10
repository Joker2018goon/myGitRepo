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

print('启动http服务')

# 发送和接收数据
while True:
    # 等待连接
    print('等待连接......')
    conn, addr = sock.accept()
    print('成功连接:', addr)

    data = conn.recv(BUFFSIZE)
    if data:
        req_path = data.decode('utf-8').splitlines()[0]
        print('收到数据：', data.decode('utf-8'))
        print('收到的第一行:', req_path)
        method, path, http = req_path.split()
        name = path.replace('/', '')
        print(f'切换URL地址到{path}')

        # 返回页面
        # response = f"""HTTP/1.1 200 OK

        # <h1>Hello {name}</h1>
        # <img class="currentImg" id="currentImg" onload="alog &amp;&amp; alog('speed.set', 'c_firstPageComplete', +new Date); alog.fire &amp;&amp; alog.fire('mark');" src="https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&amp;quality=100&amp;size=b4000_4000&amp;sec=1538039776&amp;di=1caace40f3a8f803ae5320becd2094be&amp;src=http://05.imgmini.eastday.com/mobile/20180723/20180723081610_0be87edf2340a4ac9a0c734e59ff2b22_1.jpeg" data-ispreload="0" width="349.00398406375" height="365" style="top: 0px; left: 254px; width: 480px; height: 502px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">
        # """.encode()
        # conn.sendall(response)  # 编码到bytes

        # 返回json数据，必须用双引号，注意编码 浏览器默认 gbk 网页显示中文
        response = """HTTP/1.1 200 OK

        {"k":"v","name":"joker","msg":"网页显示成功了！"}
        """.encode('gbk')
        conn.sendall(response)  # 编码到bytes

    conn.close()

# 关闭socket
sock.close()