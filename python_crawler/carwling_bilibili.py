from bs4 import BeautifulSoup
import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}
response = requests.get('https://www.bqgui.cc/xuanhuan/', headers=header).text
soup = BeautifulSoup(response, 'html.parser')
# with open('bilibili.html', 'a',encoding='utf-8') as f:
#     f.write(response)

title = soup.find_all('dt')
titlelist = []
for title1 in title:
    titlelist.append(title1.a.string)
print(titlelist)



# https://www.bilibili.com/anime/index/?from_spmid=666.4.index.0#st=1&order=3&season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&sort=0&page=2