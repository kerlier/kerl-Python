#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 本示例中使用通用的编程，读取一个csv文件，然后写到另外一个文件中

input_file = '../csv_data/input.csv'

output_file = '../csv_data/output.csv'

with open(input_file, 'r', newline='', encoding='utf8') as filereader:
    with open(output_file, 'w', newline='', encoding='utf8') as filewriter:
        header = filereader.readline()  # readline先读取第一行 ,header
        print("original header is {}".format(header))
        header = header.strip()
        print("striped header is {}".format(header))

        header_list = header.split(",")
        print("head_list : {}".format(header_list))

        # 将head_list写入到文件中
        # 这里使用map函数，map函数接收一个函数，和 list， 这个函数会作用到list的每个元素上， 返回应该list执行后的结果list
        filewriter.write(','.join(map(str, header_list))+"\n")
        for row in filereader:
            row = row.strip()
            row_list = row.split(",")
            print(row_list)
            filewriter.write(','.join(map(str, row_list))+"\n")
