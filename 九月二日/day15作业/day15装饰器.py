from time import sleep


def warrper(f):

    def inner(*args,**kwargs):

        print('这是一个装饰器')
        ret = f(*args,**kwargs)
        print('这还是一个装饰器')
        sleep(10)

        return ret
    return inner


@warrper
def func():
    print('func')

func()

