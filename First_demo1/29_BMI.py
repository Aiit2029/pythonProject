try:
    weight = float(input("Enter your weight:"))
    height = float(input("Enter your height:"))


except ValueError:
    print("数值错误")
except TypeError:
    print("类型错误")
else:
    def calculate_BMI(weight, height):
        bmi = weight / (height ** 2)
        if bmi <= 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi <= 25:
            category = 'Normal'
        elif 25 <= bmi <= 30:
            category = 'Overweight'
        else:
            category = 'Obese'
        print(f'Your BMI is:{category}')
        return category
    calculate_BMI(weight, height)
finally:
    print("结束执行")






