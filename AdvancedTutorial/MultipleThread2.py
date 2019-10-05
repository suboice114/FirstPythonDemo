#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Python多线程2:使用threading模块创建线程
"""

import threading
import time

exitFlag = 0


class MyThread(threading.Thread):   # 继承父类threading.Thread

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):      # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print('开始线程：', self.name)
        print_time(self.name, self.counter, 5)
        print('退出线程：', self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('退出主线程')
