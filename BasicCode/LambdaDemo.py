#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/2 10:47
# @Author  : su
# @File    : LambdaDemo.py
"""Lamdba函数"""
from functools import reduce


# 按照元素绝对值大小升序排序
myList = [3, 5, 10, -2, 8]
print(sorted(myList, key=lambda x: abs(x)))

# 求 1- 20 的平方
print(list(map(lambda x: x*x, range(1, 21))))

# 求 1-100之和
# reduce(function, sequence)
print(reduce(lambda x, y: x + y, range(1, 101)))

# 求1-100之和 再加上1000
print(reduce(lambda x, y: x + y, range(1, 101), 1000))
