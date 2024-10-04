# #对象是由类创建的
# #类是由谁创建的
# #  类 默认是由 type 创建的
#
# #  传统方式
#
# class Foo(object):
#     v1 = 123
#
#     def func(self):
#         return 666
# print(Foo)
#
# Fa = type('Foo',(object,),{'v1':123,'func':lambda self:666})
# obj = Fa()
# print(obj.v1)
#
# result = obj.func()
# print(result)
#

# 一般先执行 new方法，new方法调用init
class Student(object):
    def __init__(self,name):
        self.name = name
        print('hahhaha')
    def __new__(cls, *args, **kwargs):
        #负责执行init
        print(cls,*args, **kwargs)
        return object.__new__(cls)

s = Student('liu')
s.name

#  23种设计模式，gof
# 单例模式  ，避免资源浪费，只会实例化一个程序


