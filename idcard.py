#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
import time
import datetime

def is_valid_date(date_str):
    if len(date_str) == 8:
        try:
            time.strptime(date_str, "%Y%m%d")
            return True
        except:
            return False
    elif len(date_str) == 6:
        try:
            time.strptime(date_str, "%y%m%d")
            return True
        except:
            return False
    else:
        return  False

def idVerify(id_str):
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    validate = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    id = list(id_str)

    if len(id_str) == 17:
        if is_valid_date(id_str[6:14]):
            multi_weight = list(map(lambda x, y: x*int(y), weight, id))
            validate_serial = reduce(lambda x, y: x+y, multi_weight) % 11
            return id_str + validate[validate_serial]
        else:
            return id_str + "\tinvalid"

    elif len(id_str) == 18:
        if is_valid_date(id_str[6:14]):
            multi_weight = list(map(lambda x, y: x * int(y), weight, id[:-1]))
            validate_serial = reduce(lambda x, y: x + y, multi_weight) % 11
            if validate[validate_serial] == id[-1]:
                return id_str+"\tvalid"
            else:
                return id_str + "\tinvalid"
        else:
            return id_str + "\tinvalid"

    elif len(id_str) == 15:
        if is_valid_date(id_str[6:12]):
            if int(id_str[6:8]) <= int(str(datetime.datetime.now().year)[2:]):
                id_str = id_str[:6] + '20' + id_str[6:]
            else:
                id_str = id_str[:6] + '19' + id_str[6:]
            return idVerify(id_str)
        else:
            return id_str + "\tinvalid"
    else:
        return id_str + "\tinvalid"

if __name__ == "__main__":
    print(idVerify("110106180216001"))
