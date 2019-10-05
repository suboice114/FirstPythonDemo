#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/8/31 14:29
# @Author  : su
# @File    : MultipleThread5.py
"""
python多线程：线程同步，加锁与不加锁的区别 (即 MultipleThread2.py 和 MultipleThread3.py)
不加锁时 ,注释以下两行代码：
    threadLock.acquire()
    threadLock.release()
"""
import threading
import time


aList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class MyThread(threading.Thread):  # MyThread 继承父类threading.Thread
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('开始线程：', self.name)
        threadLock.acquire()
        print(self.name, self.counter)
        threadLock.release()

    def __del__(self):
        print(self.name, '线程结束！')


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        aList[counter - 1] += 1
        print("[%s] %s修改第 %d 个值，修改后的值是：%d" % (time.ctime(time.time()), thread_name, counter, aList[counter - 1]))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

# 开启线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
