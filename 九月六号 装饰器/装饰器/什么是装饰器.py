#  什么是装饰器
    # 在不改变原有代码的调用方式下 ，对原有函数进行增加功能等


# 为什么要有装饰器

# 为什么不能改变原函数的调用方式：
    # 因为要符合开放封闭原则
    # 提前写好一个功能，让别人使用的时候能够直接使用就能完成相应的功能



# 带参数的装饰器
# 有100个函数 分别添加一个计算函数执行时间的装饰器
# 有的时候需要计算时间，有时不需要
# 希望通过修改一个变量 控制这一百个函数的装饰器 是否执行
import time
def xxx(flag1):
    def func(f):
        def inner(*args, **kwargs):
            if flag1 == True:
                ret = f(*args, **kwargs)
                time_remind()
            else:
                ret = f(*args, **kwargs)
            return ret
        return inner
    return func

@xxx(flag1=True)
def func1():
    print('func1')

@xxx(flag1=True)
def func2():
    print('func2')

@xxx(flag1=False)
def func3():
    print('func3')

def time_remind():
    x = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f'现在是{x},真是一个b（￣▽￣）d 日子啊')

func1()

func2()

func3()


