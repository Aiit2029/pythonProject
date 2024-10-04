while 1:
    try:
        num1 = int(input('输入第一个数字：'))
        num2 = int(input('输入第二个数字：'))

        if num1.is_integer() and num2.is_integer():
            def sum_easy_num(num1, num2):
                sum = num1 + num2
                print("%d + %d = %d" % (num1, num2,sum))
            sum_easy_num(num1, num2)
        else:
            print('请输入数字！')
    except ValueError:
        print("数值不对")
    except TypeError:
        print("类型问题")





