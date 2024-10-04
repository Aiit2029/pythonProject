import hashlib

def get_md5(username,password):
    m = hashlib.md5()
    m.update(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.hexdigest()


def register(username, password):
    ret = get_md5(username,password)
    with open('hash.txt','a') as f:
        f.write(f'{ret}\n')
    return main()

def login(username,password):
    ret = get_md5(username,password)
    with open('hash.txt','r') as f:
        for i in f.readlines():
            if i.strip() == ret:
                print('登陆成功')



# def enter_info():
#     username = input('用户名:').strip()
#     password = input('密码:').strip()
#     ret = get_md5(username,password)
#     return ret

def main():
    print('''
       1、register
       2、login''')
    op = int(input('>>>'))
    if op == 1:
        username = input('用户名:').strip()
        password = input('密码:').strip()
        register(username, password)
    elif op == 2:
        username = input('用户名:').strip()
        password = input('密码:').strip()
        login(username, password)


if __name__ == '__main__':
    main()
