#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 创建列表 [] ：可变量
list1 = ['physics', 'chemistry', 'math', 90, 80, 147]
list2 = [1, 2, 3, 4, 5]
list3 = ['a', 'b', 'c', 'd']

# 访问列表中的值
print("list1[0]:", list1[0])
print("list2[2:5]:", list2[2:5])
print("list3[:3]:", list3[:3])

list3.append('e')   # append()总是把新的元素添加到 list 的尾部, 并且 将元素作为一个整体添加
print(list3)

list3.insert(2, 'x')   # insert()方法:它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素
print(list3)

list3.append(['y', 'm', 'p'])   # append():将元素作为一个整体添加
print(list3)

list3.extend(['y', 'm', 'p'])   # extend():将数据类型的元素分解添加至列表内
print(list3)

# 操作符
print(list1 + list2)
print(list2 * 2)
print('a' not in list3)
print('n' in list3)
print('nm' not in list3)

# 更新列表中的值
list4 = []
list4.append("Google")
list4.append("Running")
print(list4)
list4[1] = "Windows"
print(list4)

# 取出（删除）列表中的值
list5 = ['physics', 'chemistry', 1997, 2000]
print(list5)
print(list5.pop())  # list 的 pop()方法总是删掉list的最后一个元素，并且它还返回这个元素。（2000）
print(list5.pop(1))     # pop(index) :删除指定索引上的值 （chemistry）
print("pop()函数删除后的list5:", list5)

# sorted() 排序
num = [11, 55, 88, 66, 35, 42]
print('num正序：  ', sorted(num))  # 数字排序 ，默认升序
print('num倒序：', sorted(num, reverse=True))  # 加入reverse =True，则表示倒序

name = ["XWu", "little-five", "James"]
print('name排序：', sorted(name))    # 字符串排序

# 列表解析
print([i * i for i in range(1, 10)])
print([i * 2 for i in [8, -2, 5]])
print([i for i in range(8) if i % 2 == 0])

# set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
# set 中传入list
s = set(['A', 'B', 'C', 'D', 'C'])
print(s)

# enumerate() 函数 : 可以在for循环中同时绑定索引index和元素name
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print(index, "-", name)


def to_uppers(L):       # list中的所有字符串变成大写后返回，非字符串元素将被忽略。
    return [x.upper() for x in L if isinstance(x, str)]


print(to_uppers(['Hello', 'world', 101]))
