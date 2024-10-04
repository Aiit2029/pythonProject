#  什么是池
    # 在程序开始时，还没有提交任务的时候先创建几个线程或者进程放在 一个容器里面
    # 这个容器就叫做 池
# 为什么要用池， 有什么好处
    # 如果先开好进程或者线程，那么有任务之后就可以直接使用这个池中的数据
    # 并且开好的线程或者进程会一存在在池中，可以被多个任务反复使用
        #好处     # 这样加大地减少了(开启|关闭|调度)进程的时间开销
    # 池中的线程或者进程个数控制了操作系统需要调度的任务个数，控制池中的单位
    # 有利于提高操作系统的效率，减轻操作系统的负担


from concurrent.futures import ProcessPoolExecutor

# 定义一个计算任务
def compute(n):
    result = n * n
    return result
if __name__ == '__main__':

# 创建进程池
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures_result = []
        j_lst = [3, 4, 5]

        th = [executor.submit(compute,j) for j in range(3,6)]
        for  i in range(len(th)):
            print(th[i].result())
        # print(futures_result)
        # for r in futures_result:
        #     print(r)

    # 提交任务给进程池
    # future1 = executor.submit(compute, 2)
    # future2 = executor.submit(compute, 3)
    # future3 = executor.submit(compute, 4)
    #
    # # 获取任务执行结果
    # print(future1.result())  # 输出：4
    # print(future2.result())  # 输出：9
    # print(future3.result())  # 输出：16




