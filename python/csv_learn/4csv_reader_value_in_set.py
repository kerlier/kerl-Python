#!/usr/bin/env python3

import csv

input_file = '../csv_data/supplier_data.csv'

output_file = '../csv_data/supplier_data_in_set.csv'

important_dates = ['1/20/2014']

with open(input_file, 'r', encoding='utf8', newline='') as csv_in_file:
    with open(output_file, 'w', encoding='utf8', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')

        #先读取第一行数据
        header = next(filereader)
        filewriter.writerow(header)

        for row_list in filereader:
            # 获取日期
            row_date = row_list[4]
            print(row_date)
            if row_date in important_dates:
                filewriter.writerow(row_list)
