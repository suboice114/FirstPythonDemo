#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 面向对象进阶2:  __slots__


class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('__name', '__age', '__gender')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def play(self):
        if self.__age <= 16:
            print('%s正在玩飞行棋.' % self.__name)
        else:
            print('%s正在玩斗地主.' % self.__name)


def main():
    person = Person('王大锤', 15)
    person.play()
    # person.__birth = '2000-1-1'   # Person类的实例对象，只能绑定 __slots__ 中的属性
    # person.__gender = '男'     # __gender 属于私有属性，不能直接通过对象改变


if __name__ == '__main__':
    main()
