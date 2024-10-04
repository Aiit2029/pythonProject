from concurrent.futures import ThreadPoolExecutor


def func(a,b):
    return a*b

def print_func(ret):
    print(ret.result())

if __name__ == '__main__':
    th = ThreadPoolExecutor(max_workers=4)
    for i in range(20):
        ret = th.submit(func,i,b = i+1)
        ret.add_done_callback(print_func)
