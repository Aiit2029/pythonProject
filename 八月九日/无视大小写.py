import random
import string

username = input("请输入用户名：")
password = input("<PASSWORD>")
all_char = string.ascii_letters + string.digits
code = ''.join(random.choice(all_char) for _ in range(4))
print(code)
passcode = input('<code>')
if passcode.lower() == code.lower():
    print('pass')
else:
    print('fail')