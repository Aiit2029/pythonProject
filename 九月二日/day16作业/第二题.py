import time

ret = time.localtime()
# new_time = time_demo.strftime("%Y:%m:%d:%H:%M:%S")
new_time = time.strftime("%Y%m%d")



print(ret)
print(new_time)