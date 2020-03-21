#!/usr/bin/env python3

# 测试readline的函数

input_file = '../txt/learn_sys.txt'


with open(input_file, 'r') as filereader:


    row1 = filereader.readline()
    row2 = filereader.readline()
    row3 = filereader.readline()
    row4 = filereader.readline()
    row5 = filereader.readline()
    row6 = filereader.readline()

    print(row1, end='')
    print(row2, end='')
    print(row3, end='')
    print(row4, end='')
    print(row5)
    print(row6 is None)
    print(row6 == '')


with open(input_file, 'r') as filereader:
    first_row = filereader.readline()
    # readlien之后, 再执行filereader for循环中的数据是剩下的line
    print(first_row)
    print("=============")
    for row in filereader:
        print(row)