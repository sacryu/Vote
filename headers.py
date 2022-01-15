from fake_useragent import UserAgent

ua = UserAgent()
# ua.update()
USER_AGENTS = ua.random

random_header = {
    'User-Agent': USER_AGENTS,
    'Referer': 'http://m.hbtv.com.cn/',
}
