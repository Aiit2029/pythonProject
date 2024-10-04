import re
while True:
    user_name = input('请输入你的用户名：')
    if re.match(r'[\w]{6,20}', user_name):
        print('通过验证')
        break
    else:
        print('验证不通过，请重新输入')
    continue
while True:
    qq_num = (input('请输入5-12位有效数字，且首位不为0：'))
    if re.match(r'[1-9][\d]{4,11}', qq_num):
        print('验证通过')
        break
    else:
        print('验证不通过')
    continue
