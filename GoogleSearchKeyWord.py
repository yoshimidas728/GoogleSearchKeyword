from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pypasser import reCaptchaV2
import pandas as pd
import openpyxl
import time
import sys
import os


output_file = 'output.txt'
print("輸入您的 Google 搜尋關鍵字：")

# 取得允許 URL
def get_allow(results):
    cnt = 0
    out = []
    for result in results:
            out.append(result)
            cnt = cnt + 1
    return out

# 偵測 Captcha
def is_captcha_present():
    try:
        driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
        return True
    except NoSuchElementException:
        return False

def perform_search(query):
    global driver
    driver.get('https://www.google.com')
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1) # 等待結果加載。

    if is_captcha_present():
        print('DETECT CAPTCHA')
        try:
            is_checked = reCaptchaV2(driver=driver, play=False)
        except Exception as e:
            pass
        try:
            driver.find_element(By.CSS_SELECTOR, '.rc-doscaptcha-header-text')
            print('TRY AGAIN')
        except Exception as e:
            pass
    
    time.sleep(2) # 等待結果加載。

# 分析 HTML
def extract_search_results():
    global driver, result_count
    results = []
    # 尋找搜尋結果 elements
    search_results = driver.find_elements(By.CSS_SELECTOR, 'h3')
    n = 0
    for result in search_results:
        link = result.find_element(By.XPATH, '..').get_attribute('href')
        if link != None:
            results.append(link)
            n = n + 1
    return results

# 主要搜尋發動機。
def google_search(query):
    global driver
    perform_search(query)
    search_results = extract_search_results()
    return get_allow(search_results)

def delete_history():
    global driver

    # 開啟Chrome的設定頁面以清除瀏覽資料。
    driver.get('chrome://settings/clearBrowserData')

    time.sleep(1)  # 等待頁面載入（您可能需要根據您的系統增加此值）

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    time_range = driver.switch_to.active_element
    time_range.send_keys(Keys.ARROW_DOWN * 4)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
    driver.switch_to.active_element.send_keys(Keys.ENTER)

    time.sleep(5)  # 等待操作完成。

def write_results_to_txt(results):
    with open(output_file, 'w') as file:  # 以寫入模式開啟檔案。
        for result in results:
            file.write(result + '\n')  # 將每個結果寫在新行上。

if __name__ == '__main__':
    query = input()
    
    # 啟動 Chrome 的新實例。
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    delete_history()
    result = google_search(query)
    write_results_to_txt(result)
    
    print(f"搜尋 URL 結果保存到 {output_file}")
