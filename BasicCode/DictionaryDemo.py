#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 字典 : key-value序对是没有顺序的；key 不能重复；key 必须是不可变的， 如字符串，数字或元组，value 可以是任何数据类型
dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'

print(type(dict))   # <class 'dict'>
print(dict)
print(dict['one'])
print(dict[2])

tinyDict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(tinyDict)
print("dict_keys:", tinyDict.keys())    # 键
print("dict_values:", tinyDict.values())    # 值
print("dict_items:", tinyDict.items())  # 键值对

# dict 中新增
tinyDict['age'] = 8
tinyDict['school'] = 'BEIJING'
print(tinyDict)

# for循环遍历 dict
for key in tinyDict:
    print(key + ":", tinyDict[key])

# 删除 dict 中 某一项
del tinyDict['dept']
print(tinyDict)
