import random

employee_list = []
for employee in range(1,301):
    employee_list.append(f'员工{employee}')
lucky_employee_list_third = random.sample(employee_list,30)
for employ in lucky_employee_list_third:
    employee_list.remove(employ)
lucky_employee_list_second = random.sample(employee_list,6)
for employ in lucky_employee_list_second:
    employee_list.remove(employ)
lucky_employee_list_first = random.sample(employee_list,3)
print(f'{lucky_employee_list_first}中了一等奖:泰国五日游和手术费报销')
print(f'{lucky_employee_list_second}中了二等奖:iphone14手机')
print(f'{lucky_employee_list_third}中了三等奖:三斤苹果')