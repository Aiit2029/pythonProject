#  线程池中的  map
# import sys
# import time,random
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread
#
#
# def func(a):
#
#     print(current_thread().ident,"start",a)
#     time.sleep(random.randint(1,4))
#     print(current_thread().ident,"end",a)
#     return  a[0]*a[1]
#
# if __name__ == '__main__':
#     tp = ThreadPoolExecutor(max_workers=4)
#     # future_l = {}
#     # for i in range(20):
#     #     ret = tp.submit(func,i,b = i+1)
#     #     future_l[i] = ret
#     # for key in future_l:
#     #
#     #     print(key,future_l[key].result())
#     ret = tp.map(func,((i,i+1) for i in range(20)))
#     for key in ret:
#         print(key)


