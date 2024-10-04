class Dog:
    def __init__(self,name,age,breed,master):
        self.name = name
        self.age = age
        self.breed = breed
        self.master = master

    def run(self):
        print(f'{self.master.name}的狗狗{self.name} is runing')


class Person:
    def __init__(self,name):
        self.name = name

    def breed_dog(self):
        print(f'我想遛狗')

def main():
    p1 = Person('刘桑')
    dog1 = Dog('李康康',22,'二货',p1)
    p1.breed_dog()
    dog1.run()

if __name__ == '__main__':
    main()
