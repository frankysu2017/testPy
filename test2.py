#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing
import time

def worker(interval):
    n = 5
    while(n > 0):
        print('the time is {0}'.format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == '__main__':
    p_l = []
    for i in range(10):
        p_l.append(multiprocessing.Process(target=worker, args=(0,)))
    for p in p_l:
        p.start()
        time.sleep(0)
    '''
    print('p.pid: %s' %p.pid)
    print('p.name: %s' %p.name)
    print('p.is alive: %s' %p.is_alive())
    '''
