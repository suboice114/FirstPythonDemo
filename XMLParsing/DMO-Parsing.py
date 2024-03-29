#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/1 13:42
# @Author  : su
# @File    : DMO-Parsing.py
"""
DOM(Document Object Model-文件对象模型)方式解析 xml：
一个 DOM 的解析器在解析一个 XML 文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，
之后 可以利用DOM 提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过的内容写入xml文件。
"""
from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print("*****Movie*****")

    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))

    type1 = movie.getElementsByTagName('type')[0]
    print("Type: %s" % type1.childNodes[0].data)

    format1 = movie.getElementsByTagName('format')[0]
    print("Format: %s" % format1.childNodes[0].data)

    rating = movie.getElementsByTagName('rating')[0]
    print("Rating: %s" % rating.childNodes[0].data)

    description = movie.getElementsByTagName('description')[0]
    print("Description: %s" % description.childNodes[0].data)
