import threading
import time


def job1():
    global n,lock
    with lock:
        for i in range(10):
            n+=1
            print('job1',n)
            time.sleep(1)


def job2():
    global n,lock
    with lock:
        for i in range(10):
            n+=10
            print('job2',n)
            time.sleep(1)
if __name__ == '__main__':

    lock = threading.Lock()
    n = 0
    target_lst = [job1,job2]
    for tar in target_lst:
        t=threading.Thread(target=tar)
        t.start()
