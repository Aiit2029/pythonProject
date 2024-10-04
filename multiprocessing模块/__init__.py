# multiple  多元化的
# processing 进程
# multiprocessing 多元的处理进程的模块
import random
import time
from multiprocessing import Process
# 一般情况下大写的 单词是个类
import os

#
# def func(*args):
#     print(f'{args[0]}:{args[1]}')
#     time.sleep(random.random())
#     print('发送完毕')
# print('123')   在windows中执行会 输出两次 123
# 而在 linux中只会输出 1次
#  pid   == process id
#  ppid  ==  parent process id  父进程的id

# if  __name__ == '__main__':
#     p = Process(target=func,args =('alex',74))
#     #  args 中需要传入的是元组
#     p.start()

#  为什么没有if __name__ == '__main__'会报错
    # 为什么在mac电脑上 不加也不报错
    # 进程之间的所有的内存是隔离的
    # 父进程的空间 在没有执行代码之前就已经存在了
        # 因为linux中 永远把父进程的空间复制到子进程中,而不是使用import
        # 而在windows中p.start() 会再次打开一个子进程，子进程会import 父进程中的所有文件然后执行
        # 这导致如果不使用 if __name__ == '__main__'  会无限递归 p.start()


# 能不能给子进程传递参数
#     p = Process(target=func,args =('alex'))
#     #  args 中需要传入的是元组
# 能不能获取子进程的返回值
    # 不能

# 能不能同时开启多个子进程
#     可以, 异步非阻塞

# join的用法
    #
# if __name__ == '__main__':
#     arg_lst = [('张全蛋', 14),('alex', 24),('李康南', 34),('烟嗓经', 44)]
#     info_lst = []
#     for arg in arg_lst:
#         p = Process(target=func, args=arg)
#         p.start()
#         info_lst.append(p)
#     for p in info_lst:
#         p.join()
#     print('结束啦')
    # while True:
    #     while len(info_lst) == len(arg_lst):
    #
    #         break
    #     break
    # p = Process(target=func, args=('alex', 24))
    # p.start()
    # p = Process(target=func, args=('李康南', 34))
    # p.start()
    # p = Process(target=func, args=('烟嗓经', 44))
    # #  args 中需要传入的是元组
    # p.start()
    #
    # p.join()
    # p.join()
    # p.join()

    # 如果不加p.join() 则结束咯会出现在开始，这是一种欺骗行为
    # 加上p.join() 则会阻塞子进程到 发送结束之后，在发送结束咯


# 同步阻塞 异步非阻塞
    # 同步阻塞 join
    # 异步非阻塞 start


# 多进程中间的数据是否是隔离的
from multiprocessing import Process
n = 0

def func():
    global n
    n += 1

if  __name__ == '__main__':
    p_lst = []
    for i in range(100):
        p = Process(target=func)
        p.start()
        p_lst.append(p)

    for p in p_lst:p.join()
    print(n)


