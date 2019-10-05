#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 15:51
# @Author  : su
# @File    : use-hashlib.py
"""
hashlib模块：提供了常见的摘要算法。如MD5，SHA1等等。

摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
"""

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后结果是一样的.但是只要有不同字母，结果便不同
md5 = hashlib.md5()
md5.update('This is md5 using in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

print(len(md5.hexdigest()))   # 32 位

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

print(len(sha1.hexdigest()))    # 40位

