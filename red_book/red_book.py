from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchWindowException
# from selenium.webdriver.support import expected_conditions as EC
from red_book_cfg import *
from datetime import datetime
import os,re,time,random

import logging



def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


# def new_window():
#     driver.execute_script("window.open('about:blank', '_blank');")

def log_cfg(MODULE_NAME):
    log_filename = f'{MODULE_NAME}.log'
    log_path = os.path.join(LOG_PATH,log_filename)


    return log_path




class BrowserWindows:
    def __init__(self, driver):
        self.driver = driver
        self.main_window_handle = driver.current_window_handle
        self.windows = {self.main_window_handle: driver.title}


    def open_new_window(self, url):
        self.driver.execute_script("window.open('', '_blank');")
        self.window_handles = self.driver.window_handles
        # Switch to the new window
        new_window_handle = self.window_handles[-1]
        self.driver.switch_to.window(new_window_handle)
        # Open the URL in the new window
        self.driver.get(url)

    def close_current_window(self):
        current_window_handle = self.driver.current_window_handle
        self.driver.close()
        self.window_handles.remove(current_window_handle)
        self.driver.switch_to.window(self.window_handles[-1])

    def get_window_handles(self):
        self.window_handles = self.driver.window_handles
        self.update_windows()
        print(self.windows)
        return self.window_handles

    def update_windows(self):
        self.window_handles = self.driver.window_handles
        self.windows = {handle: self.driver.switch_to.window(handle).title for handle in self.window_handles if handle is not None}


def scroll_to_bottom(scroll_speed  = 400,total_scroll_distance = 4000):
    # 定义滚动速度和滚动总距离
    # scroll_speed = 400  # 滚动速度，数字越大滚动越快
    # total_scroll_distance = 4000  # 总共要滚动的距离
    # 循环逐渐滚动
    for _ in range(total_scroll_distance // scroll_speed):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(0.2)  # 等待一小段时间以控制滚动速度


def find_file(filename):
    # 在当前工作目录和其父目录中查找文件
    curr_path = os.getcwd()
    while True:
        if os.path.exists(os.path.join(curr_path, filename)):
            return curr_path + '/' + filename
        else:
            new_path = os.path.abspath(os.path.join(curr_path, '..'))
            if curr_path == new_path:
                break
            curr_path = new_path
    return None


def text_write(text,file_path,mode="a"):
    '''
    写入文件
    :param text:
    :param file_path:
    :param mode:
        "r": 读取模式，打开文件用于读取。
        "w": 写入模式，打开文件用于写入。如果文件已存在，则截断文件（即删除文件中的所有内容）。如果文件不存在，则创建新文件。
        "a": 追加模式，打开文件用于写入。如果文件已存在，则将数据写入文件末尾，而不是覆盖文件内容。如果文件不存在，则创建新文件。
        "b": 二进制模式，用于处理二进制文件（例如图片、音频等）。
        "x": 专门用于创建新文件的独占写入模式。如果文件已存在，则 FileExistsError 异常将被引发。
        这些模式可以组合使用，例如 "rb" 表示以二进制模式读取文件，"w+" 表示读写模式，如果文件不存在则创建。你可以根据具体的需求选择适当的模式。
    :param encoding:
        "UTF-8"
        "GBK"
    :return:
    '''
    # os.makedirs(file_path, exist_ok=True)

    with open(file_path, mode, encoding='utf-8') as file:
        if text is not None:
            file.write(text)
        else:
            file.write("")
# def text_write(text,file_path,mode="a",encoding='utf-8'):
#     '''
#     写入文件
#     :param text:
#     :param file_path:
#     :param mode:
#         "r": 读取模式，打开文件用于读取。
#         "w": 写入模式，打开文件用于写入。如果文件已存在，则截断文件（即删除文件中的所有内容）。如果文件不存在，则创建新文件。
#         "a": 追加模式，打开文件用于写入。如果文件已存在，则将数据写入文件末尾，而不是覆盖文件内容。如果文件不存在，则创建新文件。
#         "b": 二进制模式，用于处理二进制文件（例如图片、音频等）。
#         "x": 专门用于创建新文件的独占写入模式。如果文件已存在，则 FileExistsError 异常将被引发。
#         这些模式可以组合使用，例如 "rb" 表示以二进制模式读取文件，"w+" 表示读写模式，如果文件不存在则创建。你可以根据具体的需求选择适当的模式。
#     :param encoding:
#         "UTF-8"
#         "GBK"
#     :return:
#     '''
#     # os.makedirs(file_path, exist_ok=True)
#
#     with open(file_path, mode, encoding) as file:
#         if text is not None:
#             file.write(text)
#         else:
#             file.write("")


def merge_files(self):
    # 随机选择一个txt文件并读取内容
    random_txt_file_path = self._random_file()
    if random_txt_file_path:
        random_txt_content = self._read_txt_file(random_txt_file_path)
    else:
        print("No random txt file found.")
        return

    # 读取固定的txt文件内容
    fixed_txt_file_path = os.path.join(words_fixed_path, "fixed.txt")
    fixed_txt_content = self._read_txt_file(fixed_txt_file_path)

    return f"Random Text:\n{random_txt_content}\n\nFixed Text:\n{fixed_txt_content}"



'''登录相关'''

def login_unauto(login_elements_tag):
    '''
    用于手动登录阻塞,需要提前获取登录元素
    '''
    if login_elements_tag:
        input('可能需要登录，登录后按‘ENTER’继续！')



if __name__ == "__main__":
    driver = webdriver.Chrome()
    win = BrowserWindows(driver)
    # 打开第一个页面
    driver.get("https://www.baidu.com")

    # 打开新窗口并切换
    win.open_new_window("https://www.taobao.com")
    win.open_new_window("https://www.qq.com")
    driver.switch_to.window(win.get_window_handles()[1])

    # 在新窗口中执行一些操作
    # ...



    # 打印当前所有窗口句柄
    win.get_window_handles()
    win.close_current_window()
    win.get_window_handles()
    input()