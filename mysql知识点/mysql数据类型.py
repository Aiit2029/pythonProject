# MySQL 中的数据类型
    # 数字类型
        # tinyint
        # smallint
        # mediumint
        # int or integer
        # bigint
# 如果需要这段数字没有负值 需要在定义字段时 在后面加上 unsigned,默认是有符号的
        # float
        # double
        # decimal (10,5)
# 括号中意思是 整数和小数 总共最多是 10位数  小数最多五位数
    # 时间类型
        # date  #格式
            # 20190620
            # 1000-01-01 00：00：00 ---9999-12-31 23：59：59
        # time
            # 121953

        # datetime
            #20190620121953

        # year 范围： 1901--2155

        # timestamp 时间戳
            # 范围
            # 1970-01-01 00:00:00 ---2038-1-19 11:14:07
            # timestamp 具有专有的自动更新特性

    # 字符串类型
        # char
            # char  最多只能表示255个字符
            # char 是 定长存储
            # 当我设置字段长度为 char(18)
            # 然后存入 'alex' 其存储方式为 'alex{十四个空格}'
        # varchar
            # varchar 最多能表示65535个字符
            # varchar 是 变长存储
            # 当我设置字段长度为 varchar(18)
            # 然后存入 'alex' 其存储方式为 'alex4'
            # 其存取速度慢，
            # 因为 在存进去的时候要算一下 这个字段的长度 然后 放到字段的最后
            # 而 char则不管你多长 直接按照最长的长度存进去后面都补上空格
            # 用的时候直接用
