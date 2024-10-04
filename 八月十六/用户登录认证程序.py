
f = open("secret.txt",'r',encoding='utf-8')
acount = {
    #'liusang':'['liusang','123','1']'
}
for line in f:
    line = line.strip().split(',')
    acount[line[0]] = line

while True:
    user_name = input("请输入用户账号:")
    if user_name not in acount:
        print('请输入正确的，已经注册的账号！')
        continue
    i = 3
    while i>0:
        password = input("请输入用户密码:").strip()
        if password == acount[user_name][1]:
            print("验证通过")
            exit('结束咯')
        else:
            print("哎，朋哟，你滴，不是本人,再来一次逝世吧")
        i -= 1
        print(f'你还有{i}次机会')
