#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# 创建numpy的2维3列的数组. 默认dtype是float64
npArray = np.zeros([2, 3])
print('dtype:', npArray.dtype, 'zero array as below:')
print(npArray)

# 创建2维3列的数组,类型是np.int
npArray1 = np.zeros([2, 3], dtype=np.int)
print('int zero as below:')
print(npArray1)