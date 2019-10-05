#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
python线程 1；
    Python中使用线程有两种方式：函数或者用类来包装线程对象。
函数式：调用 _thread 模块中的start_new_thread()函数来产生新线程。语法如下:
    _thread.start_new_thread ( function, args[, kwargs] )
"""
import _thread
import time

# 为线程定义一个函数


def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s：%s" % (thread_name, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1", 2, ))
    _thread.start_new_thread(print_time, ("Thread-2", 4, ))
except:
    print("Error:无法启动线程")

while 1:
    pass
