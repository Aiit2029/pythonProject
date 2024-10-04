# recursion(递归)锁  RLock
from threading import Lock, RLock, Thread


#多线程操作全局变量，或者静态变量 导致数据不安全
#一条线程永远不会出现数据不安全
# 为什么 递归锁可以做到互斥锁能够做到的事情，在某些方面仍然用互斥锁 而不是递归锁？
    # 互斥锁的效率高， 递归锁的效率相对低一些


# # 递归锁
# lock = RLock()
# #进1门
# lock.acquire()
# #进2门
# lock.acquire()
# #进3们
# lock.acquire()
# print(lock)
# #出3门
# lock.release()



# def func(i,lock):
#     lock.acquire()
#     print(f'{i}:start')
#     lock.acquire()
#     print(f'{i}:mid')
#     lock.release()
#     print(f'{i}:end')
#     lock.release()
#
# if __name__ == '__main__':
#     lock = RLock()
#
#     for  i in  range(5):
#         Thread(target=func, args=(i,lock)).start()
#


