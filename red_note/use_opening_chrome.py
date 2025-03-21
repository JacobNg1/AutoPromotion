#命令行启动浏览器
# 接下来，在 CMD 终端中通过命令行启动 Chrome 浏览器
# 启动浏览器
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile" --window-size=1200,720

# 其中--remote-debugging-port指定浏览器调试端口号   PS：这里可以随机指定一个端口号，不要指定为已经被占用的端口号
# --user-data-dir指定用户配置文件目录，这里需要单独指定一个文件夹目录（不存在会新建），如果不显式指定该参数，运行会污染浏览器默认的配置文件



# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
import selenium,os,time

chrome_file = r'.\Chrome\AutomationProfile'

def use_chrome(port, width=1200, height=720):
    """
    用CMD打开chrome浏览器
    :param port: 使用的端口号
    width: 初始尺寸 宽度 默认1200
    height: 初始尺寸 高度 默认720
    """
    if selenium.webdriver.common.utils.is_connectable(port):
        driver = use_opening_chrome(port)
        print(f'端口号为{port}的Chrome Brower正在运行')
    else:
        os.popen(f'start chrome --remote-debugging-port={port} --user-data-dir={chrome_file} --window-size={width},{height}')
        print(f'成功开启端口号为{port}的Chrome Brower 分辨率为{width}*{height}')
        driver = use_opening_chrome(port)

    return driver


def use_opening_chrome(port):
    '''
    使用已经在运行的chrome浏览器
    :param port: 使用的端口号
    '''
    options = Options()
    options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
    driver = webdriver.Chrome(options=options)
    return driver


def switch_window(new_tag,driver):
    all_window_handles = driver.window_handles
    new_window_handle = all_window_handles[new_tag]
    driver.switch_to.window(new_window_handle)



if __name__ == "__main__":

    driver = use_chrome(9222)
    # new_driver.get(url = 'https://www.baidu.com/')
    # new_driver.execute_script("window.open();")
    # # switch_window(2,new_driver)
    # input('用于阻塞')
    driver.get(r'https://www.bilibili.com/')
    time.sleep(1)
    driver.switch_to.new_window()
    driver.get("https://www.baidu.com/")
