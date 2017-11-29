#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from multiprocessing import Process, Queue, Pool
import time

def f(x, y):
    return x or y

def getItem(list):
    return tuple(list)

resultList = []
def log_result(result):
    resultList.append(result)

def getPage(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102'}
    html = ''
    try:
        html = requests.get(url, headers=header, timeout=60) df
        html.raise_for_status()
        html.encoding = html.apparent_encoding
    except Exception as e:
        print('request error: {}'.format(e))
        with open(r'./error.txt', 'r+', encoding='utf8') as f:
            f.write(url)
    soup = bs(html.text, 'html.parser')
    tr = soup.find_all(name='tr', attrs={'class':'pointer'})
    personInfo = list(map(lambda x: list(x.find_all(name='td')), tr))
    df = pd.DataFrame(personInfo, columns=['name', 'id', 'phone', 'amount', 'status'])
    df = df.applymap(lambda x: x.text)
    return df

if __name__ == "__main__":
    urls = [r'http://www.xinyongheimingdan.cc/s?p={}'.format(i+1) for i in range(131)]
    df = pd.DataFrame([])
    pool = Pool(processes=100)
    for url in urls:
        pool.apply_async(getPage, (url, ), callback=log_result)
    pool.close()
    pool.join()
    for result in resultList:
        df = df.append(result, ignore_index=True)
    df.to_csv(r'./visa.csv')
    print(df)