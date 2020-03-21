#!/usr/bin/env python3

# 写一个求平均值的函数

#
def getMean(numericValues):
    return sum(numericValues) / len(numericValues) if len(numericValues) > 0 else float("nan")

if __name__ == '__main__':
    # numericValues = [1, 2, 3, 4, 5]
    numericValues = []
    print("output #134: mean is {}".format(getMean(numericValues)))