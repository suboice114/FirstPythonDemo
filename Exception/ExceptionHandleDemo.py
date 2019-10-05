#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
异常处理: try...except..finally
"""
# demo1
try:
    fh = open('testfile.txt', 'w')  # w:没有文件会创建一个，并不会报错；但会覆盖原有内容
    fh.write('test exception file')
except IOError:
    print('Error:没有找到文件或者读取文件失败')
else:
    print('内容成功写入')
    fh.close()


# demo2
try:
    fo = open('test.txt', 'r')
    fo.read()
except IOError:
    print('Error: not find file')

# demo3: 使用 raise 主动抛出异常


def foo(s):
    if not isinstance(s, int):
        raise ValueError('这里需要传入一个整数类型')
    else:
        print(int(s))


try:
    foo(12)
    foo('hello')
except ValueError as e:
    print(e)
