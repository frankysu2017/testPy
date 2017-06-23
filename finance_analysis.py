#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas_datareader.data as web
import datetime as dt
import os

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

ticker_list = ['0700.hk', '600000.ss']
'''
if not os.path.exists('stock_test'):
    os.makedirs('stock_test')
for ticker in ticker_list:
    if not os.path.exists('stock_test/{}.csv'.format(ticker)):
        df = web.DataReader(ticker, "yahoo", start, end)
        df.to_csv('stock_test/{}.csv'.format(ticker))
    else:
        print('Already have {}'.format(ticker))
'''
web.DataReader('600000.ss', "edgar-index", start, end)
