#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-07 18:28:26
@lastTime: 2020-06-07 21:28:06
@LastAuthor: Do not edit
@FilePath: \iPytest\testcase\sql2\test_sqlwindow2.py
@Description: 
@version: 
'''


def test_sql2(a):
    print("断点", a)
    # a = [2]
    assert a==2

if __name__ == '__main__':
    test_sql2(2)
    