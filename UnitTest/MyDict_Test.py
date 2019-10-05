#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 13:21
# @Author  : su
# @File    : MyDict_Test.py
"""
单元测试:
以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
"""
import unittest

from UnitTest.MyDict import Dict


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_key_error(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attr_error(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()
