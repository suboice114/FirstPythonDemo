#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 数字
import math

anInt = 1
aFloat = 3.141592653
aNumber = 100 * 3
aValue = 60 << 2

print(type(aValue))     # <class 'int'>
print(type(aFloat))     # <class 'float'>
print(aNumber)
print(aValue)

print('-442-12 =', -442 - 12)

print('4 ** 3 =', 4 ** 3)   # 4的3次方
print('5 ** 2 =', 5 ** 2)   # 5的2次方
print('4.2 * 3.1 =', 4.2 * 3.1)

print('-3 ** 2 = ', -3 ** 2)    # ** 运算符最高
print('(-3) ** 2 = ', (-3) ** 2)

print('8 / 3 = ', 8 / 3)    # 整数除法返回浮点型
print('8 //2 =', 8 // 3)
print('8.0 / 3.0 = ', 8.0 / 3.0)
print('8 % 3 = ', 8 % 3)

print('11 / 4 = ', 11 / 4)      # 整数除法返回浮点型 2.75
print('11 // 4 = ', 11 // 4)    # 向下取整 2
print('11.0 % 4 = ', 11.0 / 4)  # 浮点型：2.75
print('11 % 4 = ', 11 % 4)      # 取余：3

print('30 & 45 = ', 30 & 45)    # 按位与
print('30 | 45 = ', 30 | 45)    # 按位或
print('~30 = ', ~30)            # 按位求补（取反）
print('45 << 1 = ', 45 << 1)    # 左移
print('60 >> 2 = ', 60 >> 2)    # 右移
print('30 ^ 45 = ', 30 ^ 45)    # 位异或

print(abs(-1))      # abs()返回给定参数的绝对值
print(abs(0.23 - 0.78))
print(round(1.2))   # round() 按照四舍五入取整
print(divmod(10, 3))

print(math.floor(5.06))
print(math.ceil(1.443654))
print(math.sqrt(25))
print(int(math.sqrt(8)))
