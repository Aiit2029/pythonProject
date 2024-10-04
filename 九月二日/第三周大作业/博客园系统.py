import re
import sys


def wrapper(f):
    def inner(*args, **kwargs):

        ret = f(*args, **kwargs)

        return ret
    return inner


def loginper(f):
    def inner(*args, **kwargs):

        ret = f(*args, **kwargs)

        return ret

    return inner


@wrapper
def register():
    with open('secret.txt','a+',encoding='utf-8') as f:
        f.seek(0)
        while True:
            username = input('username:').strip()
            password = input('password:').strip()
            if re.match(r'^[a-zA-Z0-9]',username) and re.match(r'.{6,14}',password):
                content = f.read()
                if content:
                    for line in content.split('\n'):
                        if line:
                            existing_username, existing_password= line.split(':')
                            if username == existing_username:
                                print("用户名已存在,请重新输入")
                                break
                else:
                    f.write(f'{username}:{password}\n')
                    print('注册成功')
            else:
                print('用户名或密码不合法')
                return main()


@loginper
def login():
    with open('secret.txt','r',encoding='utf-8') as f:
        while True:
            username = input('username:').strip()
            password = input('password:').strip()
            content = f.read()

            if content:
                for line in content.split('\n'):
                    if line:
                        existing_username, existing_password= line.split(':')
                        if username == existing_username and password == existing_password:


                            print('登陆成功')






def main():
    print('''             1.login
             2.register
             3.enter articl 
             4.comment
             5.diary
             6.store
             7.destroy username
             8.exit''')
    choice = input('>>>:').strip()
    if hasattr(sys.modules[__name__],choice):
        func = getattr(sys.modules[__name__],choice)
        if callable(func):
            func()




if __name__ == '__main__':
    main()



