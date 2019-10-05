#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 类与对象
import keyword as key

print(key.kwlist)   # Python中的关键字

# demo1


class MyClass(object):

    """MyClass class definition"""

    myVersion = '1.1'

    def showMyVersion(self):
        print(MyClass.myVersion)


print(dir(MyClass))         # 列出类所有的属性

print(MyClass.__name__)     # 类的名字 （字符串）
print(MyClass.__doc__)      # 类的文档信息
print(MyClass.__bases__)    # 类 所有父类构成的元组 ()
print(MyClass.__dict__)     # 类 的 属性
print(MyClass.__module__)   # 类 定义所在的模块
print(MyClass.__class__)    # 实例C 对应的类


sType = type('What is your question?')      # sType 是一个类型对象
print(sType)
print(sType.__name__)       # 得到类型名（字符串表示）：str


# demo2


class C(object):        # 定义类
    pass


c = C()                 # 创建实例 并未添加属性
print(dir(c))
print(c.__dict__)
print(c.__class__)


# 实例 c 添加属性
c.foo = 1
c.bar = 'SPAM'
print("%d can of %s please" % (c.foo, c.bar))
# __dict__  属性由一个字典组成，包含一个实例的所有属性。键是属性名，值是对应的属性值
print(c.__dict__)


# demo3


class Foo(object):
    x = 1.5     # 类属性 不可变量，此处为数字


foo = Foo()
print(foo.x)    # 实例属性 1.5
foo.x = 1.7
print(foo.x)    # 实例属性 1.7
print(Foo.x)    # 类属性 1.5

del foo.x       # 删除 实例属性
print(foo.x)    # 可以取到值：类属性值   1.5

foo.x += .2     # 尝试 增加实例属性值 （foo.x = Foo.x + 0.2)
print(foo.x)    # 1.7
print(Foo.x)    # 依旧可以访问到类属性 1.5

# demo4


class Foo1(object):
    x = {2003: 'poe2'}  # 类属性可变，此处为字典


foo1 = Foo1()
print(foo1.x)   # {2003: 'poe2'}

foo1.x[2004] = 'valid path'
print(foo1.x)   # {2003: 'poe2', 2004: 'valid path'}
print(Foo1.x)   # 修改生效 {2003: 'poe2', 2004: 'valid path'}


# demo5 类属性的持久性：类属性的修改会影响到所有的实例


class C(object):
    spam = 100  # 类属性


c1 = C()    # 创建一个实例
print(c1.spam)  # 通过实例访问类属性 100

C.spam += 100   # 更改类属性
print(C.spam)   # 查看类属性值改变 200

print(c1.spam)  # 200

c2 = C()    # 创建另一个实例c2
print(c2.spam)  # 200

del c1  # 删除一个实例
C.spam += 200
print(C.spam)   # 400


# demo6


class TestStaticMethod:

    @staticmethod
    def foo():
        print('calling static method foo()')


class TestClassMethod:

    @classmethod
    def foo(cls):
        print("calling class method foo()")
        print("foo() is part of class:", cls.__name__)


tsm = TestStaticMethod()
tsm.foo()
TestStaticMethod.foo()

tcm = TestClassMethod()
tcm.foo()
TestClassMethod.foo()


# demo7


class Parent(object):   # 定义父类
    def parentMethod(self):
        print('calling parent method')


class Child(Parent):    # 定义子类
    def childMethod(self):
        print('calling child method')


p = Parent()
print(p.parentMethod())

c = Child()
print(c.childMethod())
print(c.parentMethod())
