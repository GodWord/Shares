# code=UTF-8
import random

from bs4 import BeautifulSoup
import requests

URL = 'http://quote.eastmoney.com/stocklist.html'
HEADERS = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'},
]


class StockCode:

    def __getHeaders(self):
        """获取从HEADERS中随机出一个headers并返回"""
        i = random.randint(0, len(HEADERS) - 1)
        headers = HEADERS[i]
        return headers

    def __getHtmlText(self, url, params=None):
        headers = self.__getHeaders()
        try:
            req = requests.get(url=url, params=params, headers=headers)
            req.encoding = req.apparent_encoding
            req.status_code
            return req.text
        except:
            print('出现异常！')

    def __getContent(text, selector):
        bs = BeautifulSoup(text, 'html.parser')
        return bs.select(selector)

    def __getStockCode(self):
        text = self.__getHtmlText(URL)
        a_Tags = self.__getContent(text, '#quotesearch a[target=\'_blank\']')
        stock_code = dict()
        for a in a_Tags:
            s = a.string
            name = s.split('(')[0]
            code = s.split('(')[1][:-1]
            stock_code[name] = code

        return stock_code

    def getStockCode(self):
        stock_code = self.__getStockCode()
        return stock_code
