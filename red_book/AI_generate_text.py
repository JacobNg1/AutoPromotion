import requests,re

AI_t2t_web = 'https://tongyi.aliyun.com/qianwen/bag/generator?code=littleRedBook'   #通义千问




cookies = {
    'cna': 'yYwVHhixrjMCAXjusbiutJ8U',
    'munb': '2217127051203',
    't': 'b52f8520a050efb3a01fff1ca83670f5',
    'login_current_pk': '1828503845613278',
    'aliyun_country': 'CN',
    'aliyun_site': 'CN',
    'aliyun_lang': 'zh',
    'login_tongyi_ticket': 'WA5QsOxjGw8JkjvK0daWq9ME91ttJZCZFuTNe_ZWdliTUP4gHrkXUaIrrMUaL5Wm0',
    'yunpk': '1828503845613278',
    'cnaui': '1828503845613278',
    'aui': '1828503845613278',
    'sca': '92082cae',
    'XSRF-TOKEN': 'b37479a6-070e-4f76-b852-0869c43c0478',
    '_samesite_flag_': 'true',
    'cookie2': '19d556acff2d9d52ac17ddee8d366de3',
    '_tb_token_': '37381ded37be5',
    'atpsida': '2c50714649beba05a02cbb13_1703905972_2',
    'login_aliyunid_csrf': '_csrf_tk_1127103905965125',
    'l': 'fBrDAMmHL-wYqZzoBO5Bnurza779PQRbzsPzaNbMiIEGa6s1aFgFaNCOtbN2udtjgT54oE-rc4M-OdhXWDU38xwUQdaRYV7CRnJp8eM3N7AN.',
    'isg': 'BOLiUlj987JCaO9bL8sKPdI2M2hEM-ZNxCPZmyx5pNUA_4B5G8HIXCI9KzsDb17l',
    'tfstk': 'choOBNVoBBAGIP8nRjLH3T9lAZZAa-OYOONcDDBJAaUDuTSAcsjrq0C_oFwX6U9d.',
}

headers = {
    'authority': 'qianwen.aliyun.com',
    'accept': 'text/event-stream',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'cna=yYwVHhixrjMCAXjusbiutJ8U; munb=2217127051203; t=b52f8520a050efb3a01fff1ca83670f5; login_current_pk=1828503845613278; aliyun_country=CN; aliyun_site=CN; aliyun_lang=zh; login_tongyi_ticket=WA5QsOxjGw8JkjvK0daWq9ME91ttJZCZFuTNe_ZWdliTUP4gHrkXUaIrrMUaL5Wm0; yunpk=1828503845613278; cnaui=1828503845613278; aui=1828503845613278; sca=92082cae; XSRF-TOKEN=b37479a6-070e-4f76-b852-0869c43c0478; _samesite_flag_=true; cookie2=19d556acff2d9d52ac17ddee8d366de3; _tb_token_=37381ded37be5; atpsida=2c50714649beba05a02cbb13_1703905972_2; login_aliyunid_csrf=_csrf_tk_1127103905965125; l=fBrDAMmHL-wYqZzoBO5Bnurza779PQRbzsPzaNbMiIEGa6s1aFgFaNCOtbN2udtjgT54oE-rc4M-OdhXWDU38xwUQdaRYV7CRnJp8eM3N7AN.; isg=BOLiUlj987JCaO9bL8sKPdI2M2hEM-ZNxCPZmyx5pNUA_4B5G8HIXCI9KzsDb17l; tfstk=choOBNVoBBAGIP8nRjLH3T9lAZZAa-OYOONcDDBJAaUDuTSAcsjrq0C_oFwX6U9d.',
    'origin': 'https://tongyi.aliyun.com',
    'referer': 'https://tongyi.aliyun.com/qianwen/bag/generator?code=littleRedBook',
    'sec-ch-ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36',
    'x-platform': 'pc_tongyi',
    'x-xsrf-token': '226e34f9-b26e-465c-a723-d819588ae824',
}

params = {
    'templateCode': 'littleRedBook',
    'pattern': 'no_control',
    'model': 'moss_v1',
    'utterance': 'text',
}



def AI_t2t(text):
    # 限制文本长度不超过500个字符
    text = text[:500]

    params = {
        'templateCode': 'littleRedBook',
        'pattern': 'no_control',
        'model': 'moss_v1',
        'utterance': text,
    }
    response = requests.get('https://qianwen.aliyun.com/market/app/execute', params=params, cookies=cookies,
                          headers=headers)

    # 检查请求是否成功（状态码为200）
    if response.status_code == 200:
        data = response.content.decode('utf-8')
        pattern = re.compile(r'data: {.+?content":"(.+?)"\s*}', re.DOTALL)
        matches = pattern.findall(data)

        if len(matches) >= 2:
            content = matches[-2]
            return content  # 返回匹配到的内容
        else:
            print("没有足够的匹配项")
            return None  # 或者返回 None
    else:
        print(f"请求失败，状态码为 {response.status_code}")
        return None


if __name__ == "__main__":
    asw = AI_t2t('小鸟依人')
    print(asw)
    # asw2 =  AI_t2t('疯狂星期四')
    # print(asw2)
    # asw3 =  AI_t2t('美好时光海滩')
    # print(asw3)