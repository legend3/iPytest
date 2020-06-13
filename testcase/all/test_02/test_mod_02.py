#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-07 20:08:23
@lastTime: 2020-06-09 23:50:28
@LastAuthor: Do not edit
@FilePath: \iPytest\testcase\all\test_02\test_mod_02.py
@Description: 
@version: 
'''


# test_mod_02.py

import pytest

# @pytest.mark.dependency()
# @pytest.mark.xfail(reason="deliberate fail")
# def test_a():
#     assert False
parallel
concurrent
@pytest.mark.dependency(
    depends=["testcase/all/test_01/test_mod_01.py::test_a", "testcase/all/test_01/test_mod_01.py::test_c"],
    scope='session'
)
def test_e():
    pass

# @pytest.mark.dependency(
#     depends=["tests/test_mod_01.py::test_b", "tests/test_mod_02.py::test_e"],
#     scope='session'
# )
# def test_f():
#     pass

# @pytest.mark.dependency(
#     depends=["tests/test_mod_01.py::TestClass::test_b"],
#     scope='session'
# )
# def test_g():
#     pass