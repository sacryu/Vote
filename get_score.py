import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html

from headers import random_header


# 从url_1和url_2获取队伍名字及各自的分数
def get_summary(int):
    url_1 = 'https://m.hbtv.com.cn/p/' + str(int) + '.html'
    url_2 = 'https://m.hbtv.com.cn/ajax/dynamic?id=' + str(int)
    headers = random_header

    response_1 = requests.get(url_1, headers=headers)
    response_1.encoding = 'utf-8'
    text_1 = html.fromstring(response_1.content)
    names = text_1.xpath('//div[contains(@class,\'g-container\')]//div[@class=\'a-title\']/h1')
    if names:
        name = [i.text for i in names][0]
    else:
        name = 'Not Available'

    response_2 = requests.get(url_2, headers=headers)
    response_2.encoding = 'utf-8'
    text_2 = BeautifulSoup(response_2.text, 'lxml')
    vote_num = text_2.get_text().split(',')[2].replace('"digg":', '')

    if '社区春晚' in name:
        print(f'{name} : {vote_num} 票, {url_1}')

    return [name, vote_num]


# 从url_2获取队伍的分数
def get_vote_num(int):
    url_2 = 'https://m.hbtv.com.cn/ajax/dynamic?id=' + str(int)
    headers = random_header
    response_2 = requests.get(url_2, headers=headers)
    response_2.encoding = 'utf-8'
    text_2 = BeautifulSoup(response_2.text, 'lxml')
    vote_num = text_2.get_text().split(',')[2].replace('"digg":', '')
    return vote_num


# 将队伍名字及各自的初始分数写入csv
def write_first_data():
    name_list = []
    vote_num_list = []
    for i in whole_list():
        name, vote_num = get_summary(i)
        name_list.append(name)
        vote_num_list.append(vote_num)

    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    df = pd.DataFrame(
        {
            '名字': name_list,
            local_time: vote_num_list,
        },
    )
    df.to_csv('票数总览.csv', mode='w', index=False, encoding='utf_8_sig')


# 创立初始分数后，更新自己的分数，并写入csv
def update_data():
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f'{local_time}: Running')

    vote_num_list = []
    for i in whole_list():
        vote_num = get_vote_num(i)
        vote_num_list.append(vote_num)

    count = len(vote_num_list) - 1

    csv = pd.read_csv('票数总览.csv')
    csv.loc[0:count, local_time] = vote_num_list
    csv.to_csv('票数总览.csv', mode='w', index=False, encoding='utf_8_sig')

    print(f'{local_time}: Done')


# 每个队伍自己的编号
def whole_list():
    # 1 - 20
    list_1 = [2112877, 2112878, 2112879, 2112881, 2112882, 2112883, 2112884, 2112885, 2112886, 2112887, 2112888,
              2112889,
              2112891, 2112892, 2112893, 2112894, 2112896, 2112897, 2112898, 2112899]
    # 21 - 40
    list_2 = list(range(2113194, 2113213 + 1))
    # 41 - 44
    list_3 = [2113292, 2113298, 2113306, 2113321]
    # 45 - 59
    list_4 = [2113329, 2113338, 2113345, 2113364, 2113373, 2113379, 2113390, 2113391, 2113395, 2113397, 2113411,
              2113425,
              2113427, 2113431, 2113433]
    # 60 - 74
    list_5 = [2113495, 2113498, 2113499, 2113501, 2113502, 2113503, 2113510, 2113514, 2113516, 2113521, 2113524,
              2113525, 2113528, 2113530, 2113532]
    # 77 - 88
    list_6 = [2113539, 2113541, 2113542, 2113543, 2113545, 2113547, 2114174, 2114289, 2114327, 2114336, 2114507,
              2114513,
              2114936, 2115324]
    whole_list = list_1 + list_2 + list_3 + list_4 + list_5 + list_6
    return whole_list


if __name__ == "__main__":
    # write_first_data()
    update_data()
    # for i in whole_list():
    #    get_summary(i)
