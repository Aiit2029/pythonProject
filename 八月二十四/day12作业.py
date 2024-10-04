#过滤长度小于3的字符串列表
import random

# list1 = []
# [i.upper for i in list1 if len(i) >= 3]
z = ([x for x in range(0,6) if x % 2 == 0],[y for y in range(0,6) if y % 2 == 1])
print(z)
# lst1 = [i**2 for i in range (1,51) if i % 3 == 0]
# print(lst1)
# x = [i for i in range(0,6)]
# y = [i for i in range(1,7)]
# z = [(x,y) for x in range(0,6) for y in range(1,7)]
# print(z)

# z = [(x,x+1) for x in range(0,6)]
# print(z)
#
# l1 = ['alex','WUsir','老男孩','太白']
# x = [f'{l1[i]}{i}' for i in range(len(l1))]
# print(x)
#
# x = {
# 'name':'alex',
# 'Values':[{'timestamp':1517991992.94,
# 'values':100,},
# {'timestamp': 1517992000.94,
# 'values': 200,},
# {'timestamp': 1517992014.94,
# 'values': 300,},
# {'timestamp': 1517992744.94,
# 'values': 350},
# {'timestamp': 1517992800.94,
# 'values': 280}
# ],}
# list1 = []
# for i in x["Values"]:
#     list1.append([i['timestamp'], i['values']])
# print(list1)
# lst2 = [[i['timestamp'], i['values']] for i in x["Values"]]
# print(lst2)

# z = [(x,y) for x in list('123456789JQK') for y in ['spades','diamonds','clubs','hearts']]
# print(z)

# map1 = [[key,value] for key,value in x.values]

# v = ({i % 2 for i in range(10)})
# print(v)

