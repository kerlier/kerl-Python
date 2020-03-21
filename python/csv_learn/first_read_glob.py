#!/usr/bin/env python3

import glob
import os
# 使用glob读取和处理多个输入文件，glob处理的是目录

# 直接import glob 就可以使用glob


# os.path.join(inputPath, '*.txt') 表示筛选出来inputPath所有的txt文件

# os.path.join(inputPath, '*') 表示匹配所有的文件

# os.path.join(inputPath,'*.csv') 表示匹配所有的csv文件

inputPath = '../glob_txt'

for input_file in glob.glob(os.path.join(inputPath, '*.csv')):
    with open(input_file, 'r') as input_file_reader:
        for row in input_file_reader:
            print("output #138 {}".format(row))