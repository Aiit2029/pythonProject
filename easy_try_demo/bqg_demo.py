import requests
from bs4 import BeautifulSoup
import time


def get_chapter_links(url):
    """
    获取所有章节的链接和名称
    :param url: 小说目录页的 URL
    :return: 包含章节名称和链接的列表
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # 找到包含章节列表的 div
        chapter_list_div = soup.find('div', class_='section-box')
        # 找到所有的章节链接
        chapter_links = []
        for link in chapter_list_div.find_all('a'):
            chapter_name = link.text
            chapter_url = 'https://www.bqgh.com' + link.get('href')
            print(chapter_url)
            chapter_links.append((chapter_name, chapter_url))
        return chapter_links
    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return []


def get_chapter_content(chapter_url):
    """
    获取单个章节的内容
    :param chapter_url: 章节的 URL
    :return: 章节的内容
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(chapter_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # 找到包含章节内容的 div
        content_div = soup.find('div', class_='content')
        if content_div:
            # 提取所有的段落
            paragraphs = content_div.find_all('p')
            content = '\n'.join([p.get_text() for p in paragraphs])
            return content
        return ""
    except requests.RequestException as e:
        print(f"请求章节内容出错: {e}")
        return ""


def main():
    url = 'https://www.bqgh.com/biquge/1475/'
    # 获取所有章节的链接和名称
    chapter_links = get_chapter_links(url)
    for chapter_name, chapter_url in chapter_links:
        print(f"正在爬取: {chapter_name}")
        # 获取章节内容
        content = get_chapter_content(chapter_url)
        if content:
            # 保存章节内容到文件
            with open(f'{chapter_name}.txt', 'w', encoding='utf-8') as f:
                f.write(content)
        # 为避免对网站造成过大压力，每次请求间隔 1 秒
        time.sleep(1)


if __name__ == "__main__":
    main()



