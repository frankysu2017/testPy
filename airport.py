#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pandas as pd


if __name__ == "__main__":
    with open(r'./json/flights.json', 'r', encoding='utf8') as f:
        load_dict = json.loads(f.readlines()[0])
        for key in load_dict.keys():
            f = open(r'./json/%s' % key, 'w', encoding='utf8')
            f.write(str(load_dict[key]))
            f.close()
        df = pd.DataFrame(load_dict['airports'], columns=load_dict['airportsFields'])
        print(df)
        df.to_csv('./json/airports.csv')