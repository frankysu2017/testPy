#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
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

def compress(dataframe, column, comp_column, sep = ','):
    '''
    compress the common rows in one row, too lazy to note this function
    :param dataframe:
    :param column:
    :param com_column:
    :param sep:
    :return:
    '''
    df_comp = pd.DataFrame([])


if __name__ == '__main__':
    df = pd.read_csv(r'./bbb.csv', sep = ',', names = ['id', 'name', 'phonelist'], header = None, dtype=str)
    print(list(expand(df, 'phonelist', 'phone', sep='，').groupby('id'))[1])
