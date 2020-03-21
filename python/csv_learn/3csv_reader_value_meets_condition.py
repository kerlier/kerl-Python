#!/usr/bin/env python3

# 使用csv模块，筛选csv中满足条件的记录
import csv

input_file = '../csv_data/supplier_data.csv'

output_file = '../csv_data/supplier_data_meets_condition.csv'

with open(input_file, 'r', encoding='utf8', newline='') as csv_in_file:
    with open(output_file, 'w', encoding='utf8', newline='') as csv_out_file:

        # 使用csv模块
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')

        # csv的获取下一行，使用是next函数
        header = next(filereader)
        # 将header写入到另外一个文件中
        filewriter.writerow(header)

        # 然后遍历剩余的数据
        for row in filereader:
            # 取出供应商的值
            supplier = str(row[0]).strip()
            # 取出cost($500.00)
            cost = str(row[3]).strip("$").replace(',', '')
            print("cost {}".format(cost))
            if supplier == 'Supplier X' and float(cost) > 200.0:
                filewriter.writerow(row)



