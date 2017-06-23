#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

url = 'http://www.wikihow.com/Take-Cornell-Notes'
html = requests.get(url)
print(html)