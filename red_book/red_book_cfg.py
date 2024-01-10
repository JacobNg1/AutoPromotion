from selenium import webdriver


# 浏览器配置对象
options = webdriver.ChromeOptions()

# 禁用自动化栏
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 修正了 'excludeSwitches' 内的拼写错误

# 屏蔽保存密码提示框
prefs = {'credentials_enable_service': False, 'profile.password_manager_enabled': False}
options.add_experimental_option('prefs', prefs)  # 修正了 'profile.password_manager_enabled' 内的拼写错误

# 反爬虫特征处理
options.add_argument('--disable-blink-features=AutomationControlled')


red_book_index_url = 'https://www.xiaohongshu.com/explore'
red_book_publish_url = 'https://creator.xiaohongshu.com/creator/home'



title_path = r'.\file\ad_titles'
words_random_path = r'.\file\ad_words_random'
words_fixed_path = r'.\file\ad_words_fixed'
pic_path = r'.\file\ad_pic'



FILE_PATH = r'.\file'


LOG_PATH = r'.\log'