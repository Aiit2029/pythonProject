# class Student:
#
#     def __init__(self, id, name, age, high):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.high = high
#
#     def avg(self):
#         sum_age = 0
#         sum_high = 0
#         for i in student_list:
#             sum_age = sum_age +  i[2]
#             sum_high = sum_high +  i[3]
#         avg_age = sum_age / len(student_list)
#         avg_high = sum_high / len(student_list)
#         print(f'学生的平均年龄为：{avg_age},学生的平均身高是：{avg_high:.2f}')
#
#     def addStudent(self):
#         while True:
#             id = input(f'请输入学生的id:')
#             name = input(f"请输入学生的姓名: ")
#             age = int(input(f"请输入学生的年龄: "))
#             high = float(input(f"请输入学生的身高:"))
#             student = [id, name, age, high]
#             student_list.append(student)
#             iend = input("是否结束：\n 1、计算平均年龄和平均身高（请按1)\n2、结束(请按2)")
#             if iend == 1:
#                 student2.avg(student2)
#                 break
#             elif iend == 2:
#                 print("结束")
#                 return None
#             elif iend == 3:
#                 print("继续")
#             break
#
#
#
#
#
# student_list = []
# student2 = Student('1','liu',18,178)
# student2.addStudent()
#
#
#
#
class Student:

    def __init__(self, id, name, age, high):
        self.id = id
        self.name = name
        self.age = age
        self.high = high

    def avg(self):
        sum_age = 0
        sum_high = 0
        for i in student_list:
            sum_age = sum_age +  i[2]
            sum_high = sum_high +  i[3]
        avg_age = sum_age / len(student_list)
        avg_high = sum_high / len(student_list)
        print(f'学生的平均年龄为：{avg_age},学生的平均身高是：{avg_high:.2f}')

    def addStudent(self):
        while True:
            id = input(f'请输入学生的id:')
            name = input(f"请输入学生的姓名: ")
            age = int(input(f"请输入学生的年龄: "))
            high = float(input(f"请输入学生的身高:"))
            self.id = id
            self.name = name
            self.age = age
            self.high = high
            student = [id, name, age, high]
            student_list.append(student)
            iend = input("是否结束：\n 1、计算平均年龄和平均身高（请按1)\n2、结束(请按2)\n3、继续(请按3)")
            if int(iend) == 1:  # 将输入转换为整数进行比较
                self.avg()  # 正确调用 avg 方法，无需传入参数
                break
            elif int(iend) == 2:  # 将输入转换为整数进行比较
                print("结束")
                return None
            elif int(iend) == 3:  # 将输入转换为整数进行比较
                print("继续")
                continue
            break

student_list = []
student2 = Student(id,self.name,age,high)
student2.addStudent()
