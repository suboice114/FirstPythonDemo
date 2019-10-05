#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/1 14:15
# @Author  : su
# @File    : DateAndTimeDemo.py
import time
import calendar

ticks = time.time()
print('当前时间戳：', ticks)

localtime = time.localtime(time.time())  # 获取当前时间
print('本地时间为：', localtime)

localtime1 = time.asctime(time.localtime(time.time()))   # 获取格式化的时间 asctime()
print('格式化-本地时间为：', localtime1)

# 格式化日期 time.strftime(format[, t])
print('格式化-当前时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 格式化成2019-09-01 14:24:30形式
print('格式化-当前时间：', time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))  # 格式化成Sun Sep 01 14:24:30 2019形式

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 获取某月日历
cal = calendar.month(2019, 9)
print("以下输出2019年9月份的日历:")
print(cal)

