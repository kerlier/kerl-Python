#!/usr/bin/python
# -*- coding:UTF-8 -*-

counter = 100
miles = 100.0
name = "data type"

print(counter)
print(miles)
print(name)


# python允许你为多个变量赋值
a = b = c = 1
print(a)
print(b)
print(c)

# 也可以为多个对象指定多个变量
a, b, c = 1, 2, "data type"

print(a)
print(b)
print(c)

# python一共有六个数据类型

# 不可变的 Number, String, Tuple
# 可变的 List, dic,Set

# 使用type()方法可以查看当前对象类型

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# 也可以使用isinstance(a, int)来判断
print(isinstance(a, int))

# 加减乘除
# 5//4 结果是一个整数
print(5//4)
# 5 / 4 结果是一个浮点数
print(5/4)
# 乘法
print(2*5)
# 乘方
print(2**5)

