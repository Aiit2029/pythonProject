# 开启进程的另一种方法
    # 通过面向对象的方法，通过继承Process和重写run方法打来启动子进程
    # 通过重写init方法和调用父类的init方法给子进程传参数
# Process的一些其他方法和属性
    #name ,(pid == ident) daemon(守护进程，在start之前设置)
    # terminate()强制杀死一个进程， is_alive()  进程是否存活
#守护进程
    # 在start一个进程之前 设置 进程.daemon = True
    # 守护进程在等待主进程的代码结束之后就立即结束
        # 为什么守护进程只守护主进程的代码？
            # 因为 守护进程也是一个子进程，只有守护进程只会在主进程结束之前结束
            # 主进程需要最后结束，为了给子进程(守护进程)回收资源
        #守护进程会等待其他子进程结束吗？
            # 不会


import os
import time
from multiprocessing import Process
#开启进程的另一种方法
# class MyProcess(Process):
#     def run(self):
#         print(os.getppid(),os.getpid())
#
# if  __name__ == '__main__':
#     p = MyProcess()
#     p.start()


# 对进程传参的方法
# class MyProcess(Process):
#     def __init__(self,a,b,c):
#         super().__init__()
#         self.a = a
#         self.b = b
#         self.c = c
#     def run(self):
#         print(os.getppid(),os.getpid())
#         print(self.a,self.b,self.c)
#
# if __name__ == '__main__':
#     p = MyProcess(1,2,3)
#     p.start()
#     print(p.is_alive())   # 子进程是否存活
#     p.terminate()   # 强制杀一个子进程
#     print(p.is_alive())    # 由于操作系统需要反应,导致 在杀死的一瞬间 查看是否存活,还是
#     time.sleep(0.5)
#     print(p.is_alive())


