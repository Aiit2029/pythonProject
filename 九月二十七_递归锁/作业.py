#   进程之间内存是否共享  ？
'''
    进程之间内存不共享 如果需要共享 可以使用Manager模块   共享数据
'''
import time
#   进程之间如何实现通讯  IPC
    #基于 socket  基于 第三方软件  消息中间件
    # 基于 队列

#   聊聊 进程队列的特点和 实现原理
    #

#   进程的三状态转换图
    #   阻塞  运行  就绪
    # 阻塞  ->就绪 -> 运行
    # 运行 -> 阻塞
    # 运行 -> 就绪
#   生产者消费者模型
# from multiprocessing import Process,Queue
#
# def consumer(q,name):
#
#     while True:
#         food = q.get()
#         if food:
#             print(f'{name}消费了{food}')
#         else:break
#
#
# def producer(q):
#     for i in range(10):
#         foodi = f'food{i}'
#         q.put(foodi)
#         print(f'生产了food{i}')
#
# if __name__ == '__main__':
#     q = Queue()
#     p2 = Process(target=producer, args=(q,))
#     p1 = Process(target=consumer, args=(q,'1'))
#     p2.start()
#     p1.start()
#     p2.join()
#     q.put(None)

#   进程在计算机中扮演什么角色    线程呢 ？
    # 进程是 资源调配的 最小角色   线程是cpu 调度的最小角色


#GIL锁 是怎么回事
#GIL 锁 是python线程 运行前必须要的得到的锁 ，python2中每 运行 100字节码 就需要释放gil锁 ，重新争抢锁或者让出锁 让其他线程争抢锁
# 在 python3中每 15ms 就会释放 gil锁 ，
# 为了保证在同一时间内  python 中只有一个线程独占 python解释器的执行权

#在python中是否线程安全
    #python中 多线程 对 全局变量或者静态变量 进行操作 是数据不安全的
    # += -=  if  while  *= /= 以及 先赋值在等于，先判断在等于 是数据不安全的
    # 而 append  pop  等操作 是数据安全的
    # 在python中是否线程安全取决于 具体的操作和场景
    # 在 python中 有实现线程安全的模块 例如 Queue，socket
# 什么叫死锁
    # 死锁的四个条件：　　互斥性　不可剥夺性　循环等待性，　请求与保持(请求新资源 保持旧资源)
    # 死锁 ：多线程之间 竞争资源，导致的 互相等待
#logging 模块是否线程安全
    # logging  是线程安全的
# queue模块是否 线程安全
    #也是线程安全的
#