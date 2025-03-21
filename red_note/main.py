from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from red_book import *
import json
#import urllib.parse

from datetime import datetime
import os,re,time,random


from red_book_cfg import options



def open_page(search_key):
    driver.get(url=index_url)

def get_product_data():
    divs = driver.find_elements(By.CSS_SELECTOR, '.Content--contentInner--QVTcU0M .Card--doubleCardWrapper--L2XFE73')
    # for div in divs:
    #     div.find_element(By.CSS_SELECTOR,

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)



def search_in_searck(search_key):
    driver.get(url=search_url)

def switch_window(new_tag):
    all_window_handles = driver.window_handles
    new_window_handle = all_window_handles[new_tag]
    driver.switch_to.window(new_window_handle)


def scroll_to_bottom(scroll_speed  = 400,total_scroll_distance = 4000):
    # 定义滚动速度和滚动总距离
    # scroll_speed = 400  # 滚动速度，数字越大滚动越快
    # total_scroll_distance = 4000  # 总共要滚动的距离
    # 循环逐渐滚动
    for _ in range(total_scroll_distance // scroll_speed):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(0.2)  # 等待一小段时间以控制滚动速度





#STAR FROM HERE
# 打开浏览器
driver_window = Options()
driver_window.add_argument("--window-size=1440,720")
driver = webdriver.Chrome(options=options)

#读取js脚本
json_script = find_file('stealth.min.js')
f = open(json_script,mode='r',encoding='utf-8').read()
# 移除seLenium当中爬虫的特征
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': f})

#打开小红书创作中心
index_url = 'https://creator.xiaohongshu.com/creator/home'
driver.get(url=index_url)
driver.implicitly_wait(3)


#login
login_elements = driver.find_elements(By.CSS_SELECTOR, '#page > div > div.content > div.con > div.login-box-container > div > div > div')
if login_elements:
    input('可能需要登录，登录后按‘ENTER’继续！')


driver.find_element(By.CSS_SELECTOR,'#content-area > main > div.menu-container.menu-panel > div > div.publish-video > a').click()
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR,'#web > div > div.upload-container > div.header > div.tab.active > span').click()
driver.implicitly_wait(3)






input('保持')


