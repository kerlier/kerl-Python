#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

'''
1. Series字典
'''
# 使用Series字典创建dataFrame: 相当于将每个Series当做列
# column索引是字典中的key
# 行是字典中的value

data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series((1, 2, 3, 4), index=['a', 'b', 'c', 'd'])}

d = pd.DataFrame(data)
print('dataFrame from dictionary:', d)

# 获取特定index的值, 并生成DataFrame
d1 = pd.DataFrame(d, index=['a', 'b'])
print('dataFrame value of [a, b] index:', d1)
print('dataFrame type of [a, b] index:', type(d1))

# 获取特定index以及特定column的值
d2 = pd.DataFrame(d, index=['a', 'b'], columns=['three', 'two'])
print('dataFrame value of [a, b] index with columns', d2)
print('dataFrame type of [a, b] index with columns', type(d2))


'''
2. Python字典
'''
# 将字典中的key当做columns
# 将value当做列. value必须要有相同的长度
# 没有传index时， 取值是range(n) n是数组的长度
# 传index时，长度必须跟数组长度一致
data = {'one': [1, 2, 3, 4],
        'two': [10, 20, 30, 40]}
d = pd.DataFrame(data)
print('dataFrame created by Python dictionary:', d)

d1 = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print('dataFrame created by Python dictionary with index:', d1)

