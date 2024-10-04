import queue    #  线程之间数据安全的容器  队列

# q = queue.Queue()  #  先进先出
q = queue.Queue(4)  #  设置队列的大小
#
# q = queue.LifoQueue()  #  后进先出
#
# q = queue.PriorityQueue()   #  优先级队列， 其中优先级 设置  是按照Asic码的大小来设置的   
q.get()
q.put(1)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print(q.get())
# q.put(5)
#
# try:
#     q.get_nowait()
# except queue.Empty:  #  queue.Empty  不是内置的错误类型，而是queue模块中的错误类型
#     print('>_<')