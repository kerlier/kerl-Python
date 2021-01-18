#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# 创建元素都是1的数组。传入一个shape. 默认dtype是float64
npArray1 = np.ones((2, 3))
print('npArray:', npArray1)
print('npArray shape:', npArray1.shape)
print('npArray dtype:', npArray1.dtype)

# 创建元素都是1的数组。传入一个shape。指定dtype
npArray2 = np.ones((2, 3), dtype=np.int)
print('npArray2:', npArray2)
print('npArray2 shape:', npArray2.shape)
print('npArray2 dtype:', npArray2.dtype)