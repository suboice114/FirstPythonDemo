#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/2 10:11
# @Author  : su
# @File    : QuickSort.py
"""快速排序：以枢轴为界将列表中的元素划分为两个部分，左边都比枢轴小，右边都比枢轴大"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}: {self.age}'

    def __repr__(self):
        return self.__str__()


def quick_sort(origin_items, comp=lambda x, y: x <= y):
    """快速排序"""
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    """递归调用划分和排序"""
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    """划分"""
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


def main():
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    print(quick_sort(items))
    items2 = [
        Person('Wang', 25), Person('Luo', 39),
        Person('Zhang', 50), Person('He', 20)
    ]
    print(quick_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    items3 = ['apple', 'orange', 'watermelon', 'durian', 'pear']
    print(quick_sort(items3))


if __name__ == '__main__':
    main()
