#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/1 13:52
# @Author  : su
# @File    : JsonExample.py

# Python3 中可以使用 json模块来对 JSON 数据进行编解码，它包含了两个函数：
#
#     json.dumps(): 对数据进行编码。（将 Python 对象编码成 JSON 字符串）
#     json.loads(): 对数据进行解码。（将已编码的 JSON 字符串解码为 Python 对象）
#
# 在json的编解码过程中，python 的原始类型可以与json类型会相互转换。
import json

# A Python字典类型转换为JSON对象: dumps()
data = {
    'no': 1,
    'name': 'google',
    'url': 'http://www.google.com'
}
json_str = json.dumps(data)
print('Python原始数据：', repr(data))  # repr() 函数将对象转化为供解释器读取的形式。返回一个对象的string格式
print('转换后的Json对象：', json_str)

# B 将Json 对象转换为Python字典类型:loads()
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])

# C
d = dict(name='Bob', age=20, score=80)
data = json.dumps(d)
print('JSON Data is a str:', data)

reborn = json.loads(data)
print(reborn)

# D 遇到中文序列化时，设置 ensure_ascii=True
obj = dict(name='小明', age=20)
data = json.dumps(obj, ensure_ascii=True)
print(data)
reData = json.loads(data)
print(reData)
