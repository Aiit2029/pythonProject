import random

i = 0
x = random.randint(0,1025)
keylist = []
valuelist = []
guessdirc = {}
while 1:
    # print('请输入你的用户名')
    # user = input("你的用户名是: ")
    # guess = int(input(f'用户：{user}请输入一个整数：'))
    guess = int(input('请输入一个整数：'))


    if guess == 3:
        break
    elif guess == 1:
        for keyt,valuet in guessdirc.items():
            print(f'{keyt},{valuet}')
        continue
    try:
        if  guess == x:
            print('你猜对了')
            break
        elif guess > x:
            print("你所猜的数字有点大")
        elif guess < x:
            print('你所猜的数字有点小')
    except ValueError:
        print("请不要传入空值")
    i += 1
    print(f'你还有{10-i}次机会,')
    keylist.append(f'第{i}次')
    valuelist.append(f'{guess}')
    for k,v in zip(keylist,valuelist):
        guessdirc[k] =v
else:
    print(f'你的猜数次数耗尽了,答案是{x}')