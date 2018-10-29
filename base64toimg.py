#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import re


if __name__ == "__main__":
    try:
        f = open(r'./base64.txt', 'r')
        str = f.read()
        f.close()
    except FileNotFoundError:
        print(r"please make sure your clipboard is pasted in the 'base64.txt' file in this dictionary")
        exit()
    img = re.findall(r';base64,(.+)"', str)
    img = base64.b64decode(img[0])
    with open(r'./image.png', 'wb') as f:
        f.write(img)
    print("the image file is created!")