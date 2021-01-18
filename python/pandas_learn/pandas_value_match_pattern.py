# -*— coding:utf-8
# !/usr/bin/env python3
# 使用startwith来筛选数据


import pandas as pd

input_file = '../csv_data/supplier_data.csv'

output_file = '../csv_data/pandas_data_match_pattern.csv'

# 使用pd.read_csv读取参数
data_frame = pd.read_csv(input_file)

# 使用startswith进行过滤数据
data_frame_match_pattern = data_frame.loc[(data_frame['InvoiceNumber'].str.startswith('001-'))]

# DataFrame中有行索引，还有列索引。 index=False表示将行索引去掉
data_frame_match_pattern.to_csv(output_file, index=False)
