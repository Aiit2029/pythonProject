filename = 'data_info.txt'


def register():
    print('我的世界'.center(50, '-'))
    print('请完成学籍注册')
    name = input('请输入您的姓名：').strip()
    age = input('请输入您的age：').strip()
    phone = input('请输入您的phone：').strip()
    id_num = input('请输入您的id_num：').strip()
    course_list = ['数据分析', 'linux', '前端', '数据处理', 'Java', 'Python']
    for index, val in enumerate(course_list):
        print(f"{index}.{val}")
    select_course = input('请输入所选课程：').strip()
    if select_course.isdigit():
        select_course = int(select_course)
        if 0 <= select_course < len(course_list):
            picked_course = course_list[select_course]
            print(picked_course)
    info_list = {}
    info_list['name'] = name
    info_list['age'] = age
    info_list['phone'] = phone
    info_list['id_num'] = id_num
    info_list['select_course'] = picked_course
    print(info_list)
    judge(filename,info_list)
    store(filename, info_list)


def store(filename, info_list):
    with open(filename, 'a+') as f:
        f.write(str(info_list) + '\n')
        print('已存入')


def judge(filename, info_list):
    phone_list = []
    id_num_list = []
    with open(filename, 'r') as f:
        for line in f:
            line = eval(line.strip())
            phone_list.append(line['phone'])
            id_num_list.append(line['id_num'])
    if info_list['phone'] in phone_list or info_list['id_num'] in id_num_list:
        exit('该(手机号码/身份证号)已经有对应的账号了')






register()


