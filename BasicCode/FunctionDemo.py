#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def print_me(str1):     # 函数 定义函数
    print(str1)
    return


print_me("调用函数")
print_me("再次调用函数")


def change_int(a):      # 传入不可变量参数
    a = 10


b = 2
change_int(b)
print(b)


def change_me(my_list):      # 传入可变参数
    my_list.append([1, 2, 3, 4])
    print("函数内取值：", my_list)
    return


myList = [10, 20, 30]
change_me(myList)
print("函数外取值：", myList)


def print_info(name, age=35):   # 默认参数
    print("Name:", name)
    print("Age:", age)
    return


print_info(age=50, name='niko')
print_info(name='Lulu')


def print_num(arg, *vartuple):    # 不定长参数
    print("输出：")
    print(arg)
    for i in vartuple:
        print(i)
    return


print_num(10)
print(70, 60, 90)


def sum0(a, b):     # return 语句
    total1 = a + b
    return total1


print(sum0(10, 20))


total = 0       # 遍历作用域


def sum1(arg1, arg2):
    total1 = arg1 + arg2
    print("函数内是局部变量：", total1)
    return total


sum1(10, 40)
print("函数外是全局变量：", total)
