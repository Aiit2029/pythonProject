##  封装了获取时间戳和字符串形式的时间的一些方法

import time

#   获取时间戳
print(time.time())  #   1725350634.3133173   从时间元年到现在为止经过的秒数  从1970年 1月1日 00：00：00开始

# 获取电脑上现在的时间  不过是time.struct_time(tm_year=2024, tm_mon=9, tm_mday=3,
# tm_hour=17, tm_min=2, tm_sec=28, tm_wday=1, tm_yday=247, tm_isdst=0)的形式
print(time.localtime())


print(time.gmtime())  # GMT 格林尼治时间

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# t1 = time_demo.localtime()
# t2 = time_demo.mktime(t1)  # 将时间对象返回成时间戳形式
# print(t2)
# new_time = time_demo.strftime()


time.sleep(2)  #暂停当前游戏，睡眠x秒










