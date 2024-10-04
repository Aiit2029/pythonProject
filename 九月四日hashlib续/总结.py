#random
import datetime
import os
import pickle
import random
import string
import sys
import time

# x = random.random()  #  从0-1中选一个随机值
# print(x)
#
# t = random.randint(10,20)  # 返回 a, b 之间任意一个整数值 包括  b
# print(t)

# a = random.randrange(1,10)  #  返回从a到b 之间任意一个整数值，不包括10
# print(a)
#
# b = random.choice([1,2,3,4,5,6,7,8,9])  # 从给出的内容中随机出一个数
# print(b)

# a = random.choices(string.ascii_letters,k=2)   #给出一个范围，从中随机取值，取数 为 k
# print(a)
#
# a = time.time()  # 从  1970年1月1日00：00：00开始到现在的秒数
# print(a)
#
# a = time.localtime()  #结构化时间
# print(a)
#
# a = time.strftime("%Y%m")   #  格式化字符
# print(a)
#
# a = datetime.datetime(year=2020, month=1, day=1, hour=10) #设置时间
# print(a)


# a = datetime.date(year=2020, month=1, day=1)  # 只能设置年月日
#
# b = datetime.time(hour=23, minute=59, second=20) # 只能设置时分秒
#
# c = datetime.timedelta(days=1) #  时间运算使用   代表时间差值
# d = time.mktime()  # 把放进去的时间转化为  时间戳时间   放进去的内容应该是一个 struct_time  如果是元组，应该包含， 年月日时分秒 星期几  一年的第几天， 夏令时标准
# print(d)

#  os

# x = os.urandom(16)
# print(x)


