#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import time

if __name__ == '__main__':
    quotes_temp = pd.read_csv(r'./quotes.csv', sep = ',', encoding = 'utf8')
    quotes = np.array(quotes_temp)
    attribute = ['date', 'open', 'low', 'high', 'close', 'volume']
    quotesdf = pd.DataFrame(quotes, columns = attribute)
    list1 = []
    for i in range(0, len(quotes)):
        x = time.strftime('%y/%m/%d', time.strptime(quotes[i][0], '%Y-%m-%d'))
        list1.append(x)
    quotesdf.index = list1
    quotesdf = quotesdf.drop(['date'], axis=1)
    df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns = ['a','b','c'])
    temp = quotesdf['16/06/27':'16/12/27'].sort_values('close', ascending = False)[:5]
    tempdf = quotesdf['16/06/27':'17/06/27']
    list2 = []
    for i in range(len(tempdf)):
        list2.append(int(tempdf.index[i][3:5]))
    #tempdf['month'] = list2
    #temp = tempdf[tempdf.close > tempdf.open]['month'].value_counts()
    #print(temp)
    #temp = tempdf.groupby('month')['volume'].sum()
    sort1 = tempdf.sort_values('close')
    temp = pd.concat([sort1[:5], sort1[-5:]])
    temp = quotesdf['16/06/27':'16/12/31'][quotesdf.close < 49]
    print(temp)