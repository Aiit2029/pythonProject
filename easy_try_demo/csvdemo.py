import base64

import requests
from bs4 import BeautifulSoup


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

def main():
    url = 'https://www.bqgh.com/1/1475/405704.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(decode_content(response.text))

if __name__ == "__main__":
    main()