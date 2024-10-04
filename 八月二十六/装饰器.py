# #装饰器遵循开放封闭原则
# #装饰器：在不改变原函数代码以及调用方式的情况下，给他增加新的功能
# #开放：对代码的拓展是开放的
# #对源码的修改是封闭的
# #装饰器就是一个函数
# #装饰器本质上就是闭包

#标准的装饰器

def wrapper(filename):
    def inner(*args, **kwargs):
        '''添加额外的功能'''
        ret = filename(*args, **kwargs)
        return ret
    return inner




# import time_demo
# # print(time_demo.time_demo())
# ##格林威治时间
# ##
# class method:
#     def time_font(self):
#         time_demo.sleep(2)
#         print('测试进入博客园首页的时间')
#
#     def time_back(self):
#         time_demo.sleep(3)
#         print('测试进入博客园后台的时间')
#
# m = method()
# choose = input('请输入要测试的方法:')
# if hasattr(method,choose):
#     o = getattr(method,choose)
#     start_time = time_demo.time_demo()
#     o(m)
#     end_time = time_demo.time_demo()
#     print(end_time - start_time)
# else:
#     print('gg')
# import time_demo
#
#
# def timer(filename):
#     def inner():
#         start_time = time_demo.time_demo()
#         filename()
#         end_time = time_demo.time_demo()
#         print(end_time - start_time)
#     return inner
#
#
# def diary():
#     time_demo.sleep(0.6)
#     print('我睡了0.6秒')
#     return 666
#
#
# @timer
# def index():
#     time_demo.sleep(3)
#     r = diary()
#     print('欢迎登陆博客园首页')
#
#
#
# index()

