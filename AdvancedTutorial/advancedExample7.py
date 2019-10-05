#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 面向对象进阶1：@property装饰器


class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self.__name

    # 访问器 - getter方法
    @property
    def age(self):
        return self.__age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self.__age = age

    @name.setter
    def name(self, name):
        self.__name = name

    def play(self):
        if self.__age <= 16:
            print('%s正在玩飞行棋.' % self.__name)
        else:
            print('%s正在玩游戏.' % self.__name)


def main():
    person = Person('王大锤', 12)
    person.play()
    # 修改对象person的属性值
    person.age = 22
    person.name = '张三'
    person.play()


if __name__ == '__main__':
    main()
