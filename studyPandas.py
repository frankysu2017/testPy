#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def expand(dataframe, column, exp_column, sep = ','):
    '''
    expand some data column such as 103403,1224382,20495 to different rows
    :param dataframe: dataframe to expanded
    :param column: the column of the dataframe to expanded
    :param exp_column: be the new column
    :param sep: seperated character
    :return: the new dataframe has been expanded
    '''
    df_exp = pd.DataFrame([])
    for x in dataframe.index:
        columnList = dataframe.ix[x][column].split(sep)
        for item in columnList:
            ser1 = pd.Series(dataframe.ix[x])
            ser1[exp_column] = item
            df_exp = df_exp.append(ser1)
    return df_exp

def compress(dataframe, comp_column, sep = ','):
    '''
    compress the common rows in one row, too lazy to note this function
    :param dataframe:
    :param column:
    :param com_column:
    :param sep:
    :return:
    '''
    df_temp = dataframe.copy(deep=True)
    df_temp[comp_column] = dataframe['type'] + ':' + dataframe['content']
    datafame_comp = df_temp.groupby('id').agg({comp_column: sep.join})
    return datafame_comp.reset_index()

if __name__ == '__main__':
    df = pd.read_csv(r'./bbb.csv', sep = ',', names = ['id', 'name', 'phonelist'], header = None, dtype=str)
    df_ex = expand(df, 'phonelist', 'phone', sep='，')

    df2 = pd.read_csv(r'./ccc.csv', sep = ',', names = ['id', 'type', 'content'], header = None, dtype = str)
    df_comp = compress(df2, 'contact', sep = ',')
    print(df_comp)
