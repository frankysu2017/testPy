#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

try:
    t = time.strptime('feg' ,'%d-%b-%y')
    print(r"It's a valid date string: %s" %time.strftime('%Y-%m-%d', t))
except:
    print(r"It's an invalid date string")