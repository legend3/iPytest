#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-07 18:28:26
@lastTime: 2020-06-08 00:04:06
@LastAuthor: Do not edit
@FilePath: \iPytest\testcase\sql4\test_sqlwindow4.py
@Description: 
@version: 
'''

import pytest


@pytest.mark.dependency(depends=["Test_Login::test_login"])  # 设置测试用例执行顺序
def test_sql4():
    a = 1
    assert a !=0