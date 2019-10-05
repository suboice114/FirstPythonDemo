#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/1 12:56
# @Author  : su
# @File    : server.py
"""
服务端:    使用 socket 模块的 socket 函数来创建一个 socket 对象。
socket 对象可以通过调用其他函数来设置一个 socket 服务。可以通过调用 bind(hostname, port) 函数来指定服务的 port(端口)。
接着，调用 socket 对象的 accept 方法。该方法等待客户端的连接，并返回 connection 对象，表示已连接到客户端。
"""
import socket

# 创建socket对象
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 9999

# 绑定端口号
serverSocket.bind((host, port))

# 设置最大连接数，超过后排队
serverSocket.listen(5)

while True:
    # 建立客户端连接
    clientSocket, addr = serverSocket.accept()
    print('连接地址：', str(addr))
    msg = '欢迎开始Python网络编程学习！' + "\r\n"
    clientSocket.send(msg.encode('utf-8'))
    clientSocket.close()
