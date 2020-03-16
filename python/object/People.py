#!/usr/bin/python3

# 面向对象
# 定义一个class

class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接访问
    __weight = 0

    # 定义无参构造方法
    def __init__(self):
        self.name = ''
        self.age = 0
        self.__weight =0

    def  __init__(self, name, age, weight):
        self.__weight = weight
        self.name = name
        self.age = age

    def speak(self):
        print("%s 说：我 %d 岁" % (self.name, self.age))

    def getWeight(self):
        return self.__weight

if __name__ == '__main__':
    p1 = people('yangyuguang', 23, 108)
    p2 = people('lvshuzhen', 23, 90)

    print(p1 == p2)
    p1.speak()
    p2.speak()

    print(p1.getWeight())