#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-06-07 20:18:16
@lastTime: 2020-06-13 14:57:40
@LastAuthor: Do not edit
@FilePath: \iPytest\tools\yamltest.py
@Description: 
@version: 
'''


import pytest
from ruamel import yaml

# @pytest.fixture()
def load_yaml():
    #开档
	with open("E:/workspace/iPytest/data/httpCommon", "r", encoding="utf-8") as docs:
		try:
			alldata = yaml.safe_load(docs)
		except yaml.YAMLError as exc:
			print(exc)
	
	#印出
	for data in alldata:
		print(alldata[data]['联络'])
	
	#修改
	alldata['Tom']['联络'][0]['公司']='963852741'
	
	#写档
	with open('E:/workspace/iPytest/data/httpCommon2', 'w+', encoding='utf8') as outfile:
		yaml.dump(alldata, outfile, default_flow_style=False, allow_unicode=True)

if __name__ == '__main__':
    load_yaml()