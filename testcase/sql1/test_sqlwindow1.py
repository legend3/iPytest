#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

'''
@Author: LEGEND
@since: 2020-06-07 18:28:26
@lastTime: 2020-06-07 23:06:15
@LastAuthor: Do not edit
@FilePath: \iPytest\testcase\sql1\test_sqlwindow1.py
@Description: 
@version: 
'''

@pytest.mark.run(order=2)  # 设置测试用例执行顺序
def test_sql1():
    assert 1==1