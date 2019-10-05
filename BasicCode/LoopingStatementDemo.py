#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
循环语句: while语句，for语句，continue, break,嵌套循环
"""

# A：while 语句
count = 0
while count < 9:
    print("This count is :", count)
    count = count + 1
print("END")

# while 中的 break 的使用 :计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
sum0 = 0
x = 1
n = 1
while True:
    if n > 20:
        break
    sum0 = sum0 + x
    x = x * 2
    n = n + 1
print("sum0 = ", sum0)

# while 中 continue 的使用:输出 0 - 10 之内的 偶数
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print("i:", i)

# while 循环中 使用 break 和 continue : 0-100之内 奇数的和
sum1 = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum1 = sum1 + x
print("sum1=", sum1)

# B：for循环
# 9*9乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d * %d = %d" % (j, i, i * j), end=" ")
    print("")

for letter in 'Python':
    print("当前字母：", letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:
    print("当前水果：", fruit)

# 通过序列索引迭代
for index in range(len(fruits)):
    print("当前水果：", fruits[index])


# for循环中使用 else
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num % i
            print("%d 等于 %d * %d " % (num, i, j))
            break
    else:
        print(num, "是一个质数")

# C：Python嵌套循环
# 嵌套循环：输出 2 - 100 之间的素数
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print(i, " 是素数")
    i = i + 1

# 嵌套循环：对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print(x * 10 + y)

# 循环中的 break 和 continue
for char in 'Python':
    if char == 'h':
        break
    print("当前字母：", char)


var = 10
while var > 0:
    print("当前变量值：", var)
    var = var - 1
    if var == 5:
        break
print("END1")


for letter in 'Python':
    if letter == 'h':
        continue
    print("当前字母：", letter)

h = 10
while h > 0:
    h = h - 1
    if h == 5:
        continue
    print("当前变量值：", h)
print("END2")

# D：pass 语句:不做任何事情，一般用做占位语句。
# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)

