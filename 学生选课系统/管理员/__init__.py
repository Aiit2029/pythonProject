import json
import pickle


# def Warpper(f):
#     def inner(self,*args, **kwargs):
#         if self.flag == 0:
#             return
#         ret = f(*args, **kwargs)
#
#         return ret
#
#     return inner

class Manager():
    courses_lst = []
    course_list = []
    stu_lst = []
    student_list = []
    student_course_dict = {}
    student_pwd_dict = {}
    count = 1

    def __init__(self,name):
        self.name = name
        self.flag = 1

    # @Warpper
    @classmethod
    def creat_course(*args,**kwargs):
        print('>>>:请输入课程名称，课程价格，课程周期，老师名称')
        course_name, price, duration, teacher = input(">>>:").split(' ' or ',')
        course = Course(course_name,price,duration,teacher)
        Manager.courses_lst.append(course)

        with open('course.txt','ab') as f:
            pickle.dump(f'{course}:{course_name}:{price}:{duration}:{teacher}\n',f)


    # @Warpper
    @classmethod
    def creat_student(*args,**kwargs):
        print('请输入学生姓名')
        student_name = input('>>>:').strip()
        if student_name is not None:
            student = Students(student_name)
            Manager.stu_lst.append(student)
            Manager.count += 1
        username = input('>>>enter your username:').strip()
        password = input('>>>enter your password:').strip()
        Manager.student_pwd_dict[student] = {username:password}
        with open('student_user_pwd.txt','ab') as f:
            pickle.dump(f'{student}:{student_name}:{username}:{password}:{student.flag}',f)


        #读内容 使用
        # with open('student_user_pwd.txt','a+',encoding='utf-8') as f:
        #     for i in Manager.student_pwd_dict.values():
        #         for user, pwds in i.items():
        #             f.write(f'{user}:{pwds}\n')


    # @Warpper
    @property
    def show_all_students(cls):
        print(f'{Manager.student_list}')

    @property
    def show_all_students_choiced_courses(cls):
        print(Manager.student_course_dict)



class Students():

    def __init__(self, name):
        self.name = name
        self.course_list = Manager.course_list
        self.choiced_course = []
        self.flag = 0
        Manager.student_list.append(self.name)
        Manager.student_course_dict[self.name] = 1

    def show_able_choice_course(self):
        for course, index in enumerate(self.course_list, 1):
            print(index, course)

    def choice_course(self):
        choice_num = int(input('>>>'))
        self.choiced_course.append(self.course_list[choice_num - 1])
        Manager.student_course_dict[self.name] = self.choiced_course
        print(f'选择了{self.course_list[choice_num - 1]}')

    def show_choiced_course(self):
        print(f'学生{self.name}选择了{self.choiced_course}课程')

    @classmethod
    def exit_program(cls):
        exit('退出程序')

class Course():
    def __init__(self,course_name,price,duration,teacher):
        self.course_name = course_name
        self.price = price
        self.duration = duration
        self.teacher = teacher
        Manager.course_list.append(self.course_name)



def login():
    username = input('>>>enter your username:')
    password = input('>>>enter your password:')
    with open(r'E:\PythonProject\pythonProject\学生选课系统\管理员\student_user_pwd.txt', 'rb') as f1 ,open(r'E:\PythonProject\pythonProject\学生选课系统\管理员\course.txt', 'rb') as f2:
        try:
            while True:
                load_file1 = pickle.load(f1)
                student, student_name, user, pwd, flag = load_file1.strip().split(':')
                if flag == '0':
                    Manager.student_pwd_dict[student] = {username: password}
                    Manager.student_list.append(student_name)
                if user == username and pwd == password:
                    try:
                        while True:
                            load_file2 = pickle.load(f2)
                            course, course_name, price, duration, teacher = load_file2.strip().split(':')
                            if flag == '0':
                                Manager.course_list.append(course_name)
                                Manager.courses_lst.append(course)
                    except EOFError as e:
                        pass
        except EOFError:
            print('1')


    #     load_file2 = pickle.load(f2)
    #     for line in load_file1:
    #         student,student_name,user, pwd, flag = line.strip().split(':')
    #         if flag =='0':
    #             Manager.student_pwd_dict[student] = {username: password}
    #             Manager.student_list.append(student_name)
    #
    #         if user == username and pwd == password:
    #             for line in f2.readlines():
    #                 course, course_name, price, duration, teacher = line.strip().split(':')
#                 if flag == '0':
#                     Manager.course_list.append(course_name)
#                     Manager.courses_lst.append(course)
    #             if flag =='0':
    #                 for i in Manager.student_pwd_dict.keys():
    #                     if i == student:
    #                         print(type(i))
    #                         return i
    #                 return main(i)
    #             elif flag =='1':
    #                 return main2()
    #             else:
    #                 print('something went wrong')
    #     print('请检查您的账号和密码')
    # return login()


def main(i):

    while True:
        print('''
        1、查看所有课程
        2、选择课程
        3、查看所选课程
        4、退出程序
        ''')
        choice = input('>>>请选择:')
        if choice == '1':
            i.show_able_choice_course()
        elif choice == '2':
            i.choice_course()
        elif choice == 3:
            i.show_choiced_course()
        elif choice == 4:
            Students.exit_program()


def main2():
    while True:
        print('''
        1、创建课程
        2、创建学生和学生账号
        3、查看所有课程
        4、查看所有学生
        5、查看所有学生的选课情况
        6、退出程序
        ''')
        choice = input('>>>:')
        if choice == '1':
            Manager.creat_course()
        elif choice == '2':
            Manager.creat_student()
        elif choice == '3':
            print(Manager.course_list)
        elif choice == '4':
            print(Manager.student_list)
        elif choice == '5':
            print(Manager.show_all_students_choiced_courses())
        elif choice == '6':
            exit('退出程序')





# manager.creat_course('python','21800','两个月','刘老师')
# manager.creat_course('linux','18888','三个月','张老师')
# manager.creat_course('网络编程','20000','四个月','问老师')
# manager.creat_course('数据库','28897','五个月','赵老师')
# manager.creat_course('数据结构与算法','31888','六个月','燕老师')
# manager.creat_student('alex')
# manager.creat_student('tom')
# print(Manager.student_pwd_dict)
# print(Manager.student_list)
# for user,pwd in Manager.student_pwd_dict.items():
if __name__ == '__main__':
    # login
    # ()
    Manager.creat_student()
    Manager.creat_student()
    login()