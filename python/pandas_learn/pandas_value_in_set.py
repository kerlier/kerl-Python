# -*- coding:utf-8
#!/usr/bin/env python3

import pandas as pd

input_file = '../csv_data/supplier_data.csv'

output_file = '../csv_data/pandas_data_in_set.csv'


'''
Supplier X,001-1001,2341,$500.00 ,1/20/2014
Supplier Y,50-9501,7009,$250.00 ,2/3/2014
'''

important_dates = ['1/20/2014']

csv_data_frame = pd.read_csv(input_file)

print('csv_data_frame type: ', type(csv_data_frame))
print(csv_data_frame)

# 将Series转换成frame,使用to_frame()
target_index_frame = csv_data_frame.loc[0].to_frame()
print('取索引为0的行:', type(target_index_frame))
print(target_index_frame)

# 使用iloc取第一行数据
first_line_frame = csv_data_frame.iloc[0].to_frame()
print('取第一行数据', type(first_line_frame))
print(first_line_frame)

# loc = data_frame.loc["Supplier X"]
# print(loc)
# # isin 后面加上一个list,表示在这个list中
# data_frame_in_set = data_frame.loc[(data_frame['Purchase Date'].isin(important_dates))]
# #
# # data_frame_in_set.to_csv(output_file, index=False)