import time

import requests


# 077号社区
def vote():
    url = 'https://tj.cjyun.org/tj.gif?sid=10008&cid=2113542&aid=4&type=app&url=http://m.hbtv.com.cn/p/2113542.html&action=like'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    datas = {
        'sid': 10008,
        'cid': 2113542,
        'aid': 4,
        'type': 'app',
        'url': 'https://m.hbtv.com.cn/p/2113542.html',
        'action': 'like',
    }
    proxies = {'http': '58.55.251.189:7082'}
    respone = requests.get(url, proxies=proxies, headers=headers, data=datas)
    if respone.status_code == 200:
        print(f'访问成功, 当前ip: {proxies}')
    else:
        print('访问失败')


i = 1
while True:
    initial_time = time.time()
    print(i)
    i += 1
    vote()
    print(f'vps: {1 / (time.time() - initial_time)}')
