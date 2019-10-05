#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 16:15
# @Author  : su
# @File    : use-itertools.py
"""
itertools模块：

"""
import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 100:    # 若没有if语句，会输出所有的自然数序列，除非按Ctrl+C退出
        break


cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:      # 若没有if语句，会循环输出 A B C 序列，同样停不下来。
        break


natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))


for c in itertools.chain('ABC', 'XYZ'):     # chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
    print(c)


for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
