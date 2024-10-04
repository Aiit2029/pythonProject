# 回调函数  add_done_callback   异步阻塞   立即处理结果


import sys
import time,random
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
def func(a):
    print(current_thread().ident,"start",a)
    time.sleep(random.randint(1,4))
    print(current_thread().ident,"end",a)
    return  a[0]*a[1]
def print_back(ret):
    print(ret.result())

if __name__ == '__main__':
    tp = ThreadPoolExecutor(max_workers=4)
    for i in range(20):                     # 异步阻塞
        ret = tp.submit(func,(i,i+1))
        ret.add_done_callback(print_back)