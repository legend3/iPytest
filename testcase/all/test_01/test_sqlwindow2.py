#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-07 18:28:26
@lastTime: 2020-06-07 23:26:24
@LastAuthor: Do not edit
@FilePath: \iPytest\testcase\sql2\test_sqlwindow2.py
@Description: 
@version: 
'''

import pytest


@pytest.mark.run(order=1)  # 设置测试用例执行顺序
def test_sql2():
    a = 1
    assert a !=0