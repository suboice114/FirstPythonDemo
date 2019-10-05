#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 文件处理

# demo1
fw = open("testFile.txt", "w")     # w :write only;  文件不存在,不报错,会创建一个文件;   会覆盖文件原有内容.
print("文件名：", fw.name)
print("是否已关闭：", fw.closed)
print("访问模式：",  fw.mode)
fw.write("add line!\nhello world!\n")
fw.close()   # close() 关闭文件

# demo2
fr = open("testFile.txt", "r")    # r: read only ; 若读取的文件不存在，会报错：FileNotFoundError
print(fr.read())
fr.close()

# demo3
fa = open("testFile.txt", "a+")   # a+: 可以执行读写操作； 文件不存在，不报错；不会覆盖文件内容，在文件原有基础新增内容。
fa.write("Append new line.")
fa.close()

# demo4
fr1 = open("testFile.txt", "r+")    # r+:可以执行读写操作;  文件不存在,会报错
print("读取的字符串：", fr1.read(10))
# tell():文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后
position = fr1.tell()
print("当前文件位置：", position)
# seek()改变当前文件的位置
fr1.seek(0, 0)
print("重新定位后再次读取字符串：", fr1.read(10))
fr1.close()

# demo5
fw1 = open("testFile.txt", "w+")    # w+: 可以执行读写操作； 文件不存在,不会报错，会创建新文件;  文件已存在，会覆盖原有内容
fw1.write("hello python\nnew content\nfile handle example\n")
fw1.close()
