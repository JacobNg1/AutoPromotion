from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from use_opening_chrome import *
from AI_generate_text import AI_t2t
from red_book_cfg import *
from red_book import *

import requests
import logging

from datetime import datetime
import os,re,time,random

'''用于爬取小红书爆款文案到通义生文'''

MODULE_NAME = 'red_book_to_AI'



hot_text_keyword = [
            #'raging water水上乐园',
            '赫本温泉',
            # '奔富bin407',
            #'奔富bin707',
            # '澳洲Coles超市',
            # '塔龙加动物园'
            ]



file_path = os.path.join(FILE_PATH, MODULE_NAME)
text_path = os.path.join(file_path,'generated_text.txt')

print('本次生成内容保存到：' + os.path.abspath(text_path))

logging.basicConfig(filename=log_cfg(MODULE_NAME), level=logging.INFO)  # 配置log  设置日志级别为 INFO，保存到文件




def red_book_hot_text(port):
    '''
    打开小红书找爆款
    :param port: 使用对应端口号的浏览器进行操作
    :return:
    '''

    # 每个关键词找文章数
    hot_text_num = 8
    # 每篇文章生成AI文章数
    AI_text_num = 8


    driver = use_opening_chrome(port)


    #每个关键词都要被搜索
    for keyword in hot_text_keyword:
        driver.get(url=red_book_index_url)
        driver.implicitly_wait(3)
        time.sleep(1.5)
        login_elements = driver.find_elements(By.CSS_SELECTOR, '#app > div:nth-child(1) > div > div.login-container')
        login_unauto(login_elements)

        driver.find_element(By.CSS_SELECTOR,
                            '#global > div.header-container > header > div.input-box > input').send_keys(keyword)
        driver.implicitly_wait(2)
        driver.find_element(By.CSS_SELECTOR,
                            '#global > div.header-container > header > div.input-box > input').send_keys(Keys.RETURN)
        text_write('\n' + keyword + '\n\n', text_path)
        driver.implicitly_wait(2)

        get_hot_text_url(port,hot_text_num,AI_text_num,driver)
        

        text_write('\n\n' + '----------' * 10 + '\n\n' , text_path)
        # driver.switch_to.new_window()

        logging.info(f'生成成功，AI根据{hot_text_num}个热文生成了{hot_text_num * AI_text_num}条文章')



# def detect_element_tag(element_type,url):
#     res = requests.get(url)
#
#     # print(res.text)
#     # 定义正则表达式模式，用于匹配包含指定data-v属性和href属性的a标签
#     pattern = r'<a .*?.*?href="(.*?)".*?>'
#
#     # 使用正则表达式查找并提取href属性值
#     match = re.search(pattern, html_fragment)





def get_hot_text_url(port,hot_text_num,AI_text_num,driver):
    divs = driver.find_elements(By.CSS_SELECTOR,'.note-item')

    for i in range(min(hot_text_num, len(divs))):
        div = divs[i]
        text = div.text
        print(text)

        div_url = div.find_element(By.CSS_SELECTOR, f'a[data-v-4eeb96ca]').get_attribute('href')
        print(div_url)
        text_write('热文:' + text + '\n' + div_url + '\n\n',text_path)

        AI_generate_text(div_url,AI_text_num)
        time.sleep(random.randint(15, 20))



def AI_generate_text(url,times):
    res = requests.get(url)
    hot_text_page = BeautifulSoup(res.text, 'html.parser')

    for j in range(times):
        hot_text = hot_text_page.find("meta", {"name": "description"})["content"] #获取热文内容
        if j <= 0:
            print('hot_text:' + hot_text)
            text_write('热文内容:' + hot_text + '\n', text_path)
        else:
            pass


        generated_text = AI_t2t(hot_text)
        if generated_text is None:
            generated_text = "生成错误"

        print(f'generated_text_{j + 1}:')
        print(generated_text)
        text_write(generated_text + '\n',text_path)

    text_write('\n\n',text_path)







if __name__ == "__main__":
    driver = red_book_hot_text(9222)

