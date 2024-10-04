#  线程池

__author__ = ''
__date__ = ''
__version__ = ''
__license__ = ''
__copyright__ = ''
__email__ = ''
__status__ = ''

import os
import queue
#  进程 ，线程
    #  进程 ：
    # from multiprocessing import Process, Queue
    #
    #
    # def func(q):
    #     for i in range(1,11):
    #         q.put(i)
    #         print(f"{i}号机甲已进入测试场地")
    #     q.put(None)
    #
    #
    # def func2(q):
    #     while True:
    #         info = q.get()
    #         if info:
    #             print(f"{info}号机甲通过测试")
    #         else:break
    #
    #
    #
    # if __name__ == '__main__':
    #     q = Queue()
    #     p = Process(target=func, args=(q,))
    #     p1 = Process(target=func2, args=(q,))
    #     p1.start()
    #     p.start()
    #     p1.join()
    #     p.join()



# 线程 生产者模型
# from  threading import Thread,Lock,RLock
# from queue import Queue
# def func1(q):
#
#     for i in range(10):
#         foodi = f'food{i}'
#         q.put(foodi)
#         print(f'已生产food{i}')
#
#     print('func1')
#     q.put(None)
# def  func2(q):
#     while True:
#         food = q.get()
#         if food:
#             print(f'已消费{food}')
#         else:break
#
#
#
#
#
# if __name__ == '__main__':
#     q = Queue()
#     # q = queue.LifoQueue()
#     # q = queue.PriorityQueue()
#     thread1 = Thread(target=func1,args=(q,))
#     thread2 = Thread(target=func2,args=(q,))
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()


#  守护进程
# 跟随 主进程代码结束而结束

#  守护线程
# 会等待所有子线程结束而结束 ，主进程结束之后 回收资源 而所有子进程结束之后


#  线程池/进城池

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from threading import current_thread


def func1(i):
    print(f"{i}--->{current_thread().ident}")

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as executor:
        for i in range(20):
            th = executor.submit(func1,i)
            print(th)
            th.map()
