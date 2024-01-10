# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
# #
# # browser = webdriver.Chrome()
# # browser.get('https://www.baidu.com')
# #
# # # 打印网页标题
# # print(browser.title)
# # # 输出内容：百度一下，你就知道
# #
# res = requests.get('https://www.xiaohongshu.com/explore/656985ac00000000090209ea')
# print(res.text)
# # with open('test.txt', 'w', encoding='utf-8') as file:
# #     file.write(res.text)
#
# soup = BeautifulSoup(res.text, 'html.parser')
#
# # 获取 meta 元素的 description 内容
# description = soup.find("meta", {"name": "description"})["content"]
# print(description)





# import requests

# headers = {
#     'authority': 'qianwen.aliyun.com',
#     'accept': '*/*',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'access-control-request-headers': 'x-platform,x-xsrf-token',
#     'access-control-request-method': 'GET',
#     'origin': 'https://tongyi.aliyun.com',
#     'referer': 'https://tongyi.aliyun.com/qianwen/bag/generator?code=littleRedBook',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36',
# }
#
# params = {
#     'templateCode': 'littleRedBook',
#     'pattern': 'no_control',
#     'model': 'moss_v1',
#     'utterance': '塔岭啊',
# }
#
# response = requests.options('https://qianwen.aliyun.com/market/app/execute', params=params, headers=headers)
#
# print(response.text)


# import requests
#
# cookies = {
#     'yunpk': '1640683779347525',
#     'login_current_pk': '1640683779347525',
#     'aliyun_lang': 'zh',
#     'cnaui': '1640683779347525',
#     'aui': '1640683779347525',
#     'cna': 'yQX9HPtiu2ACAXzwSeml08ao',
#     'XSRF-TOKEN': 'fe82bdd6-744b-4139-aa8c-a4fa128fc99b',
#     'sca': 'f6cfc349',
#     '_samesite_flag_': 'true',
#     'cookie2': '19c192d7573799cdf3cc586d5ad26fe8',
#     'munb': '2207616371449',
#     'csg': '9a0aef16',
#     't': '6a0f702d8c61e8cc44d2d927aacfd113',
#     '_tb_token_': '5533d737b8777',
#     'login_aliyunid_ticket': 'qOxbrMB_ji7IYBUZgXf_QNpoU_BOTwChTBoNM1ZJeedfK9zxYnbN5hossqIZCr6t7SGxRigm2Cb4fGaCdBZWIzmgdHq6sXXZQg4KFWufyvpeV*0*Cm58slMT1tJw3_5$$10cv2QOcCWOxb03DHyBrZ*V0',
#     'login_aliyunid_pk': '1640683779347525',
#     'hssid': 'CN-SPLIT-ARCEByIOc2Vzc2lvbl90aWNrZXQyAQE4hoauoMsxQAFKEMbWxFCHJDlqjoNNFHVzI9luyFDQKiFStAJ1o6cfuaelJM1MOw',
#     'hsite': '6',
#     'aliyun_country': 'CN',
#     'aliyun_site': 'CN',
#     'login_tongyi_ticket': 'UaHrrXUaI5WM5mLOWA5Qs10cv2QOcCWOxb03DHyBrZxV*MqOjbrin_3aOSXzErzr0',
#     'login_aliyunid_pks': 'BG+QbwGag4F3UwMzd1N/hM2W7ureLRhnJvVZEmoxuGVDP4=',
#     'login_aliyunid': 'jaco****',
#     'atpsida': 'f1872b2b90b35dddbe7af1b7_1703845209_4',
#     'login_aliyunid_csrf': '_csrf_tk_1661703827702975',
#     'l': 'fBrDAMmHL-wYqjIEBOfZFurza77TKIRAguPzaNbMi9fPOOsp5U35W1CEnhp9CnGVFsCJR3ojPYhBBeYBqfgA3epHHQAQtWDmnmOk-Wf..',
#     'isg': 'BJycCkNkFSHvzOFJVa1sj_jobbpOFUA_nq1X6Xad4gdqwTxLnidMzxK5JSk5yXiX',
#     'tfstk': 'coUOB_Du69XgYEs3A-IhgUiRHhNAaaWxdCMDkydsL1ivy9YvlsXzrzpsmGGfBg1d.',
# }
#
# headers = {
#     'authority': 'qianwen.aliyun.com',
#     'accept': 'text/event-stream',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     # 'cookie': 'yunpk=1640683779347525; login_current_pk=1640683779347525; aliyun_lang=zh; cnaui=1640683779347525; aui=1640683779347525; cna=yQX9HPtiu2ACAXzwSeml08ao; XSRF-TOKEN=fe82bdd6-744b-4139-aa8c-a4fa128fc99b; sca=f6cfc349; _samesite_flag_=true; cookie2=19c192d7573799cdf3cc586d5ad26fe8; munb=2207616371449; csg=9a0aef16; t=6a0f702d8c61e8cc44d2d927aacfd113; _tb_token_=5533d737b8777; login_aliyunid_ticket=qOxbrMB_ji7IYBUZgXf_QNpoU_BOTwChTBoNM1ZJeedfK9zxYnbN5hossqIZCr6t7SGxRigm2Cb4fGaCdBZWIzmgdHq6sXXZQg4KFWufyvpeV*0*Cm58slMT1tJw3_5$$10cv2QOcCWOxb03DHyBrZ*V0; login_aliyunid_pk=1640683779347525; hssid=CN-SPLIT-ARCEByIOc2Vzc2lvbl90aWNrZXQyAQE4hoauoMsxQAFKEMbWxFCHJDlqjoNNFHVzI9luyFDQKiFStAJ1o6cfuaelJM1MOw; hsite=6; aliyun_country=CN; aliyun_site=CN; login_tongyi_ticket=UaHrrXUaI5WM5mLOWA5Qs10cv2QOcCWOxb03DHyBrZxV*MqOjbrin_3aOSXzErzr0; login_aliyunid_pks=BG+QbwGag4F3UwMzd1N/hM2W7ureLRhnJvVZEmoxuGVDP4=; login_aliyunid=jaco****; atpsida=f1872b2b90b35dddbe7af1b7_1703845209_4; login_aliyunid_csrf=_csrf_tk_1661703827702975; l=fBrDAMmHL-wYqjIEBOfZFurza77TKIRAguPzaNbMi9fPOOsp5U35W1CEnhp9CnGVFsCJR3ojPYhBBeYBqfgA3epHHQAQtWDmnmOk-Wf..; isg=BJycCkNkFSHvzOFJVa1sj_jobbpOFUA_nq1X6Xad4gdqwTxLnidMzxK5JSk5yXiX; tfstk=coUOB_Du69XgYEs3A-IhgUiRHhNAaaWxdCMDkydsL1ivy9YvlsXzrzpsmGGfBg1d.',
#     'origin': 'https://tongyi.aliyun.com',
#     'referer': 'https://tongyi.aliyun.com/qianwen/bag/generator?code=littleRedBook',
#     'sec-ch-ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36',
#     'x-platform': 'pc_tongyi',
#     'x-xsrf-token': '4c6aada0-5b20-4647-b009-4ec842d82971',
# }
#
# params = {
#     'templateCode': 'littleRedBook',
#     'pattern': 'no_control',
#     'model': 'moss_v1',
#     'utterance': '黑暗女巫',
# }
#
# response2 = requests.get('https://qianwen.aliyun.com/market/app/execute', params=params, cookies=cookies, headers=headers)
#
# print(response2.text)
#

