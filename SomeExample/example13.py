#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/8 12:42
# @Author  : su
# @File    : example13.py
"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""
from functools import reduce


def number_sum(n, a):
    tn = 0
    sn = []
    for count in range(n):
        tn = tn + a
        a = a * 10
        sn.append(tn)
        print(tn)

    sn = reduce(lambda x, y: x + y, sn)
    print('计算和为：', sn)


if __name__ == '__main__':
    n = int(input('n = '))  # n ：次数
    a = int(input('a = '))  # a : 数字
    number_sum(n, a)


