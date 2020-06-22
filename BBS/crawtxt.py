#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import os
from bs4 import BeautifulSoup as bs
from functools import reduce
import multiprocessing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_url(page_url):
    html = requests.get(page_url)
    htmltext = html.text.encode(html.encoding).decode('utf8')
    soup = bs(htmltext, 'lxml').html.body.div.find_all(name='div', attrs={'class': 'pc_list'})[1].ul.find_all(name='li')
    url_list = [page_url + x.a['href'] for x in soup]
    title_list = ['%03d.txt' %(int(x.a['href'].split('.')[0])-14645656) for x in soup]
    return url_list, title_list


def get_text(text_url, filename):

    chrome_opt = Options()  # 创建参数设置对象.
    chrome_opt.add_argument('--headless')  # 无界面化.
    chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
    chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.

    driver = webdriver.Chrome(chrome_options=chrome_opt)
    driver.get(text_url)
    html = driver.page_source
    soup = bs(html, 'lxml').html.body.div.find(name='div', attrs={'id': 'content1'})
    driver.quit()

    with open(r'./txt/' + filename, 'w', encoding='utf8') as file:
        file.write(soup.text)


def merge_txt(path):
    cmd_str = 'cd txt & copy/b {} total.txt'.format('+'.join(os.listdir(r'./txt')))
    os.system(cmd_str)


if __name__ == '__main__':
    page_url = 'https://www.xsjtxt.com/book/73017/'
    text_url = get_url(page_url)[0]
    article_name = get_url(page_url)[1]
    '''
    pool = multiprocessing.Pool(5)
    for t, n in zip(text_url, article_name):
        pool.apply_async(func=get_text, args=(t, n))
    pool.close()
    pool.join()
    '''
    merge_txt(r'./txt')
