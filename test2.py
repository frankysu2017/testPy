#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import pandas as pd

if __name__ == '__main__':
    dates = pd.date_range('20150201', periods=10)
    listA = ['value']
    resultA = pd.DataFrame(list(range(1, 11)), index=dates, columns=listA)
    print(resultA.index)