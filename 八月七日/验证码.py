import random
import string

while 1:
    n = int(input('请输入一个数字来限定验证码的长度：'))
    confirm2 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    print(confirm2)


