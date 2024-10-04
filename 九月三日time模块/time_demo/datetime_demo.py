import datetime

# 年月日叫  date
d = datetime.date(2010, 10, 10)
print(d)

# 时分秒是 time_demo
t = datetime.time(12,12,24)
print(t)

# datetime 类

dt = datetime.datetime(2010, 10, 10, 12, 12)
print(dt)


# timedelta : 时间变化量  time得它
# 一般参与数学运算  参与数学运算的对象只能是 date ,datetime, timedelta
t1 = datetime.datetime(2010, 10,10,10,10,59)
tdt = datetime.timedelta(seconds=3)
res = t1 + tdt
print(res)


