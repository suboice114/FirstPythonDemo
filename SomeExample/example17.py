#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/8 13:30
# @Author  : su
# @File    : example17.py
"""
题目：求1+2!+3!+...+20!的和。
"""


def recursion(n):
    if n == 1:
        return 1
    else:
        return n * recursion(n-1)


l = []
for i in range(1, 21):
    l.append(recursion(i))
print("1+2!+3!+...+20! =", sum(l))

