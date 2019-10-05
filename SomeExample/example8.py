#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/8 11:47
# @Author  : su
# @File    : example8.py
"""
题目：斐波那契数列: 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。    (古典兔子问题)
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""


def fib(n):     # 输出第n个斐波那契数
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fib1(n):    # 递归方式 输出第n个斐波那契数
    if n == 1 or n == 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fibonacci(n):   # 输出n个斐波那契数列
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]

    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def main():
    print("第10个斐波那契数是：", fib(10))
    print("第13个斐波那契数是:", fib1(13))
    print("输出20个斐波那契数列：", fibonacci(20))


if __name__ == "__main__":
    main()
