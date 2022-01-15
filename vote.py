import random
import time

import numpy as np
import requests

from headers import random_header
from proxy_ip import ip_pool


def vote():
    url = 'https://tj.cjyun.org/tj.gif?sid=10008&cid=2113200&aid=4&type=app&url=http://m.hbtv.com.cn/p/2113200.html&action=like'
    headers = random_header
    proxies = {'http': random.choice(ip_pool)}
    datas = {
        'sid': 10008,
        'cid': 2113200,
        'aid': 4,
        'type': 'app',
        'url': 'http://m.hbtv.com.cn/p/2113200.html',
        'action': 'like',
    }
    respone = requests.get(url, proxies=proxies, headers=headers, data=datas)
    if respone.status_code == 200:
        print(f'访问成功, 当前ip: {proxies}')
    else:
        print('访问失败')


i = 0
while True:
    # Random!!!
    counts = np.random.poisson(100, 1)[0]
    speed = np.random.uniform(0, 1, 10)[0]
    for count in range(counts):
        try:
            vote()
        except:
            pass
            continue
        count += 1
        i += 1
        print(f'{count}/{counts}. Total Votes: {i} times')
        sleeptime = abs(np.random.normal(loc=10, scale=10, size=None)) * speed
        print(f'Sleep {round(sleeptime, 2)} sec')
        print(' ')
        time.sleep(sleeptime)
