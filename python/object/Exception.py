#!/usr/bin/python3

# 异常的实现
if __name__ == '__main__':
    while True:
        try:
            x = int(input("请输入一个数字"))
            print(x)
            break
        except Exception:
            print("输入错误")
        else:
            print("输入正确")
        finally:
            print("输入完毕")