import re


#  判断是否是闰年
# 判断年份后看 每个月多少天，先判断年（是否是四位数字，是否是闰年，）
# 判断月（月份相加，限制1-12）
# 在加上天数（限制天数不能小于1，不能大于31，30，28）

# def year_month_day():
#      year = int(input("请输入年份："))
#      if re.match(r'^(19|20)?[0-9]{2}$',year):
#          month = int(input("请输入月份："))
#          if re.match(r'^(0?[1-9]|1[012])$',month):
#              if month == (1 | 3 | 5 | 7 | 8 | 10 | 12):
#                  full_day = 31
#              elif month == (4 | 6 | 7 | 8 | 9 | 10):
#                  full_day = 30
#              else:
#                  if year % 4 == 0:
#
#                      print('这是个闰年，二月只有28天')
#                      full_day = 28
#
#                  else:
#                      full_day = 29
#              day = int(input("请输入天数："))
#              if re.match(r'^0?[1-9]|[12][0-9]|3[01]$',day):


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_date(year,month,day):
    days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],[31,29, 31, 30, 31, 30, 31, 31, 30, 31, 30,31,]][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + day



print(which_date(2018,10,11))












     # ayear_month_day1 = n.replace(',','-')
     #
     # if re.match(r"^(19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])$", ayear_month_day1):





# year_month_day()