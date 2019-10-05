#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
from collections import Counter
from collections.abc import Iterable
# 1：创建文件data.txt 2：找出文件中数字出现次数最多的10个数字，写入文件mostNum.txt;
f = open("data.txt", "w+")
for i in range(150):
    f.write(str(random.randint(1, 100)) + '\n')
print(f.read())
f.close()

dict = {}
f = open("data.txt", "r+")
print(isinstance(f, Iterable))
for i in f:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1
d = Counter(dict)
with open('mostNum.txt', 'w+') as k:
    for i in d.most_common(10):
        k.write(i[0].strip() + '\n')
    k.seek(0, 0)
    print(k.read())
f.close()
