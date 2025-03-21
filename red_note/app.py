
from red_book_publish import *
from use_opening_chrome import *
from red_book_to_AI import *

# from red_book_cfg import options


def red_book_browse():
    scroll_to_bottom(400,8000)




def remove_machine_control_features():
    '''
    移除seLenium当中爬虫的特征
    '''
    #读取js脚本
    json_script = find_file('stealth.min.js')
    f = open(json_script,mode='r',encoding='utf-8').read()
    # 移除seLenium当中爬虫的特征
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': f})



r'''
命令行启动浏览器
接下来，在 CMD 终端中通过命令行启动 Chrome 浏览器

chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile" --window-size=1200,720

其中--remote-debugging-port指定浏览器调试端口号   PS：这里可以随机指定一个端口号，不要指定为已经被占用的端口号
--user-data-dir指定用户配置文件目录，这里需要单独指定一个文件夹目录（不存在会新建），如果不显式指定该参数，运行会污染浏览器默认的配置文件
'''

'''---STAR FROM HERE---'''

if __name__ == "__main__":


    # 用cmd打开浏览器并设置端口
    driver = use_chrome(9222)

    remove_machine_control_features()

    #red_book_publish(9222)


    #用AI参考热文生成小红书营销文案
    driver = red_book_hot_text(9222)





