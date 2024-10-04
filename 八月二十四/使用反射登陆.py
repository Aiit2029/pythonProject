class User():
    def login(self):
        print('denglu')
    def logout(self):
        print('dengchu')
    def register(self):
        print('zhuce')
    def change_password(self):
        print('xiugaimima')

user1 = User()
while 1:
    choose = input('>>>').strip()
    if hasattr(user1,choose):
        fun = getattr(user1,choose)
        fun()
    else:
        print('invalid')