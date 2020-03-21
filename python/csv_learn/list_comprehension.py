#!/usr/bin/env python3

original_list = [1, 2, 3, 4, 5]

# 使用简单的for循环
for x in original_list:
    print(x)

powers = []
# 获取乘方
for x in original_list:
    powers.append(x*x)

print(powers)

# 使用列表生成式
powers = [x*x for x in original_list]
print(powers)

# 使用列表生成式，后面可以加上if 条件
powers = [x*x for x in original_list if x > 3 and x != 4]
print(powers)



