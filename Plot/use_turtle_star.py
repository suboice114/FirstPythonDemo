#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/14 12:59
# @Author  : su
# @File    : use_turtle_star.py
"""
“海龟绘图”
绘制五个五角星
"""
from turtle import *


def draw_star(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


for x in range(0, 250, 50):
    draw_star(x, 0)

done()
