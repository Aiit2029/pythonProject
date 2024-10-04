from multiprocessing import Process, Manager, Lock


def change_dic(dic,lock):
    with lock:
        dic['count'] -= 1

if __name__ == '__main__':
    lock = Lock()
    m = Manager()
    dic =m.dict({'count':100})

    pl = []
    for i in range(100):
        p = Process(target=change_dic,args=(dic,lock))
        pl.append(p)
        p.start()

    for p in pl:p.join()
    print(dic['count'])