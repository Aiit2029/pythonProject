# l = [{"name":"alex"},{"name":"y"}]
# print(list(map(lambda x: {"name": x["name"] + "_sb"}, l)))

class A:
    def func(self):
        print('in A')

class B:
    def func(self):
        print('in B')

class C(A,B):
    def func(self):
        print('in C')


if __name__ == '__main__':
    c1 = C()
    c1.func()
    super(A,c1).func()
