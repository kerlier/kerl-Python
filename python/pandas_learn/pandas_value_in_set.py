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

# 使用loc提取列数据
target_column_frame = csv_data_frame.loc[:, "Supplier Name"].to_frame()
print('target column frame:', type(target_column_frame))
print(target_column_frame)

# 使用iloc提取列数据
first_column_frame = csv_data_frame.iloc[:, 0].to_frame()
print('first_column_frame',type(first_column_frame))
print(first_column_frame)

# 提取特定列 特定行数据
target_column_index_frame = csv_data_frame.loc[[0], ['Supplier Name']]
print('target_index_column_frame:', type(target_column_index_frame))
print(target_column_index_frame)

# 提取第一行，第一列的数据
first_index_column_frame = csv_data_frame.iloc[[0], [0]]
print('first_index_column_frame:', type(first_index_column_frame))
print(first_index_column_frame)

# 提取所有数据
all_frame = csv_data_frame.loc[:, :]
print('all_frame:', type(all_frame))
print(all_frame)

# 使用iloc提取所有数据
all_frame1 = csv_data_frame.iloc[:, :]
print('all_frame1', type(all_frame1))
print(all_frame1)

# 使用loc提取相关的行
filter_frame = csv_data_frame.loc[csv_data_frame['Supplier Name'] == 'Supplier X']
print('filter_frame:', type(filter_frame))
print(filter_frame)

loc = csv_data_frame.loc["Supplier X"]
print(loc)
# isin 后面加上一个list,表示在这个list中
data_frame_in_set = csv_data_frame.loc[(csv_data_frame['Purchase Date'].isin(important_dates))]
data_frame_in_set.to_csv(output_file, index=False)