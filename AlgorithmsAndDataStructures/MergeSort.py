#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/2 11:09
# @Author  : su
# @File    : MergeSort.py
"""归并排序"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}: {self.age}'

    def __repr__(self):
        return self.__str__()


def merge_sort(items, comp=lambda x, y: x <= y):
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp=lambda x, y: x <= y):
    """合并（将两个有序列表合并成一个新的有序列表）"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def main():
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    print(merge_sort(items))
    items2 = [
        Person('Wang', 25), Person('Luo', 39),
        Person('Zhang', 50), Person('He', 20)
    ]
    print(merge_sort(items2, comp=lambda p1, p2: p1.age <= p2.age))
    items3 = ['apple', 'orange', 'watermelon', 'durian', 'pear']
    print(merge_sort(items3))


if __name__ == '__main__':
    main()
