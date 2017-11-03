#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

@log
def put():
    print(datetime.datetime.now())

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

if __name__ == '__main__':
    f = fib(100)
    print(f)