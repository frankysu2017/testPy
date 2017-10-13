#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
def readData(filename):
    df = pd.read_csv(filename, sep='#*#', header=None)
    return df

if __name__ == '__main__':
    print(readData(r'C:\twdata\sample100.txt'))