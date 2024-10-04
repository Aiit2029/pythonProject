class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__life_val = 100

    def get_life_val(self):
        print(f'生命值还有{self.__life_val}')

    def __breath(self):
        print(f'{self.name} is breathing')
    def get_attack(self):
        self.__life_val -= 20
        self.__breath()
        print('被攻击了哟，生命值减少了20')
        return self.__life_val



a = Person('alex',22)
a.get_life_val()
a.get_attack()
a.get_life_val()

a.__val = 666
print(a.__val)
