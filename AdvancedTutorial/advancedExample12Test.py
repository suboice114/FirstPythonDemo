#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/9 9:58
# @Author  : su
# @File    : advancedExample12Test.py
"""
advancedExample12.py 测试类
"""
from AdvancedTutorial.advancedExample12 import EmployeeFactory


def main():
    """主函数"""
    emps = [
        EmployeeFactory.create('M', '陆谦'),
        EmployeeFactory.create('P', '一叶孤舟', 120),
        EmployeeFactory.create('P', '啦啦', 85),
        EmployeeFactory.create('S', '珠珠女孩', 123000)
    ]
    for emp in emps:
        print('%s: %.2f元' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
