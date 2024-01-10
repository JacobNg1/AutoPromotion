from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from Tmall_crawler_cfg import options
import json
# import urllib.parse

from datetime import datetime
import os,re,time,random



def save_json_to_file(json_data, file_name):
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
    print(f'JSON数据已保存到文件: {file_name}')


def save_txt():
    file_name = 'output.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(response.text)


def save_prodact_info(data):
    # 获取当前时间
    current_time = datetime.now()

    # 格式化时间戳字符串，例如："20231026143000"（年月日时分秒）
    timestamp = current_time.strftime("%Y%m%d%H%M%S")

    file_path = r'.\product_info'
    # 构建带有时间戳的文件名
    file_name = f"product_info_{timestamp}.txt"

    full_file_path = os.path.join(file_path, file_name)

    # 打开文件并保存内容
    with open(full_file_path, 'a', encoding='utf-8') as file:
        for item in data:
            file.write(str(item) + '\n')
    print(f'成功保存文件：{file_name}')

def get_TargetData(target_data):
    # 提取所需信息，使用get方法获取键，如果不存在则返回空值
    uniqpid = target_data.get("uniqpid", 'N/A')
    auctionURL = target_data.get("auctionURL", 'N/A')
    price = target_data.get("priceShow", {}).get("price", 'N/A')
    image_url = target_data.get("pic_path", 'N/A')
    title = target_data.get("title", 'N/A')
    sales = target_data.get("realSales", 'N/A')

    shop_title = target_data.get("shopInfo", {}).get("title", 'N/A')
    shop_url = target_data.get("shopInfo", {}).get("url", 'N/A')
    shop_location = target_data.get("procity", 'N/A')



    with open('product_info.txt', 'a', encoding='utf-8') as file:
        file.write("商品ID: " + uniqpid + '\n')
        file.write("商品链接: " + auctionURL + '\n')
        file.write("价格: " + price + '\n')
        file.write("商品图片链接: " + image_url + '\n')
        file.write("标题: " + remove_html_tags(title) + '\n')
        file.write("实际销量: " + sales + '\n')

        file.write("商铺名称: " + shop_title + '\n')
        file.write("商铺链接: " + shop_url + '\n')
        file.write("商铺所在地: " + shop_location + '\n')

        file.write('\n')


def get_product_data():
    divs = driver.find_elements(By.CSS_SELECTOR, '.Content--contentInner--QVTcU0M .Card--doubleCardWrapper--L2XFE73')
    # for div in divs:
    #     div.find_element(By.CSS_SELECTOR,

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def search_in_index(search_key):
    driver.get(url=index_url)
    driver.find_element(By.CSS_SELECTOR, 'body > div.rax-view-v2.Home--home--HvP_ZHj > div.rax-view-v2.Search--searchCotent1--_JVT_2R > div.rax-view-v2.SearchInput--searchInput--1i75LwN > input').send_keys(search_key)
    driver.find_element(By.CSS_SELECTOR,'body > div.rax-view-v2.Home--home--HvP_ZHj > div.rax-view-v2.Search--searchCotent1--_JVT_2R > div.rax-view-v2.SearchInput--searchInput--1i75LwN > div').click()

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
driver = webdriver.Chrome(options=options)

#读取js脚本
f = open('stealth.min.js',mode='r',encoding='utf-8').read()
# 移除seLenium当中爬虫的特征
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': f})


search_key = '硬盘'


index_url = 'https://www.tmall.com/'
search_url = f'https://s.taobao.com/search?fromTmallRedirect=true&q={search_key}&spm=875.7931836%2FB.a2227oh.d100&tab=mall'

# search_in_index(search_key)
search_in_index(search_key)

driver.implicitly_wait(5)

switch_window(-1)  #切换到新窗口
login_elements = driver.find_elements(By.CSS_SELECTOR, '#login > div.login-content.nc-outer-box > div > div.login-blocks.login-switch-tab')
if login_elements:
    input('可能需要登录，登录后按‘ENTER’继续！')
else:
    pass



scroll_to_bottom()  #滚到底部加载页面

wait = WebDriverWait(driver, 5)  # 最多等待10秒
