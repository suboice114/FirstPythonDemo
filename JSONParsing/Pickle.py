#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 14:02
# @Author  : su
# @File    : Pickle.py
"""
Python 提供了pickle模块来实现序列化。

pickle.dumps()
pickle.loads()
"""
import pickle

d = dict(name='Bob', age=20, score=80)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)
