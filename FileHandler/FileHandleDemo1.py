#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 文件处理1
import os

print(os.path.basename(__file__))   # 获取当前文件名
print(os.sep)    # 路径分隔符,输出为“\”
print(os.name)    # 输出系统的名称，window输出为“nt”, linux等为‘posix’
print(os.getcwd())    # 获取当前工作目录，即当前python脚本工作的目录路径

print(os.path.isabs('/FileHandler/data.txt'))      # 判断文件或者目录是否是 绝对路径
print(os.path.isabs('/mostNum.txt'))
print(os.path.abspath('testFile.txt'))    # 生成参数文件的 绝对路径
print(os.path.isdir('testFile.txt'))    # 判断 所传参数文件（testFile.txt）是否是目录，不是就返回False
print(os.path.isfile('mostNum.txt'))    # 判断 所传参数文件（mostNum.txt）是否是文件，不是就返回False
print(os.path.getsize('data.txt'))      # 获取文件大小，如果是目录就返回 0


print(os.path.splitext('data.txt'))    # 分离后缀名和文件名, ('data', '.txt')
print(os.path.split('/FirstPythonDemo/FileHandler/data.txt'))    # 将目录名和文件名分离
print(os.listdir())     # 返回指定目录下的所有文件和目录名

# os.mkdir('dir')    # 当前目录下创建文件夹 file
# os.makedirs('dir/file')   # dir下创建文件夹 file
