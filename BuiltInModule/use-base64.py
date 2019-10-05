#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 15:21
# @Author  : su
# @File    : use-base64.py
"""
Base64：一种用64个字符来表示任意二进制数据的方法。

Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_

"""
import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s1 = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s1)
d1 = base64.urlsafe_b64decode(s).decode('utf-8')
print(d1)
