from gevent import monkey
monkey.patch_all()
import time
import gevent

def func():
    print('start gevent')
    time.sleep(1)
    print('end gevent')


g1 = gevent.spawn(func)
g2 = gevent.spawn(func)
g3 = gevent.spawn(func)
g4 = gevent.spawn(func)

gevent.joinall([g1, g2, g3,g4])