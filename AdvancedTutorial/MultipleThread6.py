#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/1 12:09
# @Author  : su
# @File    : MultipleThread6.py
"""
多线程实现账户转账功能
"""
import threading
import time


class Account(object):

    def __init__(self):
        self._balance = 0   # 账户余额
        self._lock = threading.Lock()

    def deposit(self, money):
        # 当多个线程同时访问一个资源的时候 就有可能因为竞争资源导致资源的状态错误
        # 被多个线程访问的资源我们通常称之为临界资源 对临界资源的访问需要加上保护
        if money > 0:
            # 先获取锁才能执行后续的代码
            self._lock.acquire()
            try:
                # 计算存款后的余额
                new_balance = self._balance + money
                # 模拟受理存款业务需要0.01秒的时间
                time.sleep(0.01)
                # 修改账户余额
                self._balance = new_balance
            finally:
                # 在finally中执行释放锁的操作保证正常异常锁都能释放
                self._lock.release()

    @property
    def balance(self):      # _balance的getter方法
        return self._balance


class AddMoneyThread(threading.Thread):     # 账户增加金额的类，继承threading.Thread, 多个线程进行存钱操作

    def __init__(self, account, money):
        threading.Thread.__init__(self)
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
