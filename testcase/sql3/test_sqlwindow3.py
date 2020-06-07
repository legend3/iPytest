#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os, sys

'''
@Author: LEGEND
@since: 2020-06-07 18:28:26
@lastTime: 2020-06-08 00:47:53
@LastAuthor: Do not edit
@Description: 
@version: 
'''


@pytest.mark.dependency()   # 设置测试用例执行顺序
def test_sql3():
    assert 1 == 1
