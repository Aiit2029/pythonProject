# def func(*args):
#     sum = 0
#     for i in args:
#         sum = i + sum
#     print(sum)
#
# func(1,2,3,4,5,6,7,8,9,10)

# def func(**kwargs):
#     print(kwargs)
#
# func(name = '刘桑',age = 22)

# def func(a,b,*args,**kwargs):
#     print(a,b,args,kwargs)
#
# func(1,2,3,4,5,sex = 'male',age = 18,)

# def func(a,b,sex = '男',*args):
#     print(a,b)
#     print(sex)
#     print(args)
#
# func(1,2,3,4,5,6,7,8,9,10)


#
# def func():
#     a = 1
#     def foo():
#         b = 2
#         print(b)  # 2
#         print(a)  # 1
#         def f1():
#             print(b) # 2
#         return f1()
#     return foo()
#
#
# print(func())


# def func(*args, **kwargs):
#     print(args, kwargs)
#
#
# # func([11, 22], 33, k1='v1', k2='v2')
# func(*{'吴佩姬','金鑫','女友'})

# def func(a,list = []):
#     list.append(a)
#     return list
# ret1 = (func(10,))
# ret2 = (func(20,[]))
# ret3 = (func(100,))
#
# print(ret1)
# print(ret2)
# print(ret3)


