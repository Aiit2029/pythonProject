import sys


class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print("walk alone")

def talk(self):
    print("talk with me")

s1 = Student('liuasng',18)
mod = sys.modules[__name__]
if hasattr(mod,'talk'):
    o = getattr(mod,'talk')
    o(s1)
else:
    print('当当当当')