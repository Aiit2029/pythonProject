import time

print('开始运行')

name = input("阻塞")

print('就绪')

print(f'{name}:运行')
print('time.sleep阻塞一秒')
time.sleep(1)
print('回到就绪')
print('运行然后结束')