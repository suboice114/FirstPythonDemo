#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 访问字符串中的值
var1 = 'Hello world!'
var2 = 'Python'
aString = "Python is cool!"

print(type(var1))   # <class 'str'>
print(aString)
print("var1[0]:", var1[0])
print("var1[0:6]", var1[0:6])
print("var2[:3]", var2[:3])
print("var2[2:]", var2[2:])
print("var2[:]:", var2[:])
print("var2 * 2:", var2 * 2)
print("var1+var2:", var1 + var2)

# 字符串更新
print("更新字符串var1：", var1[:6] + "PyCharm!")

# 字符串格式化
print("My name is %s and age is %d !" % ('Zara', 21))

# 字符串删除
print("删除var1中元素 :", var1[:3] + var1[4:])

# len()函数
str1 = 'abcdefg'
print(str1)
print("str1 length:", len(str1))

# 小写转换为大写
print('upper:', str1.upper())

# 成员操作符 in ，not in
print("'bc' in str1:", 'bc' in str1)
print("'n' in str1:", 'n' in str1)
print("'nm' not in str1：", 'nm' not in str1)
