#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 15:39
# @Author  : su
# @File    : use-struct.py
"""
struct模块： 解决bytes和其他二进制数据类型的转换。

准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。

1:  pack() 函数 把任意数据类型变成bytes.
pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。后面的参数个数要和处理指令一致。

2： unpack()函数 把bytes变成相应的数据类型.
'>IH':  bytes依次变为 I：4字节无符号整数 H：2字节无符号整数。
"""
import struct

# 未使用struct模块：python 中 把一个32位无符号整数变成字节，也就是4个长度的bytes。
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print('n转换为字节：', bs)    # b'\x00\x9c@c'

# 使用struct模块 pack()函数
by = struct.pack('>I', 10240099)
print(by)

# unpack()函数
n = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(n)

bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', bmp_header))
