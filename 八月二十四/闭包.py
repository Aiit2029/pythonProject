#  封闭的，保证数据的安全，只允许特定的人去用
#闭包 只会产生在嵌套函数中
def make_averager():
    l1 = []
    # 自由变量  一旦函数中存在嵌套函数使用了l1
    # 内层函数对外层函数非全局变量的引用就会形成闭包
    # 被引用的全局变量也被称为自由变量
    # 这个自由变量一旦与内层函数产生绑定联系，这个自由变量在内存中就不会再消失
    def averager(new_value):
        l1.append(new_value)
        total = sum(l1)
        print(l1)
        return total/len(l1)
    return averager
#
avg = make_averager()
print(avg(100000))
print(avg(110000))
# # 如何判断一个嵌套函数是不是闭包
#
# a = 2
# b = 3
# def wrapper(a,b):
#     def inner():
#         print(a)
#         print(b)
#     return inner
#
# ret = wrapper(a,b)
# ret()


# 闭包只存在于嵌套函数中
# 内层函数对外层函数中非全局变量的引用就会形成闭包
#被引用的非全局变量被叫做自由变量
#闭包的作用是 保证数据的安全

# a = 2
# def wrapper(a,b):
#     def inner():
#         print(a)
#         print(b)
#     return inner
# a = 2
# b = 3
# ret = wrapper(a,b)
# print(ret.__code__.co_freevars)