#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import pandas as pd
from _datetime import datetime

if __name__ == "__main__":
    df = pd.read_csv(u'C:/Users/Junie_WEB/Desktop/test.txt', sep=',', header=None)
    print(datetime(df[1]))

