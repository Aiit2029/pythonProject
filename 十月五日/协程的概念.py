#协程  是 单线程下的并发 ， 是 用户级别的 一条 轻量级线程 ，
# 即 在  一条 线程上 进行 切换多个任务 来 规避 所有的 io 操作
# gevent 利用了  greenlet  底层模块实现的切换 和 自动规避 io的功能
# asyncio 利用了 python 自己的 yield 底层语法完成的切换  + 自动规避 io的功能
    # tornado 异步的 web框架
    # yield from 的出现 是 为了更好的实现协程
    # send  也是 为了更好的实现协程
    # asyncio模块 基于python 原生的 协程 的概念正式被成立
    # 这个模块特殊到 ， python中提供了 协程功能的关键字  async await

# 协程 是由 用户程序自己调控的
# 缺点 ：
# 协程的本质 ： 是单线程的 ，无法利用多核
#  协程 是 单个线程 ，一旦出现阻塞 ，将会阻塞整个线程
#  修改共享数据 不需要加锁



#   协程 是 数据安全的      用户级别的      开销更小
#   线程 是 数据不安全的    操作系统级别的   开销小
#   进程 是 数据不安全的    操作系统级别的   开销非常大
#  有人说  协程 这么好 为什么 还有线程 ， 都用协程不好吗 ？
    # 协程 的缺点之一 ： 就是 不能利用多核
    # 线程 可以 ，  而且 协程 规避的io操作 是用户级别的 ，
    # 许多 io 操作 在 操作系统级别，协程规避不掉啊
    # 这个时候 就需要用 线程
#  gevent
# import random
#
# import gevent
# from gevent import monkey
# monkey.patch_all()
# import time
# from threading import Thread, current_thread
#
# def func(n):
#     print("start gevent")
#     x = random.randint(1,5)
#     time.sleep(x)
#     print(x)
#     print(f'{n},{current_thread().ident}')
#     print("end gevent")
#
# if __name__ == '__main__':
#     g1 = gevent.spawn(func,1)
#     g2 = gevent.spawn(func,2)
#     g3 = gevent.spawn(func,3)
#     g4 = gevent.spawn(func,4)
#
#     gevent.joinall([g1, g2,g3,g4])