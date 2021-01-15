#!/usr/bin/env python3

# 创建字典,在python中 ,花括号表示字典

empty_dict = {}
a_dict = {'one': 1, 'two': 2, 'three': 3}

print("output #102: {}".format(a_dict))

print("output #103: a_dict has {} elements".format(len(a_dict)))

# 字典中可以存放list,第一次知道
another_dict = {'x': 'printer', 'y': 5, 'z': ['star', 'circle', 9]}
print("output #104: another_dict {}".format(another_dict))

print("output #105: another_dict has {} elements".format(len(another_dict)))


# 引用字典中的值,直接使用中括号，然后返回结果即可
print("output #106: {}".format(another_dict['x']))

print("output #107: {}".format(another_dict['z']))


# copy一个字典
another_new_dict = another_dict.copy()

print(another_new_dict)

# 获取字典中的键
another_dict_keys = another_dict.keys()
print("output #108: {}".format(another_dict_keys))

# 获取字典中的值
another_dict_values = another_dict.values()
print("output #109: {}".format(another_dict_values))

# 获取字段中item
another_dict_items = another_dict.items()
print("output #110: {}".format(another_dict_items))

# 使用for循环来遍历字典中的数据
for key, value in another_dict_items:
    print("key: {}, value:{}".format(key, value))


# 使用字典的中in
print('dict:', another_dict)
print('in', 'x' in another_dict)

# 使用get获取参数值
print("x 's value in dict is {}".format(another_dict.get('x')))
print("y 's value in dict is {}".format(another_dict.get('y')))

print("c 's value in dict is {}".format(another_dict.get('c')))