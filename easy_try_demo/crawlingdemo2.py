# from bs4 import BeautifulSoup
# import requests
# import re
#
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}
#
# response = requests.get('https://tieba.baidu.com/p/9109260051', headers=header)
#
# # with open('baidu.html', 'w',encoding='utf-8') as f:
# #     f.write(response.text)
# print(response)
# soup = BeautifulSoup(response.text, 'html.parser')
# result_name = soup.find_all('a', class_='p_author_name j_user_card')
# result_content = soup.find_all('div', class_='d_post_content j_d_post_content')
# result_time = soup.find_all('span', class_='tail-info')
#
#
# # 定义正则表达式模式，这里假设只允许包含字母和空格
# name_pattern = r'^(.*)$'
# content_pattern = r'(.*)$'
# time_pattern = r'^[0-9-: ]$'
#
# data_dict = {}
# for name, content, time_demo in zip(result_name, result_content, result_time):
#     name_text = name.get_text().strip()
#     content_text = content.get_text().strip()
#     time_text = time_demo.get_text().strip()
#
#     if re.match(name_pattern, name_text) and re.match(content_pattern, content_text) and re.match(time_pattern,time_text):
#         data_dict[name_text] = {'content': content_text, 'time_demo': time_text}
#
# print(data_dict)
#
from bs4 import BeautifulSoup
import requests
import re

# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}
#
response = requests.get('https://tieba.baidu.com/p/9109260051', headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
result_name = soup.find_all('a', class_='p_author_name j_user_card')
result_content = soup.find_all('div', class_='d_post_content j_d_post_content')
result_time = soup.find_all('span', class_='tail-info')

# 定义正则表达式模式
name_pattern = r'^[\w\s\u4e00-\u9fff]+$'
content_pattern = r'.*'
time_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}'  # 匹配 2024-07-30 04:44 这种格式

data_dict = {}
for name, content, time in zip(result_name, result_content, result_time):
    name_text = name.get_text().strip()
    content_text = content.get_text().strip()
    time_text = time.get_text().strip()

    # 检查文本是否为空
    if name_text and content_text and time_text:
        if re.match(name_pattern, name_text) and re.match(content_pattern, content_text) and re.match(time_pattern, time_text):
            data_dict[name_text] = {'content': content_text, 'time_demo': time_text}

print(data_dict)