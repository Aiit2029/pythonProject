class Person(object):
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name}'

    def run(self):
        self.weight = self.weight - 0.5

    def eat(self):
        self.weight = self.weight + 1

xiaoming = Person('xiaoming',75)

xiaoming.run()
xiaoming.eat()
print(xiaoming.weight)
