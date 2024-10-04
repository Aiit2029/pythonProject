class Person(object):

    # 限定只许绑定以下三个属性
    # __solts__ =('_name','_age','_gender')
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('正在愉快的打无畏契约')

    def watch_movie(self):
        if int(self.age) < 18:
            print('老老实实的看你的少儿频道')
        else:
            print('嗨嗨嗨，老八来了')

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self):
        print('哈哈哈，我真爱学习')

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self._subject = subject
    @property
    def subject(self):
        return self._subject
    @subject.setter
    def subject(self, subject):
        self._subject = subject

    def teach(self):
        print(f'我是一名光荣的{self.subject}老师')
def main():
    student1 = Student('小张','14','初二')
    teacher1 = Teacher('老李','58','化学')
    (student1.play())
    (student1.watch_movie())
    (student1.study())
    teacher1.play()
    (teacher1.teach())
    (teacher1.watch_movie())



if __name__ == '__main__':
    main()
