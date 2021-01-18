#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd


input_file = '../csv_data/supplier_data.csv'
file_dataFrame = pd.read_csv(input_file)

# 获取dataFrame中的列
for col in file_dataFrame.columns:
    series1 = file_dataFrame[col]
    print(series1)
    print('---------------')
