class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def pay_roll(self):
        #发工资
        pass

    def count_staff_num(self):
        #统计员工人数
        pass

    def count_stu_num(self):
        #统计学⚪人数
        pass


    def new_staff_enrollment(self):
        #新员工注册
        pass

class BranchSchool(School):
    def __init__(self,name,address,headquater):
        super().__init__(name,address)
        self.__headquater=headquater

class Class():
    def __init__(self,class_num,course_obj,school_obj):
        self.class_num=class_num
        self.course_obj=course_obj
        self.school_obj= school_obj

    def create_teaching_record(self):
        #创建上课记录
        pass

    def drop_out(self):
        #退学
        pass

class Course():
    def __init__(self,name,price,outline):
        self.name= name
        self.price= price
        self.__outline= outline


class  Staff():
    def __init__(self,name,age,position,salary,dept,school_obj):
        self.name=name
        self.age= age
        self.position= position
        self.salary= salary
        self.dept= dept
        self.school_obj= school_obj

    def count_salary(self):
        #统计各校区账户余额
        pass

class Teacher(Staff):
    def __init__(self,name,age,position,salary,dept,school_obj):
        super().__init__(name,age,position,salary,dept,school_obj)

    def teaching(self,class_obj):
        pass


class Student():
    def __init__(self,name,age,degree,class_obj,balance):
        self.name = name
        self.age = age
        self.degree = degree
        self.class_obj = class_obj
        self.balance = balance

    def pay_tuition(self):
        #交学费
        pass
