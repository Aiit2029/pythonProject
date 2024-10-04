#  生产者消费者模型默写
import random
import time
from multiprocessing import Process, Queue


def consumor(q,name):
    while True:
        food = q.get()
        if food:
            print(f'{name}吃了{food}')
        else:
            break

def producer(q,name):
    for i in range(10):
        foodi = f'{name}的答辩{i}号'
        print(f'生成了{foodi}')
        time.sleep(random.random())
        q.put(foodi)




if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer,args=(q,'刘政'))
    p2 = Process(target=producer,args=(q,'燕志强'))
    c1 = Process(target=consumor,args=(q,'尹子润')).start()
    c2 = Process(target=consumor,args=(q,'李康康')).start()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    q.put(None)
    q.put(None)

