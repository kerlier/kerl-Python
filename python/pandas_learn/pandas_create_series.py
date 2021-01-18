#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
'''
创建Pandas中的Series
'''

'''
1. 多维数组
'''
# 使用np创建一个array,长度为5
data = np.random.randn(5)
print('data：', data)
s = pd.Series(data, index=['a', 'b', 'c', 'e', 'e'])
print('series from arrays:', s)
# 获取Series中的索引
print('series from arrays, index:', s.index)
# Series中的索引值可以重复，获取重复的索引值时，会得到不同的值
print("series e's column value:", s['e'])

'''
2. 字典
'''
data = {'a': 1, 'b': 2, 'c': '3'}

# 在未指定index时，字典创建Series, 默认将key当做索引，value作为值
s = pd.Series(data)
print('series from dictionary:', s)
print('series from dictionary index:', s.index)

# 指定index时，会从data中获取每个索引的值，缺失数据为Nan
s = pd.Series(data, index=['e', 'f', 'g', 'a'])
print('series from dictionary with index:', s)

'''
3. 标量值(必须提供索引)
'''
# 标量值必须提供索引: 会按照索引长度重复标量值
s = pd.Series(5, index=['a', 'b', 'c'])
print(s)
'''
output:
    a    5
    b    5
    c    5
    dtype: int64
'''