# text = '【超时空惊喜！🌟】哆啦A梦的神奇道具，你最想拥有哪个？👀\n\\n小时候的我们，都曾梦想有个无所不能的哆啦A梦在身边。🔍 想象一下，如果能从那个四次元口袋掏出任意门🚪，是不是就能瞬间穿越到想去的地方？或者戴上记忆面包🍞，再也不怕考试前夜的临时抱佛脚？还有那可以实现愿望的竹蜻蜓直升飞机🚁，带你翱翔天际，俯瞰世界！\n\n今天，就让我们一起重返童年，探索那些藏在哆啦A梦口袋里的神奇道具吧！💡 不仅是童年的回忆，更是对未来科技与生活的无尽想象。每一个道具背后，都藏着对美好生活的向往和追求。💖\n\n那么，亲爱的朋友们，你们心中最渴望拥有的哆啦A梦道具是什么呢？在评论区告诉我吧！🤔 一起来畅谈那些年我们一起追过的哆啦A梦和他的秘密武器！🚀\n\n#哆啦A梦 #童年回忆 #神奇道具分享【超时空惊喜！🌟】哆啦A梦的神奇道具，你最想拥有哪个？🤔\n\n穿越二次元世界，那个蓝胖子——哆啦A梦的四次元口袋里，藏着无数让人瞠目结舌的秘密武器！🔍 任意门、记忆面包、竹蜻蜓...每一个都像是开启新世界的钥匙，帮你解决生活中的小烦恼，实现大梦想！🚀\n\n假如你有机会拥有一件，你会选择瞬间移动到心仪之地的“任意门”呢？还是会选择考试前夜救急的“记忆面包”？或者是自由翱翔天际的“竹蜻蜓”？🤔 每个道具背后都蕴含着对美好生活的向往与追求，唤醒我们内心深处那份纯真与勇气。💪\n\n快来留言分享你的选择吧，看看有多少人和你一样怀揣着同样的愿望！💕 #哆啦A梦#神奇道具#童年回忆【超时空惊喜！🌟】哆啦A梦的神奇道具，你最想拥有哪个？👀\n\n小时候，我们都梦想有个哆啦A梦在身边，那个蓝胖子的四次元口袋里藏着无数令人惊叹的秘密武器。🚀从能带你穿越时空的任意门🚪，到帮你实现愿望的记忆面包🍞，每一样都让人充满无尽遐想！\n\n今天，就让我们一起重返童年，探索那些年我们曾渴望拥有的神奇道具吧！💡也许你会想起考试前想要的“记忆凝缩灯”💡，或是面对困难时急需的“解决问题机”🔧... 每个道具背后都蕴含着生活的智慧与勇气，教会我们在现实中勇敢面对挑战💪。\n\n#哆啦A梦回忆杀 #童年经典动漫 #神奇道具大揭秘 一起来聊聊，如果让你选一个，你的首选会是哪一个呢？🤔 快来评论区分享你的梦幻之选吧！💕【超时空惊喜！🌟】哆啦A梦的神奇道具，你最想拥有哪个？🤔\n\n小时候的我们，都曾梦想拥有那只来自未来的蓝色机器猫——哆啦A梦。它的四次元口袋里藏着无数令人瞠目结舌的秘密武器，从竹蜻蜓到任意门，再到记忆面包📚，每一样都能让我们心跳加速、充满期待！\n\n设想一下，如果可以，你最想拥有哪一款神奇道具呢？是能带你瞬间环游世界的任意门🌍，还是帮你解决学习难题的记忆面包？亦或是那个能实现心中所愿的“如果电话亭”📞？\n\n这些超越现实的想象，不仅带给我们无尽的乐趣与惊喜，更在潜移默化中教会我们勇敢面对生活的挑战💪和珍惜身边的人与事。那么，你的选择会是什么呢？留言告诉我吧！😉\n\n#哆啦A梦回忆杀 #童年经典动漫 #神奇道具大揭秘【超时空惊喜！🌟】哆啦A梦的神奇道具，你最想拥有哪一个？👀\n\n打开记忆的大门，那个蓝胖子承载了我们多少童年幻想与梦想实现的瞬间。🔍 想象一下，如果能拥有任意门🚪，是不是就能瞬间穿越到想去的任何地方？或者拥有一台记忆面包🍞，考试前再也不用临时抱佛脚；再或者，让时间包袱巾掀起岁月的面纱，回到无忧无虑的纯真年代⋯⋯ nostalgia满满有木有？！\n\n今天，就让我们一起重温那些年哆啦A梦带给我们的神奇与感动，选出你心中最渴望的那个道具吧！💖 无论你是想要竹蜻蜓带你翱翔天际，还是希望空气炮帮你解决小麻烦，每一样道具都藏着一个充满想象力的世界。\n\n留言告诉我，你的“梦幻首选”是哪个？🤔 让我们一起在哆啦A梦的奇幻世界里，唤醒那份深藏心底的童真与快乐吧！ Childhood never ends! 🌟 '#哆啦A梦#神奇道具#童年回忆'
# print(text)

# generated_text = "这是一个包含中文字符的文本，同时也包含English和符号！" * 20  # 长度超过500个字符
#
# print(len(generated_text))
# generated_text = generated_text[:500]
# print(generated_text)
# print(len(generated_text))

import re,requests

res = requests.get('https://www.xiaohongshu.com/explore')

print(res.text)

# 定义正则表达式模式，用于匹配a标签中的href属性及其值
pattern = r'<a[^>]*href="([^"]*)"[^>]*>'

# 使用正则表达式查找并提取href属性值
match = re.search(pattern, res.text)


# 使用正则表达式查找并提取href属性值
match = re.search(pattern, res.text)

if match:
    href_value = match.group()
    print(href_value)
else:
    print("未找到匹配项")

｛我｝{w}