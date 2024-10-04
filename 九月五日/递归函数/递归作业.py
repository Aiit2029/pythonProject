# 1、 阶乘
# count = 0
# sum = 1
#
# def func(choice_num):
#     global count
#     global sum
#     count = count + 1
#     sum *= count
#     if count == choice_num:
#         return sum
#     func(choice_num)
#     return sum

# def main():
#     choice_num = int(input('>>>:'))
#     print(func(choice_num))


# 2、 os模块查看 文件夹下文件
# import os
#
# print(os.path.)


# 5、 三级菜单
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

# def open_three(choice):
#     while True:
#         count = 0
#         for i in choice:
#             count += 1
#             print(f'{count}、{i}')
#         key = input('input>>>:').strip()
#         if key == 'b' or key == 'q':return key
#         elif key in choice.keys() and choice[key]:
#             ret = open_three(choice[key])
#             if ret == 'q':return 'q'
#
# open_three(menu)


def open_three(dic):
    while True:
        for i in dic:
            print(i)
        key = input('>>>:').strip()
        if key == 'b' or key =='q':return key
        elif key in dic.keys() and dic[key]:
            ret = open_three(dic[key])
            if ret == 'q' :return 'q'









open_three(menu)
# def main():
#     count = 0
#     for j in menu.keys():
#         count += 1
#         print(f'{count}、{j}')
#     choice = input(">>>:")
#     open_three(choice)

# if __name__ == '__main__':
#     main()
