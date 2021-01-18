#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
bracket: 括号
不同括号的区别
'''
a = (5)  # 表示是一个int类型
print("a 's value:", a, ", type:", type(a))
# output:("a 's value:", 5, ', type:', <type 'int'>)

b = (5,)  # 括号加一个元素还有一个逗号，表示是一个tuple类型
print("b 's value:", b, ", type:", type(b))
# output: ("b 's value:", (5,), ', type:', <type 'tuple'>)

c = (5, 5)  # tuple类型
print("c 's value:", c, ", type:", type(c))
# output: ("c 's value:", (5, 5), ', type:', <type 'tuple'>)

d = [5]  # list类型
print("d 's value:", d, ", type:", type(d))
# output:("d 's value:", [5], ', type:', <type 'list'>)

e = [5, ]  # list类型
print("e 's value:", e, ", type:", type(e))
# output:("e 's value:", [5], ', type:', <type 'list'>)

f = [5, 5]  # list类型
print("f 's value:", f, ", type:", type(f))
# output: ("f 's value:", [5, 5], ', type:', <type 'list'>)
