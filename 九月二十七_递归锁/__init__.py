from multiprocessing import Process,Queue


def func(q):
    pass

if __name__ == '__main__':
    q = Queue()
    p = Process(target=func, args=(q,))
    p.start()
    p.join()