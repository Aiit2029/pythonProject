class method_decorator:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.__sex = sex

    def get_sex(self):
        print(f'get性别{self.__sex}')

if __name__ == '__main__':
    md = method_decorator('alex',18,'male')
    print(md.name)