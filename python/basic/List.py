#!/usr/bin/python3
# -*- coding:UTF-8 -*-


list = ['a', 'b', 'c', 'd', 'e']

secondList = ['www', 'baidu', 'com']

# list[头下标：尾下标]
# 左闭右开

print(list[1:3])  # 输出的是 b,c
print(list[:4])   # 输出的是 a, b, c, d
print(list[3:])   # 输出的是 d, e
print(list[:])    # 输出list的所有元素
print(list * 2)   # 输出两遍 list
print(list + secondList)  # 拼接两个list

# list的元素是可变的
list[0] = 9       # 将list中第一个元素设置为9
print(list)
list[2:3] = [10]  # 将 list中第二个元素到第三个元素设置为10
print(list)

list[2:5] = []    # 将list设置为空
print(list)


# 翻转list
def reverseWords(input):
    intputWords = input.split(" ")
    inputWords = intputWords[-1::-1]
    output = ' '.join(inputWords)
    return output

if __name__ == '__main__':
    input = 'I like python'
    output = reverseWords(input)
    print(output)



