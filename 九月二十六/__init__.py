﻿import time
from threading import Thread,Lock
noodle_lock = Lock()
fork_lock = Lock()
def eat1(name):
    noodle_lock.acquire()
    print('%s 抢到了面条'%name)
    fork_lock.acquire()
    print('%s 抢到了叉子'%name)
    print('%s 吃面'%name)
    fork_lock.release()
    noodle_lock.release()

def eat2(name):
    noodle_lock.acquire()
    print('%s 抢了面条' % name)
    fork_lock.acquire()
    print('%s 抢了叉子' % name)
    time.sleep(1)

    print('%s 吃面' % name)
    noodle_lock.release()
    fork_lock.release()

for name in ['哪吒','egon','yuan']:
    t1 = Thread(target=eat1,args=(name,))
    t2 = Thread(target=eat2,args=(name,))
    t1.start()
    t2.start()

