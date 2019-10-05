#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/2 9:59
# @Author  : su
# @File    : BubbleSort.py
"""冒泡排序"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}: {self.age}'

    def __repr__(self):
        return self.__str__()


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def main():
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    print(bubble_sort(items))
    items2 = [
        Person('Wang', 25), Person('Luo', 39),
        Person('Su', 50), Person('He', 20)
    ]
    # print(bubble_sort(items2, comp=lambda p1, p2: p1.age > p2.age))
    print(bubble_sort(items2, comp=lambda p1, p2: p1.name < p2.name))
    items3 = ['apple', 'orange', 'watermelon', 'durian', 'pear']
    print(bubble_sort(items3))


if __name__ == '__main__':
    main()
