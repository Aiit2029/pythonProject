'''
和python解释器相关的操作
'''
import sys

# 获取命令行方式运行的脚本后面的参数

# print(sys.argv)
# sys.argv[0]        # 脚本名
# print(sys.argv[1]) # 第一个参数
# print(sys.argv[2]) # 第二个参数

# arg1 = int(sys.argv[1])
# arg2 = int(sys.argv[2])
# print(arg1 + arg2)


# 解释器 寻找模块的路径
# print(sys.path)

print(sys.modules[__name__])