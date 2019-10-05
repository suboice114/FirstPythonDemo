#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/9 10:27
# @Author  : su
# @File    : advancedExample14.py
"""面向对象：
迭代器  __iter__ / __next__
itertools - 生成可迭代序列的工具模块
"""
import itertools
from math import sqrt


def is_prime(num):
    """判断素数: 大于1的自然数中，一个数字只能被1和他本身整数时，这个数就是素数，也叫质数。"""
    if num < 1:
        return False
    for factor in range(2, int(sqrt(num)) + 1):
        if num % factor == 0:
            return False
    return True


class PrimeIter:
    """素数迭代器"""
    def __init__(self, min_value, max_value):
        assert 2 <= min_value <= max_value
        self.min_value = min_value - 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        self.min_value += 1
        while self.min_value <= self.max_value:
            if is_prime(self.min_value):
                return self.min_value
            self.min_value += 1
        raise StopIteration()


def main():
    for val in itertools.permutations('ABCD'):
        print(val)
    for val in itertools.permutations('ABCDE', 2):
        print(val)

    for value in itertools.combinations('CDEFG', 3):
        print(value)

    for value in itertools.product('黑红梅方', range(1, 14)):
        print(value)

    # 素数迭代器 2-100之间的素数
    prime_iter = PrimeIter(2, 100)
    for prime in prime_iter:
        print(prime)


if __name__ == '__main__':
    main()
