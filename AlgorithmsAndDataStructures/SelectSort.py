#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""简单选择排序：每次从剩下元素中选择最小"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}: {self.age}'

    def __repr__(self):
        return self.__str__()


def select_sort(origin_items, comp=lambda x, y: x < y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def main():
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    print(select_sort(items))
    items2 = [
        Person('Wang', 13), Person('Luo', 35),
        Person('Su', 26), Person('He', 44)
    ]
    print(select_sort(items2, comp=lambda p1, p2: p1.name < p2.name))
    items3 = ['apple', 'orange', 'watermelon', 'durian', 'pear']
    print(select_sort(items3))


if __name__ == '__main__':
    main()
