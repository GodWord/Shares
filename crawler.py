import random
import requests
from bs4 import BeautifulSoup

HEADERS = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'},
]


def getHeaders():
    """获取从HEADERS中随机出一个headers并返回"""
    i = random.randint(0, len(HEADERS) - 1)
    headers = HEADERS[i]
    return headers


def getHtmlText(url, params=None):
    headers = getHeaders()
    try:
        req = requests.get(url=url, params=params, headers=headers)
        req.encoding = req.apparent_encoding
        req.status_code
        return req.text
    except:
        print('出现异常！')


def getContent(text, selector=''):
    bs = BeautifulSoup(text, 'html.parser')
    return bs.select(selector)
