#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pylab as pl
import time

def MaxClose():
    listMonth = []
    quotesMSFT = pd.read_csv(r'./quotes_MSFT.csv', header=0, encoding='gbk', index_col=None)
    quotesINTC = pd.read_csv(r'./quotes_INTC.csv', header=0, encoding='gbk', index_col=None)
    listMonth = pd.Series(map(lambda x: time.strptime(x, '%Y-%m-%d')[1], quotesMSFT.date))
    print(listMonth)

if __name__ == '__main__':
    MaxClose()
    print()