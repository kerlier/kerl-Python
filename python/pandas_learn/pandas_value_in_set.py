#!/usr/bin/env python3


import pandas as pd

input_file = '../csv_data/supplier_data.csv'

output_file = '../csv_data/pandas_data_in_set.csv'


important_dates = ['11/20/2014']

data_frame = pd.read_csv(input_file)

# isin 后面加上一个list,表示在这个list中
data_frame_in_set = data_frame.loc[(data_frame['Purchase Date'].isin(important_dates)),:]

data_frame_in_set.to_csv(output_file,index=False)