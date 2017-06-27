#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import json
import pandas as pd
from datetime import date

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' %(stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return [item for item in quotes if not 'type' in item]

quotes = retrieve_quotes_historical('INTC')
list1 = []
for item in quotes:
    x = date.fromtimestamp(item['date'])
    y = date.strftime(x, '%Y-%m-%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index = list1)
quotesdf_m = quotesdf_ori.drop(['unadjclose'], axis=1)
quotesdf = quotesdf_m.drop(['date'], axis=1)
u = ['open', 'low', 'high', 'close', 'volume']
print(quotesdf.ix[:, u].to_csv(r'./quotes_INTC.csv', sep=',', encoding='utf8', index_label='date'))
