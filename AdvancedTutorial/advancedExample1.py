#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# python 面向对象1：类的创建 与 对象


class Employee:
    """所有员工的基类"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_employee(self):
        print('Name:', self.name, ", Salary:", self.salary)


# 创建 Employee 类的第1 个对象
emp1 = Employee('Zara', 2000)
# 创建 Employee 类的第2 个对象
emp2 = Employee('Tom', 5000)

# 访问属性
emp1.display_employee()
emp2.display_employee()
print("Total Employee %d" % Employee.empCount)

# Python 内置类属性
print('Employee.__doc__:', Employee.__doc__)
print('Employee.__name__:', Employee.__name__)
print('Employee.__module__:', Employee.__module__)  # module__: 类定义所在的模块
print('Employee.__bases__:', Employee.__bases__)
print('Employee.__dict__:', Employee.__dict__)
