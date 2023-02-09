#!/usr/bin/env python
# coding=utf-8
"""
Author: xiaobin.zhu
since: 2023-01-29 13:59:33
LastAuthor: xiaobin.zhu
LastEditTime: 2023-01-29 13:59:35
Description: write something
FilePath: gen_template
Copyright(c): 企知道-数据采集部
"""

for i in range(1, 37, 1):
    print("{" + f"{{args{i}.DATA}}" + "}")
