#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/8 12:00
# @Author  : su
# @File    : example10.py
"""
题目：暂停一秒输出，并格式化当前时间。
"""
import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 暂停一秒
time.sleep(1)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
