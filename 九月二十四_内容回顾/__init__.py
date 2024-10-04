__author__ = 'liuzheng'
# 进程的内容
    # 生产者消费者模型
        #爬取网页  bs4   requests
    # 数据共享
        #manager类
# 守护进城  ： 等待主进程代码结束之后就立即结束
    #p.daemon = True  设置为守护代码  ，在 p.start()之前


# Lock  互斥锁
# 会降低程序的运行效率，但能够保证程序数据的安全


# from multiprocessing import Lock
#
# def func1():
#     global n,lock
#     with lock:
#         n +=1
#         print(n)
#
# def func2():
#     global n,lock
#     with lock:
#         n += 10
#         print(n)
#
# if __name__ == '__main__':
#     lock = Lock()
#

# 队列  IPC (Internet Process  communacation)  进程之间通信

    # 基于socket|pickle|lock实现的
    # pipe管道 是基于socket和pickle实现的 由于不加锁的，管道数据不安全
    # 基于网络实现


# 线程的概念
# python中线程的特点你
# threading模块开启线程

# ftp作业需求分析
