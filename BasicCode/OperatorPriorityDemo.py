#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/1 14:40
# @Author  : su
# @File    : OperatorPriorityDemo.py
"""
python 运算符 及 优先级
1、算术运算符(+ - * / % ** //)、关系运算符 (== != > < >= <=)、赋值运算符(= += -= *= /= %= **= //=)、
   逻辑运算符(and or not)、位运算符(& | ^ ~ << >>)、成员运算符(in ; not in)、身份运算符(is ; is not)
2、运算符优先级:
 **(指数优先级最高)
 ~ + -          按位翻转, 一元加号和减号
 * / % //       乘，除，取模和取整除
 + -            加法减法
 >> <<          右移，左移运算符
 &              位 'AND'
 ^ |            位运算符
 <= < >= >      比较运算符
 <> == !=       等于运算符
 = %= /= //= -= += *= **=       赋值运算符
 is is not      身份运算符
 in not in      成员运算符
 not and or     逻辑运算符

"""
# 算术运算符
a = 21
b = 10
c = 0

c = a + b
print('1-c的值为：', c)

c = a - b
print('2-c的值为：', c)

c = a * b
print('3-c的值为：', c)

c = a / b
print('4-c的值为：', c)

c = a % b
print('5-c的值为：', c)

# 修改变量a b c
a = 2
b = 3
c = a ** b
print('6-c的值为：', c)

a = 10
b = 5
c = a // b
print('7-c的值为：', c)

# 比较运算符
m = 21
n = 10
p = 0
if m == n:
    print('1-m等于n')
else:
    print('1-m不等于n')

if m != n:
    print('2-m不等于n')
else:
    print('2-m等于n')

if m < n:
    print('3-m小于n')
else:
    print('3-m大于等于n')

if m > n:
    print('4-m大于n')
else:
    print('4-m小于等于n')

# 修改m n的值
m = 5
n = 20
if m <= n:
    print('5-m小于等于n')
else:
    print('5-m大于n')

if n >= m:
    print('6-n大于等于m')
else:
    print('6-n小于m')

# 运算符优先级1
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)

e = (a + b) * (c / d)  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)

e = a + (b * c) / d   # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)

f = 3 * 1 ** 3
print('f =', f)  # f = 3 （ ** 优先级最高）

j = 9 // 2
print('j =', j)

x = True
y = False
z = False
# 1
if x or y and z:    # not and or 中 and 拥有较高优先级，会先行运算。
    print('yes')
else:
    print('no')

# 2
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)
