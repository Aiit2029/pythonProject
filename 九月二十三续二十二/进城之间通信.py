#  进程之间通信 (IPC) Inter Process communication
    # 基于文件 : 同一台机器身上的多个进程之间的通信
        # 基于socket的文件级别的通信来完成数据传递的
        # Queue(队列)
        # 先进先出
    # 基于网络： 同一台机器或者多台机器上的多进程间通信
        # 第三方通信(消息中间件)
            # redis
            # rabbitmq
            # kafka
            # memcache

from multiprocessing import Queue, Process


# 帮助你完成进程之间的通信

def father(q):
    while True:
        item = q.get().upper()
        print(item)
def son(q):
    q.put('info')





if __name__ == '__main__':
    q = Queue()
    Process(target=son, args=(q,)).start()
    Process(target=father, args=(q,)).start()
