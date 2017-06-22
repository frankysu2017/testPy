#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(r'./bbb.csv', name = ['id', 'name', 'phonelist'])
    print(df['phonelist'])