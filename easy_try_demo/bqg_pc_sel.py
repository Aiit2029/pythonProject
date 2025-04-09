import base64

import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_chapter_links(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Referer': 'https://www.bqgh.com/biquge/1475/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        chapter_list_div = soup.find('div', class_='section-box')
        chapter_links = []
        for link in chapter_list_div.find_all('a'):
            chapter_name = link.text
            chapter_url = 'https://www.bqgh.com' + link.get('href')
            chapter_links.append((chapter_name, chapter_url))
            print("到这了")
            # 动态检查后续页面
            page_num = 1
            while True:
                next_page_url = chapter_url.replace('.html', f'_{page_num}.html')
                print("到了这了")
                if get_chapter_content(next_page_url) == "":
                    break
                chapter_links.append((f"{chapter_name}_第{page_num}页", next_page_url))
                page_num += 1
                print("没错，刚到这")

        return chapter_links
    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return []

def decode_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all('script')
    content = []
    for script in scripts:
        if 'qsbs.bb' in script.text:
            encoded = script.text.split("bb('")[1].split("')")[0]
            decoded = base64.b64decode(encoded).decode('utf-8')
            content.append(decoded)
    return '\n'.join(content)

def get_chapter_content(chapter_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Referer': 'https://www.bqgh.com/biquge/1475/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    try:
        # 先尝试使用 requests 方法
        response = requests.get(chapter_url, headers=headers)
        response.raise_for_status()
        unclean_content = decode_content(response.text)
        soup = BeautifulSoup(unclean_content, 'html.parser')

        if soup:
            paragraphs = soup.find_all('p')
            content = '\n'.join([p.get_text() for p in paragraphs])
            return content
        # content = soup.find('div', class_='content')
        # if content:
        #     paragraphs = content.find_all('p')
        # content = soup.find_all('a')
        # if content:
        #     paragraphs = unclean_content.find_all('p')
        #     content = '\n'.join([p.get_text() for p in paragraphs])
        #     return content

        # 如果 requests 方法失败，使用 Selenium
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get(chapter_url)
        # time.sleep(3)  # 等待页面加载
        page_source = driver.page_source
        driver.quit()
        soup = BeautifulSoup(page_source, 'html.parser')
        content_div = soup.find('div', class_='content')
        if content_div:
            paragraphs = content_div.find_all('p')
            content = '\n'.join([p.get_text() for p in paragraphs])
            return content
        return ""
    except requests.RequestException as e:
        print(f"请求章节内容出错: {e}")
        return ""


def main():

    url = 'https://www.bqgh.com/biquge/1475/'
    chapter_links = get_chapter_links(url)
    for chapter_name, chapter_url in chapter_links:
        print(f"正在爬取: {chapter_name}")
        content = get_chapter_content(chapter_url)
        if content:
            with open(f'{chapter_name}.txt', 'w', encoding='utf-8') as f:
                f.write(content)
        # time.sleep(2)  # 增加请求间隔时间



if __name__ == "__main__":
    main()
