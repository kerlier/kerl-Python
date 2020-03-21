#!/usr/bin/env python3


# 使用字典生成式

my_dictionary = {'customer7': 7, 'customer2': 9, 'customer3': 11}


# 字典中的前面表示使用的： 表示生成的是一个字典. 如果满足 if后面的条件，就保留这个键值对
my_results = {key:value for key, value in my_dictionary.items() if value > 10}

print("output # 133 {}".format(my_results))
