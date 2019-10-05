#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/1 13:04
# @Author  : su
# @File    : client.py
"""
客户端：socket.connect(hosname, port ) 方法打开一个 TCP 连接到主机为 hostname 端口为 port 的服务商。
连接后 就可以从服务端获取数据。操作完成后需要关闭连接。
"""
import socket

# 创建socket对象
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
clientSocket.connect((host, port))

# 接收小于 1024 字节的数据
msg = clientSocket.recv(1024)

clientSocket.close()

print(msg.decode('utf-8'))
