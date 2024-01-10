from selenium.webdriver.common.by import By
from use_opening_chrome import *
from red_book import *
from red_book_cfg import *
import json
import os,re,time,random
import logging


MODULE_NAME = 'red_book_publish_log'


class RandomFile:
    #该类可以将两段广告词合并生成新的广告词
    def __init__(self, file_path):
        self.file_path = file_path

    def _random_file(self):
        files = [f for f in os.listdir(self.file_path)]
        if not files:
            return None
        return os.path.join(self.file_path, random.choice(files))

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()




ad_titles = RandomFile(title_path)
ad_words_random = RandomFile(words_random_path)
ad_words_fixed = RandomFile(words_fixed_path)
ad_words = json.dumps(
    read_txt_file(ad_words_random._random_file()) + '\n\n' + read_txt_file(ad_words_fixed._random_file()))


log_cfg(MODULE_NAME)



ad_pics = RandomFile(pic_path)



def red_book_publish(port):
    '''
    打开小红书创作者中心并发布文章
    :param port: 使用对应端口号的浏览器进行操作
    :return:
    '''
    driver = use_opening_chrome(port)
    driver.get(url=red_book_publish_url)
    driver.implicitly_wait(3)
    time.sleep(1.5)

    login_elements = driver.find_elements(By.CSS_SELECTOR, '#page > div > div.content > div.con > div.login-box-container > div > div > div')

    login_unauto(login_elements)


    red_book_auto_publish(port)



def red_book_auto_publish(port):
    driver = use_opening_chrome(port)
    driver.find_element(By.CSS_SELECTOR,'#content-area > main > div.menu-container.menu-panel > div > div.publish-video > a').click()
    time.sleep(1.5)
    driver.find_element(By.XPATH,'//*[@id="web"]/div/div[1]/div[1]/div[2]/span').click()
    driver.implicitly_wait(3)
    driver.find_element(By.CSS_SELECTOR,'#web > div > div.upload-container > div.video-uploader-container.upload-area > div.upload-wrapper > div > input').send_keys(os.path.abspath(ad_pics._random_file()))
    driver.implicitly_wait(3)
    driver.find_element(By.CSS_SELECTOR,'#web > div > div.img-post > div.content > div.c-input.titleInput > input').send_keys(read_txt_file(ad_titles._random_file()))
    driver.execute_script(f"arguments[0].innerText = {ad_words};", driver.find_element(By.CSS_SELECTOR,'#post-textarea'))
    driver.implicitly_wait(3)

    is_published = False

    while not is_published:
        try:
            # 找到并点击按钮
            update_button = driver.find_element(By.CSS_SELECTOR, '#web > div > div.img-post > div.content > div.submit > button.css-k3hpu2.css-osq2ks.dyn.publishBtn.red')
            update_button.click()
            driver.implicitly_wait(3)
            # 找到发布成功标题
            update_success_title = driver.find_elements(By.CSS_SELECTOR, '#content-area > main > div:nth-child(3) > div > div.content > p.title')

            if not update_success_title:
                time.sleep(1)
                continue
            else:
                logging.info('小红书笔记发布成功')
                is_published = True
                break


        except Exception as e:
            logging.error(f"An error occurred: {e}")
            time.sleep(1)
            continue

