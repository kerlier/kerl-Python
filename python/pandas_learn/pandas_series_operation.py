#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


data = np.random.randn(5)
print('data：', data)
s = pd.Series(data, index=['a', 'b', 'c', 'e', 'e'])
# 根据列的下标值获取数据
print("series value of 4' columns is:", s[[4]])