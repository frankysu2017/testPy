#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import sqrt, floor
from functools import reduce

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

if __name__ == '__main__':
    for i in range(1, 100):
        if isPrime(i):
            print("\t%d;" %i, end='')
