#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import math


def square_of_sum(l):       # list中每个元素的平方和
    sum1 = 0
    for x in l:
        sum1 = sum1 + x * x
    return sum1


print(square_of_sum([1, 2, 3, 4, 5]))
print(square_of_sum([-4, -5, 3, 9, 1, 7]))


def quadratic_equation(a, b, c):        # 给定a,b,c值  求一元二次方程 ax^2+bx+c = 0 的两个解
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a), (-b - t) / (2 * a)


print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))


def average(*args):     # 接收 可变参数的 average()函数
    sum1 = 0.0
    if len(args) == 0:
        return sum1
    for x in args:
        sum1 = sum1 + x
    return sum1 / len(args)


print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))

