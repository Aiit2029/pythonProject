# 生产者消费者模型

    # 爬虫的时候会用到
    # 分布式操作中celery 会用到，celery的本质是由两个生产者消费者模型组成的
    # 生产者消费者模型的本质是： 让生产数据和消费数据的效率达到平衡并且最大化

from multiprocessing import Queue, Process


#  consumer 消费者 ： 通常取到数据之后还需要进行某些操作
def consumer(q):
    pass

# producer 生产者 ： 通常在放数据之前需要通过某写代码来得到数据
def producer(q):
    pass


if __name__ == '__main__':
    q = Queue()
    c1 = Process(target=consumer,args=(q,)).start()
    p1 = Process(target=producer,args=(q,)).start()




