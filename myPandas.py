#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import json
import pandas as pd
from datetime import date

def retrieve_quotes_historical(stock_code):
    quotes = []
    list1 = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' %(stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*),"isPending"',r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    quotes_valid = [item for item in quotes if not 'type' in item]
    for item in quotes_valid:
            x = date.fromtimestamp(item['date'])
            y = date.strftime(x, '%Y-%m-%d')
            list1.append(y)
    quotesdf_ori = pd.DataFrame(quotes_valid, index = list1)
    quotesdf_m = quotesdf_ori.drop(['unadjclose'], axis = 1)
    quotesdf = quotesdf_m.drop(['date'], axis = 1)
    return quotesdf

def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30')
    search_pattern = re.compile('class="wsod_symbol">(.*)<\/a>.*<span.*">(.*)<\/span>.*\n.*class="wsod_stream">(.*)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append({'code': item[0], 'name': item[1], 'price': float(item[2])})
    return pd.DataFrame(dji_list)

if __name__ == '__main__':
    #quotes = retrieve_quotes_historical('AXP')
    #print(quotes)
    #quotes.to_csv(r'./aaa.csv')
    quotes = pd.read_csv(r'./aaa.csv', index_col = 0)
    attributes = ['open', 'close', 'high', 'low', 'volume']
    quotes = pd.DataFrame(quotes, columns=attributes)
    print(quotes)
    #print(retrieve_dji_list()[11:13].sort('price', ascending = 1))