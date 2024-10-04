class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('动物都会吃东西')


class Person(Animal):
    def __init__(self, name, age, sex, hobbies):
        super().__init__(name, age, sex)
        self.hobbies = hobbies

    def eat(self):
        super(Person, self).eat()
        print('人类会吃老八迷之小憨包')


p1 = Person('liusang', 22, 'male','female')
p1.eat()
