#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

'''
@Author: LEGEND
@since: 2020-06-07 18:28:26
@lastTime: 2020-06-08 00:03:17
@LastAuthor: Do not edit
@FilePath: \iPytest\testcase\sql3\test_sqlwindow3.py
@Description: 
@version: 
'''

@pytest.mark.dependency()   # 设置测试用例执行顺序
def test_sql3():
    assert 1==1