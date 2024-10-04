import datetime

#练习  统计某年的二月份有多少天

time_before = datetime.timedelta(days = 1)
year  = int(input('>>>'))

d = datetime.date(year,3,1)

res = d - time_before
# res 的结果类型  和  前面做运算的 d 的类型有关

print(res.day)