#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/9 17:27
# @Author  : su
# @File    : advancedExample15.py
"""
面向对象： 魔术方法
如果要把自定义对象放到set或者用作dict的键
那么必须要重写 __hash__ 和 __eq__ 两个魔术方法

前者用来计算对象的哈希码，后者用来判断两个对象是否相同
哈希码不同的对象一定是不同的对象，但哈希码相同未必是相同的对象（哈希码冲撞）
所以在哈希码相同的时候还要通过 __eq__ 来判定对象是否相同
"""


class Student:
    # 限定Student对象只能绑定stu_id, name和gender属性
    __slots__ = ('__stu_id', '__name', '__gender')

    def __init__(self, stu_id, name):
        self.__stu_id = stu_id
        self.__name = name

    @property
    def stu_id(self):
        return self.__stu_id

    @property
    def name(self):
        return self.__name

    @stu_id.setter
    def stu_id(self, stu_id):
        self.__stu_id = stu_id

    @name.setter
    def name(self, name):
        self.__name = name

    def __hash__(self):
        return hash(self.__stu_id) + hash(self.__name)

    def __eq__(self, other):
        return self.__stu_id == other.__stu_id and \
               self.__name == other.__name

    def __str__(self):
        return f'{self.__stu_id}: {self.__name}'

    def __repr__(self):
        return self.__str__()


class School:
    def __init__(self, name):
        self.name = name
        self.students = {}  # 字典类型 key；value

    def __setitem__(self, key, student):    # __setitem__：索引赋值语句
        self.students[key] = student

    def __getitem__(self, key):     # __getitem__:索引重载
        return self.students[key]


def main():
    stu = Student(1234, '李白')
    print(stu.name, stu.stu_id)

    stu1 = Student(1234, '李白')
    print(stu == stu1)

    students = set()    # set的元素没有重复，而且是无序的
    students.add(Student(1001, '李雷'))
    students.add(Student(1001, '李雷'))
    students.add(Student(1001, '韩梅梅'))
    print(len(students))    # 2
    print(students)         # {1001: 李雷, 1001: 韩梅梅}

    school = School('北京大学')
    school[1001] = Student(1001, '小明')
    school[1002] = Student(1002, '小红')
    school[1003] = Student(1003, '小亮')
    print(school[1002])
    print(school[1003])


if __name__ == '__main__':
    main()
