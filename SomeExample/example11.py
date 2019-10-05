#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/8 12:05
# @Author  : su
# @File    : example11.py
"""
题目：打印出所有的"水仙花数".   所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
"""


def flower_fun():
    flower_list = []
    for n in range(100, 1000):
        i = int(n / 100)
        j = int(n / 10 % 10)
        k = int(n % 10)
        n_sum = i * i * i + j * j * j + k * k * k
        if n == n_sum:
            flower_list.append(n_sum)
    return flower_list


def main():
    print(flower_fun())
    print(153 in flower_fun())


if __name__ == "__main__":
    main()
