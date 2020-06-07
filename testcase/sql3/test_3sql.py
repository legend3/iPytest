#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os, sys
# sys.path.append(os.path.abspath(os.path.split(os.path.abspath(__file__))[0]))

'''
@Author: LEGEND
@since: 2020-06-07 18:28:26
@lastTime: 2020-06-08 04:06:28
@LastAuthor: Do not edit
@Description: testcase\sql3\test_3sql.py
@version: 
'''


@pytest.mark.dependency()   # 设置测试用例执行顺序
@pytest.mark.flaky(reruns=2, reruns_delay=4)  # 失败重跑该方法
def test_sql3():
    print("3")
    assert True
