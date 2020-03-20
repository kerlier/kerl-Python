#!/usr/bin/env python3

y = ['Jan', 'Feb', 'Mar', 'Apr', 'May']


# 直接使用in 来遍历列表
for month in y:
    print("current month is {}".format(month))

# 使用range先获取长度，然后再进行遍历
for index in range(len(y)):
    print("current month is {}".format(y[index]))

# for循环中，加上一个if判断，注意缩进
for month in y:
    if month.startswith('J'):
        print("the month that meet the requirement is {}".format(month))