#!/usr/bin/env python3

import pandas as pd

# 使用pandas模块，筛选csv中满足条件的记录
input_file = '../csv_data/supplier_data.csv'

output_file = '../csv_data/pandas_data_meets_condition.csv'

data_frame = pd.read_csv(input_file)

#print("pandas data_frame: \n{}".format(data_frame))

# 取出data_frame中的Cost的值

#print("Cost :\n{}".format(data_frame['Cost']))

# 进行过滤date_frame
data_frame['Cost'] = data_frame['Cost'].str.strip("$").astype(float)

#
data_frame_value_meet_condition = data_frame.loc[(data_frame['Supplier Name'].str.contains('Y')) & (data_frame['Cost']> 200),:]

data_frame_value_meet_condition.to_csv(output_file,index=False)