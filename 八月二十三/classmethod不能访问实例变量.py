class Sudent:
    mingzi = '王大锤'
    stu_num = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def display(self):
        self.stu_num += 1
        print(f'学生的名字:{self.mingzi}')
        print(self.stu_num)


student1 = Sudent('liusang', 18)

student2 = Sudent('lisang', 18)

student3 = Sudent('langsang', 18)

student1.display()
student2.display()
student3.display()
