#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
@Author: LEGEND
@since: 2020-06-07 18:15:13
@lastTime: 2020-06-08 00:37:09
@LastAuthor: Do not edit
@FilePath: \iPytest\run.py
@Description: 
@version: 
'''


import pytest
import os, sys
sys.path.append(os.path.abspath(os.path.split(os.path.abspath(__file__))[0]))


if __name__ == '__main__':
    args = ['-v', '-s', './testcase/sql4/test_sqlwindow4.py']
    pytest.main(args)
