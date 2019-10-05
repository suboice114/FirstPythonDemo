#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 条件语句 1
flag = False
name = 'Lulu'
if name == 'Lulu':
    flag = True
    print("welcome boss")
else:
    print(name)

# 条件语句 2
number = 5
if number == 3:
    print("boss")
elif number == 2:
    print("user")
elif number == 1:
    print("worker")
elif number < 0:
    print("error")
else:
    print("roadMan")

# 条件语句 3
value = 9
if value >= 0 and value <= 10:
    print("hello")
else:
    print("undefined")

num = 8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print("hello")
else:
    print("none")

# 条件语句 4
var = 100
if var == 100:
    print("变量var的值为100")

# 条件语句 5
# age = 8  输出 teenager 但是 age = 20 仍然输出 teenager 。
# 这是因为 if - elif 语句 如果某个判断为 True，执行完对应的代码块，后面的条件判断就直接忽略，不再执行了。
age = 8
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# 修改为：
age = 20
if age >= 6 and age <= 18:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')