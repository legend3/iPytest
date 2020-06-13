#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-07 20:18:16
@lastTime: 2020-06-13 14:39:27
@LastAuthor: Do not edit
@FilePath: \iPytest\testcase\conftest.py
@Description: 
@version: 
'''


import pytest


@pytest.fixture()
def load_yaml():
    #开档
with open("人资.yaml", "r",encoding="utf-8") as docs:
	try:
		alldata = ruamel.yaml.safe_load(docs)
	except ruamel.yaml.YAMLError as exc:
		print(exc)
 
#印出
for data in alldata:
	print(alldata[data]['联络'])
 
#修改
alldata['Tom']['联络'][0]['公司']='963852741'
 
#写档
with open('人资1.yaml', 'w+', encoding='utf8') as outfile:
	ruamel.yaml.dump(alldata, outfile, default_flow_style=False, allow_unicode=True)