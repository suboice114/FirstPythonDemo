#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/8 13:11
# @Author  : su
# @File    : example15.py
"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
init_height = 100.0  # 初始高度
tim = 10   # 次数

tour = []
height = []

for i in range(1, tim + 1):

    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(init_height)
    else:
        tour.append(init_height * 2)

    init_height /= 2
    height.append(init_height)

print('总高度：tour = {0}'.format(sum(tour)))
print('第10次反弹高度：height = {0}'.format(height[-1]))

