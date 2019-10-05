#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 13:41
# @Author  : su
# @File    : StringIO.py
"""
StringIO : 在内存中读写str

要把str写入StringIO，需要先创建一个StringIO，然后，像文件一样写入即可.

要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取.
"""
from io import StringIO

# write to StingIO
f = StringIO()
f.write('hello')
f.write('  ')
f.write('world!')
print(f.getvalue())    # getvalue()方法用于获得写入后的str。


# read from StringIO
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
