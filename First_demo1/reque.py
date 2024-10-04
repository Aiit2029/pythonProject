from bs4 import BeautifulSoup
import requests
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}
response = requests.get('https://books.toscrape.com/',headers=header).text
soup = BeautifulSoup(response,'html.parser')

# 找到所有书籍的价格
all_prices = soup.find_all(attrs={"class":'price_color'})

# 找到所有书籍的名称
all_titles = soup.find_all('h3')

# 创建一个空字典存储名称和价格
book_name_price = {}

for price,titles in zip(all_prices, all_titles):
    price_value = price.string[2:]
    title_value = titles.a.string
    book_name_price[title_value] = price_value


for key,value in book_name_price.items():
    print(f"{key},{value}")

