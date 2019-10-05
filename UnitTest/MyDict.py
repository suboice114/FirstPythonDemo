#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 13:15
# @Author  : su
# @File    : MyDict.py


class Dict(dict):

    def __init__(self, **kwargs):
        super.__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
