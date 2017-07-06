#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pylab as pl
import time

def MaxClose():
    quotesMSFT = pd.read_csv(r'./quotes_MSFT.csv', header=0, encoding='gbk', index_col=None)
    quotesINTC = pd.read_csv(r'./quotes_INTC.csv', header=0, encoding='gbk', index_col=None)
    listMonth = pd.Series(map(lambda x: time.strptime(x, '%Y-%m-%d')[1], quotesMSFT.date))
    quotesMSFT['month'] = listMonth
    quotesINTC['month'] = listMonth
    closeMaxMSFT = quotesMSFT.groupby('month').close.max()
    closeMaxINTC = quotesINTC.groupby('month').close.max()
    #plt.subplot(211)
    plt.plot(closeMaxMSFT.index, closeMaxMSFT, '-.*r')
    #plt.subplot(212)
    plt.plot(closeMaxINTC.index, closeMaxINTC, 'g-o')
    plt.title('Max Close of MS and INTEL')
    plt.xlabel('month')
    plt.ylabel('<Max Close>')
    plt.legend(['MSFT', 'INTC'], loc = 'best')
    plt.show()

def movieLens():
    dataDF = pd.read_csv(r'./ml-100k/u.data', encoding='gbk', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])
    userDF = pd.read_csv(r'./ml-100k/u.user', encoding='gbk', sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
    listItem = ['movie_id', 'movie_title', 'release_date', 'video_release_date', 'IMDb_URL', 'unknown',
                'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama',
                'Fantasy', 'Film_Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci_Fi', 'Thriller',
                'War', 'Western']
    itemDF = pd.read_csv(r'./ml-100k/u.item', encoding='gbk', sep='|', names=listItem)
    udDF = pd.merge(dataDF, userDF, on='user_id', how='left')
    timeSeries = pd.Series(map(lambda x: time.strftime('%Y-%m-%d', time.localtime(x)), udDF.timestamp))
    udDF['date'] = timeSeries
    #index = (udDF.timestamp < time.mktime(time.strptime('1998-1-1', '%Y-%m-%d'))) & (udDF.timestamp > time.mktime(time.strptime('1997-6-30', '%Y-%m-%d')))
    #print(udDF[index])
    print(udDF.groupby('gender').rating.std())

def testSeek():
    fp = open('./test.txt', 'r+')
    fp.seek(0,1)
    line = fp.readline()
    print(line)

def sparse_vector(indices, values):
    vector = [indices, values]
    print(vector)
    ind = values.index(max(values))
    print(indices[ind], values[ind])

    return x

if __name__ == '__main__':
    movieLens()
    #print(sparse_vector([1,8,231,500],[0.1,2.3,2.0,10.0]))