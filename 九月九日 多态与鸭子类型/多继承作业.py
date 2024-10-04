# # #
# # #
# # # class Base1():
# # #     def f1(self):
# # #         print('base1.f1')
# # #
# # #     def f2(self):
# # #         print('base1.f2')
# # #
# # #     def f3(self):
# # #         print('base1.f3')
# # #         self.f1()
# # #
# # # class Base2:
# # #     def f1(self):
# # #         print('base2.f1')
# # #
# # # class Foo(Base2, Base1):
# # #     def f0(self):
# # #         print('foo.f0')
# # #         self.f3()
# # #
# # # obj = Foo()
# # # obj.f0()
# #
# # class Foo():
# #     n1 = '123'
# #     n2 = '321'
# #     def __init__(self):
# #         self.n1 = 'alex'
# #
# # obj = Foo()
# # print(obj.n1)
# # print(obj.n2)
# #
#
# class A(object):
#     def func(self):
#         print('A')
#
# class B(A):
#     def func(self):
#         print('B')
#         super().func()
#
# class C(B):
#     def func(self):
#         print('C')
#         super().func()
#
# C().func()
#
# # print('C')
# # super().func() = print('B')
# # super().func() = print('A')


# class User():
#     def __init__(self,name):
#         self.__name = name
#
#     def getName(self):
#         return self.__name
#
#     def setName(self,name):
#         self.__name = name
#
# class Student(User):
#     def __init__(self):
#         super().__init__(name= 'animal')




#
# u = User('alex')
# print(u.getName())
#
# print(dir(Student))
# print(u.__dict__)
# stu = Student()

# print(stu._User__name)



class father():
    def __init__(self):
        self.__func()

    def __func(self):
        print('这是父类啊')


class son(father):

    def __func(self):
        print('这是子类啊')







