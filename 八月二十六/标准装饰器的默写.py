# 标准装饰器

def wrapper(f):
    def inner(*args, **kwargs):
        ret = f(*args, **kwargs)
        return ret
    return inner

@wrapper
def func():
    pass

func()