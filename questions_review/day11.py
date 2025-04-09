# def func1():
# 	print('in func1')
#
# def func2():
# 	print('in func2')
#
# ret = func1
#
# ret()
#
# ret1 = func2
#
# ret1()
#
# ret2 = ret
#
# ret3 = ret2
#
# ret2()
#
# ret3()
# def func1():
#     print('in func1')
#
#
# def func2():
#     print('in func2')
#
#
# def func3(x, y):
#     x()
#
#     print('in func3')
#
#     y()
#
#
# print(111)
# func3(func2, func1)
# print(222)


# def func():
#     return '大烧饼'
#
#
# def bar():
#     return '吃煎饼'
#
#
# def base(a1, a2):
#     return a1() + a2()
#
#
# result = base(func, bar)
# print(result)
# list1 = [1,2,3,4,5]
# it = iter(list1)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break


# [s.upper() for s in strings if len(s) > 3 and if isinstance(strings,(str,list))]


# v = [i % 2 for i in range(10)]
# print(v)


# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         # print("res:",res)
# g = foo()
# print(next(g))
# # print(next(g))
# # print("*"*20)
# # print(next(g))

# for i in range(5):
#      print(i)
# print(i)


# x = {
#     'name': 'alex',
#     'alues': [{'timestamp': 1517991992.94,
#                 'values': 100, },
#                {'timestamp': 1517992000.94,
#                 'values': 200, },
#                {'timestamp': 1517992014.94,
#                 'values': 300, },
#                {'timestamp': 1517992744.94,
#                 'values': 350},
#                {'timestamp': 1517992800.94,
#                 'values': 280}
#                ], }
# list2 = [[x["alues"][i]["timestamp"],x["alues"][i]["values"]] for i in range(len(x["alues"]))]
# print(list2)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
stores = [(colors[i], sizes[j]) for i in range(len(colors)) for j in range(len(sizes))]
print(stores)