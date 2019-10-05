#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 面向对象5：类的属性和方法

# 类的私有属性：__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 类的私有方法：__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods。
# 类的方法：在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数。


class JustCounter:
    __secretCount = 0    # 私有属性
    publicCount = 0      # 公有属性

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()    # 1
counter.count()    # 2
print(counter.publicCount)    # 2
# print(counter.__secretCount)    # 报错，实例不能访问私有变量
