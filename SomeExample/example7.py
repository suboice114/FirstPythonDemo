#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/8 11:38
# @Author  : su
# @File    : example7.py
"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""
l = []
for i in range(3):
    x = int(input("integer:\n"))
    l.append(x)
l.sort()
print(l)
