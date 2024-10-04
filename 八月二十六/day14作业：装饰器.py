# # def wrapper(f):
# #     def inner(*args, **kwargs):
# #         print(111)
# #         ret = f(*args, **kwargs)
# #         return ret
# #     return inner
# #
# # def func():
# #     print('func')
# #
# # print(333)
# # func()
# # print(444)
#
# def wrapper(f):
#     cout = 0
#     def inner(*args, **kwargs):
#         nonlocal cout
#         for i in range(5):
#             ret = f(*args, **kwargs)
#             cout += ret
#         return cout
#     return inner
# @wrapper
# def func():
#     return 7
#
#
# print(func())
# print(func())

import time

def wrapper(file):
    def inner(*args, **kwargs):
        with open('test.txt', 'a',encoding='utf-8)') as f:
            ret = file(*args, **kwargs)
            struct_time = time.localtime()
            time_info = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
            f.write(f'北京时间:{time_info}执行了函数{file.__name__}\n')
        return ret
    return inner


@wrapper
def func():
    print(func.__name__)
func()
