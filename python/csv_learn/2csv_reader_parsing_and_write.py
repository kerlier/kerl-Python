#!/usr/bin/env python3

import csv
# 使用csv模块来操作csv文件，第一步：先import

input_file = '../csv_data/input.csv'

output_file = '../csv_data/output_with_csv.csv'

with open(input_file, 'r', encoding='utf8', newline= '') as csv_in_file:
    with open(output_file, 'w', encoding='utf8', newline='') as csv_out_file:
        # csv.reader 读取一个文件基本的fileReader，需要传一个delimiter
        filereader = csv.reader(csv_in_file, delimiter=',')
        # csv.writer 也是需要传一个基本的filewriter，
        filewriter = csv.writer(csv_out_file, delimiter=',')
        for row in filereader:
            print(row)
            filewriter.writerow(row)