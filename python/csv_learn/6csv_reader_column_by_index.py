#!/usr/bin/env python3


# 使用基本的csv模块，根据列的索引 选取特定的列
import csv


input_file = '../csv_data/supplier_data.csv'

output_file = '../csv_data/supplier_data_column_by_index.csv'

# 保留的索引值
my_columns = [0, 3]
with open(input_file, 'r', encoding='utf8', newline='') as csv_in_file:
    with open(output_file, 'w', encoding='utf8', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')

        for row in filereader:
            new_row = []
            for index_value in my_columns:
                new_row.append(row[index_value])
            #输入到文件中
            filewriter.writerow(new_row)


