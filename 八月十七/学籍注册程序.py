def register(**kwargs):
    dict_student = {}
    list_student = []
    list_old_student = []
    list_sum_student = []
    with open('data_student_info.txt', 'a+', encoding='utf-8') as f1:
        f1.seek(0)
        data = f1.read()
        print(data)
        # line = line.strip().split(',')
        # list_old_student.append(line)
        # list_student.append([name, age, phonenumber, id, resourse])
        # list_sum_student = list_old_student + list_student
        # f1.write(list_sum_student)

        # for i in range(len(list_sum_student)):
        #     dict_student[list_sum_student[i][3]] = list_sum_student[i]
        # # judge(phonenumber, id)
        # for i in dict_student.values():
        #     f1.write(str(i)+'\n')


# def judge():
#     list_judge_phone = []
#     list_judge_id = []
#     with open('data_student_info.txt', 'r', encoding='utf-8') as f2:
#         if f2 != None:
#             while f2.readline() != '':
#                 print(f2.readline())
#             # list_judge_phone.append(line[2])
#             # list_judge_id.append(line[3])
#             # print(list_judge_phone)
#             # print(list_judge_id)
#             # if phonenumber in list_judge_phone or id in list_judge_id:
#             #     exit('您已经注册过帐号了')
#             # else:
#             #     print('经检验，可以注册')

register()
# judge()

# def post_info():


# with open('data_student_info.txt','w+') as f:
# if __name__ == '__main__':
#     name = input("请输入您的姓名：")
#     age = input("请输入您的年龄：")
#     phonenumber = input("请输入您的手机号码：")
#     id = input("请输入您的身份证号：")
#     resourse = input("请输入您所选的课程：(仅限'python,linux,网络安全，前端，数据分析')")
#     # judge(phonenumber,id)
# register(name, age, phonenumber, id, resourse)
