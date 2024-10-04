class Student():
    def __init__(self, name, sutdent_id):
        self.name = name
        self.sutdent_id = sutdent_id
        self.grades = {'语文': 0, '数学': 0, '英语': 0}

    def set_grades(self, course, grade):
        if course in self.grades.keys():
            self.grades[course] = grade
        else:
            print('没有这个科目')
            return None

    def print_grades(self):
        print(f'学生{self.name}(学号为{self.sutdent_id})的成绩为:')
        for course in self.grades.keys():
            print(f'{course}:{self.grades[course]}')


liu = Student('小刘', 100)
liu.set_grades('语文', 98)
liu.set_grades('数学',89)
liu.print_grades()

