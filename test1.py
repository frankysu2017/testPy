#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import time
from matplotlib.pyplot import plot, show

engine = create_engine("mysql+pymysql://hsiaoguo:Qwerzxcv123@localhost:3306/test",connect_args={'charset':'utf8'})
df = pd.read_sql('select * from qlog where QQacc = "QQ8" order by Qlog;' ,con=engine)
lstQ = list(df['Qlog'])
lstQ = list(map(lambda x: int(time.mktime(time.strptime(str(x), '%Y-%m-%d %H:%M:%S'))), lstQ))
t_min = np.min(lstQ)
t_max = np.max(lstQ)
print('%d  %d' %(t_min, t_max))
