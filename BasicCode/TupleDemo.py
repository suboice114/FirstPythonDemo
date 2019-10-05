#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 元组
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinyTuple = (123, 'john')
tup1 = (50,)    # 元组中只包含一个元素时，需要在元素后面添加逗号

print(type(tinyTuple))      # <class 'tuple'>
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinyTuple * 2)
print(tuple + tinyTuple)

t = (['xyz', 123], 23, -103.4)  # 元组t 包含 list元组，t的内容是可变的。 若改为 (('xyz', 123), 23, -103.4) 则不可以改变内容。
print("原元组 t :", t)
L = t[0]
L[1] = 'abc'
print("修改元组t 中第一个元素list，得到新的L：", L)

print("修改后的元组 t :", t)  # 改变的是 list元素 而不是 元组元素
t = t + (23, ['easy', 'free'])
print(t)

print(str(t))
print(list(t))
print(len(t))

print((4, 2) < (3, 5))      # False
print((2, 4) < (3, -1))     # True
print((2, 4) == (3, -1))    # False
print((2, 4) == (2, 4))     # True
