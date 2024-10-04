# import math
#
# radius = float(input("圆的半径："))
# area = math.pi * radius**2
# long = math.pi * radius
#







# print(f'再圆的半径为{radius}的情况下\n圆的面积为{area}\n圆的周长为{long}')

##水仙花数：每个位数上的数字的三次方相加时这个数本身
# for num in range(100,1000):
#     lownum = num % 10
#     midnum = num // 10 % 10
#     highnum = num // 100
#     if num == lownum ** 3 + midnum ** 3 + highnum ** 3:
#         print(num)


## 数字反转

#将数字放入列表 list1  然后   list1[::-1]  步长为 -1 从后往前取，直接得到反转的列表


num = list(input("请输入一串数字："))

for n in range(0, len(num)// 2):
    temp = num[n]
    num[n]  = num[-(n + 1)]
    num[-(n + 1)] = temp
if num[-1] == '-':
    del num[-1]
    numtwo = ['-']
    numtwo.append("".join(num))
# print(num)
    finalnum = int("".join(numtwo))
    print(finalnum)
    print(type(finalnum))
else:
    print(''.join(num))

