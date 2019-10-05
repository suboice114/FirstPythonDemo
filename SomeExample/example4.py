#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math

# 练习1：华氏温度转为摄氏温度    F = 1.8C + 32
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# 练习2 ：输入半径，计算圆的周长和面积
radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：', perimeter)
print('面积：', area)

# 练习3：输入年份判断是不是闰年。
year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)

# 练习4： 输入三条边长如果能构成三角形就计算周长和面积
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长：%f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积：%f' % area)
else:
    print('不能构成三角形')

