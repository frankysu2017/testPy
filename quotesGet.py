#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import json
import pandas as pd
import time
from datetime import date

def retrieve_quotes_historical(stock_code, startdate, enddate):
    quotes = []
    start = time.mktime(time.strptime(startdate, '%Y-%m-%d'))
    end = time.mktime(time.strptime(enddate, '%Y-%m-%d'))
    url = 'https://finance.yahoo.com/quote/%s/history?period1=%d&period2=%d&interval=1d&filter=history&frequency=1d' %(stock_code, start, end)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return [item for item in quotes if not 'type' in item]

if __name__ == '__main__':
    quotes = retrieve_quotes_historical('MSFT', '2016-1-1', '2016-12-31')
    list1 = []
    for item in quotes:
        x = date.fromtimestamp(item['date'])
        y = date.strftime(x, '%Y-%m-%d')
        list1.append(y)
    quotesdf_ori = pd.DataFrame(quotes, index = list1)
    quotesdf_m = quotesdf_ori.drop(['unadjclose'], axis=1)
    quotesdf = quotesdf_m.drop(['date'], axis=1)
    u = ['open', 'low', 'high', 'close', 'volume']
    print(quotesdf.ix[:, u].to_csv(r'./quotes_MSFT.csv', sep=',', encoding='utf8', index_label='date'))
