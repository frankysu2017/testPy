#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import sqrt, floor
from functools import reduce
import os
import time
import multiprocessing

def isPrime(num):
    if num <= 1:
        return False;
    elif num == 2 or num == 3:
        return True;
    else:
        lst = range(2, int(floor(sqrt(num))) + 1)
        boollist = map(lambda x: num%x != 0, lst)
        result = reduce(lambda x, y: x&y, boollist)
        return result

def fileCodec(filepath, sourceCode='utf8', destCode='utf8'):
    for root, dirs, files in os.walk(filepath):
        for file in files:
            print(file)
            f = open(filepath+'\\'+file, 'r', encoding=sourceCode)
            content = f.read()
            f.close()
            f = open(filepath+"\\"+file, 'w', encoding=destCode)
            f.write(content)
            f.close()

def prn(num):
    print(num, end='\r')

if __name__ == '__main__':
    print('hello, world!')