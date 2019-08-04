#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    s = 'abc, aaa, "bbb, 123, cc", abc, "ddd, 666, hhh", xcf'
    p = re.compile('"(.+?)"')
    l = re.findall(p, s)
    for item in l:
        s = s.replace(item, item.replace(',', '|'))
    print(s)
