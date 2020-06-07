#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-07 18:28:26
@lastTime: 2020-06-08 00:47:45
@LastAuthor: Do not edit
@FilePath: \iPytest\testcase\sql4\test_sqlwindow4.py
@Description: 
@version: 
'''

import pytest
import os, sys
sys.path.append(os.path.abspath(os.path.split(os.path.abspath(__file__))[0]))


# @pytest.mark.dependency(depends=["test_sql3"], scope='session')
# def test_sql4():
#     a = 1
#     assert a != 0

# @pytest.mark.dependency()
# def test_01():
#     assert True
#
#
# @pytest.mark.dependency(depends=["test_01"])
# def test_02():
#     print("执行测试2")


@pytest.mark.dependency(name="a")
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert True

@pytest.mark.dependency(name="b")
def test_b():
    assert 2==2

@pytest.mark.dependency(name="c", depends=["a"])
def test_c():
    pass

@pytest.mark.dependency(name="d", depends=["b"])
def test_d():
    pass

@pytest.mark.dependency(name="e", depends=["b", "c"])
def test_e():
    pass
