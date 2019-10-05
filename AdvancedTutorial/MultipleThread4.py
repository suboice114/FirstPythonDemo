#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/8/31 13:58
# @Author  : su
# @File    : MultipleThread4.py
"""
python 多线程4： 线程优先级队列（Queue)
 Queue模块 : 提供了同步的、线程安全的队列类，
   包括FIFO队列 Queue，LIFO队列 LifoQueue，和优先级队列 PriorityQueue。

"""
import threading
import time
import queue

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self):
        print('开启线程：', self.name)
        process_data(self.thread_id, self.name, self.q)
        print('退出线程：', self.name)


def process_data(thread_id, thread_name, q):
    while not exitFlag:
        thread_id += 1
        if thread_id >= 4:
            data = q.get()
            print("%s processing %s" % (thread_name, data))
        time.sleep(1)


threadList = ['Thread-1', 'Thread-2', 'Thread-3']
nameList = ['One', 'Two', 'Three', 'Four', 'Five']
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadId = 1

# 创建新线程
for tName in threadList:
    thread = MyThread(threadId, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print('退出主线程')
