import requests


# 004号社区
def vote():
    url = 'https://tj.cjyun.org/tj.gif?sid=10008&cid=2112881&aid=4&type=app&url=http://m.hbtv.com.cn/p/2112881.html&action=like'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
    datas = {
        'sid': 10008,
        'cid': 2112881,
        'aid': 4,
        'type': 'app',
        'url': 'https://m.hbtv.com.cn/p/2112881.html',
        'action': 'like',
    }
    proxies = {'http': '122.226.57.70:8888'}
    respone = requests.get(url, proxies=proxies, headers=headers, data=datas)
    if respone.status_code == 200:
        print(f'访问成功, 当前ip: {proxies}')
    else:
        print('访问失败')


i = 1
while True:
    try:
        print(i)
        vote()
        i += 1
    except:
        pass
        continue
