#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import pandas as pd
import requests

if __name__ == '__main__':
    html = requests.get('http://www.wikihow.com/Take-Cornell-Notes')
    print(html)