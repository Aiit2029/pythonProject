# 装饰器的应用 ： 登录认证

status_dict = {
    'username': '123',
    'status': False
}


def register():
    pass


def login():
    # username = input('please input your username: ')
    # if username == status_dict['username']:
    #     status_dict['status'] = True
    # else:
    #     print('invalid')
    username = input('please input your username: ').strip()
    password = input('please input your password: ').strip()
    if username == 'taibai' and password == '123':
        print('login success')
        status_dict['username'] = username
        status_dict['status'] = True
    else:
        print('login fail')

def auth(method_name):
    '''
    访问被装饰函数之前需要进行一个三次登录认证

    :param method_name:
    :return:
    '''

    def confirm_status(*args, **kwargs):
        count = 0
        if status_dict['status']:
            ret = method_name(*args, **kwargs)
            return ret
        else:
            print('''you can not enter the door
            please input your username and password''')
            login()
    return confirm_status


def logout():
    pass


@auth
def article():
    print('已进入文章页面')


def comment():
    print('已进入评论页面')


def diary():
    print('已进入日记页面')


# choose = input('>>>:')

# if choose in x.keys():
#     # choose()'
# for key, value in globals().items():
#     print(f"键: {key}, 值的类型: {type(value)}")



# 出错：dictionary changed size during iteration
# 原因，程序执行到下一行时，将name,obj加入到globals()中，因此字典的大小改变
'''
for name, obj in iteritems(globals()):
    print(name)
    print(globals())
'''


# 解决方法:定义函数，将代码包括在里面,函数中globals()不会变化

# iteritems = lambda d, *args, **kwargs: iter(d.items(*args, **kwargs))
# def _find_exceptions():
#     lst1 = []
#     def lst():
#         for name, obj in iteritems(globals()):
#             lst1.append(name)
#         print(lst1)
#     return lst
# ret = _find_exceptions()
# list1 = ret()







# print(status_dict['username'])
# print(type(status_dict['username']))
