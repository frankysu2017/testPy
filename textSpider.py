#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import multiprocessing
import time


def getText(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102'}
    html = ''
    try:
        html = requests.get(url, verify=True, headers=header, timeout=60)
        html.raise_for_status()
        html.encoding = html.apparent_encoding
    except Exception as e:
        print(url)
        with open(r'./error.txt', 'a', encoding='utf8') as f:
            f.write(url+'\n')
    soup = BeautifulSoup(html.text.encode(html.encoding).decode('utf8'), 'lxml')
    filename = r'C:/Users/WEB_PC_X1/Documents/novel_c/' + soup.title.string.split(' - ')[0].replace('/', '-') + '.txt'
    toWrite = soup.body.find('div', class_="novelContent")
    with open(filename, 'w', encoding='utf8') as f:
        f.write(str(toWrite.text).replace('　　', '\n　　'))
    #print("%s done!" %url)

def getList(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102'}
    html = requests.get(url, verify=True, headers=header)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text.encode(html.encoding).decode('utf8'), 'lxml')
        list = soup.find_all('a', target='_blank')
        siteUrl = url[:url.index('.com')+4]
        novelUrl = map(lambda x: siteUrl+x.get('href'), list)
        #for item in novelUrl:
        #    print(item)
        return novelUrl

if __name__ == "__main__":
    urls = [r'https://www.814aa.com/htm/novellist5/'+str(x+1)+r'.htm' for x in range(10)]
    f = open(r'./error.txt', 'w', encoding='utf8')
    f.close()
    for i, url in enumerate(urls):
        print(i)
        SpiderList = []
        getList(url)
        for item in getList(url):
            SpiderList.append(multiprocessing.Process(target=getText, args=(item, )))
        for proc in SpiderList:
            try:
                proc.start()
            except Exception as e:
                print('error occured!!!')
                proc.terminate()

    with open(r'./error.txt', 'r', encoding='utf8') as f:
        for url in f:
            url = url.replace('\n', '')
            print(url)
            getText(url)