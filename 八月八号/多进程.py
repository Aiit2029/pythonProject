from multiprocessing import Process
from time import sleep, time
from os import getpid
from random import random, randint


def download_task(filename):
    print(f'启动下载进程，进程号为{getpid()}')
    print(f'开始下载{filename}')
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print(f'{filename}下载成功，用时{time_to_download}秒')

def main():
    start_time = time()
    p1 = Process(target=download_task, args=('学python用pycharm.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('学java从入门到入土',))
    p2.start()
    p1.join()
    p2.join()
    end_time = time()
    print(f'总共耗时{end_time-start_time}秒')

if __name__ == '__main__':
    main()