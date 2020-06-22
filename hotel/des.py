#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import pandas_profiling

if __name__ == '__main__':
    data = pd.read_csv(r'./test', encoding='gbk')
    print(data.columns.values)
    print(data.head()['Taste'])
    #data.profile_report(title='华住会')