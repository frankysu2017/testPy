#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(r'./bbb.csv', sep = ',', names = ['id', 'name', 'phonelist'], header = None, dtype=str)
    for x in df.index:
        phones = df.ix[x]['phonelist'].split('，')
        for phone in phones:
            print(df.ix[x]['id'], df.ix[x]['name'], phone)