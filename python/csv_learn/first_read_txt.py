#!/usr/bin/env python3


# 读取文本文件，然后将内容输出到控制台上


# 使用open方法打开一个文件, 不提倡使用直接使用open方法获取文件内容
# 推荐使用with 结合 open的方法，具体内容看 read_txt_with_and_open.py

input_file = '../txt/learn_sys.txt'

# r表示 读， w表示写
filereader = open(input_file, 'r')


# 直接使用for循环来获取文本的内容

for line in filereader:
    if line is not None and line.strip() != '' and len(line) != 0:
        print("output #136:{}".format(line), end='')


# 最后都要关闭filereader
filereader.close()