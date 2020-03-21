#!/usr/bin/env python3

# 学习if_else的使用

x = 5

if x > 4 or x != 9:
    print("output #124: {}".format(x))
else:
    print("output #125: x is not greater than 4")


y = 5

# 在python中， 可以在语句后面加上 if else,(类似于列表表达式)
x = y if y > 6 else 7

print(x)