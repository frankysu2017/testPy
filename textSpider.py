#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def getText(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102'}
    html = requests.get(url, verify=True, headers=header)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text.encode(html.encoding).decode('utf8'), 'lxml')
        filename = './novel/' + soup.title.string.split(' - ')[0] + '.txt'
        toWrite = soup.body.find('div', class_="novelContent")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(toWrite.text))

def getList(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102'}
    html = requests.get(url, verify=True, headers=header)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text.encode(html.encoding).decode('utf8'), 'lxml')
        pub = soup.find('ul')
        soup2 = BeautifulSoup(pub)
        print(soup2.text)

if __name__ == "__main__":
    url = r'https://www.uuu711.com/htm/novellist5/'
    getList(url)