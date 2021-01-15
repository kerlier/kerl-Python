#!/usr/bin/python3

# python可以实现继承
# 引用当前文件夹下的类
from People import people


class Customer(people):
    customerId = ''

    def __init__(self):
        super
        self.customerId  = ''

    def __init__(self, name, age, weight, customerId):
        # 调用父类的构造方法
        people.__init__(self,name, age, weight)
        self.customerId = customerId

    # 覆盖父类的方法
    def speak(self):
        print("customerId: %s, name: %s, age: %d" % (self.customerId, self.name,self.age))


if __name__ == '__main__':
    c = Customer("yang",10, 102, "001")
    print(c.name)
    print(c.customerId)
    print(c.age)
    c.speak()

    print(c.getWeight())