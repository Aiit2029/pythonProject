#  守护进程  daemon
#   主进程会等待所有子进程结束,是为了回收子进程的资源
#   守护进程会等待(主进程的【代码】)结束之后在结束，而不是等待整个主进程结束
#   主进程的代码什么时候结束，守护进程就会在什么时候结束，与其他子进程无关



import time
from multiprocessing import Process


def func1():
    while True:
        print('-->in func1',flush= True)
        time.sleep(1)

def func2():
    for i in range(10):
        print('in func2')
        time.sleep(1)

if  __name__ == '__main__':
    p1 = Process(target=func1)
    p1.daemon = True
    p1.start()

    p2 = Process(target=func2)
    p2.start()
    time.sleep(3)
    print('结束')

