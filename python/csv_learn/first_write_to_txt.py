#!/usr/bin/env python3

# 接下来，通过python程序将内容输出到文件中

my_letters = ['a', 'b', 'c', 'd', 'e']

max_index = len(my_letters)


output_file = '../txt/first_write_to_txt.txt'

# 这里使用open 加 w的方式来写入文件

# r 是读取， w是写， a 是追加
filewriter = open(output_file, 'a')
for index_value in range(len(my_letters)):
    if index_value < (max_index - 1):
        filewriter.write(my_letters[index_value] + "\t")
    else:
        filewriter.write(my_letters[index_value] + "\n")

filewriter.close()
print("output #138 : output written to file")