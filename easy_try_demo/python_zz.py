import re

big_small_text = '''
有效用户:
姓名:张三
姓名:李四
姓名:王五
无效用户:
姓名:三猫
姓名:二狗
'''
user_big = re.findall('有效用户:*(.*?)无效用户', big_small_text,re.S)
print(f'{user_big}')
user_small = re.findall('(?<=姓名:)(.*?)\n', user_big[0])
print(f'{user_small}')
