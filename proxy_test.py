import time

import requests
from lxml import html


# Check if ip_proxy works
def ip_check():
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    url = 'http://www.checkip.org'  # 你用于测试自己ip的网站
    # proxies = {'http': random.choice(ip_pool)}
    proxies = {'http': '58.251.94.56:6666'}
    request = requests.get(url, proxies=proxies, headers=head)  # 让问这个网页 随机生成一个ip
    if request.status_code == 200:
        print('访问成功')
    else:
        print('访问失败')
    text = html.fromstring(request.content)
    ips = text.xpath('//div[@id=\'yourip\']//span')

    for ip in ips:
        print(f'当前ip: {ip.text}')


def fps():
    url = 'http://www.baidu.com'
    initial_time = time.time()
    request = requests.get(url)
    if request.status_code == 200:
        print('访问成功')
        print(f'fps: {1 / (time.time() - initial_time)}')
    else:
        print('访问失败')


while True:
    ip_check()
    # fps()
