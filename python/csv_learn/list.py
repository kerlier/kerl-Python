#!/usr/bin/env python3
from operator import itemgetter

a_list = [1 , 2, 3]


print(a_list)

# 这个是引用
a_new_list = a_list

# 列表复制
b_new_list = a_list[:]

a_list.append(4)

print("a_new_list:" + str(a_new_list))
print("b_new_list:" + str(b_new_list))

print(a_new_list == a_list)

print(b_new_list == a_list)


# python中可以 使用in 和 not in
print(1 in a_list)
print(1 not in a_list)

# 列表反转
# a_list.remove(3)
a_list.reverse()
print(a_list)

# 列表排序
a_list.sort(reverse=True)

print(a_list)

# 使用sorted函数，对某个位置进行排序
my_lists = [[5, 2, 3, 4], [4, 3, 2, 4], [2, 4, 1, 3]]

# 相当于没有排序
default_sorted_my_list = sorted(my_lists)

print(default_sorted_my_list)

# 这里使用的lambda函数 ，这个函数需要另外学习
my_lists_sorted_by_index_3 = sorted(my_lists,key= lambda index_value:index_value[3])

print(my_lists_sorted_by_index_3)

# 使用operator 中itemgetter进行多个元素的排序

my_lists_sorted_by_index_3_and_0 = sorted(my_lists,key=itemgetter(3, 0))

print(my_lists_sorted_by_index_3_and_0)
