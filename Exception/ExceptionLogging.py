#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 12:49
# @Author  : su
# @File    : ExceptionLogging.py
"""
程序异常记录：

断言 assert
打印 logging
"""
import logging
logging.basicConfig(level=logging.INFO)


def foo(s):    # print()打印有可能是程序出现错误的变量
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n


def foo1(s):    # 使用assert来代替print()打印
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n


def foo2(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10 / n


def main():
    # foo('0')
    # foo1('0')
    foo2('0')


if __name__ == '__main__':
    main()
