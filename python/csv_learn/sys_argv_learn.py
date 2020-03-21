#!/usr/bin/env python3

import sys
# 这里使用sys模块来获取系统变量,方法是sys.argv[index]


# 需要在命令行中执行 python sys_argv_learn.py
if __name__ == '__main__':
    argv0 = sys.argv[0]  # 第一个参数 就是脚本的名字
    argv1 = sys.argv[1]  # 后面的参数可以自定义
    argv2 = sys.argv[2]

    print("output #135: arg0 {}".format(argv0))
    print("output #135: arg1 {}".format(argv1))
    print("output #135: arg2 {}".format(argv2))