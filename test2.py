#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import pandas as pd
from mpl_finance import fetch_historical_yahoo

if __name__ == '__main__':
    data = fetch_historical_yahoo('600028.ss', datetime.datetime(2016,1,1), datetime.datetime(2017,1,1))
    print(data)