#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 14:09
# @Author  : su
# @File    : JsonExample2.py
"""
json模块： 对象序列化
"""
import json


class Student(object):

    def __init__(self, name, age, score):
        self.name = name

        self.age = age

        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)


s = Student('Bob', 20, 90)
# print(json.dumps(s))    # TypeError: Object of type Student is not JSON serializable 即 Student对象不是一个可序列化为JSON的对象。
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)

rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)
