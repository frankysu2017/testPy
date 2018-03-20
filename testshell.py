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


from multiprocessing import Pool
import os, time

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(2)
    for i in range(4):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
