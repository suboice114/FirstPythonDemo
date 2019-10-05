#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/14 12:48
# @Author  : su
# @File    : use_turtle.py
"""
“海龟绘图”
Python内置了turtle库.通过编程指挥一个小海龟（turtle）在屏幕上绘图.
绘制出一个长方形
"""
from turtle import *

# 设置笔刷宽度:
width(3)

# 前进:
forward(200)

# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)


# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
