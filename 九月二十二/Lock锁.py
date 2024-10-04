#  进程同步
    # 进程之间数据安全的问题
    # 进程之间是怎么共享数据的
    # 进城之间数据隔离的方法 ：  锁
    


import time
from multiprocessing import Process, Lock


def func(i,lock):
    lock.acquire()
    print(
        f'{i},god damn it'
    )

    lock.release()
    time.sleep(1)


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=func, args=(i,lock))
        p.start()