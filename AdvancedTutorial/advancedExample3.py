#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 面向对象3：继承


class Parent:    # 定义父类
    parentArr = 100

    def __init__(self):
        print('调用父类的构造函数')

    @staticmethod
    def parent_method():
        print('调用父类方法')

    def set_attr(self, attr):
        Parent.parentArr = attr

    def get_atrr(self):
        print('父类属性：', Parent.parentArr)


class Child(Parent):    # 定义子类

    def __init__(self):
        Parent.__init__(self)
        print('调用子类构造方法')

    @staticmethod
    def child_method():
        print('调用子类方法')


c = Child()         # 实例化子类
c.child_method()     # 调用子类的方法
c.parent_method()    # 调用父类方法
c.set_attr(200)      # 再次调用父类的方法 - 设置属性值
c.get_atrr()          # 再次调用父类的方法 - 获取属性值
