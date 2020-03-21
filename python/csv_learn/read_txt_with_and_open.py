#!/usr/bin/env python3


# python2.5之后，可以使用with语句创建文件对象，在with语句执行完，会自动关闭文件


input_file = '../txt/learn_sys.txt'

# with语句中 as 将前面的对象赋值到 as后的这个变量中
with open(input_file, 'r') as filereader:
    for row in filereader:
        print("output# 137 {}".format(row))

# 语句处理完，会直接关闭文件