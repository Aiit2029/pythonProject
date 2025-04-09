# 完整代码示例（以Selenium为主）
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def get_chapter_content(chapter_url):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(chapter_url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'content'))
        )
        # 关闭广告弹窗
        close_btn = driver.find_elements(By.XPATH, '//a[contains(@onclick, "closeWin")]')
        if close_btn:
            close_btn[0].click()
            time.sleep(1)

        content_div = driver.find_element(By.CLASS_NAME, 'content')
        content = content_div.text
        return content
    except Exception as e:
        print(f"获取内容失败: {e}")
        return ""
    finally:
        driver.quit()


# 调用示例
if __name__ == "__main__":
    chapter_url = 'https://www.bqgh.com/1/1475/405704.html'
    content = get_chapter_content(chapter_url)
    print(content)