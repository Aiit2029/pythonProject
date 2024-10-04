# tip = input('请输入一个整数：')
# number = int(tip)
# while number >0:
#     print(' '*(number-1)+'*'*number)
#     number = number-1


# year = int(input("Enter your year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("It is a leap year")
# else:
#     print("It is not a leap year")


# for i in range(0,100):
#     if i % 2 == 1:
#         print("这是个奇数",i)
# x = 7
# i = 1
# flag = 0
#
# while i <= 1000:
#     if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5):
#         flag = 1
#     else:
#         x = 7 * (i+1) # 根据题意，x一定是7的整数倍，所以每次乘以7
#     i += 1
#
# if flag == 1:
#     print('阶梯数是：', x)
# else:
#     print('在程序限定的范围内找不到答案！')

# x = 7
# i = 1
# flag =0
#
# while i<100:
#     if x%6 ==5 and x%5 ==4 and x%3 ==2 and x%2 ==1:
#         flag = 1
#     else:
#         x = 7 * (i+1)
#     i = i + 1
# if flag == 1:
#     print("这个数真难熊:", x)
# else:
#     print('找不到这个b数')


sum = 0
for i in range(1,10):
    j = 1
    while j<10:
        sum = i*j
        print(i,'*',j,'=',sum,end='    ',sep='')
        j = j + 1
    print('\n')
    i = i + 1








