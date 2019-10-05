#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 13:45
# @Author  : su
# @File    : BytesIO.py
"""
StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
"""
from io import BytesIO

# write to BytesIO
f = BytesIO()
f.write(b'hello')
f.write(b'  ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())
