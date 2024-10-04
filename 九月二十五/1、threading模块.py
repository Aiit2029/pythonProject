import queue
import threading
import time
from threading import Thread

# def thread_func(i):
#
#     print(f'start{i}')
#     time.sleep(0.01)
#     print(f'end{i}')
# if __name__ == '__main__':
#     for i in range(10):
#         Thread(target=thread_func, args=(i,)).start()

class MyThread(Thread):
    def __init__(self,name):
        super(MyThread,self).__init__()
        self.name = name

    def fun1(self):
        print('func')

    def run(self):
        print('>_<')
        self.fun1()



if __name__ == '__main__':
    # q = queue.LifoQueue()#  后进先出
    # q = queue.PriorityQueue(20,'12312') # 可以设置优先级
    t1 = MyThread('alex')
    t1.start()

