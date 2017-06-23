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

def compress(dataframe, comp_column, sep = ','):
    '''
    compress the common rows in one row, too lazy to note this function
    :param dataframe:
    :param column:
    :param com_column:
    :param sep:
    :return:
    '''
    df_comp = pd.DataFrame([])
    for item in list(dataframe.groupby(list(dataframe.columns)[0])):
        type = item[1]['type']
        content = item[1]['content']
        zipList = list(map(lambda x: x[0]+':'+x[1],list(zip(type, content))))
        contact = ','.join(zipList)
        df_comp = df_comp.append({'id':item[0], comp_column: contact}, ignore_index = True)
    return df_comp

if __name__ == '__main__':
    df = pd.read_csv(r'./bbb.csv', sep = ',', names = ['id', 'name', 'phonelist'], header = None, dtype=str)
    df_ex = expand(df, 'phonelist', 'phone', sep='，')

    df2 = pd.read_csv(r'./ccc.csv', sep = ',', names = ['id', 'type', 'content'], header = None, dtype = str)
    #for item in list(df2.groupby(list(df2.columns)[0])):
    #    print('item = ', item)
    #phones = list(list(df_ex.groupby(list(df_ex.columns)[0])['phone'])[0][1])
    #print(list(df2.groupby(list(df2.columns)[0]))[1])
    #content = list(list(df2.groupby(list(df2.columns)[0]))[0][1]['content'])
    #type = list(list(df2.groupby(list(df2.columns)[0]))[0][1]['type'])
    #res = list(map(lambda x: x[0]+':'+x[1], list(zip(type, content))))
    #print(','.join(res))
    print(compress(df2, 'contact'))