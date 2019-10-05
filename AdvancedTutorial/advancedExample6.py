#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 面向对象6： 多继承


class People:

    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('%s 说：我 %d 岁了。' % (self.name, self.age))


# 单继承 示例
class Student(People):

    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构造方法
        People.__init__(self, n, a, w)
        self.grade = g

    # 重写父类的speak 方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类
class Speaker:

    topic = ''
    name = ''

    def __init__(self, t, n):
        self.topic = t
        self.name = n

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):

    a = ''

    def __init__(self, n, a, w, g, t):
        Speaker.__init__(self, t, n)
        Student.__init__(self, n, a, w, g)


# Sample 的一个实例
sample = Sample('Tim', 18, 80, '高三', 'Python')
sample.speak()     # 方法名同，默认调用的是__init__中排前的父类的方法
