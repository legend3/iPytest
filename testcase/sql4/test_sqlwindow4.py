#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-07 18:28:26
@lastTime: 2020-06-08 00:29:27
@LastAuthor: Do not edit
@FilePath: \iPytest\testcase\sql4\test_sqlwindow4.py
@Description: 
@version: 
'''

import pytest
import os, sys
# sys.path.append(os.path.abspath(os.path.split(os.path.abspath(__file__))[0]))


@pytest.mark.dependency(depends=["sql3/test_sqlwindow3.py::test_sql3"])  # 设置测试用例执行顺序
# @pytest.mark.run(order=3)
def test_sql4():
    a = 1
    assert a != 0
