# 已完成到统计员工人数和学生人数

class School:
    def __init__(self, name, address, balance):
        self.name = name
        self.address = address
        self.balance = balance
        self.staff_list = []
        self.student_list = []
        self.class_list = []
        self.all_school_list = [self.name]
        self.other_staff_list = []
        self.all_class_student_num = []
        self.all_class_list = []
        self.all_staff_list = []
        self.dict_name_salary = {}


    def pay_roll(self):
        # 发工资
        sum = 0
        for staff,money in self.dict_name_salary.items():
            money = int(money)
            print(f'这个月发给{staff}:{money}元')
            sum += money
            self.balance -= money
        print(f'{self.name}这个月总共发了{sum}元,学校还剩{self.balance}元')

    def new_staff_enrollment(self):
        # 新员工注册
        pass

    def count_school_money(self):
        print(self.balance)
        return self.balance

    def count_current_school_staff_num(self):
        # 统计员工人数
        return len(self.staff_list)

    # def  count_all_school_staff_num(self):

    def show_school_class(self):
        # 统计学校有哪些班级
        for school_class in self.class_list:
            print(school_class.course_obj.name)

    # 统计学员人数
    def count_all_sutdent_num(self):
        sum = 0
        for i in self.all_class_student_num:
            sum += i
        print(sum)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


#  未完成：统计院校余额   将所有分校和本校的余额加在一起   学生转校和退学   转校需要修改学生的  class_obj的school_obj  退学，需要删除学生，同时删除班级学生列表中的学生和学校列表中的学生


class BranchSchool(School):
    def __init__(self, name, address, balance, headquater):
        super().__init__(name, address, balance)
        self.headquater = headquater
        self.staff_list = []
        self.class_list = []
        self.dict_name_salary = {}
        self.headquater.all_school_list.append(self)

    # def count_staff_num(self):
    #     return len(self.staff_list)

    # def show_school_class(self):
    #     # 统计学校有哪些班级
    #     for school_class in self.class_list:
    #         print(school_class,end=' ')


class Course():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # self.__outline= outline


class Staff():
    def __init__(self, name, age, position, salary, dept, school_obj):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.dept = dept
        self.school_obj = school_obj
        self.school_obj.staff_list.append(self.name)
        self.school_obj.dict_name_salary[self.name] = salary
        if hasattr(school_obj, 'headquarter'):
            self.school_obj.headquater.other_staff_list.append(self)
        else:
            pass

    def count_salary(self):
        # 统计各校区账户余额
        pass


class Teacher(Staff):
    def __init__(self, name, age, position, salary, dept, school_obj):
        super().__init__(name, age, position, salary, dept, school_obj)
        self.school_obj.dict_name_salary[self.name] = salary
        if hasattr(school_obj, 'headquater'):
            self.school_obj.headquater.other_staff_list.append(self)
        else:
            pass

    def teaching(self, class_obj):
        print(f'老师我啊，名叫{self.name}，今年{self.age}岁啦，教的这门课程是{class_obj.course_obj.name}')


class Class():
    def __init__(self, name, course_obj, school_obj):
        self.name = name
        self.course_obj = course_obj  # course_obj传入的是course类的实例
        self.school_obj = school_obj  # school_obj传入的是该校区的实例的
        self.class_student_list = []
        self.school_obj.class_list.append(self)

    def create_teaching_record(self, teacher):
        # 创建上课记录,上课需要老师，创建一个老师类，实例化一个老师，并传入，老师需要和班级关联，代表这个老师讲这个班级的课程
        print('记录下来啦！Sense上课的英姿')
        teacher.teaching(self)

    def count_class_student_num(self):
        print(f'{self.name}有{len(self.class_student_list)}个学生')
        self.school_obj.all_class_student_num.append(len(self.class_student_list))

    def show_class_student_name(self):
        for sutdent in self.class_student_list:
            print(sutdent, end=' ')

    def drop_out(self):
        # 退学，退学需要和班级中的学生关联，传入一个学生，退学一个学生
        pass


class Student():
    def __init__(self, name, age, degree, class_obj, balance):
        self.name = name
        self.age = age
        self.degree = degree
        self.class_obj = class_obj
        # class_obj 和 Class类的创建的对象有关，class创建的对象和course的name有关
        # 想要判断学生余额和班级课程的费用是否足够，先从course.price 关联到 Class.course_obj.price 然后判断 balance >= Class.course_obj.price
        self.balance = balance

    def pay_tuition(self):
        # 交学费
        self.balance = self.balance - self.class_obj.course_obj.price
        return self.balance

    def sign_up(self, class_obj):
        if self.balance >= class_obj.course_obj.price:
            print('余额足够可以报这个课程')
            self.pay_tuition()
            class_obj.class_student_list.append(self.name)
        else:
            print('余额不足，想想自己有没有足够在努力')


#  学生有 余额，余额足够交所报 班级 的 课程 的费用，
school1 = School('安徽信息工程学院', '永和路一号', 100000000)
school1001 = BranchSchool('安徽信息工程学院文津校区', '芜湖市内', 50000000, school1)
course1 = Course('python', 19888)
course2 = Course('Linux', 18000)
c1 = Class('高二三班', course1, school1)
c2 = Class('九年级十三班', course2, school1)
student1 = Student('刘政', 22, '本科', c1, 20000)
student2 = Student('李康康', 21, '本科', c1, 20000)
student3 = Student('燕志强', 21, '本科', c2, 20000)
student1.sign_up(c1)
student2.sign_up(c1)
student3.sign_up(c2)
teacher1 = Teacher('郝老师', 54, '副校长', '8000', '教育部门', school1)
teacher2 = Teacher('尹老师', 54, '副校长', '8000', '教育部门', school1)
teacher3 = Teacher('章老师', 54, '副校长', '8000', '教育部门', school1001)
c1.create_teaching_record(teacher1)
c2.create_teaching_record(teacher2)
c1.count_class_student_num()
c2.count_class_student_num()
print(c1.class_student_list)
print(c2.class_student_list)
print(school1.all_school_list)
school1.show_school_class()
c1.show_class_student_name()
school1.count_all_sutdent_num()
print(school1.all_staff_list)
print(school1.staff_list)
school1.count_school_money()
school1001.count_school_money()

print(school1.dict_name_salary)
print(school1001.dict_name_salary)
school1.pay_roll()
school1001.pay_roll()