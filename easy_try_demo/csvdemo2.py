import re
import csv
import requests

with open('baidu.html','r',encoding='utf-8') as f:
    source = f.read()
result_list = []
username = re.findall(r'class="p_author_name j_user_card".*?>(.*?)</a',source,re.S)
content = re.findall(r'class="d_post_content j_d_post_content ".*?>(.*?)</div',source,re.S)
time = re.findall(r'class="tail-info">(\d{4}-\d{2}-\d{2} \d{2}:\d{2})<',source,re.S)
for i in range(len(username)):
    result = {'username':username[i], 'content':content[i], 'time_demo':time[i]}
    result_list.append(result)
print(result_list)
with open('baidu.csv','w',encoding='utf-8') as t:
    writer1 = csv.DictWriter(t,fieldnames=['username','content','time_demo'])
    writer1.writeheader()
    writer1.writerows(result_list)

