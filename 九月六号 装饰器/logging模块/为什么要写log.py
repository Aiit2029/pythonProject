#  为什么要写log
    # log是为了排错
    # log 是用来做数据分析的

# 购物商城 -- 数据库里
    # 什么时间购买了什么商品
    # 把那些商品加入了购物车

# 一个用户 在什么地点什么时间  登陆了那些购物程序
# 搜索了那些信息。，多长时间
# 什么时候关闭了软件
# 点开了哪些商品  看了多久



# fh = logging.FileHandler('test.log')
# sh = logging.StreamHandler()
#
# logging.basicConfig(
#     format='%(asctime)s - %(name)s [line: %(lineno)d]- %(levelname)s - %(message)s,',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     level=logging.DEBUG,
#     handlers=[fh,sh]
# )
#
#
#
# # 输出内容是有等级的
# logging.debug('debug message')            #调试
# logging.info('info message')              # 信息
# logging.warning('warning message')        # 警告
# logging.error('error message')            # 错误
# logging.critical('critical message')      # 批判性的


# 做日志的切分


import time
from logging import handlers
import logging

sh = logging.StreamHandler()

rh = handlers.RotatingFileHandler('test.log', maxBytes=1024,backupCount=5)

th = handlers.TimedRotatingFileHandler('x2.log',when = 's',interval=5,encoding='utf-8')


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M',
    level=logging.ERROR,
    handlers=[sh,rh,th]
)

for i in range(1,100000):
    time.sleep(1)
    logging.error(f'keyboard interrupt in this file{i}')



