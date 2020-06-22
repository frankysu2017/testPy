#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import collections
import pickle
from PIL import Image
from selenium import webdriver as wd
import time
import os
import bz2

def getMedicine(mname):
    driver = wd.Chrome()
    url = 'http://www.baidu.com/'
    driver.get(url)
    driver.find_element_by_id('virus-2020').click()
    h = driver.window_handles
    driver.switch_to.window(h[-1])
    time.sleep(4)
    print(driver.page_source)


def puzzle3():
    html = requests.get(r'http://www.pythonchallenge.com/pc/def/equality.html').text
    p = re.compile('<!--(.*?)-->', flags=re.DOTALL)
    p2 = re.compile('[^A-Z][A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]')
    r = re.findall(p, html)
    print(''.join(re.findall(p2, r[0])))


def puzzle4():
    number = '123456'
    result = '0'
    i = 0
    while result.isdigit():
        number = result
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(number)
        html = requests.get(url).text
        result = html.split(' ')[-1]
        print('{}: {}'.format(i, result))
        i += 1
    url_new = 'http://www.pythonchallenge.com/pc/def/{}'.format(result)
    print(url_new)


def puzzle5():
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    html = requests.get(url).text
    result = bytes(html, encoding='utf8')
    r = pickle.loads(result)
    for i in r:
        for j in i:
            print(j[0] * j[1], end='')
        print('\n')


def puzzle7():
    if not os.path.isfile('./oxygen.png'):
        with open('./oxygen.png', 'wb') as f:
            f.write(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content)
    img = Image.open(r'./oxygen.png')
    width, height = img.size
    for y in range(height):
        count = 0
        for x in range(width):
            r, g, b, a = img.getpixel((x,y))
            if r == g and g == b:
                count += 1
            if count > 300:
                h_mask = y
                break
    lst = []
    for x in range(width):
        r, g, b, a = img.getpixel((x, h_mask))
        if r == g and g == b:
            lst.append(chr(r))
    s = ''.join(lst[::7])
    p = re.compile('\[(.*)\]')
    l = [chr(x) for x in eval(re.search(p, s).group(0))]
    print(''.join(l))


def puzzle8():
    html = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html').text
    p = re.compile('<!--(.*)-->', re.DOTALL)
    s = re.search(p, html).group(0)
    un = eval('b' + s.split('\n')[1].split(': ')[1])
    pw = eval('b' + s.split('\n')[2].split(': ')[1])
    un = bz2.decompress(un).decode()
    pw = bz2.decompress(pw).decode()
    print('un: {}\npw: {}'.format(un, pw))


def puzzle9():
    html = requests.post('http://huge:file@www.pythonchallenge.com/pc/return/good.html').text
    p1 = re.compile('first:\n([\d\,\n]*)\n\nsecond:')
    p2 = re.compile('second:\n([\d\,\n]*)\n\n')
    first = re.search(p1, html).group(0).replace('\n', '').replace('first:', '').replace('second:', '').split(',')
    second = re.search(p2, html).group(0).replace('\n', '').replace('second:', '').split(',')
    coordinate = list(zip((first+second)[::2], (first+second)[1::2]))
    if not os.path.isfile('./good.jpg'):
        with open('./good.jpg', 'wb') as f:
            f.write(requests.get('http://huge:file@www.pythonchallenge.com/pc/return/good.jpg').content)
    img = Image.open('./good.jpg')
    print(img.mode)
    img_new = Image.new(img.mode, img.size)
    for item in coordinate:
        img_new.putpixel((eval(item[0]), eval(item[1])), (255,255,255))
    img_new.show()




if __name__ == '__main__':
    puzzle9()