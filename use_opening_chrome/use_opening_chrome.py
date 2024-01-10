#命令行启动浏览器
# 接下来，在 CMD 终端中通过命令行启动 Chrome 浏览器
# 启动浏览器
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"

# 其中--remote-debugging-port指定浏览器调试端口号   PS：这里可以随机指定一个端口号，不要指定为已经被占用的端口号
# --user-data-dir指定用户配置文件目录，这里需要单独指定一个文件夹目录（不存在会新建），如果不显式指定该参数，运行会污染浏览器默认的配置文件



# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By


def use_opening_chrome(port):
    options = Options()
    options.debugger_address = f'localhost:{port}'
    driver = webdriver.Chrome(options=options)
    return driver

if __name__ == "__main__":

    driver = use_opening_chrome(9222)
    driver.get('https://www.baidu.com/')


