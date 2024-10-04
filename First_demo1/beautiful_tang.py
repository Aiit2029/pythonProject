from bs4 import BeautifulSoup
import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}

titleall = []

for start_num in range(0,250,25):
    response = requests.get(f'https://movie.douban.com/top250?start={start_num}',headers=header ).text
    soup = BeautifulSoup(response, 'html.parser')

    titles = soup.find_all(attrs={'class': 'title'})
    titleslist = []
    for title in titles:
        # if  '\u4e00' <= title.string <= '\u9fff':
        #     titleslist.append(title.string)
        if '/' not in title.string:
            titleslist.append(title.string)
            titleall.append(title.string)


print(titleall)
print(len(titleall))


