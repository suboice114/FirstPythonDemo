#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 正则表达式:
# re.match(pattern,string,flags=0):尝试用正则表达式 pattern 匹配字符串 string, flags 是可选标识符。如果匹配成功，则返回一个匹配对象，否则返回None
# re.search(pattern,string,flags=0):在字符串string中搜索正则表达式pattern的第一次出现，flags是可选标识符。如果匹配成功，则返回一个匹配对象，否则返回None
# re.sub(pattern, repl, string, count=0, max=0):检索与替换。把字符串string中所有匹配正则表达式的地方替换成字符串repl,囚max的值没有给出，则对所有匹配的地方进行替换。
# compile(pattern[, flags]): compile函数用于编译正则表达式，生成一个正则表达式对象（Pattern）,供match()和search()这两个函数使用
# findall(string[, pos[, endpos]]):在字符串string中找到正则表达式所匹配的所有子串，并返回一个列表。如果没有匹配的，则返回空列表。match 和 search 是匹配一次；findall 匹配所有
# re.finditer(pattern,string,flags=0):和 findall类似，在字符串string中找到正则表达式pattern所有匹配的子串，并把它们作为一个迭代器返回。flags是标示位。
# re.split(pattern, string[, maxspilt=0, flags=0]): 按照能够与正则表达式pattern匹配的子串将字符串string分割后返回列表list。

# re.I: 匹配时 忽略大小写；  re.M : 多行匹配，影响^和$
# ^:匹配字符串的开头；   $:匹配字符串的末尾； re*:匹配0个或多个的表达式；    re+:匹配一个或多个表达式

import re
# A. re.match()方法
print(re.match('www', 'www.Google.com').span())
print(re.match('com', 'www.Google.com'))

# B. re.search()方法
print(re.search('www', 'www.Google.com').span())
print(re.search('com', 'www.Google.com').span())

# 使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
line = 'Cats are smarter than dogs'
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Nothing found!")


# C.检索与替换
phone = '2004-959-559 # 这是一个国外电话号码'

num = re.sub(r'#.*$', "", phone)    # 删除电话号码中的注释
print('电话号码：', num)

num1 = re.sub(r'\D', "", phone)     # 移除非数字的内容
print('电话号码1：', num1)

# repl 参数


def double(matches):    # 将匹配的数字乘以 2
    value = int(matches.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))    # A46G8HFD1134

# D. compile()函数
pattern = re.compile(r'\d+')    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')
print(m)    # None

m = pattern.match('one12twothree34four', 2, 10)    # 从 'e'的位置开始匹配
print(m)    # None

m = pattern.match('one12twothree34four', 3, 10)     # 从 '1'的位置开始匹配
print(m)    # 返回一个Match对象：<re.Match object; span=(3, 5), match='12'>
print(m.group())    # 12
print(m.start())    # 3
print(m.span())     # (3, 5)

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = pattern.match('Hello World Wide Web')
print(m)    # 返回一个 Match 对象 ： <re.Match object; span=(0, 11), match='Hello World'>
print(m.group(0))   # 0 可以省略；返回匹配成功的整个字符串：Hello World
print(m.span(0))    # 0可以省略；返回匹配成功的字符串的索引：(0, 11)
print(m.group(1))   # group(1)返回第一个分组匹配成功的子串：Hello
print(m.span(2))    # (6, 11)
print(m.groups())   # ('Hello', 'World')

# E. findall()函数
# 查找字符串中所有数字
pattern = re.compile(r'\d+')
result1 = pattern.findall('google 234 runoob 456')
result2 = pattern.findall('run88ob123google3457', 0, 10)
result3 = pattern.findall('run88ob123google8796')
print(result1)      # ['234', '456']
print(result2)      # ['88', '123']
print(result3)      # ['88', '123', '8796']

# F.re.finditer()函数
it = re.finditer(r'\d+', '12a34bc9hg78')
for match in it:
    print(match.group())

# G.re.spilt()函数
slt = re.split(':', 'str1:str2:str3')
print(slt)      # ['str1', 'str2', 'str3']

# H. 匹配多个字符串（|）
bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
print(m.group())        # bat

m1 = re.match(bt, 'blt')
# print(m1.group())   # AttributeError: 'NoneType' object has no attribute 'group'
if m1 is not None:
    print(m1.group())
else:
    print('没有相匹配的')

m2 = re.match(bt, 'He bit me!')
# print(m2.group())       # AttributeError: 'NoneType' object has no attribute 'group'
if m2 is not None:
    print(m1.group())
else:
    print('没有相匹配的')

m3 = re.search(bt, 'He bit me!')
print(m3.group())       # bit

# I. 匹配任意单个字符(.)
anyEnd = '.end'
m = re.match(anyEnd, 'bend')
print(m.group())

m1 = re.match(anyEnd, 'end')
# print(m1.group())       # AttributeError: 'NoneType' object has no attribute 'group'
if m1 is not None:
    print(m1.group())
else:
    print('没有相匹配的')

m2 = re.search('.end', 'The end.')
print(m2.group())

# J. 创建字符集合（[]）
m = re.match('[cr][23][dp][o2]', 'c3po')
print(m.group())

m = re.match('[cr][23][dp][o2]', 'c2do')
print(m.group())

m = re.match('r2d2|c3po', 'r2d2')
print(m.group())

# 转义字符
print('My brother\'s name is \'007\'')
# 原始字符串
print(r'My brother\'s name is \'007\'')
