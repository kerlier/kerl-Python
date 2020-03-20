#!/usr/bin/env python3

print("output #1 : I'm excited to learn python")

x = 9
y = 10
z = 11
print("output #2 : {0} {1} {2}".format(x, y, z))

print("output # 3: {0}".format(3**4))

my_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 列表生成式
rows_to_keep = [row for row in my_data if row[2] > 5]

print(rows_to_keep)