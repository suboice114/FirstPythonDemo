#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 15:02
# @Author  : su
# @File    : use-collections.py
"""
collections模块：Python内建的一个集合模块，提供了许多有用的集合类。

1：namedtuple('名称', [属性list]): 一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

2：使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。

3：使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

4: 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
   如果要保持Key的顺序，可以用OrderedDict.(OrderedDict的Key会按照插入的顺序排列，不是Key本身排序)

5: Counter是一个简单的计数器，例如，统计字符出现的个数：
"""
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 3)
print('p.x =', p.x, 'p.y =', p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(4, 3, 4)
print(c.r)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
