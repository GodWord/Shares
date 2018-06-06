from crawler import *


def __getStockCode():
    url = 'http://quote.eastmoney.com/stocklist.html'
    text = getHtmlText(url)
    a_Tags = getContent(text, '#quotesearch a[target=\'_blank\']')
    stock_code = dict()
    for a in a_Tags:
        s = a.string
        name = s.split('(')[0]
        code = s.split('(')[1][:-1]
        stock_code[name] = code

    return stock_code


def getStockCode():
    stock_code = __getStockCode()
    return stock_code
