from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from threading import current_thread, Thread


def func(*args, name,flag):
    print(current_thread().ident)
    print(args[0])
    print(name,flag)



th = ThreadPoolExecutor(4)

for i in range(10):
    th.submit(func,'1',name='aelx',flag = 1)